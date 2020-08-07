
# Make control variables
SHELL := bash

# User variables
builddir := $(or $(builddir),build/sam)
VERSION := $(or $(version),2020.2.29.r2)

# Workarounds
_ :=
SP := $(_) $(_)

# Constants
BASE_URL := https://sam.nrel.gov
SAM_URL := $(BASE_URL)/download$(if $(version),/version-$(subst $(SP),-,$(wordlist 1,3,$(subst ., ,$(version))))).html
_VERSION = $(subst .,-,$(VERSION))
BUILDDIR := $(builddir)/$(VERSION)
SDK := $(BUILDDIR)/sdk
PLATFORM := case `uname` in Darwin) echo macos;; Linux) echo linux;; *) echo windows;; esac
PLATFORM := $(shell $(PLATFORM))

linux_LIB := $(SDK)/linux/libssc.so
macos_LIB := $(SDK)/macos/libssc.dylib
windows_LIB := $(SDK)/windows/ssc.dll
ZIP_FILES := sam-sdk/sscapi.h $(SDK)/LICENSE $(linux_LIB) $(macos_LIB) $(windows_LIB)

# Functions
installer_url = $(BASE_URL)$(shell grep for-$(1) $(BUILDDIR)/catalog)
have_python_lib = $(shell python3 -c 'import $(1)' >& /dev/null && echo yes || echo no)
have_exe = $(shell type -f $(1) >& /dev/null && echo yes || echo no)
archive_start = $(shell NR=$$(grep -ahnm1 '^__ARCHIVE_BELOW__$$' "$(1)" | cut -d : -f 1); echo $$((NR+1)))
ssc_version = $(shell python3 -c 'import ctypes; print(ctypes.CDLL("$($(PLATFORM)_LIB)").ssc_version())')


# Base rules
.PHONY: help
help:
	@echo -e \
	"Builds SAM SDK zip file from official SAM installers.\\n"\
	"\\n"\
	"TARGETS:\\n"\
	"  about: show information about the source and output\\n"\
	"  check: print summary of prerequisites/dependencies\\n"\
	"  clean: remove build intermediates, but not final archive\\n"\
	"  help: print this help message\\n"\
	"  tidy: remove locally built intermediates, but keep remote files\\n"\
	"  zip: build archive in the sam-sdk directory\\n"\
	"\\n"\
	"PLATFORM TARGETS:\\n"\
	"  linux: build Linux artifacts\\n"\
	"  macos: build macOS artifacts\\n"\
	"  windows: build Windows artifacts\\n"\
	"\\n"\
	"VARIABLES:\\n"\
	"  builddir: override build directory [$(builddir)]\\n"\
	"  version: override version [$(VERSION)]\\n"

.PHONY: about
about:
	@echo Version: $(VERSION)
	@echo URL: $(SAM_URL)
	@echo Platform: $(PLATFORM)

.PHONY: clean
clean:
	-rm -r $(BUILDDIR)/*
	-rmdir -p $(BUILDDIR)

.PHONY: tidy
tidy:
	-rm -r $(SDK)
	-rm $(BUILDDIR)/{*.failed,linux.tgz,macos.img,ssc.{so,dylib}}

.PHONY: check
check:
	@echo -e \
	"Linux build requires one of:\\n"\
	"   patchelf (preferred): $(call have_exe,patchelf)\\n"\
	"   lief (python3 library): $(call have_python_lib,lief)\\n"\
	"\\n"\
	"macOS build requires one of:\\n"\
	"   install_name_tool (macOS only): $(call have_exe,install_name_tool)\\n"\
	"   macholib (python3 library, preferred): $(call have_python_lib,macholib)\\n"\
	"   lief (python3 library): $(call have_python_lib,lief)\\n"
  ifneq ($(PLATFORM),macos)
	@echo -e \
	"Additional requirements for macOS builds on non-macOS systems:\\n"\
	"   dmg2img: $(call have_exe,dmg2img)\\n"\
	"   gnome-disk-image-mounter (optional): $(call have_exe,gnome-disk-image-mounter)\\n"
  endif
	@echo -e \
	"Windows build requires:\\n"\
	"   innoextract: $(call have_exe,innoextract)\\n"

.PHONY: zip
ifdef _ZIP
zip: sam-sdk/ssc-$(_SSC_VERSION).zip

ifdef _SSC_VERSION
sam-sdk/ssc-$(_SSC_VERSION).zip: $(ZIP_FILES)
	@mkdir -p $(@D)
	@-rm $@
	cd $(SDK) && zip -r $(CURDIR)/$@ .
endif
else
zip: $(ZIP_FILES)
	@$(MAKE) $@ _ZIP=yes _SSC_VERSION=$(call ssc_version)
endif

$(SDK)/LICENSE: sam-sdk/LICENSE
	@mkdir -p $(@D)
	cp $< $@



# Linux rules
.PHONY: header
header: sam-sdk/sscapi.h

.PHONY: linux
linux: $(linux_LIB)

$(linux_LIB): $(BUILDDIR)/ssc.so
	@mkdir -p $(@D)
  ifeq ($(call have_exe,patchelf),yes)
	cp $< $@ && patchelf --set-soname $(@F) $@
  else ifeq ($(call have_python_lib,lief),yes)
#	 Alternate pure-python conversion using lief
	@python3 -c 'import lief.ELF; lib = lief.parse("$<"); next(filter(lambda e: e.tag == lief.ELF.DYNAMIC_TAGS.SONAME, lib.dynamic_entries)).name = "$(@F)"; lib.write("$@")'
  else
	@echo "error: missing prerequisite for $@"
	@echo "Requires either patchelf tool or lief python package."
	@exit 1
  endif
	-chmod 0755 $@

.INTERMEDIATE: $(BUILDDIR)/ssc.so
$(BUILDDIR)/ssc.so sam-sdk/sscapi.h: $(BUILDDIR)/linux.tgz
	tar -xzOf $< ./sam.deploy/linux_64/$(@F) | sed -E 's/[[:space:]]+$$//' > $@

.INTERMEDIATE: $(BUILDDIR)/linux.tgz
$(BUILDDIR)/linux.tgz: $(BUILDDIR)/linux.run
	tail -n+$(call archive_start,$<) $< > $@

$(BUILDDIR)/linux.run: $(BUILDDIR)/catalog
	curl -o $@ "$(call installer_url,linux)"



# macOS rules
.PHONY: macos
macos: $(macos_LIB)

$(macos_LIB): $(BUILDDIR)/ssc.dylib
	@mkdir -p $(@D)
  ifeq ($(PLATFORM),macos)
	cp $< $@ && install_name_tool -id '@loader_path/$(@F)' $@
  else ifeq ($(call have_python_lib,macholib),yes)
#	 Alternate pure-python conversion using machlib
	@cp $< $@ && python3 -c 'import os, macholib.MachO; h, = macholib.MachO.MachO("$@").headers; h.rewriteInstallNameCommand(b"@loader_path/$(@F)"); h.write(open("$@", "rb+"))'
  else ifeq ($(call have_python_lib,lief),yes)
#	 Alternate pure-python conversion using lief
	@python3 -c 'import lief.MachO; lib = lief.parse("$<"); lib.get(lief.MachO.LOAD_COMMAND_TYPES.ID_DYLIB).name = "@loader_path/$(@F)"; lib.write("$@")'
  else
	@echo "error: missing prerequisite for $@"
	@echo "Requires either macOS with install_name_tool or the macholib or lief python packages."
	@exit 1
  endif
	-chmod 0755 $@

.INTERMEDIATE: $(BUILDDIR)/ssc.dylib
ifeq ($(PLATFORM),macos)

$(BUILDDIR)/ssc.dylib: $(BUILDDIR)/macos.dmg
	hdiutil attach -readonly $<
	read _ _ mountpoint _ < <(mount | grep SystemAdvisorModel); \
	trap "hdiutil detach '$$mountpoint'" EXIT INT; \
	cp "$$mountpoint/SAM.app/Contents/Frameworks/$(@F)" $@

else

$(BUILDDIR)/ssc.dylib: $(BUILDDIR)/macos.img
  ifeq ($(call have_exe,gnome-disk-image-mounter),yes)
    # User mount
	gnome-disk-image-mounter $<
	read _ _ mountpoint _ < <(mount | grep SystemAdvisorModel) && \
	trap 'umount "$$mountpoint" || { echo "Retrying in 3 seconds..."; sleep 3; umount "$$mountpoint"; }' EXIT INT && \
	cp "$$mountpoint/SAM.app/Contents/Frameworks/$(@F)" $@
  else
    # Sudo mount
	mkdir -p $(@D)/mnt
	sudo mount -t hfsplus -o loop,ro $< $(@D)/mnt
	trap 'sudo umount $(@D)/mnt || { echo "Retrying in 3 seconds..."; sleep 3; umount "$(@D)/mnt"; }' EXIT INT && \
	cp "$(@D)/mnt/SAM.app/Contents/Frameworks/$(@F)" $@
	-rmdir $(@D)/mnt
  endif

.INTERMEDIATE: $(BUILDDIR)/macos.img
$(BUILDDIR)/macos.img: $(BUILDDIR)/macos.dmg
  ifeq ($(call have_exe,dmg2img),no)
	@echo "error: missing prerequisite for $@"
	@echo "Requires dmg2img tool."
	@exit 1
  endif
	dmg2img -p 4 $< $@
endif

$(BUILDDIR)/macos.dmg: $(BUILDDIR)/catalog
	curl -o $@ "$(call installer_url,mac)"


# Windows rules
.PHONY: windows
windows: $(windows_LIB)

$(windows_LIB): $(BUILDDIR)/windows.exe
  ifeq ($(call have_exe,innoextract),no)
	@echo "error: missing prerequisite for $@"
	@echo "Requires innoextract tool."
	@exit 1
  endif
	@mkdir -p $(@D)
	set -e; \
	tmpdir="$$(mktemp -d)"; \
	trap "rm -r '$$tmpdir'" EXIT INT; \
	innoextract -I app/x64/$(@F) -d "$$tmpdir" $<; \
	cp "$$tmpdir/app/x64/$(@F)" $@
	-chmod 0644 $@

$(BUILDDIR)/windows.exe: $(BUILDDIR)/catalog
	curl -o $@ "$(call installer_url,windows)"


# Catalog rules
$(BUILDDIR)/catalog: $(BUILDDIR)/index.html
	sed -En '/href="\/download\/.*-for-(linux|mac|windows)\/file.html"/{s/^.*href="//;s/".*$$//;p;}' $< > $@

$(BUILDDIR)/index.html:
	mkdir -p $(@D)
	curl -o $@ "$(SAM_URL)"
	@grep -q '"sam-windows-$(_VERSION).exe"' $@ || { \
	  mv $@ $@.failed; \
	  echo 'error: index contains wrong version; saved as $@.failed'; \
	  exit 1; \
	}


# Special targets
.DELETE_ON_ERROR:
