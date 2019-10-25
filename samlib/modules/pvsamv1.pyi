
# This is a generated file

"""pvsamv1 - Photovoltaic performance model, SAM component models V.1"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'solar_resource_file': str,
        'solar_resource_data': Table,
        'transformer_no_load_loss': float,
        'transformer_load_loss': float,
        'system_use_lifetime_output': float,
        'analysis_period': float,
        'dc_degradation': Array,
        'dc_degrade_factor': Array,
        'en_dc_lifetime_losses': float,
        'dc_lifetime_losses': Array,
        'en_ac_lifetime_losses': float,
        'ac_lifetime_losses': Array,
        'en_snow_model': float,
        'system_capacity': float,
        'use_wf_albedo': float,
        'albedo': Array,
        'irrad_mode': float,
        'sky_model': float,
        'inverter_count': float,
        'enable_mismatch_vmax_calc': float,
        'subarray1_nstrings': float,
        'subarray1_modules_per_string': float,
        'subarray1_mppt_input': float,
        'subarray1_tilt': float,
        'subarray1_tilt_eq_lat': float,
        'subarray1_azimuth': float,
        'subarray1_track_mode': float,
        'subarray1_rotlim': float,
        'subarray1_shade_mode': float,
        'subarray1_gcr': float,
        'subarray1_monthly_tilt': Array,
        'subarray1_shading:string_option': float,
        'subarray1_shading:timestep': Matrix,
        'subarray1_shading:mxh': Matrix,
        'subarray1_shading:azal': Matrix,
        'subarray1_shading:diff': float,
        'subarray1_soiling': Array,
        'subarray1_rear_irradiance_loss': float,
        'subarray1_mismatch_loss': float,
        'subarray1_diodeconn_loss': float,
        'subarray1_dcwiring_loss': float,
        'subarray1_tracking_loss': float,
        'subarray1_nameplate_loss': float,
        'subarray2_rear_irradiance_loss': float,
        'subarray2_mismatch_loss': float,
        'subarray2_diodeconn_loss': float,
        'subarray2_dcwiring_loss': float,
        'subarray2_tracking_loss': float,
        'subarray2_nameplate_loss': float,
        'subarray3_rear_irradiance_loss': float,
        'subarray3_mismatch_loss': float,
        'subarray3_diodeconn_loss': float,
        'subarray3_dcwiring_loss': float,
        'subarray3_tracking_loss': float,
        'subarray3_nameplate_loss': float,
        'subarray4_rear_irradiance_loss': float,
        'subarray4_mismatch_loss': float,
        'subarray4_diodeconn_loss': float,
        'subarray4_dcwiring_loss': float,
        'subarray4_tracking_loss': float,
        'subarray4_nameplate_loss': float,
        'dcoptimizer_loss': float,
        'acwiring_loss': float,
        'transmission_loss': float,
        'subarray1_mod_orient': float,
        'subarray1_nmodx': float,
        'subarray1_nmody': float,
        'subarray1_backtrack': float,
        'subarray2_enable': float,
        'subarray2_modules_per_string': float,
        'subarray2_nstrings': float,
        'subarray2_mppt_input': float,
        'subarray2_tilt': float,
        'subarray2_tilt_eq_lat': float,
        'subarray2_azimuth': float,
        'subarray2_track_mode': float,
        'subarray2_rotlim': float,
        'subarray2_shade_mode': float,
        'subarray2_gcr': float,
        'subarray2_monthly_tilt': Array,
        'subarray2_shading:string_option': float,
        'subarray2_shading:timestep': Matrix,
        'subarray2_shading:mxh': Matrix,
        'subarray2_shading:azal': Matrix,
        'subarray2_shading:diff': float,
        'subarray2_soiling': Array,
        'subarray2_mod_orient': float,
        'subarray2_nmodx': float,
        'subarray2_nmody': float,
        'subarray2_backtrack': float,
        'subarray3_enable': float,
        'subarray3_modules_per_string': float,
        'subarray3_nstrings': float,
        'subarray3_mppt_input': float,
        'subarray3_tilt': float,
        'subarray3_tilt_eq_lat': float,
        'subarray3_azimuth': float,
        'subarray3_track_mode': float,
        'subarray3_rotlim': float,
        'subarray3_shade_mode': float,
        'subarray3_gcr': float,
        'subarray3_monthly_tilt': Array,
        'subarray3_shading:string_option': float,
        'subarray3_shading:timestep': Matrix,
        'subarray3_shading:mxh': Matrix,
        'subarray3_shading:azal': Matrix,
        'subarray3_shading:diff': float,
        'subarray3_soiling': Array,
        'subarray3_mod_orient': float,
        'subarray3_nmodx': float,
        'subarray3_nmody': float,
        'subarray3_backtrack': float,
        'subarray4_enable': float,
        'subarray4_modules_per_string': float,
        'subarray4_nstrings': float,
        'subarray4_mppt_input': float,
        'subarray4_tilt': float,
        'subarray4_tilt_eq_lat': float,
        'subarray4_azimuth': float,
        'subarray4_track_mode': float,
        'subarray4_rotlim': float,
        'subarray4_shade_mode': float,
        'subarray4_gcr': float,
        'subarray4_monthly_tilt': Array,
        'subarray4_shading:string_option': float,
        'subarray4_shading:timestep': Matrix,
        'subarray4_shading:mxh': Matrix,
        'subarray4_shading:azal': Matrix,
        'subarray4_shading:diff': float,
        'subarray4_soiling': Array,
        'subarray4_mod_orient': float,
        'subarray4_nmodx': float,
        'subarray4_nmody': float,
        'subarray4_backtrack': float,
        'module_model': float,
        'module_aspect_ratio': float,
        'spe_area': float,
        'spe_rad0': float,
        'spe_rad1': float,
        'spe_rad2': float,
        'spe_rad3': float,
        'spe_rad4': float,
        'spe_eff0': float,
        'spe_eff1': float,
        'spe_eff2': float,
        'spe_eff3': float,
        'spe_eff4': float,
        'spe_reference': float,
        'spe_module_structure': float,
        'spe_a': float,
        'spe_b': float,
        'spe_dT': float,
        'spe_temp_coeff': float,
        'spe_fd': float,
        'spe_vmp': float,
        'spe_voc': float,
        'spe_is_bifacial': float,
        'spe_bifacial_transmission_factor': float,
        'spe_bifaciality': float,
        'spe_bifacial_ground_clearance_height': float,
        'cec_area': float,
        'cec_a_ref': float,
        'cec_adjust': float,
        'cec_alpha_sc': float,
        'cec_beta_oc': float,
        'cec_gamma_r': float,
        'cec_i_l_ref': float,
        'cec_i_mp_ref': float,
        'cec_i_o_ref': float,
        'cec_i_sc_ref': float,
        'cec_n_s': float,
        'cec_r_s': float,
        'cec_r_sh_ref': float,
        'cec_t_noct': float,
        'cec_v_mp_ref': float,
        'cec_v_oc_ref': float,
        'cec_temp_corr_mode': float,
        'cec_is_bifacial': float,
        'cec_bifacial_transmission_factor': float,
        'cec_bifaciality': float,
        'cec_bifacial_ground_clearance_height': float,
        'cec_standoff': float,
        'cec_height': float,
        'cec_mounting_config': float,
        'cec_heat_transfer': float,
        'cec_mounting_orientation': float,
        'cec_gap_spacing': float,
        'cec_module_width': float,
        'cec_module_length': float,
        'cec_array_rows': float,
        'cec_array_cols': float,
        'cec_backside_temp': float,
        '6par_celltech': float,
        '6par_vmp': float,
        '6par_imp': float,
        '6par_voc': float,
        '6par_isc': float,
        '6par_bvoc': float,
        '6par_aisc': float,
        '6par_gpmp': float,
        '6par_nser': float,
        '6par_area': float,
        '6par_tnoct': float,
        '6par_standoff': float,
        '6par_mounting': float,
        '6par_is_bifacial': float,
        '6par_bifacial_transmission_factor': float,
        '6par_bifaciality': float,
        '6par_bifacial_ground_clearance_height': float,
        'snl_module_structure': float,
        'snl_a': float,
        'snl_b': float,
        'snl_dtc': float,
        'snl_ref_a': float,
        'snl_ref_b': float,
        'snl_ref_dT': float,
        'snl_fd': float,
        'snl_a0': float,
        'snl_a1': float,
        'snl_a2': float,
        'snl_a3': float,
        'snl_a4': float,
        'snl_aimp': float,
        'snl_aisc': float,
        'snl_area': float,
        'snl_b0': float,
        'snl_b1': float,
        'snl_b2': float,
        'snl_b3': float,
        'snl_b4': float,
        'snl_b5': float,
        'snl_bvmpo': float,
        'snl_bvoco': float,
        'snl_c0': float,
        'snl_c1': float,
        'snl_c2': float,
        'snl_c3': float,
        'snl_c4': float,
        'snl_c5': float,
        'snl_c6': float,
        'snl_c7': float,
        'snl_impo': float,
        'snl_isco': float,
        'snl_ixo': float,
        'snl_ixxo': float,
        'snl_mbvmp': float,
        'snl_mbvoc': float,
        'snl_n': float,
        'snl_series_cells': float,
        'snl_vmpo': float,
        'snl_voco': float,
        'sd11par_nser': float,
        'sd11par_area': float,
        'sd11par_AMa0': float,
        'sd11par_AMa1': float,
        'sd11par_AMa2': float,
        'sd11par_AMa3': float,
        'sd11par_AMa4': float,
        'sd11par_glass': float,
        'sd11par_tnoct': float,
        'sd11par_standoff': float,
        'sd11par_mounting': float,
        'sd11par_Vmp0': float,
        'sd11par_Imp0': float,
        'sd11par_Voc0': float,
        'sd11par_Isc0': float,
        'sd11par_alphaIsc': float,
        'sd11par_n': float,
        'sd11par_Il': float,
        'sd11par_Io': float,
        'sd11par_Egref': float,
        'sd11par_d1': float,
        'sd11par_d2': float,
        'sd11par_d3': float,
        'sd11par_c1': float,
        'sd11par_c2': float,
        'sd11par_c3': float,
        'mlm_N_series': float,
        'mlm_N_parallel': float,
        'mlm_N_diodes': float,
        'mlm_Width': float,
        'mlm_Length': float,
        'mlm_V_mp_ref': float,
        'mlm_I_mp_ref': float,
        'mlm_V_oc_ref': float,
        'mlm_I_sc_ref': float,
        'mlm_S_ref': float,
        'mlm_T_ref': float,
        'mlm_R_shref': float,
        'mlm_R_sh0': float,
        'mlm_R_shexp': float,
        'mlm_R_s': float,
        'mlm_alpha_isc': float,
        'mlm_beta_voc_spec': float,
        'mlm_E_g': float,
        'mlm_n_0': float,
        'mlm_mu_n': float,
        'mlm_D2MuTau': float,
        'mlm_T_mode': float,
        'mlm_T_c_no_tnoct': float,
        'mlm_T_c_no_mounting': float,
        'mlm_T_c_no_standoff': float,
        'mlm_T_c_fa_alpha': float,
        'mlm_T_c_fa_U0': float,
        'mlm_T_c_fa_U1': float,
        'mlm_AM_mode': float,
        'mlm_AM_c_sa0': float,
        'mlm_AM_c_sa1': float,
        'mlm_AM_c_sa2': float,
        'mlm_AM_c_sa3': float,
        'mlm_AM_c_sa4': float,
        'mlm_AM_c_lp0': float,
        'mlm_AM_c_lp1': float,
        'mlm_AM_c_lp2': float,
        'mlm_AM_c_lp3': float,
        'mlm_AM_c_lp4': float,
        'mlm_AM_c_lp5': float,
        'mlm_IAM_mode': float,
        'mlm_IAM_c_as': float,
        'mlm_IAM_c_sa0': float,
        'mlm_IAM_c_sa1': float,
        'mlm_IAM_c_sa2': float,
        'mlm_IAM_c_sa3': float,
        'mlm_IAM_c_sa4': float,
        'mlm_IAM_c_sa5': float,
        'mlm_IAM_c_cs_incAngle': Array,
        'mlm_IAM_c_cs_iamValue': Array,
        'mlm_groundRelfectionFraction': float,
        'inverter_model': float,
        'mppt_low_inverter': float,
        'mppt_hi_inverter': float,
        'inv_num_mppt': float,
        'inv_snl_c0': float,
        'inv_snl_c1': float,
        'inv_snl_c2': float,
        'inv_snl_c3': float,
        'inv_snl_paco': float,
        'inv_snl_pdco': float,
        'inv_snl_pnt': float,
        'inv_snl_pso': float,
        'inv_snl_vdco': float,
        'inv_snl_vdcmax': float,
        'inv_cec_cg_c0': float,
        'inv_cec_cg_c1': float,
        'inv_cec_cg_c2': float,
        'inv_cec_cg_c3': float,
        'inv_cec_cg_paco': float,
        'inv_cec_cg_pdco': float,
        'inv_cec_cg_pnt': float,
        'inv_cec_cg_psco': float,
        'inv_cec_cg_vdco': float,
        'inv_cec_cg_vdcmax': float,
        'inv_ds_paco': float,
        'inv_ds_eff': float,
        'inv_ds_pnt': float,
        'inv_ds_pso': float,
        'inv_ds_vdco': float,
        'inv_ds_vdcmax': float,
        'inv_pd_paco': float,
        'inv_pd_pdco': float,
        'inv_pd_partload': Array,
        'inv_pd_efficiency': Array,
        'inv_pd_pnt': float,
        'inv_pd_vdco': float,
        'inv_pd_vdcmax': float,
        'ond_PNomConv': float,
        'ond_PMaxOUT': float,
        'ond_VOutConv': float,
        'ond_VMppMin': float,
        'ond_VMPPMax': float,
        'ond_VAbsMax': float,
        'ond_PSeuil': float,
        'ond_ModeOper': str,
        'ond_CompPMax': str,
        'ond_CompVMax': str,
        'ond_ModeAffEnum': str,
        'ond_PNomDC': float,
        'ond_PMaxDC': float,
        'ond_IMaxDC': float,
        'ond_INomDC': float,
        'ond_INomAC': float,
        'ond_IMaxAC': float,
        'ond_TPNom': float,
        'ond_TPMax': float,
        'ond_TPLim1': float,
        'ond_TPLimAbs': float,
        'ond_PLim1': float,
        'ond_PLimAbs': float,
        'ond_VNomEff': Array,
        'ond_NbInputs': float,
        'ond_NbMPPT': float,
        'ond_Aux_Loss': float,
        'ond_Night_Loss': float,
        'ond_lossRDc': float,
        'ond_lossRAc': float,
        'ond_effCurve_elements': float,
        'ond_effCurve_Pdc': Matrix,
        'ond_effCurve_Pac': Matrix,
        'ond_effCurve_eta': Matrix,
        'ond_doAllowOverpower': float,
        'ond_doUseTemperatureLimit': float,
        'inv_tdc_cec_db': Matrix,
        'inv_tdc_cec_cg': Matrix,
        'inv_tdc_ds': Matrix,
        'inv_tdc_plc': Matrix,
        'en_batt': float,
        'load': Array,
        'gh': Array,
        'dn': Array,
        'df': Array,
        'wfpoa': Array,
        'gh_calc': Array,
        'dn_calc': Array,
        'df_calc': Array,
        'wspd': Array,
        'tdry': Array,
        'alb': Array,
        'snowdepth': Array,
        'sol_zen': Array,
        'sol_alt': Array,
        'sol_azi': Array,
        'sunup': Array,
        'sunpos_hour': Array,
        'airmass': Array,
        'subarray1_surf_tilt': Array,
        'subarray1_surf_azi': Array,
        'subarray1_aoi': Array,
        'subarray1_aoi_modifier': Array,
        'subarray1_axisrot': Array,
        'subarray1_idealrot': Array,
        'subarray1_poa_eff_beam': Array,
        'subarray1_poa_eff_diff': Array,
        'subarray1_poa_nom': Array,
        'subarray1_poa_shaded': Array,
        'subarray1_poa_shaded_soiled': Array,
        'subarray1_poa_front': Array,
        'subarray1_poa_rear': Array,
        'subarray1_poa_eff': Array,
        'subarray1_soiling_derate': Array,
        'subarray1_beam_shading_factor': Array,
        'subarray1_linear_derate': Array,
        'subarray1_ss_diffuse_derate': Array,
        'subarray1_ss_reflected_derate': Array,
        'subarray1_ss_derate': Array,
        'shadedb_subarray1_shade_frac': Array,
        'subarray1_snow_coverage': Array,
        'subarray1_snow_loss': Array,
        'subarray1_modeff': Array,
        'subarray1_celltemp': Array,
        'subarray1_dc_voltage': Array,
        'subarray1_dc_gross': Array,
        'subarray1_voc': Array,
        'subarray1_isc': Array,
        'subarray2_surf_tilt': Array,
        'subarray2_surf_azi': Array,
        'subarray2_aoi': Array,
        'subarray2_aoi_modifier': Array,
        'subarray2_axisrot': Array,
        'subarray2_idealrot': Array,
        'subarray2_poa_eff_beam': Array,
        'subarray2_poa_eff_diff': Array,
        'subarray2_poa_nom': Array,
        'subarray2_poa_shaded': Array,
        'subarray2_poa_shaded_soiled': Array,
        'subarray2_poa_front': Array,
        'subarray2_poa_rear': Array,
        'subarray2_poa_eff': Array,
        'subarray2_soiling_derate': Array,
        'subarray2_beam_shading_factor': Array,
        'subarray2_linear_derate': Array,
        'subarray2_ss_diffuse_derate': Array,
        'subarray2_ss_reflected_derate': Array,
        'subarray2_ss_derate': Array,
        'shadedb_subarray2_shade_frac': Array,
        'subarray2_snow_coverage': Array,
        'subarray2_snow_loss': Array,
        'subarray2_modeff': Array,
        'subarray2_celltemp': Array,
        'subarray2_dc_voltage': Array,
        'subarray2_dc_gross': Array,
        'subarray2_voc': Array,
        'subarray2_isc': Array,
        'subarray3_surf_tilt': Array,
        'subarray3_surf_azi': Array,
        'subarray3_aoi': Array,
        'subarray3_aoi_modifier': Array,
        'subarray3_axisrot': Array,
        'subarray3_idealrot': Array,
        'subarray3_poa_eff_beam': Array,
        'subarray3_poa_eff_diff': Array,
        'subarray3_poa_nom': Array,
        'subarray3_poa_shaded': Array,
        'subarray3_poa_shaded_soiled': Array,
        'subarray3_poa_front': Array,
        'subarray3_poa_rear': Array,
        'subarray3_poa_eff': Array,
        'subarray3_soiling_derate': Array,
        'subarray3_beam_shading_factor': Array,
        'subarray3_linear_derate': Array,
        'subarray3_ss_diffuse_derate': Array,
        'subarray3_ss_reflected_derate': Array,
        'subarray3_ss_derate': Array,
        'shadedb_subarray3_shade_frac': Array,
        'subarray3_snow_coverage': Array,
        'subarray3_snow_loss': Array,
        'subarray3_modeff': Array,
        'subarray3_celltemp': Array,
        'subarray3_dc_voltage': Array,
        'subarray3_dc_gross': Array,
        'subarray3_voc': Array,
        'subarray3_isc': Array,
        'subarray4_surf_tilt': Array,
        'subarray4_surf_azi': Array,
        'subarray4_aoi': Array,
        'subarray4_aoi_modifier': Array,
        'subarray4_axisrot': Array,
        'subarray4_idealrot': Array,
        'subarray4_poa_eff_beam': Array,
        'subarray4_poa_eff_diff': Array,
        'subarray4_poa_nom': Array,
        'subarray4_poa_shaded': Array,
        'subarray4_poa_shaded_soiled': Array,
        'subarray4_poa_front': Array,
        'subarray4_poa_rear': Array,
        'subarray4_poa_eff': Array,
        'subarray4_soiling_derate': Array,
        'subarray4_beam_shading_factor': Array,
        'subarray4_linear_derate': Array,
        'subarray4_ss_diffuse_derate': Array,
        'subarray4_ss_reflected_derate': Array,
        'subarray4_ss_derate': Array,
        'shadedb_subarray4_shade_frac': Array,
        'subarray4_snow_coverage': Array,
        'subarray4_snow_loss': Array,
        'subarray4_modeff': Array,
        'subarray4_celltemp': Array,
        'subarray4_dc_voltage': Array,
        'subarray4_dc_gross': Array,
        'subarray4_voc': Array,
        'subarray4_isc': Array,
        'poa_nom': Array,
        'poa_beam_nom': Array,
        'poa_beam_eff': Array,
        'poa_shaded': Array,
        'poa_shaded_soiled': Array,
        'poa_front': Array,
        'poa_rear': Array,
        'poa_eff': Array,
        'dc_snow_loss': Array,
        'dc_net': Array,
        'inverterMPPT1_DCVoltage': Array,
        'inverterMPPT2_DCVoltage': Array,
        'inverterMPPT3_DCVoltage': Array,
        'inverterMPPT4_DCVoltage': Array,
        'inv_eff': Array,
        'dc_invmppt_loss': Array,
        'inv_cliploss': Array,
        'inv_psoloss': Array,
        'inv_pntloss': Array,
        'inv_tdcloss': Array,
        'inv_total_loss': Array,
        'ac_wiring_loss': Array,
        'xfmr_nll_ts': Array,
        'xfmr_ll_ts': Array,
        'xfmr_loss_ts': Array,
        'ac_transmission_loss': Array,
        'ac_loss': float,
        'annual_energy': float,
        'annual_dc_invmppt_loss': float,
        'annual_inv_cliploss': float,
        'annual_inv_psoloss': float,
        'annual_inv_pntloss': float,
        'annual_inv_tdcloss': float,
        'subarray1_dcloss': float,
        'subarray2_dcloss': float,
        'subarray3_dcloss': float,
        'subarray4_dcloss': float,
        'xfmr_nll_year1': float,
        'xfmr_ll_year1': float,
        'xfmr_loss_year1': float,
        'monthly_poa_nom': Array,
        'monthly_poa_beam_nom': Array,
        'monthly_poa_front': Array,
        'monthly_poa_rear': Array,
        'monthly_poa_eff': Array,
        'monthly_poa_beam_eff': Array,
        'monthly_dc': Array,
        'monthly_energy': Array,
        'annual_gh': float,
        'annual_poa_nom': float,
        'annual_poa_beam_nom': float,
        'annual_poa_shaded': float,
        'annual_poa_shaded_soiled': float,
        'annual_poa_front': float,
        'annual_poa_rear': float,
        'annual_poa_eff': float,
        'annual_poa_beam_eff': float,
        'annual_dc_nominal': float,
        'annual_dc_gross': float,
        'annual_dc_net': float,
        'annual_ac_gross': float,
        'annual_dc_loss_ond': float,
        'annual_ac_loss_ond': float,
        'monthly_snow_loss': Array,
        'annual_snow_loss': float,
        'annual_subarray1_dc_gross': float,
        'annual_subarray1_dc_mismatch_loss': float,
        'annual_subarray1_dc_diodes_loss': float,
        'annual_subarray1_dc_wiring_loss': float,
        'annual_subarray1_dc_tracking_loss': float,
        'annual_subarray1_dc_nameplate_loss': float,
        'annual_subarray2_dc_gross': float,
        'annual_subarray2_dc_mismatch_loss': float,
        'annual_subarray2_dc_diodes_loss': float,
        'annual_subarray2_dc_wiring_loss': float,
        'annual_subarray2_dc_tracking_loss': float,
        'annual_subarray2_dc_nameplate_loss': float,
        'annual_subarray3_dc_gross': float,
        'annual_subarray3_dc_mismatch_loss': float,
        'annual_subarray3_dc_diodes_loss': float,
        'annual_subarray3_dc_wiring_loss': float,
        'annual_subarray3_dc_tracking_loss': float,
        'annual_subarray3_dc_nameplate_loss': float,
        'annual_subarray4_dc_gross': float,
        'annual_subarray4_dc_mismatch_loss': float,
        'annual_subarray4_dc_diodes_loss': float,
        'annual_subarray4_dc_wiring_loss': float,
        'annual_subarray4_dc_tracking_loss': float,
        'annual_subarray4_dc_nameplate_loss': float,
        'annual_dc_mismatch_loss': float,
        'annual_dc_diodes_loss': float,
        'annual_dc_wiring_loss': float,
        'annual_dc_tracking_loss': float,
        'annual_dc_nameplate_loss': float,
        'annual_dc_optimizer_loss': float,
        'annual_poa_shading_loss_percent': float,
        'annual_poa_soiling_loss_percent': float,
        'annual_poa_cover_loss_percent': float,
        'annual_poa_rear_gain_percent': float,
        'annual_dc_module_loss_percent': float,
        'annual_dc_snow_loss_percent': float,
        'annual_dc_mppt_clip_loss_percent': float,
        'annual_dc_mismatch_loss_percent': float,
        'annual_dc_diodes_loss_percent': float,
        'annual_dc_wiring_loss_percent': float,
        'annual_dc_tracking_loss_percent': float,
        'annual_dc_nameplate_loss_percent': float,
        'annual_dc_optimizer_loss_percent': float,
        'annual_dc_perf_adj_loss_percent': float,
        'annual_dc_lifetime_loss_percent': float,
        'annual_dc_battery_loss_percent': float,
        'annual_ac_inv_clip_loss_percent': float,
        'annual_ac_inv_pso_loss_percent': float,
        'annual_ac_inv_pnt_loss_percent': float,
        'annual_ac_inv_tdc_loss_percent': float,
        'annual_ac_inv_eff_loss_percent': float,
        'annual_ac_wiring_loss_percent': float,
        'annual_transmission_loss_percent': float,
        'annual_ac_lifetime_loss_percent': float,
        'annual_ac_battery_loss_percent': float,
        'annual_xfmr_loss_percent': float,
        'annual_ac_perf_adj_loss_percent': float,
        'annual_ac_wiring_loss': float,
        'annual_transmission_loss': float,
        '6par_a': float,
        '6par_Io': float,
        '6par_Il': float,
        '6par_Rs': float,
        '6par_Rsh': float,
        '6par_Adj': float,
        'performance_ratio': float,
        'capacity_factor': float,
        'capacity_factor_ac': float,
        'kwh_per_kw': float,
        'ts_shift_hours': float,
        'nameplate_dc_rating': float,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix,
        'dc_adjust:constant': float,
        'dc_adjust:hourly': Array,
        'dc_adjust:periods': Matrix,
        'gen': Array,
        'batt_chem': float,
        'inv_snl_eff_cec': float,
        'inv_pd_eff': float,
        'inv_cec_cg_eff_cec': float,
        'batt_ac_or_dc': float,
        'batt_dc_dc_efficiency': float,
        'batt_dc_ac_efficiency': float,
        'batt_ac_dc_efficiency': float,
        'batt_meter_position': float,
        'batt_losses': Array,
        'batt_losses_charging': Array,
        'batt_losses_discharging': Array,
        'batt_losses_idle': Array,
        'batt_loss_choice': float,
        'batt_current_choice': float,
        'batt_computed_strings': float,
        'batt_computed_series': float,
        'batt_computed_bank_capacity': float,
        'batt_current_charge_max': float,
        'batt_current_discharge_max': float,
        'batt_power_charge_max': float,
        'batt_power_discharge_max': float,
        'batt_voltage_choice': float,
        'batt_Vfull': float,
        'batt_Vexp': float,
        'batt_Vnom': float,
        'batt_Vnom_default': float,
        'batt_Qfull': float,
        'batt_Qfull_flow': float,
        'batt_Qexp': float,
        'batt_Qnom': float,
        'batt_C_rate': float,
        'batt_resistance': float,
        'batt_voltage_matrix': Matrix,
        'LeadAcid_q20_computed': float,
        'LeadAcid_q10_computed': float,
        'LeadAcid_qn_computed': float,
        'LeadAcid_tn': float,
        'batt_initial_SOC': float,
        'batt_minimum_SOC': float,
        'batt_maximum_SOC': float,
        'batt_minimum_modetime': float,
        'batt_lifetime_matrix': Matrix,
        'batt_calendar_choice': float,
        'batt_calendar_lifetime_matrix': Matrix,
        'batt_calendar_q0': float,
        'batt_calendar_a': float,
        'batt_calendar_b': float,
        'batt_calendar_c': float,
        'batt_replacement_capacity': float,
        'batt_replacement_option': float,
        'batt_replacement_schedule': Array,
        'batt_replacement_cost': float,
        'batt_mass': float,
        'batt_length': float,
        'batt_width': float,
        'batt_height': float,
        'batt_Cp': float,
        'batt_h_to_ambient': float,
        'T_room': float,
        'cap_vs_temp': Matrix,
        'dispatch_manual_charge': Array,
        'dispatch_manual_discharge': Array,
        'dispatch_manual_gridcharge': Array,
        'dispatch_manual_percent_discharge': Array,
        'dispatch_manual_percent_gridcharge': Array,
        'dispatch_manual_sched': Matrix,
        'dispatch_manual_sched_weekend': Matrix,
        'batt_target_power': Array,
        'batt_target_power_monthly': Array,
        'batt_target_choice': float,
        'batt_custom_dispatch': Array,
        'batt_dispatch_choice': float,
        'batt_pv_clipping_forecast': Array,
        'batt_pv_dc_forecast': Array,
        'batt_dispatch_auto_can_gridcharge': float,
        'batt_dispatch_auto_can_charge': float,
        'batt_dispatch_auto_can_clipcharge': float,
        'batt_auto_gridcharge_max_daily': float,
        'batt_look_ahead_hours': float,
        'batt_dispatch_update_frequency_hours': float,
        'batt_cycle_cost_choice': float,
        'batt_cycle_cost': float,
        'en_electricity_rates': float,
        'ur_ec_sched_weekday': Matrix,
        'ur_ec_sched_weekend': Matrix,
        'ur_ec_tou_mat': Matrix,
        'ppa_price_input': float,
        'ppa_multiplier_model': float,
        'dispatch_factors_ts': Array,
        'dispatch_tod_factors': Array,
        'dispatch_sched_weekday': Matrix,
        'dispatch_sched_weekend': Matrix,
        'batt_q0': Array,
        'batt_q1': Array,
        'batt_q2': Array,
        'batt_SOC': Array,
        'batt_DOD': Array,
        'batt_qmaxI': Array,
        'batt_qmax': Array,
        'batt_qmax_thermal': Array,
        'batt_I': Array,
        'batt_voltage_cell': Array,
        'batt_voltage': Array,
        'batt_DOD_cycle_average': Array,
        'batt_cycles': Array,
        'batt_temperature': Array,
        'batt_capacity_percent': Array,
        'batt_capacity_thermal_percent': Array,
        'batt_bank_replacement': Array,
        'batt_power': Array,
        'grid_power': Array,
        'pv_to_load': Array,
        'batt_to_load': Array,
        'grid_to_load': Array,
        'pv_to_batt': Array,
        'grid_to_batt': Array,
        'pv_to_grid': Array,
        'batt_to_grid': Array,
        'batt_conversion_loss': Array,
        'batt_system_loss': Array,
        'grid_power_target': Array,
        'batt_power_target': Array,
        'batt_cost_to_cycle': Array,
        'market_sell_rate_series_yr1': Array,
        'monthly_pv_to_load': Array,
        'monthly_batt_to_load': Array,
        'monthly_grid_to_load': Array,
        'monthly_pv_to_grid': Array,
        'monthly_batt_to_grid': Array,
        'monthly_pv_to_batt': Array,
        'monthly_grid_to_batt': Array,
        'batt_annual_charge_from_pv': Array,
        'batt_annual_charge_from_grid': Array,
        'batt_annual_charge_energy': Array,
        'batt_annual_discharge_energy': Array,
        'batt_annual_energy_loss': Array,
        'batt_annual_energy_system_loss': Array,
        'annual_export_to_grid_energy': Array,
        'annual_import_to_grid_energy': Array,
        'average_battery_conversion_efficiency': float,
        'average_battery_roundtrip_efficiency': float,
        'batt_pv_charge_percent': float,
        'batt_bank_installed_capacity': float,
        'batt_dispatch_sched': Matrix
}, total=False)

class Data(ssc.DataDict):
    solar_resource_file: str = INPUT(label='Weather file in TMY2, TMY3, EPW, or SAM CSV.', type='STRING', group='pvsamv1', required='?')
    solar_resource_data: Table = INPUT(label='Weather data', type='TABLE', group='pvsamv1', required='?', meta='lat,lon,tz,elev,year,month,hour,minute,gh,dn,df,poa,tdry,twet,tdew,rhum,pres,snow,alb,aod,wspd,wdir')
    transformer_no_load_loss: float = INPUT(label='Power transformer no load loss', units='%', type='NUMBER', group='pvsamv1', required='?=0')
    transformer_load_loss: float = INPUT(label='Power transformer load loss', units='%', type='NUMBER', group='pvsamv1', required='?=0')
    system_use_lifetime_output: float = INPUT(label='PV lifetime simulation', units='0/1', type='NUMBER', group='pvsamv1', required='?=0', constraints='INTEGER,MIN=0,MAX=1')
    analysis_period: float = INPUT(label='Lifetime analysis period', units='years', type='NUMBER', group='pvsamv1', required='system_use_lifetime_output=1')
    dc_degradation: Array = INPUT(label='Annual module degradation', units='%/year', type='ARRAY', group='pvsamv1', required='system_use_lifetime_output=1')
    dc_degrade_factor: Final[Array] = OUTPUT(label='Annual module degrade factor', type='ARRAY', group='Annual', required='system_use_lifetime_output=1')
    en_dc_lifetime_losses: float = INPUT(label='Enable lifetime daily DC losses', units='0/1', type='NUMBER', group='pvsamv1', required='?=0', constraints='INTEGER,MIN=0,MAX=1')
    dc_lifetime_losses: Array = INPUT(label='Lifetime daily DC losses', units='%', type='ARRAY', group='pvsamv1', required='en_dc_lifetime_losses=1')
    en_ac_lifetime_losses: float = INPUT(label='Enable lifetime daily AC losses', units='0/1', type='NUMBER', group='pvsamv1', required='?=0', constraints='INTEGER,MIN=0,MAX=1')
    ac_lifetime_losses: Array = INPUT(label='Lifetime daily AC losses', units='%', type='ARRAY', group='pvsamv1', required='en_ac_lifetime_losses=1')
    en_snow_model: float = INPUT(label='Toggle snow loss estimation', units='0/1', type='NUMBER', group='snowmodel', required='?=0', constraints='BOOLEAN')
    system_capacity: float = INPUT(label='DC Nameplate capacity', units='kWdc', type='NUMBER', group='pvsamv1', required='*')
    use_wf_albedo: float = INPUT(label='Use albedo in weather file if provided', units='0/1', type='NUMBER', group='pvsamv1', required='?=1', constraints='BOOLEAN')
    albedo: Array = INPUT(label='User specified ground albedo', units='0..1', type='ARRAY', group='pvsamv1', required='*', constraints='LENGTH=12')
    irrad_mode: float = INPUT(label='Irradiance input translation mode', type='NUMBER', group='pvsamv1', required='?=0', constraints='INTEGER,MIN=0,MAX=4', meta='0=beam&diffuse,1=total&beam,2=total&diffuse,3=poa_reference,4=poa_pyranometer')
    sky_model: float = INPUT(label='Diffuse sky model', type='NUMBER', group='pvsamv1', required='?=2', constraints='INTEGER,MIN=0,MAX=2', meta='0=isotropic,1=hkdr,2=perez')
    inverter_count: float = INPUT(label='Number of inverters', type='NUMBER', group='pvsamv1', required='*', constraints='INTEGER,POSITIVE')
    enable_mismatch_vmax_calc: float = INPUT(label='Enable mismatched subarray Vmax calculation', type='NUMBER', group='pvsamv1', required='?=0', constraints='BOOLEAN')
    subarray1_nstrings: float = INPUT(label='Sub-array 1 Number of parallel strings', type='NUMBER', group='pvsamv1', constraints='INTEGER')
    subarray1_modules_per_string: float = INPUT(label='Sub-array 1 Modules per string', type='NUMBER', group='pvsamv1', required='*', constraints='INTEGER,POSITIVE')
    subarray1_mppt_input: float = INPUT(label='Sub-array 1 Inverter MPPT input number', type='NUMBER', group='pvsamv1', required='?=1', constraints='INTEGER,POSITIVE')
    subarray1_tilt: float = INPUT(label='Sub-array 1 Tilt', units='deg', type='NUMBER', group='pvsamv1', constraints='MIN=0,MAX=90', meta='0=horizontal,90=vertical')
    subarray1_tilt_eq_lat: float = INPUT(label='Sub-array 1 Tilt=latitude override', units='0/1', type='NUMBER', group='pvsamv1', constraints='BOOLEAN')
    subarray1_azimuth: float = INPUT(label='Sub-array 1 Azimuth', units='deg', type='NUMBER', group='pvsamv1', constraints='MIN=0,MAX=359.9', meta='0=N,90=E,180=S,270=W')
    subarray1_track_mode: float = INPUT(label='Sub-array 1 Tracking mode', type='NUMBER', group='pvsamv1', required='*', constraints='INTEGER,MIN=0,MAX=4', meta='0=fixed,1=1axis,2=2axis,3=azi,4=monthly')
    subarray1_rotlim: float = INPUT(label='Sub-array 1 Tracker rotation limit', units='deg', type='NUMBER', group='pvsamv1', required='?=45', constraints='MIN=0,MAX=85')
    subarray1_shade_mode: float = INPUT(label='Sub-array 1 shading mode (fixed tilt or 1x tracking)', units='0/1/2', type='NUMBER', group='pvsamv1', required='*', constraints='INTEGER,MIN=0,MAX=2', meta='0=none,1=standard(non-linear),2=thin film(linear)')
    subarray1_gcr: float = INPUT(label='Sub-array 1 Ground coverage ratio', units='0..1', type='NUMBER', group='pvsamv1', required='?=0.3', constraints='MIN=0,MAX=3')
    subarray1_monthly_tilt: Array = INPUT(label='Sub-array 1 monthly tilt input', units='deg', type='ARRAY', group='pvsamv1', required='subarray1_track_mode=4', constraints='LENGTH=12')
    subarray1_shading_string_option: float = INPUT(name='subarray1_shading:string_option', label='Sub-array 1 shading string option', type='NUMBER', group='pvsamv1', required='?=-1', constraints='INTEGER,MIN=-1,MAX=4', meta='0=shadingdb,1=shadingdb_notc,2=average,3=maximum,4=minimum')
    subarray1_shading_timestep: Matrix = INPUT(name='subarray1_shading:timestep', label='Sub-array 1 timestep beam shading losses', units='%', type='MATRIX', group='pvsamv1', required='?')
    subarray1_shading_mxh: Matrix = INPUT(name='subarray1_shading:mxh', label='Sub-array 1 Month x Hour beam shading losses', units='%', type='MATRIX', group='pvsamv1', required='?')
    subarray1_shading_azal: Matrix = INPUT(name='subarray1_shading:azal', label='Sub-array 1 Azimuth x altitude beam shading losses', units='%', type='MATRIX', group='pvsamv1', required='?')
    subarray1_shading_diff: float = INPUT(name='subarray1_shading:diff', label='Sub-array 1 Diffuse shading loss', units='%', type='NUMBER', group='pvsamv1', required='?')
    subarray1_soiling: Array = INPUT(label='Sub-array 1 Monthly soiling loss', units='%', type='ARRAY', group='pvsamv1', required='*', constraints='LENGTH=12')
    subarray1_rear_irradiance_loss: float = INPUT(label='Sub-array 1 rear irradiance loss', units='%', type='NUMBER', group='pvsamv1', required='*', constraints='MIN=0,MAX=100')
    subarray1_mismatch_loss: float = INPUT(label='Sub-array 1 DC mismatch loss', units='%', type='NUMBER', group='pvsamv1', required='*', constraints='MIN=0,MAX=100')
    subarray1_diodeconn_loss: float = INPUT(label='Sub-array 1 DC diodes and connections loss', units='%', type='NUMBER', group='pvsamv1', required='*', constraints='MIN=0,MAX=100')
    subarray1_dcwiring_loss: float = INPUT(label='Sub-array 1 DC wiring loss', units='%', type='NUMBER', group='pvsamv1', required='*', constraints='MIN=0,MAX=100')
    subarray1_tracking_loss: float = INPUT(label='Sub-array 1 DC tracking error loss', units='%', type='NUMBER', group='pvsamv1', required='*', constraints='MIN=0,MAX=100')
    subarray1_nameplate_loss: float = INPUT(label='Sub-array 1 DC nameplate loss', units='%', type='NUMBER', group='pvsamv1', required='*', constraints='MIN=-5,MAX=100')
    subarray2_rear_irradiance_loss: float = INPUT(label='Sub-array 2 rear irradiance loss', units='%', type='NUMBER', group='pvsamv1', required='subarray2_enable=1', constraints='MIN=0,MAX=100')
    subarray2_mismatch_loss: float = INPUT(label='Sub-array 2 DC mismatch loss', units='%', type='NUMBER', group='pvsamv1', required='?', constraints='MIN=0,MAX=100')
    subarray2_diodeconn_loss: float = INPUT(label='Sub-array 2 DC diodes and connections loss', units='%', type='NUMBER', group='pvsamv1', required='?', constraints='MIN=0,MAX=100')
    subarray2_dcwiring_loss: float = INPUT(label='Sub-array 2 DC wiring loss', units='%', type='NUMBER', group='pvsamv1', required='?', constraints='MIN=0,MAX=100')
    subarray2_tracking_loss: float = INPUT(label='Sub-array 2 DC tracking error loss', units='%', type='NUMBER', group='pvsamv1', required='?', constraints='MIN=0,MAX=100')
    subarray2_nameplate_loss: float = INPUT(label='Sub-array 2 DC nameplate loss', units='%', type='NUMBER', group='pvsamv1', required='?', constraints='MIN=-5,MAX=100')
    subarray3_rear_irradiance_loss: float = INPUT(label='Sub-array 3 rear irradiance loss', units='%', type='NUMBER', group='pvsamv1', required='subarray3_enable=1', constraints='MIN=0,MAX=100')
    subarray3_mismatch_loss: float = INPUT(label='Sub-array 3 DC mismatch loss', units='%', type='NUMBER', group='pvsamv1', required='?', constraints='MIN=0,MAX=100')
    subarray3_diodeconn_loss: float = INPUT(label='Sub-array 3 DC diodes and connections loss', units='%', type='NUMBER', group='pvsamv1', required='?', constraints='MIN=0,MAX=100')
    subarray3_dcwiring_loss: float = INPUT(label='Sub-array 3 DC wiring loss', units='%', type='NUMBER', group='pvsamv1', required='?', constraints='MIN=0,MAX=100')
    subarray3_tracking_loss: float = INPUT(label='Sub-array 3 DC tracking error loss', units='%', type='NUMBER', group='pvsamv1', required='?', constraints='MIN=0,MAX=100')
    subarray3_nameplate_loss: float = INPUT(label='Sub-array 3 DC nameplate loss', units='%', type='NUMBER', group='pvsamv1', required='?', constraints='MIN=-5,MAX=100')
    subarray4_rear_irradiance_loss: float = INPUT(label='Sub-array 4 rear irradiance loss', units='%', type='NUMBER', group='pvsamv1', required='subarray4_enable=1', constraints='MIN=0,MAX=100')
    subarray4_mismatch_loss: float = INPUT(label='Sub-array 4 DC mismatch loss', units='%', type='NUMBER', group='pvsamv1', required='?', constraints='MIN=0,MAX=100')
    subarray4_diodeconn_loss: float = INPUT(label='Sub-array 4 DC diodes and connections loss', units='%', type='NUMBER', group='pvsamv1', required='?', constraints='MIN=0,MAX=100', meta='?')
    subarray4_dcwiring_loss: float = INPUT(label='Sub-array 4 DC wiring loss', units='%', type='NUMBER', group='pvsamv1', required='?', constraints='MIN=0,MAX=100')
    subarray4_tracking_loss: float = INPUT(label='Sub-array 4 DC tracking error loss', units='%', type='NUMBER', group='pvsamv1', required='?', constraints='MIN=0,MAX=100')
    subarray4_nameplate_loss: float = INPUT(label='Sub-array 4 DC nameplate loss', units='%', type='NUMBER', group='pvsamv1', required='?', constraints='MIN=-5,MAX=100')
    dcoptimizer_loss: float = INPUT(label='DC power optimizer loss', units='%', type='NUMBER', group='pvsamv1', required='*', constraints='MIN=0,MAX=100')
    acwiring_loss: float = INPUT(label='AC wiring loss', units='%', type='NUMBER', group='pvsamv1', required='*', constraints='MIN=0,MAX=100')
    transmission_loss: float = INPUT(label='Transmission loss', units='%', type='NUMBER', group='pvsamv1', required='*', constraints='MIN=0,MAX=100')
    subarray1_mod_orient: float = INPUT(label='Sub-array 1 Module orientation', units='0/1', type='NUMBER', group='pvsamv1', required='*', constraints='INTEGER,MIN=0,MAX=1', meta='0=portrait,1=landscape')
    subarray1_nmodx: float = INPUT(label='Sub-array 1 Number of modules along bottom of row', type='NUMBER', group='pvsamv1', required='*', constraints='INTEGER,POSITIVE')
    subarray1_nmody: float = INPUT(label='Sub-array 1 Number of modules along side of row', type='NUMBER', group='pvsamv1', required='*', constraints='INTEGER,POSITIVE')
    subarray1_backtrack: float = INPUT(label='Sub-array 1 Backtracking enabled', type='NUMBER', group='pvsamv1', required='subarray1_track_mode=1', constraints='BOOLEAN', meta='0=no backtracking,1=backtrack')
    subarray2_enable: float = INPUT(label='Sub-array 2 Enable', units='0/1', type='NUMBER', group='pvsamv1', required='?=0', constraints='BOOLEAN', meta='0=disabled,1=enabled')
    subarray2_modules_per_string: float = INPUT(label='Sub-array 2 Modules per string', type='NUMBER', group='pvsamv1', required='subarray2_enable=1', constraints='INTEGER,MIN=1')
    subarray2_nstrings: float = INPUT(label='Sub-array 2 Number of parallel strings', type='NUMBER', group='pvsamv1', required='subarray2_enable=1', constraints='INTEGER,MIN=1')
    subarray2_mppt_input: float = INPUT(label='Sub-array 2 Inverter MPPT input number', type='NUMBER', group='pvsamv1', required='?=1', constraints='INTEGER,POSITIVE')
    subarray2_tilt: float = INPUT(label='Sub-array 2 Tilt', units='deg', type='NUMBER', group='pvsamv1', constraints='MIN=0,MAX=90', meta='0=horizontal,90=vertical')
    subarray2_tilt_eq_lat: float = INPUT(label='Sub-array 2 Tilt=latitude override', units='0/1', type='NUMBER', group='pvsamv1', constraints='BOOLEAN')
    subarray2_azimuth: float = INPUT(label='Sub-array 2 Azimuth', units='deg', type='NUMBER', group='pvsamv1', constraints='MIN=0,MAX=359.9', meta='0=N,90=E,180=S,270=W')
    subarray2_track_mode: float = INPUT(label='Sub-array 2 Tracking mode', type='NUMBER', group='pvsamv1', required='subarray2_enable=1', constraints='INTEGER,MIN=0,MAX=4', meta='0=fixed,1=1axis,2=2axis,3=azi,4=monthly')
    subarray2_rotlim: float = INPUT(label='Sub-array 2 Tracker rotation limit', units='deg', type='NUMBER', group='pvsamv1', required='?=45', constraints='MIN=0,MAX=85')
    subarray2_shade_mode: float = INPUT(label='Sub-array 2 Shading mode (fixed tilt or 1x tracking)', units='0/1/2', type='NUMBER', group='pvsamv1', required='subarray2_enable=1', constraints='INTEGER,MIN=0,MAX=2', meta='0=none,1=standard(non-linear),2=thin film(linear)')
    subarray2_gcr: float = INPUT(label='Sub-array 2 Ground coverage ratio', units='0..1', type='NUMBER', group='pvsamv1', required='?=0.3', constraints='MIN=0,MAX=3')
    subarray2_monthly_tilt: Array = INPUT(label='Sub-array 2 Monthly tilt input', units='deg', type='ARRAY', group='pvsamv1', constraints='LENGTH=12')
    subarray2_shading_string_option: float = INPUT(name='subarray2_shading:string_option', label='Sub-array 2 Shading string option', type='NUMBER', group='pvsamv1', required='?=-1', constraints='INTEGER,MIN=-1,MAX=4', meta='0=shadingdb,1=shadingdb_notc,2=average,3=maximum,4=minimum')
    subarray2_shading_timestep: Matrix = INPUT(name='subarray2_shading:timestep', label='Sub-array 2 Timestep beam shading losses', units='%', type='MATRIX', group='pvsamv1', required='?')
    subarray2_shading_mxh: Matrix = INPUT(name='subarray2_shading:mxh', label='Sub-array 2 Month x Hour beam shading losses', units='%', type='MATRIX', group='pvsamv1', required='?')
    subarray2_shading_azal: Matrix = INPUT(name='subarray2_shading:azal', label='Sub-array 2 Azimuth x altitude beam shading losses', units='%', type='MATRIX', group='pvsamv1', required='?')
    subarray2_shading_diff: float = INPUT(name='subarray2_shading:diff', label='Sub-array 2 Diffuse shading loss', units='%', type='NUMBER', group='pvsamv1', required='?')
    subarray2_soiling: Array = INPUT(label='Sub-array 2 Monthly soiling loss', units='%', type='ARRAY', group='pvsamv1', required='subarray2_enable=1', constraints='LENGTH=12')
    subarray2_mod_orient: float = INPUT(label='Sub-array 2 Module orientation', units='0/1', type='NUMBER', group='pvsamv1', required='subarray2_enable=1', constraints='INTEGER,MIN=0,MAX=1', meta='0=portrait,1=landscape')
    subarray2_nmodx: float = INPUT(label='Sub-array 2 Number of modules along bottom of row', type='NUMBER', group='pvsamv1', required='subarray2_enable=1', constraints='INTEGER,POSITIVE')
    subarray2_nmody: float = INPUT(label='Sub-array 2 Number of modules along side of row', type='NUMBER', group='pvsamv1', required='subarray2_enable=1', constraints='INTEGER,POSITIVE')
    subarray2_backtrack: float = INPUT(label='Sub-array 2 Backtracking enabled', type='NUMBER', group='pvsamv1', constraints='BOOLEAN', meta='0=no backtracking,1=backtrack')
    subarray3_enable: float = INPUT(label='Sub-array 3 Enable', units='0/1', type='NUMBER', group='pvsamv1', required='?=0', constraints='BOOLEAN', meta='0=disabled,1=enabled')
    subarray3_modules_per_string: float = INPUT(label='Sub-array 3 Modules per string', type='NUMBER', group='pvsamv1', required='subarray3_enable=1', constraints='INTEGER,MIN=1')
    subarray3_nstrings: float = INPUT(label='Sub-array 3 Number of parallel strings', type='NUMBER', group='pvsamv1', required='subarray3_enable=1', constraints='INTEGER,MIN=1')
    subarray3_mppt_input: float = INPUT(label='Sub-array 3 Inverter MPPT input number', type='NUMBER', group='pvsamv1', required='?=1', constraints='INTEGER,POSITIVE')
    subarray3_tilt: float = INPUT(label='Sub-array 3 Tilt', units='deg', type='NUMBER', group='pvsamv1', constraints='MIN=0,MAX=90', meta='0=horizontal,90=vertical')
    subarray3_tilt_eq_lat: float = INPUT(label='Sub-array 3 Tilt=latitude override', units='0/1', type='NUMBER', group='pvsamv1', constraints='BOOLEAN')
    subarray3_azimuth: float = INPUT(label='Sub-array 3 Azimuth', units='deg', type='NUMBER', group='pvsamv1', constraints='MIN=0,MAX=359.9', meta='0=N,90=E,180=S,270=W')
    subarray3_track_mode: float = INPUT(label='Sub-array 3 Tracking mode', type='NUMBER', group='pvsamv1', required='subarray3_enable=1', constraints='INTEGER,MIN=0,MAX=4', meta='0=fixed,1=1axis,2=2axis,3=azi,4=monthly')
    subarray3_rotlim: float = INPUT(label='Sub-array 3 Tracker rotation limit', units='deg', type='NUMBER', group='pvsamv1', required='?=45', constraints='MIN=0,MAX=85')
    subarray3_shade_mode: float = INPUT(label='Sub-array 3 Shading mode (fixed tilt or 1x tracking)', units='0/1/2', type='NUMBER', group='pvsamv1', required='subarray3_enable=1', constraints='INTEGER,MIN=0,MAX=2', meta='0=none,1=standard(non-linear),2=thin film(linear)')
    subarray3_gcr: float = INPUT(label='Sub-array 3 Ground coverage ratio', units='0..1', type='NUMBER', group='pvsamv1', required='?=0.3', constraints='MIN=0,MAX=3')
    subarray3_monthly_tilt: Array = INPUT(label='Sub-array 3 Monthly tilt input', units='deg', type='ARRAY', group='pvsamv1', constraints='LENGTH=12')
    subarray3_shading_string_option: float = INPUT(name='subarray3_shading:string_option', label='Sub-array 3 Shading string option', type='NUMBER', group='pvsamv1', required='?=-1', constraints='INTEGER,MIN=-1,MAX=4', meta='0=shadingdb,1=shadingdb_notc,2=average,3=maximum,4=minimum')
    subarray3_shading_timestep: Matrix = INPUT(name='subarray3_shading:timestep', label='Sub-array 3 Timestep beam shading losses', units='%', type='MATRIX', group='pvsamv1', required='?')
    subarray3_shading_mxh: Matrix = INPUT(name='subarray3_shading:mxh', label='Sub-array 3 Month x Hour beam shading losses', units='%', type='MATRIX', group='pvsamv1', required='?')
    subarray3_shading_azal: Matrix = INPUT(name='subarray3_shading:azal', label='Sub-array 3 Azimuth x altitude beam shading losses', units='%', type='MATRIX', group='pvsamv1', required='?')
    subarray3_shading_diff: float = INPUT(name='subarray3_shading:diff', label='Sub-array 3 Diffuse shading loss', units='%', type='NUMBER', group='pvsamv1', required='?')
    subarray3_soiling: Array = INPUT(label='Sub-array 3 Monthly soiling loss', units='%', type='ARRAY', group='pvsamv1', required='subarray3_enable=1', constraints='LENGTH=12')
    subarray3_mod_orient: float = INPUT(label='Sub-array 3 Module orientation', units='0/1', type='NUMBER', group='pvsamv1', required='subarray3_enable=1', constraints='INTEGER,MIN=0,MAX=1', meta='0=portrait,1=landscape')
    subarray3_nmodx: float = INPUT(label='Sub-array 3 Number of modules along bottom of row', type='NUMBER', group='pvsamv1', required='subarray3_enable=1', constraints='INTEGER,POSITIVE')
    subarray3_nmody: float = INPUT(label='Sub-array 3 Number of modules along side of row', type='NUMBER', group='pvsamv1', required='subarray3_enable=1', constraints='INTEGER,POSITIVE')
    subarray3_backtrack: float = INPUT(label='Sub-array 3 Backtracking enabled', type='NUMBER', group='pvsamv1', constraints='BOOLEAN', meta='0=no backtracking,1=backtrack')
    subarray4_enable: float = INPUT(label='Sub-array 4 Enable', units='0/1', type='NUMBER', group='pvsamv1', required='?=0', constraints='BOOLEAN', meta='0=disabled,1=enabled')
    subarray4_modules_per_string: float = INPUT(label='Sub-array 4 Modules per string', type='NUMBER', group='pvsamv1', required='subarray4_enable=1', constraints='INTEGER,MIN=1')
    subarray4_nstrings: float = INPUT(label='Sub-array 4 Number of parallel strings', type='NUMBER', group='pvsamv1', required='subarray4_enable=1', constraints='INTEGER,MIN=1')
    subarray4_mppt_input: float = INPUT(label='Sub-array 4 Inverter MPPT input number', type='NUMBER', group='pvsamv1', required='?=1', constraints='INTEGER,POSITIVE')
    subarray4_tilt: float = INPUT(label='Sub-array 4 Tilt', units='deg', type='NUMBER', group='pvsamv1', constraints='MIN=0,MAX=90', meta='0=horizontal,90=vertical')
    subarray4_tilt_eq_lat: float = INPUT(label='Sub-array 4 Tilt=latitude override', units='0/1', type='NUMBER', group='pvsamv1', constraints='BOOLEAN')
    subarray4_azimuth: float = INPUT(label='Sub-array 4 Azimuth', units='deg', type='NUMBER', group='pvsamv1', constraints='MIN=0,MAX=359.9', meta='0=N,90=E,180=S,270=W')
    subarray4_track_mode: float = INPUT(label='Sub-array 4 Tracking mode', type='NUMBER', group='pvsamv1', required='subarray4_enable=1', constraints='INTEGER,MIN=0,MAX=4', meta='0=fixed,1=1axis,2=2axis,3=azi,4=monthly')
    subarray4_rotlim: float = INPUT(label='Sub-array 4 Tracker rotation limit', units='deg', type='NUMBER', group='pvsamv1', required='?=45', constraints='MIN=0,MAX=85')
    subarray4_shade_mode: float = INPUT(label='Sub-array 4 shading mode (fixed tilt or 1x tracking)', units='0/1/2', type='NUMBER', group='pvsamv1', required='subarray4_enable=1', constraints='INTEGER,MIN=0,MAX=2', meta='0=none,1=standard(non-linear),2=thin film(linear)')
    subarray4_gcr: float = INPUT(label='Sub-array 4 Ground coverage ratio', units='0..1', type='NUMBER', group='pvsamv1', required='?=0.3', constraints='MIN=0,MAX=3')
    subarray4_monthly_tilt: Array = INPUT(label='Sub-array 4 Monthly tilt input', units='deg', type='ARRAY', group='pvsamv1', constraints='LENGTH=12')
    subarray4_shading_string_option: float = INPUT(name='subarray4_shading:string_option', label='Sub-array 4 Shading string option', type='NUMBER', group='pvsamv1', required='?=-1', constraints='INTEGER,MIN=-1,MAX=4', meta='0=shadingdb,1=shadingdb_notc,2=average,3=maximum,4=minimum')
    subarray4_shading_timestep: Matrix = INPUT(name='subarray4_shading:timestep', label='Sub-array 4 Timestep beam shading losses', units='%', type='MATRIX', group='pvsamv1', required='?')
    subarray4_shading_mxh: Matrix = INPUT(name='subarray4_shading:mxh', label='Sub-array 4 Month x Hour beam shading losses', units='%', type='MATRIX', group='pvsamv1', required='?')
    subarray4_shading_azal: Matrix = INPUT(name='subarray4_shading:azal', label='Sub-array 4 Azimuth x altitude beam shading losses', units='%', type='MATRIX', group='pvsamv1', required='?')
    subarray4_shading_diff: float = INPUT(name='subarray4_shading:diff', label='Sub-array 4 Diffuse shading loss', units='%', type='NUMBER', group='pvsamv1', required='?')
    subarray4_soiling: Array = INPUT(label='Sub-array 4 Monthly soiling loss', units='%', type='ARRAY', group='pvsamv1', required='subarray4_enable=1', constraints='LENGTH=12')
    subarray4_mod_orient: float = INPUT(label='Sub-array 4 Module orientation', units='0/1', type='NUMBER', group='pvsamv1', required='subarray4_enable=1', constraints='INTEGER,MIN=0,MAX=1', meta='0=portrait,1=landscape')
    subarray4_nmodx: float = INPUT(label='Sub-array 4 Number of modules along bottom of row', type='NUMBER', group='pvsamv1', required='subarray4_enable=1', constraints='INTEGER,POSITIVE')
    subarray4_nmody: float = INPUT(label='Sub-array 4 Number of modules along side of row', type='NUMBER', group='pvsamv1', required='subarray4_enable=1', constraints='INTEGER,POSITIVE')
    subarray4_backtrack: float = INPUT(label='Sub-array 4 Backtracking enabled', type='NUMBER', group='pvsamv1', constraints='BOOLEAN', meta='0=no backtracking,1=backtrack')
    module_model: float = INPUT(label='Photovoltaic module model specifier', type='NUMBER', group='pvsamv1', required='*', constraints='INTEGER,MIN=0,MAX=5', meta='0=spe,1=cec,2=6par_user,3=snl,4=sd11-iec61853,5=PVYield')
    module_aspect_ratio: float = INPUT(label='Module aspect ratio', type='NUMBER', group='pvsamv1', required='?=1.7')
    spe_area: float = INPUT(label='Module area', units='m2', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_rad0: float = INPUT(label='Irradiance level 0', units='W/m2', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_rad1: float = INPUT(label='Irradiance level 1', units='W/m2', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_rad2: float = INPUT(label='Irradiance level 2', units='W/m2', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_rad3: float = INPUT(label='Irradiance level 3', units='W/m2', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_rad4: float = INPUT(label='Irradiance level 4', units='W/m2', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_eff0: float = INPUT(label='Efficiency at irradiance level 0', units='%', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_eff1: float = INPUT(label='Efficiency at irradiance level 1', units='%', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_eff2: float = INPUT(label='Efficiency at irradiance level 2', units='%', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_eff3: float = INPUT(label='Efficiency at irradiance level 3', units='%', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_eff4: float = INPUT(label='Efficiency at irradiance level 4', units='%', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_reference: float = INPUT(label='Reference irradiance level', type='NUMBER', group='pvsamv1', required='module_model=0', constraints='INTEGER,MIN=0,MAX=4')
    spe_module_structure: float = INPUT(label='Mounting and module structure', type='NUMBER', group='pvsamv1', required='module_model=0', constraints='INTEGER,MIN=0,MAX=5', meta='0=glass/cell/polymer sheet - open rack,1=glass/cell/glass - open rack,2=polymer/thin film/steel - open rack,3=Insulated back, building-integrated PV,4=close roof mount,5=user-defined')
    spe_a: float = INPUT(label='Cell temp parameter a', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_b: float = INPUT(label='Cell temp parameter b', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_dT: float = INPUT(label='Cell temp parameter dT', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_temp_coeff: float = INPUT(label='Temperature coefficient', units='%/C', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_fd: float = INPUT(label='Diffuse fraction', units='0..1', type='NUMBER', group='pvsamv1', required='module_model=0', constraints='MIN=0,MAX=1')
    spe_vmp: float = INPUT(label='Nominal max power voltage', units='V', type='NUMBER', group='pvsamv1', required='module_model=0', constraints='POSITIVE')
    spe_voc: float = INPUT(label='Nominal open circuit voltage', units='V', type='NUMBER', group='pvsamv1', required='module_model=0', constraints='POSITIVE')
    spe_is_bifacial: float = INPUT(label='Modules are bifacial', units='0/1', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_bifacial_transmission_factor: float = INPUT(label='Bifacial transmission factor', units='0-1', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_bifaciality: float = INPUT(label='Bifaciality factor', units='%', type='NUMBER', group='pvsamv1', required='module_model=0')
    spe_bifacial_ground_clearance_height: float = INPUT(label='Module ground clearance height', units='m', type='NUMBER', group='pvsamv1', required='module_model=0')
    cec_area: float = INPUT(label='Module area', units='m2', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_a_ref: float = INPUT(label='Nonideality factor a', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_adjust: float = INPUT(label='Temperature coefficient adjustment', units='%', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_alpha_sc: float = INPUT(label='Short circuit current temperature coefficient', units='A/C', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_beta_oc: float = INPUT(label='Open circuit voltage temperature coefficient', units='V/C', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_gamma_r: float = INPUT(label='Maximum power point temperature coefficient', units='%/C', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_i_l_ref: float = INPUT(label='Light current', units='A', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_i_mp_ref: float = INPUT(label='Maximum power point current', units='A', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_i_o_ref: float = INPUT(label='Saturation current', units='A', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_i_sc_ref: float = INPUT(label='Short circuit current', units='A', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_n_s: float = INPUT(label='Number of cells in series', type='NUMBER', group='pvsamv1', required='module_model=1', constraints='POSITIVE')
    cec_r_s: float = INPUT(label='Series resistance', units='ohm', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_r_sh_ref: float = INPUT(label='Shunt resistance', units='ohm', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_t_noct: float = INPUT(label='Nominal operating cell temperature', units='C', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_v_mp_ref: float = INPUT(label='Maximum power point voltage', units='V', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_v_oc_ref: float = INPUT(label='Open circuit voltage', units='V', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_temp_corr_mode: float = INPUT(label='Cell temperature model selection', type='NUMBER', group='pvsamv1', required='module_model=1', constraints='INTEGER,MIN=0,MAX=1', meta='0=noct,1=mc')
    cec_is_bifacial: float = INPUT(label='Modules are bifacial', units='0/1', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_bifacial_transmission_factor: float = INPUT(label='Bifacial transmission factor', units='0-1', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_bifaciality: float = INPUT(label='Bifaciality factor', units='%', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_bifacial_ground_clearance_height: float = INPUT(label='Module ground clearance height', units='m', type='NUMBER', group='pvsamv1', required='module_model=1')
    cec_standoff: float = INPUT(label='Standoff mode', type='NUMBER', group='pvsamv1', required='module_model=1', constraints='INTEGER,MIN=0,MAX=6', meta='0=bipv,1=>3.5in,2=2.5-3.5in,3=1.5-2.5in,4=0.5-1.5in,5=<0.5in,6=ground/rack')
    cec_height: float = INPUT(label='Array mounting height', type='NUMBER', group='pvsamv1', required='module_model=1', constraints='INTEGER,MIN=0,MAX=1', meta='0=one story,1=two story')
    cec_mounting_config: float = INPUT(label='Mounting configuration', type='NUMBER', group='pvsamv1', required='module_model=1&cec_temp_corr_mode=1', constraints='INTEGER,MIN=0,MAX=3', meta='0=rack,1=flush,2=integrated,3=gap')
    cec_heat_transfer: float = INPUT(label='Heat transfer dimensions', type='NUMBER', group='pvsamv1', required='module_model=1&cec_temp_corr_mode=1', constraints='INTEGER,MIN=0,MAX=1', meta='0=module,1=array')
    cec_mounting_orientation: float = INPUT(label='Mounting structure orientation', type='NUMBER', group='pvsamv1', required='module_model=1&cec_temp_corr_mode=1', constraints='INTEGER,MIN=0,MAX=2', meta='0=do not impede flow,1=vertical supports,2=horizontal supports')
    cec_gap_spacing: float = INPUT(label='Gap spacing', units='m', type='NUMBER', group='pvsamv1', required='module_model=1&cec_temp_corr_mode=1')
    cec_module_width: float = INPUT(label='Module width', units='m', type='NUMBER', group='pvsamv1', required='module_model=1&cec_temp_corr_mode=1')
    cec_module_length: float = INPUT(label='Module height', units='m', type='NUMBER', group='pvsamv1', required='module_model=1&cec_temp_corr_mode=1')
    cec_array_rows: float = INPUT(label='Rows of modules in array', type='NUMBER', group='pvsamv1', required='module_model=1&cec_temp_corr_mode=1')
    cec_array_cols: float = INPUT(label='Columns of modules in array', type='NUMBER', group='pvsamv1', required='module_model=1&cec_temp_corr_mode=1')
    cec_backside_temp: float = INPUT(label='Module backside temperature', units='C', type='NUMBER', group='pvsamv1', required='module_model=1&cec_temp_corr_mode=1', constraints='POSITIVE')
    _6par_celltech: float = INPUT(name='6par_celltech', label='Solar cell technology type', type='NUMBER', group='pvsamv1', required='module_model=2', constraints='INTEGER,MIN=0,MAX=5', meta='monoSi=0,multiSi=1,CdTe=2,CIS=3,CIGS=4,Amorphous=5')
    _6par_vmp: float = INPUT(name='6par_vmp', label='Maximum power point voltage', units='V', type='NUMBER', group='pvsamv1', required='module_model=2')
    _6par_imp: float = INPUT(name='6par_imp', label='Imp', units='A', type='NUMBER', group='pvsamv1', required='module_model=2')
    _6par_voc: float = INPUT(name='6par_voc', label='Voc', units='V', type='NUMBER', group='pvsamv1', required='module_model=2')
    _6par_isc: float = INPUT(name='6par_isc', label='Isc', units='A', type='NUMBER', group='pvsamv1', required='module_model=2')
    _6par_bvoc: float = INPUT(name='6par_bvoc', label='Open circuit voltage temperature coefficient', units='V/C', type='NUMBER', group='pvsamv1', required='module_model=2')
    _6par_aisc: float = INPUT(name='6par_aisc', label='Short circuit current temperature coefficient', units='A/C', type='NUMBER', group='pvsamv1', required='module_model=2')
    _6par_gpmp: float = INPUT(name='6par_gpmp', label='Maximum power point temperature coefficient', units='%/C', type='NUMBER', group='pvsamv1', required='module_model=2')
    _6par_nser: float = INPUT(name='6par_nser', label='Nseries', type='NUMBER', group='pvsamv1', required='module_model=2', constraints='INTEGER,POSITIVE')
    _6par_area: float = INPUT(name='6par_area', label='Module area', units='m2', type='NUMBER', group='pvsamv1', required='module_model=2')
    _6par_tnoct: float = INPUT(name='6par_tnoct', label='Nominal operating cell temperature', units='C', type='NUMBER', group='pvsamv1', required='module_model=2')
    _6par_standoff: float = INPUT(name='6par_standoff', label='Standoff mode', type='NUMBER', group='pvsamv1', required='module_model=2', constraints='INTEGER,MIN=0,MAX=6', meta='0=bipv,1=>3.5in,2=2.5-3.5in,3=1.5-2.5in,4=0.5-1.5in,5=<0.5in,6=ground/rack')
    _6par_mounting: float = INPUT(name='6par_mounting', label='Array mounting height', type='NUMBER', group='pvsamv1', required='module_model=2', constraints='INTEGER,MIN=0,MAX=1', meta='0=one story,1=two story')
    _6par_is_bifacial: float = INPUT(name='6par_is_bifacial', label='Modules are bifacial', units='0/1', type='NUMBER', group='pvsamv1', required='module_model=2')
    _6par_bifacial_transmission_factor: float = INPUT(name='6par_bifacial_transmission_factor', label='Bifacial transmission factor', units='0-1', type='NUMBER', group='pvsamv1', required='module_model=2')
    _6par_bifaciality: float = INPUT(name='6par_bifaciality', label='Bifaciality factor', units='%', type='NUMBER', group='pvsamv1', required='module_model=2')
    _6par_bifacial_ground_clearance_height: float = INPUT(name='6par_bifacial_ground_clearance_height', label='Module ground clearance height', units='m', type='NUMBER', group='pvsamv1', required='module_model=2')
    snl_module_structure: float = INPUT(label='Module and mounting structure configuration', type='NUMBER', group='pvsamv1', required='module_model=3', constraints='INTEGER,MIN=0,MAX=6', meta='0=Use Database Values,1=glass/cell/polymer sheet - open rack,2=glass/cell/glass - open rack,3=polymer/thin film/steel - open rack,4=Insulated back building-integrated PV,5=close roof mount,6=user-defined')
    snl_a: float = INPUT(label='Temperature coefficient a', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_b: float = INPUT(label='Temperature coefficient b', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_dtc: float = INPUT(label='Temperature coefficient dT', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_ref_a: float = INPUT(label='User-specified a', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_ref_b: float = INPUT(label='User-specified b', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_ref_dT: float = INPUT(label='User-specified dT', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_fd: float = INPUT(label='Diffuse fraction', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_a0: float = INPUT(label='Air mass polynomial coeff 0', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_a1: float = INPUT(label='Air mass polynomial coeff 1', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_a2: float = INPUT(label='Air mass polynomial coeff 2', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_a3: float = INPUT(label='Air mass polynomial coeff 3', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_a4: float = INPUT(label='Air mass polynomial coeff 4', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_aimp: float = INPUT(label='Max power point current temperature coefficient', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_aisc: float = INPUT(label='Short circuit current temperature coefficient', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_area: float = INPUT(label='Module area', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_b0: float = INPUT(label='Incidence angle modifier polynomial coeff 0', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_b1: float = INPUT(label='Incidence angle modifier polynomial coeff 1', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_b2: float = INPUT(label='Incidence angle modifier polynomial coeff 2', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_b3: float = INPUT(label='Incidence angle modifier polynomial coeff 3', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_b4: float = INPUT(label='Incidence angle modifier polynomial coeff 4', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_b5: float = INPUT(label='Incidence angle modifier polynomial coeff 5', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_bvmpo: float = INPUT(label='Max power point voltage temperature coefficient', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_bvoco: float = INPUT(label='Open circuit voltage temperature coefficient', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_c0: float = INPUT(label='C0', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_c1: float = INPUT(label='C1', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_c2: float = INPUT(label='C2', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_c3: float = INPUT(label='C3', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_c4: float = INPUT(label='C4', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_c5: float = INPUT(label='C5', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_c6: float = INPUT(label='C6', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_c7: float = INPUT(label='C7', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_impo: float = INPUT(label='Max power point current', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_isco: float = INPUT(label='Short circuit current', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_ixo: float = INPUT(label='Ix midpoint current', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_ixxo: float = INPUT(label='Ixx midpoint current', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_mbvmp: float = INPUT(label='Irradiance dependence of Vmp temperature coefficient', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_mbvoc: float = INPUT(label='Irradiance dependence of Voc temperature coefficient', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_n: float = INPUT(label='Diode factor', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_series_cells: float = INPUT(label='Number of cells in series', type='NUMBER', group='pvsamv1', required='module_model=3', constraints='INTEGER')
    snl_vmpo: float = INPUT(label='Max power point voltage', type='NUMBER', group='pvsamv1', required='module_model=3')
    snl_voco: float = INPUT(label='Open circuit voltage', type='NUMBER', group='pvsamv1', required='module_model=3')
    sd11par_nser: float = INPUT(label='Nseries', type='NUMBER', group='pvsamv1', required='module_model=4', constraints='INTEGER,POSITIVE')
    sd11par_area: float = INPUT(label='Module area', units='m2', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_AMa0: float = INPUT(label='Air mass modifier coeff 0', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_AMa1: float = INPUT(label='Air mass modifier coeff 1', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_AMa2: float = INPUT(label='Air mass modifier coeff 2', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_AMa3: float = INPUT(label='Air mass modifier coeff 3', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_AMa4: float = INPUT(label='Air mass modifier coeff 4', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_glass: float = INPUT(label='Module cover glass type', type='NUMBER', group='pvsamv1', required='module_model=4', meta='0=normal,1=AR glass')
    sd11par_tnoct: float = INPUT(label='Nominal operating cell temperature', units='C', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_standoff: float = INPUT(label='Standoff mode', type='NUMBER', group='pvsamv1', required='module_model=4', constraints='INTEGER,MIN=0,MAX=6', meta='0=bipv,1=>3.5in,2=2.5-3.5in,3=1.5-2.5in,4=0.5-1.5in,5=<0.5in,6=ground/rack')
    sd11par_mounting: float = INPUT(label='Array mounting height', type='NUMBER', group='pvsamv1', required='module_model=4', constraints='INTEGER,MIN=0,MAX=1', meta='0=one story,1=two story')
    sd11par_Vmp0: float = INPUT(label='Vmp (STC)', units='V', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_Imp0: float = INPUT(label='Imp (STC)', units='A', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_Voc0: float = INPUT(label='Voc (STC)', units='V', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_Isc0: float = INPUT(label='Isc (STC)', units='A', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_alphaIsc: float = INPUT(label='Short curcuit current temperature coefficient', units='A/C', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_n: float = INPUT(label='Diode nonideality factor', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_Il: float = INPUT(label='Light current', units='A', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_Io: float = INPUT(label='Saturation current', units='A', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_Egref: float = INPUT(label='Bandgap voltage', units='eV', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_d1: float = INPUT(label='Rs fit parameter 1', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_d2: float = INPUT(label='Rs fit parameter 2', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_d3: float = INPUT(label='Rs fit parameter 3', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_c1: float = INPUT(label='Rsh fit parameter 1', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_c2: float = INPUT(label='Rsh fit parameter 2', type='NUMBER', group='pvsamv1', required='module_model=4')
    sd11par_c3: float = INPUT(label='Rsh fit parameter 3', type='NUMBER', group='pvsamv1', required='module_model=4')
    mlm_N_series: float = INPUT(label='Number of cells in series', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_N_parallel: float = INPUT(label='Number of cells in parallel', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_N_diodes: float = INPUT(label='Number of diodes', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_Width: float = INPUT(label='Module width (short side)', units='m', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_Length: float = INPUT(label='Module length (long side)', units='m', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_V_mp_ref: float = INPUT(label='V_mp at STC', units='V', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_I_mp_ref: float = INPUT(label='I_mp at STC', units='A', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_V_oc_ref: float = INPUT(label='V_oc at STC', units='V', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_I_sc_ref: float = INPUT(label='I_sc at STC', units='A', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_S_ref: float = INPUT(label='Reference irradiance (Typically 1000W/m²)', units='W/m²', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_T_ref: float = INPUT(label='Reference temperature (Typically 25°C)', units='°C', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_R_shref: float = INPUT(label='Reference shunt resistance', units='V/A', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_R_sh0: float = INPUT(label='Rsh,0', units='V/A', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_R_shexp: float = INPUT(label='Rsh exponential coefficient', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_R_s: float = INPUT(label='Series resistance', units='V/A', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_alpha_isc: float = INPUT(label='Temperature coefficient for I_sc', units='A/K', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_beta_voc_spec: float = INPUT(label='Temperature coefficient for V_oc', units='V/K', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_E_g: float = INPUT(label='Reference bandgap energy', units='eV', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_n_0: float = INPUT(label='Gamma', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_mu_n: float = INPUT(label='Temperature coefficient of gamma', units='1/K', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_D2MuTau: float = INPUT(label='Coefficient for recombination losses', units='V', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_T_mode: float = INPUT(label='Cell temperature model mode', units='-', type='NUMBER', group='pvsamv1', required='module_model=5', meta='1: NOCT')
    mlm_T_c_no_tnoct: float = INPUT(label='NOCT cell temperature', units='°C', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_T_c_no_mounting: float = INPUT(label='NOCT Array mounting height', units='-', type='NUMBER', group='pvsamv1', required='module_model=5', meta='0=one story,1=two story')
    mlm_T_c_no_standoff: float = INPUT(label='NOCT standoff mode', units='-', type='NUMBER', group='pvsamv1', required='module_model=5', meta='0=bipv,1=>3.5in,2=2.5-3.5in,3=1.5-2.5in,4=0.5-1.5in,5=<0.5in,6=ground/rack')
    mlm_T_c_fa_alpha: float = INPUT(label='Extended Faiman model absorptivity', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_T_c_fa_U0: float = INPUT(label='Extended Faiman model U_0', units='W/m²K', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_T_c_fa_U1: float = INPUT(label='Extended Faiman model U_1', units='W/m³sK', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_AM_mode: float = INPUT(label='Air-mass modifier mode', units='-', type='NUMBER', group='pvsamv1', required='module_model=5', meta='1: Do not consider AM effects, 2: Use Sandia polynomial [corr=f(AM)], 3: Use standard coefficients from DeSoto model [corr=f(AM)], 4: Use First Solar polynomial [corr=f(AM, p_wat)]')
    mlm_AM_c_sa0: float = INPUT(label='Coefficient 0 for Sandia Air Mass Modifier', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_AM_c_sa1: float = INPUT(label='Coefficient 1 for Sandia Air Mass Modifier', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_AM_c_sa2: float = INPUT(label='Coefficient 2 for Sandia Air Mass Modifier', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_AM_c_sa3: float = INPUT(label='Coefficient 3 for Sandia Air Mass Modifier', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_AM_c_sa4: float = INPUT(label='Coefficient 4 for Sandia Air Mass Modifier', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_AM_c_lp0: float = INPUT(label='Coefficient 0 for Lee/Panchula Air Mass Modifier', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_AM_c_lp1: float = INPUT(label='Coefficient 1 for Lee/Panchula Air Mass Modifier', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_AM_c_lp2: float = INPUT(label='Coefficient 2 for Lee/Panchula Air Mass Modifier', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_AM_c_lp3: float = INPUT(label='Coefficient 3 for Lee/Panchula Air Mass Modifier', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_AM_c_lp4: float = INPUT(label='Coefficient 4 for Lee/Panchula Air Mass Modifier', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_AM_c_lp5: float = INPUT(label='Coefficient 5 for Lee/Panchula Air Mass Modifier', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_IAM_mode: float = INPUT(label='Incidence Angle Modifier mode', units='-', type='NUMBER', group='pvsamv1', required='module_model=5', meta='1: Use ASHRAE formula, 2: Use Sandia polynomial, 3: Use cubic spline with user-supplied data')
    mlm_IAM_c_as: float = INPUT(label='ASHRAE incidence modifier coefficient b_0', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_IAM_c_sa0: float = INPUT(label='Sandia IAM coefficient 0', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_IAM_c_sa1: float = INPUT(label='Sandia IAM coefficient 1', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_IAM_c_sa2: float = INPUT(label='Sandia IAM coefficient 2', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_IAM_c_sa3: float = INPUT(label='Sandia IAM coefficient 3', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_IAM_c_sa4: float = INPUT(label='Sandia IAM coefficient 4', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_IAM_c_sa5: float = INPUT(label='Sandia IAM coefficient 5', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    mlm_IAM_c_cs_incAngle: Array = INPUT(label='Spline IAM - Incidence angles', units='deg', type='ARRAY', group='pvsamv1', required='module_model=5')
    mlm_IAM_c_cs_iamValue: Array = INPUT(label='Spline IAM - IAM values', units='-', type='ARRAY', group='pvsamv1', required='module_model=5')
    mlm_groundRelfectionFraction: float = INPUT(label='Ground reflection fraction', units='-', type='NUMBER', group='pvsamv1', required='module_model=5')
    inverter_model: float = INPUT(label='Inverter model specifier', type='NUMBER', group='pvsamv1', required='*', constraints='INTEGER,MIN=0,MAX=4', meta='0=cec,1=datasheet,2=partload,3=coefficientgenerator,4=PVYield')
    mppt_low_inverter: float = INPUT(label='Minimum inverter MPPT voltage window', units='Vdc', type='NUMBER', group='pvsamv1', required='?=0')
    mppt_hi_inverter: float = INPUT(label='Maximum inverter MPPT voltage window', units='Vdc', type='NUMBER', group='pvsamv1', required='?=0')
    inv_num_mppt: float = INPUT(label='Number of MPPT inputs', type='NUMBER', group='pvsamv1', required='?=1', constraints='INTEGER,MIN=0,MAX=4')
    inv_snl_c0: float = INPUT(label='Curvature between AC power and DC power at ref', units='1/W', type='NUMBER', group='pvsamv1', required='inverter_model=0')
    inv_snl_c1: float = INPUT(label='Coefficient of Pdco variation with DC input voltage', units='1/V', type='NUMBER', group='pvsamv1', required='inverter_model=0')
    inv_snl_c2: float = INPUT(label='Coefficient of Pso variation with DC input voltage', units='1/V', type='NUMBER', group='pvsamv1', required='inverter_model=0')
    inv_snl_c3: float = INPUT(label='Coefficient of Co variation with DC input voltage', units='1/V', type='NUMBER', group='pvsamv1', required='inverter_model=0')
    inv_snl_paco: float = INPUT(label='AC maximum power rating', units='Wac', type='NUMBER', group='pvsamv1', required='inverter_model=0')
    inv_snl_pdco: float = INPUT(label='DC input power at which AC power rating is achieved', units='Wdc', type='NUMBER', group='pvsamv1', required='inverter_model=0')
    inv_snl_pnt: float = INPUT(label='AC power consumed by inverter at night', units='Wac', type='NUMBER', group='pvsamv1', required='inverter_model=0')
    inv_snl_pso: float = INPUT(label='DC power required to enable the inversion process', units='Wdc', type='NUMBER', group='pvsamv1', required='inverter_model=0')
    inv_snl_vdco: float = INPUT(label='DC input voltage for the rated AC power rating', units='Vdc', type='NUMBER', group='pvsamv1', required='inverter_model=0')
    inv_snl_vdcmax: float = INPUT(label='Maximum DC input operating voltage', units='Vdc', type='NUMBER', group='pvsamv1', required='inverter_model=0')
    inv_cec_cg_c0: float = INPUT(label='Curvature between AC power and DC power at ref', units='1/W', type='NUMBER', group='pvsamv1', required='inverter_model=3')
    inv_cec_cg_c1: float = INPUT(label='Coefficient of Pdco variation with DC input voltage', units='1/V', type='NUMBER', group='pvsamv1', required='inverter_model=3')
    inv_cec_cg_c2: float = INPUT(label='Coefficient of Pso variation with DC input voltage', units='1/V', type='NUMBER', group='pvsamv1', required='inverter_model=3')
    inv_cec_cg_c3: float = INPUT(label='Coefficient of Co variation with DC input voltage', units='1/V', type='NUMBER', group='pvsamv1', required='inverter_model=3')
    inv_cec_cg_paco: float = INPUT(label='AC maximum power rating', units='Wac', type='NUMBER', group='pvsamv1', required='inverter_model=3')
    inv_cec_cg_pdco: float = INPUT(label='DC input power at which AC power rating is achieved', units='Wdc', type='NUMBER', group='pvsamv1', required='inverter_model=3')
    inv_cec_cg_pnt: float = INPUT(label='AC power consumed by inverter at night', units='Wac', type='NUMBER', group='pvsamv1', required='inverter_model=3')
    inv_cec_cg_psco: float = INPUT(label='DC power required to enable the inversion process', units='Wdc', type='NUMBER', group='pvsamv1', required='inverter_model=3')
    inv_cec_cg_vdco: float = INPUT(label='DC input voltage for the rated AC power rating', units='Vdc', type='NUMBER', group='pvsamv1', required='inverter_model=3')
    inv_cec_cg_vdcmax: float = INPUT(label='Maximum DC input operating voltage', units='Vdc', type='NUMBER', group='pvsamv1', required='inverter_model=3')
    inv_ds_paco: float = INPUT(label='AC maximum power rating', units='Wac', type='NUMBER', group='pvsamv1', required='inverter_model=1')
    inv_ds_eff: float = INPUT(label='Weighted or Peak or Nominal Efficiency', units='Wdc', type='NUMBER', group='pvsamv1', required='inverter_model=1')
    inv_ds_pnt: float = INPUT(label='AC power consumed by inverter at night', units='Wac', type='NUMBER', group='pvsamv1', required='inverter_model=1')
    inv_ds_pso: float = INPUT(label='DC power required to enable the inversion process', units='Wdc', type='NUMBER', group='pvsamv1', required='inverter_model=1')
    inv_ds_vdco: float = INPUT(label='DC input voltage for the rated AC power rating', units='Vdc', type='NUMBER', group='pvsamv1', required='inverter_model=1')
    inv_ds_vdcmax: float = INPUT(label='Maximum DC input operating voltage', units='Vdc', type='NUMBER', group='pvsamv1', required='inverter_model=1')
    inv_pd_paco: float = INPUT(label='AC maximum power rating', units='Wac', type='NUMBER', group='pvsamv1', required='inverter_model=2')
    inv_pd_pdco: float = INPUT(label='DC input power at which AC power rating is achieved', units='Wdc', type='NUMBER', group='pvsamv1', required='inverter_model=2')
    inv_pd_partload: Array = INPUT(label='Partload curve partload values', units='%', type='ARRAY', group='pvsamv1', required='inverter_model=2')
    inv_pd_efficiency: Array = INPUT(label='Partload curve efficiency values', units='%', type='ARRAY', group='pvsamv1', required='inverter_model=2')
    inv_pd_pnt: float = INPUT(label='AC power consumed by inverter at night', units='Wac', type='NUMBER', group='pvsamv1', required='inverter_model=2')
    inv_pd_vdco: float = INPUT(label='DC input voltage for the rated AC power rating', units='Vdc', type='NUMBER', group='pvsamv1', required='inverter_model=2')
    inv_pd_vdcmax: float = INPUT(label='Maximum DC input operating voltage', units='Vdc', type='NUMBER', group='pvsamv1', required='inverter_model=2')
    ond_PNomConv: float = INPUT(units='W', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_PMaxOUT: float = INPUT(units='W', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_VOutConv: float = INPUT(units='W', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_VMppMin: float = INPUT(units='V', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_VMPPMax: float = INPUT(units='V', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_VAbsMax: float = INPUT(units='V', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_PSeuil: float = INPUT(units='W', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_ModeOper: str = INPUT(units='-', type='STRING', group='pvsamv1', required='inverter_model=4')
    ond_CompPMax: str = INPUT(units='-', type='STRING', group='pvsamv1', required='inverter_model=4')
    ond_CompVMax: str = INPUT(units='-', type='STRING', group='pvsamv1', required='inverter_model=4')
    ond_ModeAffEnum: str = INPUT(units='-', type='STRING', group='pvsamv1', required='inverter_model=4')
    ond_PNomDC: float = INPUT(units='W', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_PMaxDC: float = INPUT(units='W', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_IMaxDC: float = INPUT(units='A', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_INomDC: float = INPUT(units='A', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_INomAC: float = INPUT(units='A', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_IMaxAC: float = INPUT(units='A', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_TPNom: float = INPUT(units='°C', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_TPMax: float = INPUT(units='°C', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_TPLim1: float = INPUT(units='°C', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_TPLimAbs: float = INPUT(units='°C', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_PLim1: float = INPUT(units='W', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_PLimAbs: float = INPUT(units='W', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_VNomEff: Array = INPUT(units='V', type='ARRAY', group='pvsamv1', required='inverter_model=4')
    ond_NbInputs: float = INPUT(units='-', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_NbMPPT: float = INPUT(units='-', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_Aux_Loss: float = INPUT(units='W', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_Night_Loss: float = INPUT(units='W', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_lossRDc: float = INPUT(units='V/A', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_lossRAc: float = INPUT(units='A', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_effCurve_elements: float = INPUT(units='-', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_effCurve_Pdc: Matrix = INPUT(units='W', type='MATRIX', group='pvsamv1', required='inverter_model=4')
    ond_effCurve_Pac: Matrix = INPUT(units='W', type='MATRIX', group='pvsamv1', required='inverter_model=4')
    ond_effCurve_eta: Matrix = INPUT(units='-', type='MATRIX', group='pvsamv1', required='inverter_model=4')
    ond_doAllowOverpower: float = INPUT(units='-', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    ond_doUseTemperatureLimit: float = INPUT(units='-', type='NUMBER', group='pvsamv1', required='inverter_model=4')
    inv_tdc_cec_db: Matrix = INPUT(label='Temperature derate curves for CEC Database', units='Vdc', type='MATRIX', group='pvsamv1', required='inverter_model=0')
    inv_tdc_cec_cg: Matrix = INPUT(label='Temperature derate curves for CEC Coef Gen', units='Vdc', type='MATRIX', group='pvsamv1', required='inverter_model=3')
    inv_tdc_ds: Matrix = INPUT(label='Temperature derate curves for Inv Datasheet', units='Vdc', type='MATRIX', group='pvsamv1', required='inverter_model=1')
    inv_tdc_plc: Matrix = INPUT(label='Temperature derate curves for Part Load Curve', units='C', type='MATRIX', group='pvsamv1', required='inverter_model=2')
    en_batt: float = INPUT(label='Enable battery storage model', units='0/1', type='NUMBER', group='Battery', required='?=0')
    load: Array = INPUT(label='Electricity load (year 1)', units='kW', type='ARRAY', group='Battery', required='?')
    gh: Final[Array] = OUTPUT(label='Irradiance GHI from weather file', units='W/m2', type='ARRAY', group='Time Series', required='*')
    dn: Final[Array] = OUTPUT(label='Irradiance DNI from weather file', units='W/m2', type='ARRAY', group='Time Series', required='*')
    df: Final[Array] = OUTPUT(label='Irradiance DHI from weather file', units='W/m2', type='ARRAY', group='Time Series', required='*')
    wfpoa: Final[Array] = OUTPUT(label='Irradiance POA from weather file', units='W/m2', type='ARRAY', group='Time Series')
    gh_calc: Final[Array] = OUTPUT(label='Irradiance GHI calculated', units='W/m2', type='ARRAY', group='Time Series')
    dn_calc: Final[Array] = OUTPUT(label='Irradiance DNI calculated', units='W/m2', type='ARRAY', group='Time Series')
    df_calc: Final[Array] = OUTPUT(label='Irradiance DHI calculated', units='W/m2', type='ARRAY', group='Time Series')
    wspd: Final[Array] = OUTPUT(label='Weather file wind speed', units='m/s', type='ARRAY', group='Time Series', required='*')
    tdry: Final[Array] = OUTPUT(label='Weather file ambient temperature', units='C', type='ARRAY', group='Time Series', required='*')
    alb: Final[Array] = OUTPUT(label='Weather file albedo', type='ARRAY', group='Time Series', required='*')
    snowdepth: Final[Array] = OUTPUT(label='Weather file snow depth', units='cm', type='ARRAY', group='Time Series')
    sol_zen: Final[Array] = OUTPUT(label='Sun zenith angle', units='deg', type='ARRAY', group='Time Series', required='*')
    sol_alt: Final[Array] = OUTPUT(label='Sun altitude angle', units='deg', type='ARRAY', group='Time Series', required='*')
    sol_azi: Final[Array] = OUTPUT(label='Sun azimuth angle', units='deg', type='ARRAY', group='Time Series', required='*')
    sunup: Final[Array] = OUTPUT(label='Sun up over horizon', units='0/1/2/3', type='ARRAY', group='Time Series', required='*')
    sunpos_hour: Final[Array] = OUTPUT(label='Sun position time', units='hour', type='ARRAY', group='Time Series')
    airmass: Final[Array] = OUTPUT(label='Absolute air mass', type='ARRAY', group='Time Series', required='*')
    subarray1_surf_tilt: Final[Array] = OUTPUT(label='Subarray 1 Surface tilt', units='deg', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_surf_azi: Final[Array] = OUTPUT(label='Subarray 1 Surface azimuth', units='deg', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_aoi: Final[Array] = OUTPUT(label='Subarray 1 Angle of incidence', units='deg', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_aoi_modifier: Final[Array] = OUTPUT(label='Subarray 1 Angle of incidence Modifier', units='0-1', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_axisrot: Final[Array] = OUTPUT(label='Subarray 1 Axis rotation for 1 axis trackers', units='deg', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_idealrot: Final[Array] = OUTPUT(label='Subarray 1 Axis rotation ideal for 1 axis trackers', units='deg', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_poa_eff_beam: Final[Array] = OUTPUT(label='Subarray 1 POA front beam irradiance after shading and soiling', units='W/m2', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_poa_eff_diff: Final[Array] = OUTPUT(label='Subarray 1 POA front diffuse irradiance after shading and soiling', units='W/m2', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_poa_nom: Final[Array] = OUTPUT(label='Subarray 1 POA front total irradiance nominal', units='W/m2', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_poa_shaded: Final[Array] = OUTPUT(label='Subarray 1 POA front total irradiance after shading only', units='W/m2', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_poa_shaded_soiled: Final[Array] = OUTPUT(label='Subarray 1 POA front total irradiance after shading and soiling', units='W/m2', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_poa_front: Final[Array] = OUTPUT(label='Subarray 1 POA front total irradiance after reflection (IAM)', units='W/m2', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_poa_rear: Final[Array] = OUTPUT(label='Subarray 1 POA rear total irradiance after reflection (IAM)', units='W/m2', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_poa_eff: Final[Array] = OUTPUT(label='Subarray 1 POA total irradiance after reflection (IAM)', units='W/m2', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_soiling_derate: Final[Array] = OUTPUT(label='Subarray 1 Soiling beam irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_beam_shading_factor: Final[Array] = OUTPUT(label='Subarray 1 External shading and soiling beam irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_linear_derate: Final[Array] = OUTPUT(label='Subarray 1 Self-shading linear beam irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_ss_diffuse_derate: Final[Array] = OUTPUT(label='Subarray 1 Self-shading non-linear sky diffuse irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_ss_reflected_derate: Final[Array] = OUTPUT(label='Subarray 1 Self-shading non-linear ground diffuse irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_ss_derate: Final[Array] = OUTPUT(label='Subarray 1 Self-shading non-linear DC factor', units='frac', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    shadedb_subarray1_shade_frac: Final[Array] = OUTPUT(label='Subarray 1 Partial external shading DC factor', units='frac', type='ARRAY', group='Time Series (Subarray 1)')
    subarray1_snow_coverage: Final[Array] = OUTPUT(label='Subarray 1 Snow cover', units='0..1', type='ARRAY', group='Time Series (Subarray 1)')
    subarray1_snow_loss: Final[Array] = OUTPUT(label='Subarray 1 Snow cover DC power loss', units='kW', type='ARRAY', group='Time Series (Subarray 1)')
    subarray1_modeff: Final[Array] = OUTPUT(label='Subarray 1 Module efficiency', units='%', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_celltemp: Final[Array] = OUTPUT(label='Subarray 1 Cell temperature', units='C', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_dc_voltage: Final[Array] = OUTPUT(label='Subarray 1 Operating DC voltage', units='V', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_dc_gross: Final[Array] = OUTPUT(label='Subarray 1 DC power gross', units='kW', type='ARRAY', group='Time Series (Subarray 1)', required='*')
    subarray1_voc: Final[Array] = OUTPUT(label='Subarray 1 Open circuit DC voltage', units='V', type='ARRAY', group='Time Series (Subarray 1)')
    subarray1_isc: Final[Array] = OUTPUT(label='Subarray 1 Short circuit DC current', units='A', type='ARRAY', group='Time Series (Subarray 1)')
    subarray2_surf_tilt: Final[Array] = OUTPUT(label='Subarray 2 Surface tilt', units='deg', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_surf_azi: Final[Array] = OUTPUT(label='Subarray 2 Surface azimuth', units='deg', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_aoi: Final[Array] = OUTPUT(label='Subarray 2 Angle of incidence', units='deg', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_aoi_modifier: Final[Array] = OUTPUT(label='Subarray 2 Angle of incidence Modifier', units='0-1', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_axisrot: Final[Array] = OUTPUT(label='Subarray 2 Axis rotation for 1 axis trackers', units='deg', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_idealrot: Final[Array] = OUTPUT(label='Subarray 2 Axis rotation ideal for 1 axis trackers', units='deg', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_poa_eff_beam: Final[Array] = OUTPUT(label='Subarray 2 POA front beam irradiance after shading and soiling', units='W/m2', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_poa_eff_diff: Final[Array] = OUTPUT(label='Subarray 2 POA front diffuse irradiance after shading and soiling', units='W/m2', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_poa_nom: Final[Array] = OUTPUT(label='Subarray 2 POA front total irradiance nominal', units='W/m2', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_poa_shaded: Final[Array] = OUTPUT(label='Subarray 2 POA front total irradiance after shading only', units='W/m2', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_poa_shaded_soiled: Final[Array] = OUTPUT(label='Subarray 2 POA front total irradiance after shading and soiling', units='W/m2', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_poa_front: Final[Array] = OUTPUT(label='Subarray 2 POA front total irradiance after reflection (IAM)', units='W/m2', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_poa_rear: Final[Array] = OUTPUT(label='Subarray 2 POA rear irradiance after reflection (IAM)', units='W/m2', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_poa_eff: Final[Array] = OUTPUT(label='Subarray 2 POA total irradiance after module reflection (IAM)', units='W/m2', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_soiling_derate: Final[Array] = OUTPUT(label='Subarray 2 Soiling beam irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_beam_shading_factor: Final[Array] = OUTPUT(label='Subarray 2 External shading and soiling beam irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_linear_derate: Final[Array] = OUTPUT(label='Subarray 2 Self-shading linear beam irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_ss_diffuse_derate: Final[Array] = OUTPUT(label='Subarray 2 Self-shading non-linear sky diffuse irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_ss_reflected_derate: Final[Array] = OUTPUT(label='Subarray 2 Self-shading non-linear ground diffuse irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_ss_derate: Final[Array] = OUTPUT(label='Subarray 2 Self-shading non-linear DC factor', units='frac', type='ARRAY', group='Time Series (Subarray 2)')
    shadedb_subarray2_shade_frac: Final[Array] = OUTPUT(label='Subarray 2 Partial shading DC factor', units='frac', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_snow_coverage: Final[Array] = OUTPUT(label='Subarray 2 Snow cover', units='0..1', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_snow_loss: Final[Array] = OUTPUT(label='Subarray 2 Snow cover DC power loss', units='kW', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_modeff: Final[Array] = OUTPUT(label='Subarray 2 Module efficiency', units='%', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_celltemp: Final[Array] = OUTPUT(label='Subarray 2 Cell temperature', units='C', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_dc_voltage: Final[Array] = OUTPUT(label='Subarray 2 Operating DC voltage', units='V', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_dc_gross: Final[Array] = OUTPUT(label='Subarray 2 DC power gross', units='kW', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_voc: Final[Array] = OUTPUT(label='Subarray 2 Open circuit DC voltage', units='V', type='ARRAY', group='Time Series (Subarray 2)')
    subarray2_isc: Final[Array] = OUTPUT(label='Subarray 2 Short circuit DC current', units='A', type='ARRAY', group='Time Series (Subarray 2)')
    subarray3_surf_tilt: Final[Array] = OUTPUT(label='Subarray 3 Surface tilt', units='deg', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_surf_azi: Final[Array] = OUTPUT(label='Subarray 3 Surface azimuth', units='deg', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_aoi: Final[Array] = OUTPUT(label='Subarray 3 Angle of incidence', units='deg', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_aoi_modifier: Final[Array] = OUTPUT(label='Subarray 3 Angle of incidence Modifier', units='0-1', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_axisrot: Final[Array] = OUTPUT(label='Subarray 3 Axis rotation for 1 axis trackers', units='deg', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_idealrot: Final[Array] = OUTPUT(label='Subarray 3 Axis rotation ideal for 1 axis trackers', units='deg', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_poa_eff_beam: Final[Array] = OUTPUT(label='Subarray 3 POA front beam irradiance after shading and soiling', units='W/m2', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_poa_eff_diff: Final[Array] = OUTPUT(label='Subarray 3 POA front diffuse irradiance after shading and soiling', units='W/m2', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_poa_nom: Final[Array] = OUTPUT(label='Subarray 3 POA font total irradiance nominal', units='W/m2', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_poa_shaded: Final[Array] = OUTPUT(label='Subarray 3 POA front total irradiance after shading only', units='W/m2', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_poa_shaded_soiled: Final[Array] = OUTPUT(label='Subarray 3 POA front total irradiance after shading and soiling', units='W/m2', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_poa_front: Final[Array] = OUTPUT(label='Subarray 3 POA front total irradiance after reflection (IAM)', units='W/m2', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_poa_rear: Final[Array] = OUTPUT(label='Subarray 3 POA rear irradiance after reflection (IAM)', units='W/m2', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_poa_eff: Final[Array] = OUTPUT(label='Subarray 3 POA total irradiance after reflection (IAM)', units='W/m2', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_soiling_derate: Final[Array] = OUTPUT(label='Subarray 3 Soiling beam irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_beam_shading_factor: Final[Array] = OUTPUT(label='Subarray 3 External shading and soiling beam irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_linear_derate: Final[Array] = OUTPUT(label='Subarray 3 Self-shading linear beam irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_ss_diffuse_derate: Final[Array] = OUTPUT(label='Subarray 3 Self-shading non-linear sky diffuse irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_ss_reflected_derate: Final[Array] = OUTPUT(label='Subarray 3 Self-shading non-linear ground diffuse irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_ss_derate: Final[Array] = OUTPUT(label='Subarray 3 Self-shading non-linear DC factor', units='frac', type='ARRAY', group='Time Series (Subarray 3)')
    shadedb_subarray3_shade_frac: Final[Array] = OUTPUT(label='Subarray 3 Partial external shading DC factor', units='frac', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_snow_coverage: Final[Array] = OUTPUT(label='Subarray 3 Snow cover', units='0..1', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_snow_loss: Final[Array] = OUTPUT(label='Subarray 3 Snow cover DC power loss', units='kW', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_modeff: Final[Array] = OUTPUT(label='Subarray 3 Module efficiency', units='%', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_celltemp: Final[Array] = OUTPUT(label='Subarray 3 Cell temperature', units='C', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_dc_voltage: Final[Array] = OUTPUT(label='Subarray 3 Operating DC voltage', units='V', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_dc_gross: Final[Array] = OUTPUT(label='Subarray 3 DC power gross', units='kW', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_voc: Final[Array] = OUTPUT(label='Subarray 3 Open circuit DC voltage', units='V', type='ARRAY', group='Time Series (Subarray 3)')
    subarray3_isc: Final[Array] = OUTPUT(label='Subarray 3 Short circuit DC current', units='A', type='ARRAY', group='Time Series (Subarray 3)')
    subarray4_surf_tilt: Final[Array] = OUTPUT(label='Subarray 4 Surface tilt', units='deg', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_surf_azi: Final[Array] = OUTPUT(label='Subarray 4 Surface azimuth', units='deg', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_aoi: Final[Array] = OUTPUT(label='Subarray 4 Angle of incidence', units='deg', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_aoi_modifier: Final[Array] = OUTPUT(label='Subarray 4 Angle of incidence Modifier', units='0-1', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_axisrot: Final[Array] = OUTPUT(label='Subarray 4 Axis rotation for 1 axis trackers', units='deg', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_idealrot: Final[Array] = OUTPUT(label='Subarray 4 Axis rotation ideal for 1 axis trackers', units='deg', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_poa_eff_beam: Final[Array] = OUTPUT(label='Subarray 4 POA front beam irradiance after shading and soiling', units='W/m2', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_poa_eff_diff: Final[Array] = OUTPUT(label='Subarray 4 POA front diffuse irradiance after shading and soiling', units='W/m2', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_poa_nom: Final[Array] = OUTPUT(label='Subarray 4 POA front total irradiance nominal', units='W/m2', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_poa_shaded: Final[Array] = OUTPUT(label='Subarray 4 POA front total irradiance after shading only', units='W/m2', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_poa_shaded_soiled: Final[Array] = OUTPUT(label='Subarray 4 POA front total irradiance after shading and soiling', units='W/m2', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_poa_front: Final[Array] = OUTPUT(label='Subarray 4 POA front total irradiance after reflection (IAM)', units='W/m2', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_poa_rear: Final[Array] = OUTPUT(label='Subarray 4 POA rear irradiance after reflection (IAM)', units='W/m2', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_poa_eff: Final[Array] = OUTPUT(label='Subarray 4 POA total irradiance after reflection (IAM)', units='W/m2', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_soiling_derate: Final[Array] = OUTPUT(label='Subarray 4 Soiling beam irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_beam_shading_factor: Final[Array] = OUTPUT(label='Subarray 4 External shading and soiling beam irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_linear_derate: Final[Array] = OUTPUT(label='Subarray 4 Self-shading linear beam irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_ss_diffuse_derate: Final[Array] = OUTPUT(label='Subarray 4 Self-shading non-linear sky diffuse irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_ss_reflected_derate: Final[Array] = OUTPUT(label='Subarray 4 Self-shading non-linear ground diffuse irradiance factor', units='frac', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_ss_derate: Final[Array] = OUTPUT(label='Subarray 4 Self-shading non-linear DC factor', units='frac', type='ARRAY', group='Time Series (Subarray 4)')
    shadedb_subarray4_shade_frac: Final[Array] = OUTPUT(label='Subarray 4 Partial external shading DC factor', units='frac', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_snow_coverage: Final[Array] = OUTPUT(label='Subarray 4 Snow cover', units='0..1', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_snow_loss: Final[Array] = OUTPUT(label='Subarray 4 Snow cover DC power loss', units='kW', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_modeff: Final[Array] = OUTPUT(label='Subarray 4 Module efficiency', units='%', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_celltemp: Final[Array] = OUTPUT(label='Subarray 4 Cell temperature', units='C', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_dc_voltage: Final[Array] = OUTPUT(label='Subarray 4 Operating DC voltage', units='V', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_dc_gross: Final[Array] = OUTPUT(label='Subarray 4 DC power gross', units='kW', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_voc: Final[Array] = OUTPUT(label='Subarray 4 Open circuit DC voltage', units='V', type='ARRAY', group='Time Series (Subarray 4)')
    subarray4_isc: Final[Array] = OUTPUT(label='Subarray 4 Short circuit DC current', units='A', type='ARRAY', group='Time Series (Subarray 4)')
    poa_nom: Final[Array] = OUTPUT(label='Array POA front-side total radiation nominal', units='kW', type='ARRAY', group='Time Series (Array)', required='*')
    poa_beam_nom: Final[Array] = OUTPUT(label='Array POA front-side beam radiation nominal', units='kW', type='ARRAY', group='Time Series (Array)', required='*')
    poa_beam_eff: Final[Array] = OUTPUT(label='Array POA beam radiation after shading and soiling', units='kW', type='ARRAY', group='Time Series (Array)', required='*')
    poa_shaded: Final[Array] = OUTPUT(label='Array POA front-side total radiation after shading only', units='kW', type='ARRAY', group='Time Series (Array)', required='*')
    poa_shaded_soiled: Final[Array] = OUTPUT(label='Array POA front-side total radiation after shading and soiling', units='kW', type='ARRAY', group='Time Series (Array)', required='*')
    poa_front: Final[Array] = OUTPUT(label='Array POA front-side total radiation after reflection (IAM)', units='kW', type='ARRAY', group='Time Series (Array)', required='*')
    poa_rear: Final[Array] = OUTPUT(label='Array POA rear-side total radiation after reflection (IAM)', units='kW', type='ARRAY', group='Time Series (Array)', required='*')
    poa_eff: Final[Array] = OUTPUT(label='Array POA radiation total after reflection (IAM)', units='kW', type='ARRAY', group='Time Series (Array)', required='*')
    dc_snow_loss: Final[Array] = OUTPUT(label='Array DC power loss due to snow', units='kW', type='ARRAY', group='Time Series (Array)')
    dc_net: Final[Array] = OUTPUT(label='Array DC power', units='kW', type='ARRAY', group='Time Series (Array)', required='*')
    inverterMPPT1_DCVoltage: Final[Array] = OUTPUT(label='Inverter MPPT 1 Nominal DC voltage', units='V', type='ARRAY', group='Time Series (MPPT)')
    inverterMPPT2_DCVoltage: Final[Array] = OUTPUT(label='Inverter MPPT 2 Nominal DC voltage', units='V', type='ARRAY', group='Time Series (MPPT)')
    inverterMPPT3_DCVoltage: Final[Array] = OUTPUT(label='Inverter MPPT 3 Nominal DC voltage', units='V', type='ARRAY', group='Time Series (MPPT)')
    inverterMPPT4_DCVoltage: Final[Array] = OUTPUT(label='Inverter MPPT 4 Nominal DC voltage', units='V', type='ARRAY', group='Time Series (MPPT)')
    inv_eff: Final[Array] = OUTPUT(label='Inverter efficiency', units='%', type='ARRAY', group='Time Series (Inverter)', required='*')
    dc_invmppt_loss: Final[Array] = OUTPUT(label='Inverter clipping loss DC MPPT voltage limits', units='kW', type='ARRAY', group='Time Series (Inverter)', required='*')
    inv_cliploss: Final[Array] = OUTPUT(label='Inverter clipping loss AC power limit', units='kW', type='ARRAY', group='Time Series (Inverter)', required='*')
    inv_psoloss: Final[Array] = OUTPUT(label='Inverter power consumption loss', units='kW', type='ARRAY', group='Time Series (Inverter)', required='*')
    inv_pntloss: Final[Array] = OUTPUT(label='Inverter night time loss', units='kW', type='ARRAY', group='Time Series (Inverter)', required='*')
    inv_tdcloss: Final[Array] = OUTPUT(label='Inverter thermal derate loss', units='kW', type='ARRAY', group='Time Series (Inverter)', required='*')
    inv_total_loss: Final[Array] = OUTPUT(label='Inverter total power loss', units='kW', type='ARRAY', group='Time Series (Inverter)', required='*')
    ac_wiring_loss: Final[Array] = OUTPUT(label='AC wiring loss', units='kW', type='ARRAY', group='Time Series (Inverter)', required='*')
    xfmr_nll_ts: Final[Array] = OUTPUT(label='Transformer no load loss', units='kW', type='ARRAY', group='Time Series (Transformer)')
    xfmr_ll_ts: Final[Array] = OUTPUT(label='Transformer load loss', units='kW', type='ARRAY', group='Time Series (Transformer)')
    xfmr_loss_ts: Final[Array] = OUTPUT(label='Transformer total loss', units='kW', type='ARRAY', group='Time Series (Transformer)')
    ac_transmission_loss: Final[Array] = OUTPUT(label='Transmission loss', units='kW', type='ARRAY', group='Time Series (Transmission)')
    ac_loss: Final[float] = OUTPUT(label='AC wiring loss', units='%', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_energy: Final[float] = OUTPUT(label='Annual AC energy', units='kWh', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_dc_invmppt_loss: Final[float] = OUTPUT(label='Inverter clipping loss DC MPPT voltage limits', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_inv_cliploss: Final[float] = OUTPUT(label='Inverter clipping loss AC power limit', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_inv_psoloss: Final[float] = OUTPUT(label='Inverter power consumption loss', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_inv_pntloss: Final[float] = OUTPUT(label='Inverter night time loss', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_inv_tdcloss: Final[float] = OUTPUT(label='Inverter thermal derate loss', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    subarray1_dcloss: Final[float] = OUTPUT(label='Subarray 1 Total DC power loss', units='%', type='NUMBER', group='Annual (Year 1)', required='*')
    subarray2_dcloss: Final[float] = OUTPUT(label='Subarray 2 Total DC power loss', units='%', type='NUMBER', group='Annual (Year 1)')
    subarray3_dcloss: Final[float] = OUTPUT(label='Subarray 3 Total DC power loss', units='%', type='NUMBER', group='Annual (Year 1)')
    subarray4_dcloss: Final[float] = OUTPUT(label='Subarray 4 Total DC power loss', units='%', type='NUMBER', group='Annual (Year 1)')
    xfmr_nll_year1: Final[float] = OUTPUT(label='Transformer no load loss', units='kWh/yr', type='NUMBER', group='Annual (Year 1)')
    xfmr_ll_year1: Final[float] = OUTPUT(label='Transformer load loss', units='kWh/yr', type='NUMBER', group='Annual (Year 1)')
    xfmr_loss_year1: Final[float] = OUTPUT(label='Transformer total loss', units='kWh/yr', type='NUMBER', group='Annual (Year 1)')
    monthly_poa_nom: Final[Array] = OUTPUT(label='POA front-side irradiance total nominal', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    monthly_poa_beam_nom: Final[Array] = OUTPUT(label='POA front-side irradiance beam nominal', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    monthly_poa_front: Final[Array] = OUTPUT(label='POA front-side irradiance total', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    monthly_poa_rear: Final[Array] = OUTPUT(label='POA rear-side irradiance total', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    monthly_poa_eff: Final[Array] = OUTPUT(label='POA irradiance total after shading and soiling', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    monthly_poa_beam_eff: Final[Array] = OUTPUT(label='POA front-side irradiance beam after shading and soiling', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    monthly_dc: Final[Array] = OUTPUT(label='PV array DC energy', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    monthly_energy: Final[Array] = OUTPUT(label='System AC energy', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    annual_gh: Final[float] = OUTPUT(label='Annual GHI', units='Wh/m2/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_poa_nom: Final[float] = OUTPUT(label='POA front-side irradiance total nominal', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_poa_beam_nom: Final[float] = OUTPUT(label='POA front-side irradiance beam nominal', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_poa_shaded: Final[float] = OUTPUT(label='POA front-side irradiance total after shading', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_poa_shaded_soiled: Final[float] = OUTPUT(label='POA front-side irradiance total after shading and soiling', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_poa_front: Final[float] = OUTPUT(label='POA front-side irradiance total after reflection (IAM)', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_poa_rear: Final[float] = OUTPUT(label='POA rear-side irradiance total after reflection (IAM)', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_poa_eff: Final[float] = OUTPUT(label='POA irradiance total after reflection (IAM)', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_poa_beam_eff: Final[float] = OUTPUT(label='POA front-side irradiance beam after shading and soiling', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_dc_nominal: Final[float] = OUTPUT(label='Annual DC energy nominal', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_dc_gross: Final[float] = OUTPUT(label='Annual DC energy gross', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_dc_net: Final[float] = OUTPUT(label='Annual DC energy', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_ac_gross: Final[float] = OUTPUT(label='Annual AC energy gross', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_dc_loss_ond: Final[float] = OUTPUT(label='Annual DC loss OND model', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_ac_loss_ond: Final[float] = OUTPUT(label='Annual AC loss OND model', units='kWh/yr', type='NUMBER', group='Annual (Year 1)', required='*')
    monthly_snow_loss: Final[Array] = OUTPUT(label='Snow DC energy loss', units='kWh/mo', type='ARRAY', group='Monthly')
    annual_snow_loss: Final[float] = OUTPUT(label='Snow DC energy loss', units='kWh/yr', type='NUMBER', group='Annual (Year 1)')
    annual_subarray1_dc_gross: Final[float] = OUTPUT(label='Subarray 1 Gross DC energy', units='kWh', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_subarray1_dc_mismatch_loss: Final[float] = OUTPUT(label='Subarray 1 DC mismatch loss', units='kWh', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_subarray1_dc_diodes_loss: Final[float] = OUTPUT(label='Subarray 1 DC diodes and connections loss', units='kWh', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_subarray1_dc_wiring_loss: Final[float] = OUTPUT(label='Subarray 1 DC wiring loss', units='kWh', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_subarray1_dc_tracking_loss: Final[float] = OUTPUT(label='Subarray 1 DC tracking loss', units='kWh', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_subarray1_dc_nameplate_loss: Final[float] = OUTPUT(label='Subarray 1 DC nameplate loss', units='kWh', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_subarray2_dc_gross: Final[float] = OUTPUT(label='Subarray 2 Gross DC energy', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray2_dc_mismatch_loss: Final[float] = OUTPUT(label='Subarray 2 DC mismatch loss', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray2_dc_diodes_loss: Final[float] = OUTPUT(label='Subarray 2 DC diodes and connections loss', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray2_dc_wiring_loss: Final[float] = OUTPUT(label='Subarray 2 DC wiring loss', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray2_dc_tracking_loss: Final[float] = OUTPUT(label='Subarray 2 DC tracking loss', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray2_dc_nameplate_loss: Final[float] = OUTPUT(label='Subarray 2 DC nameplate loss', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray3_dc_gross: Final[float] = OUTPUT(label='Subarray 3 Gross DC energy', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray3_dc_mismatch_loss: Final[float] = OUTPUT(label='Subarray 3 DC mismatch loss', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray3_dc_diodes_loss: Final[float] = OUTPUT(label='Subarray 3 DC diodes and connections loss', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray3_dc_wiring_loss: Final[float] = OUTPUT(label='Subarray 3 DC wiring loss', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray3_dc_tracking_loss: Final[float] = OUTPUT(label='Subarray 3 DC tracking loss', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray3_dc_nameplate_loss: Final[float] = OUTPUT(label='Subarray 3 DC nameplate loss', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray4_dc_gross: Final[float] = OUTPUT(label='Subarray 4 Gross DC energy', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray4_dc_mismatch_loss: Final[float] = OUTPUT(label='Subarray 4 DC mismatch loss', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray4_dc_diodes_loss: Final[float] = OUTPUT(label='Subarray 4 DC diodes and connections loss', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray4_dc_wiring_loss: Final[float] = OUTPUT(label='Subarray 4 DC wiring loss', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray4_dc_tracking_loss: Final[float] = OUTPUT(label='Subarray 4 DC tracking loss', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_subarray4_dc_nameplate_loss: Final[float] = OUTPUT(label='Subarray 4 DC nameplate loss', units='kWh', type='NUMBER', group='Annual (Year 1)')
    annual_dc_mismatch_loss: Final[float] = OUTPUT(label='DC mismatch loss', units='kWh', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_dc_diodes_loss: Final[float] = OUTPUT(label='DC diodes and connections loss', units='kWh', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_dc_wiring_loss: Final[float] = OUTPUT(label='DC wiring loss', units='kWh', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_dc_tracking_loss: Final[float] = OUTPUT(label='DC tracking loss', units='kWh', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_dc_nameplate_loss: Final[float] = OUTPUT(label='DC nameplate loss', units='kWh', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_dc_optimizer_loss: Final[float] = OUTPUT(label='DC power optimizer loss', units='kWh', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_poa_shading_loss_percent: Final[float] = OUTPUT(label='POA front-side shading loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_poa_soiling_loss_percent: Final[float] = OUTPUT(label='POA front-side soiling loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_poa_cover_loss_percent: Final[float] = OUTPUT(label='POA front-side reflection (IAM) loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_poa_rear_gain_percent: Final[float] = OUTPUT(label='POA rear-side bifacial gain', units='%', type='NUMBER', group='Loss', required='*')
    annual_dc_module_loss_percent: Final[float] = OUTPUT(label='DC module modeled loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_dc_snow_loss_percent: Final[float] = OUTPUT(label='DC snow loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_dc_mppt_clip_loss_percent: Final[float] = OUTPUT(label='DC inverter MPPT clipping loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_dc_mismatch_loss_percent: Final[float] = OUTPUT(label='DC mismatch loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_dc_diodes_loss_percent: Final[float] = OUTPUT(label='DC diodes and connections loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_dc_wiring_loss_percent: Final[float] = OUTPUT(label='DC wiring loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_dc_tracking_loss_percent: Final[float] = OUTPUT(label='DC tracking loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_dc_nameplate_loss_percent: Final[float] = OUTPUT(label='DC nameplate loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_dc_optimizer_loss_percent: Final[float] = OUTPUT(label='DC power optimizer loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_dc_perf_adj_loss_percent: Final[float] = OUTPUT(label='DC performance adjustment loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_dc_lifetime_loss_percent: Final[float] = OUTPUT(label='Lifetime daily DC loss- year 1', units='%', type='NUMBER', group='Loss', required='*')
    annual_dc_battery_loss_percent: Final[float] = OUTPUT(label='DC connected battery loss- year 1', units='%', type='NUMBER', group='Loss', required='*')
    annual_ac_inv_clip_loss_percent: Final[float] = OUTPUT(label='AC inverter power clipping loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_ac_inv_pso_loss_percent: Final[float] = OUTPUT(label='AC inverter power consumption loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_ac_inv_pnt_loss_percent: Final[float] = OUTPUT(label='AC inverter night tare loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_ac_inv_tdc_loss_percent: Final[float] = OUTPUT(label='AC inverter thermal derate loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_ac_inv_eff_loss_percent: Final[float] = OUTPUT(label='AC inverter efficiency loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_ac_wiring_loss_percent: Final[float] = OUTPUT(label='AC wiring loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_transmission_loss_percent: Final[float] = OUTPUT(label='Transmission loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_ac_lifetime_loss_percent: Final[float] = OUTPUT(label='Lifetime daily AC loss- year 1', units='%', type='NUMBER', group='Loss', required='*')
    annual_ac_battery_loss_percent: Final[float] = OUTPUT(label='AC connected battery loss- year 1', units='%', type='NUMBER', group='Loss', required='*')
    annual_xfmr_loss_percent: Final[float] = OUTPUT(label='Transformer loss percent', units='%', type='NUMBER', group='Loss')
    annual_ac_perf_adj_loss_percent: Final[float] = OUTPUT(label='AC performance adjustment loss', units='%', type='NUMBER', group='Loss', required='*')
    annual_ac_wiring_loss: Final[float] = OUTPUT(label='AC wiring loss', units='kWh', type='NUMBER', group='Annual (Year 1)', required='*')
    annual_transmission_loss: Final[float] = OUTPUT(label='Transmission loss', units='kWh', type='NUMBER', group='Annual (Year 1)', required='*')
    _6par_a: Final[float] = OUTPUT(name='6par_a', label='CEC 6-parameter: a', type='NUMBER', group='Module CEC 6-parameter model parameters', required='*')
    _6par_Io: Final[float] = OUTPUT(name='6par_Io', label='CEC 6-parameter: Io', type='NUMBER', group='Module CEC 6-parameter model parameters', required='*')
    _6par_Il: Final[float] = OUTPUT(name='6par_Il', label='CEC 6-parameter: Il', type='NUMBER', group='Module CEC 6-parameter model parameters', required='*')
    _6par_Rs: Final[float] = OUTPUT(name='6par_Rs', label='CEC 6-parameter: Rs', type='NUMBER', group='Module CEC 6-parameter model parameters', required='*')
    _6par_Rsh: Final[float] = OUTPUT(name='6par_Rsh', label='CEC 6-parameter: Rsh', type='NUMBER', group='Module CEC 6-parameter model parameters', required='*')
    _6par_Adj: Final[float] = OUTPUT(name='6par_Adj', label='CEC 6-parameter: Adj', type='NUMBER', group='Module CEC 6-parameter model parameters', required='*')
    performance_ratio: Final[float] = OUTPUT(label='Performance ratio', type='NUMBER', group='Annual (Year 1)', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', group='Annual (Year 1)', required='*')
    capacity_factor_ac: Final[float] = OUTPUT(label='Capacity factor based on AC system capacity', units='%', type='NUMBER', group='Annual (Year 1)', required='*')
    kwh_per_kw: Final[float] = OUTPUT(label='First year kWh(AC)/kW(DC)', units='kWh/kW', type='NUMBER', group='Annual (Year 1)', required='*')
    ts_shift_hours: Final[float] = OUTPUT(label='Sun position time offset', units='hours', type='NUMBER', group='Miscellaneous', required='*')
    nameplate_dc_rating: Final[float] = OUTPUT(label='System nameplate DC rating', units='kW', type='NUMBER', group='Miscellaneous', required='*')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    dc_adjust_constant: float = INPUT(name='dc_adjust:constant', label='DC Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', constraints='MAX=100')
    dc_adjust_hourly: Array = INPUT(name='dc_adjust:hourly', label='DC Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', constraints='LENGTH=8760')
    dc_adjust_periods: Matrix = INPUT(name='dc_adjust:periods', label='DC Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    gen: Final[Array] = OUTPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')
    batt_chem: float = INPUT(label='Battery chemistry', type='NUMBER', group='Battery', meta='0=LeadAcid,1=LiIon')
    inv_snl_eff_cec: float = INPUT(label='Inverter Sandia CEC Efficiency', units='%', type='NUMBER', group='pvsamv1')
    inv_pd_eff: float = INPUT(label='Inverter Partload Efficiency', units='%', type='NUMBER', group='pvsamv1')
    inv_cec_cg_eff_cec: float = INPUT(label='Inverter Coefficient Generator CEC Efficiency', units='%', type='NUMBER', group='pvsamv1')
    batt_ac_or_dc: float = INPUT(label='Battery interconnection (AC or DC)', type='NUMBER', group='Battery', meta='0=DC_Connected,1=AC_Connected')
    batt_dc_dc_efficiency: float = INPUT(label='PV DC to battery DC efficiency', type='NUMBER', group='Battery')
    batt_dc_ac_efficiency: float = INPUT(label='Battery DC to AC efficiency', type='NUMBER', group='Battery')
    batt_ac_dc_efficiency: float = INPUT(label='Inverter AC to battery DC efficiency', type='NUMBER', group='Battery')
    batt_meter_position: float = INPUT(label='Position of battery relative to electric meter', type='NUMBER', group='Battery', meta='0=BehindTheMeter,1=FrontOfMeter')
    batt_losses: Array = INPUT(label='Battery system losses at each timestep', units='kW', type='ARRAY', group='Battery', required='?=0')
    batt_losses_charging: Array = INPUT(label='Battery system losses when charging', units='kW', type='ARRAY', group='Battery', required='?=0')
    batt_losses_discharging: Array = INPUT(label='Battery system losses when discharging', units='kW', type='ARRAY', group='Battery', required='?=0')
    batt_losses_idle: Array = INPUT(label='Battery system losses when idle', units='kW', type='ARRAY', group='Battery', required='?=0')
    batt_loss_choice: float = INPUT(label='Loss power input option', units='0/1', type='NUMBER', group='Battery', required='?=0', meta='0=Monthly,1=TimeSeries')
    batt_current_choice: float = INPUT(label='Limit cells by current or power', type='NUMBER', group='Battery')
    batt_computed_strings: float = INPUT(label='Number of strings of cells', type='NUMBER', group='Battery')
    batt_computed_series: float = INPUT(label='Number of cells in series', type='NUMBER', group='Battery')
    batt_computed_bank_capacity: float = INPUT(label='Computed bank capacity', units='kWh', type='NUMBER', group='Battery')
    batt_current_charge_max: float = INPUT(label='Maximum charge current', units='A', type='NUMBER', group='Battery')
    batt_current_discharge_max: float = INPUT(label='Maximum discharge current', units='A', type='NUMBER', group='Battery')
    batt_power_charge_max: float = INPUT(label='Maximum charge power', units='kW', type='NUMBER', group='Battery')
    batt_power_discharge_max: float = INPUT(label='Maximum discharge power', units='kW', type='NUMBER', group='Battery')
    batt_voltage_choice: float = INPUT(label='Battery voltage input option', units='0/1', type='NUMBER', group='Battery', required='?=0', meta='0=UseVoltageModel,1=InputVoltageTable')
    batt_Vfull: float = INPUT(label='Fully charged cell voltage', units='V', type='NUMBER', group='Battery')
    batt_Vexp: float = INPUT(label='Cell voltage at end of exponential zone', units='V', type='NUMBER', group='Battery')
    batt_Vnom: float = INPUT(label='Cell voltage at end of nominal zone', units='V', type='NUMBER', group='Battery')
    batt_Vnom_default: float = INPUT(label='Default nominal cell voltage', units='V', type='NUMBER', group='Battery')
    batt_Qfull: float = INPUT(label='Fully charged cell capacity', units='Ah', type='NUMBER', group='Battery')
    batt_Qfull_flow: float = INPUT(label='Fully charged flow battery capacity', units='Ah', type='NUMBER', group='Battery')
    batt_Qexp: float = INPUT(label='Cell capacity at end of exponential zone', units='Ah', type='NUMBER', group='Battery')
    batt_Qnom: float = INPUT(label='Cell capacity at end of nominal zone', units='Ah', type='NUMBER', group='Battery')
    batt_C_rate: float = INPUT(label='Rate at which voltage vs. capacity curve input', type='NUMBER', group='Battery')
    batt_resistance: float = INPUT(label='Internal resistance', units='Ohm', type='NUMBER', group='Battery')
    batt_voltage_matrix: Matrix = INPUT(label='Battery voltage vs. depth-of-discharge', type='MATRIX', group='Battery')
    LeadAcid_q20_computed: float = INPUT(label='Capacity at 20-hour discharge rate', units='Ah', type='NUMBER', group='Battery')
    LeadAcid_q10_computed: float = INPUT(label='Capacity at 10-hour discharge rate', units='Ah', type='NUMBER', group='Battery')
    LeadAcid_qn_computed: float = INPUT(label='Capacity at discharge rate for n-hour rate', units='Ah', type='NUMBER', group='Battery')
    LeadAcid_tn: float = INPUT(label='Time to discharge', units='h', type='NUMBER', group='Battery')
    batt_initial_SOC: float = INPUT(label='Initial state-of-charge', units='%', type='NUMBER', group='Battery')
    batt_minimum_SOC: float = INPUT(label='Minimum allowed state-of-charge', units='%', type='NUMBER', group='Battery')
    batt_maximum_SOC: float = INPUT(label='Maximum allowed state-of-charge', units='%', type='NUMBER', group='Battery')
    batt_minimum_modetime: float = INPUT(label='Minimum time at charge state', units='min', type='NUMBER', group='Battery')
    batt_lifetime_matrix: Matrix = INPUT(label='Cycles vs capacity at different depths-of-discharge', type='MATRIX', group='Battery')
    batt_calendar_choice: float = INPUT(label='Calendar life degradation input option', units='0/1/2', type='NUMBER', group='Battery', meta='0=NoCalendarDegradation,1=LithiomIonModel,2=InputLossTable')
    batt_calendar_lifetime_matrix: Matrix = INPUT(label='Days vs capacity', type='MATRIX', group='Battery')
    batt_calendar_q0: float = INPUT(label='Calendar life model initial capacity cofficient', type='NUMBER', group='Battery')
    batt_calendar_a: float = INPUT(label='Calendar life model coefficient', units='1/sqrt(day)', type='NUMBER', group='Battery')
    batt_calendar_b: float = INPUT(label='Calendar life model coefficient', units='K', type='NUMBER', group='Battery')
    batt_calendar_c: float = INPUT(label='Calendar life model coefficient', units='K', type='NUMBER', group='Battery')
    batt_replacement_capacity: float = INPUT(label='Capacity degradation at which to replace battery', units='%', type='NUMBER', group='Battery')
    batt_replacement_option: float = INPUT(label='Enable battery replacement?', units='0=none,1=capacity based,2=user schedule', type='NUMBER', group='Battery', required='?=0', constraints='INTEGER,MIN=0,MAX=2')
    batt_replacement_schedule: Array = INPUT(label='Battery bank replacements per year (user specified)', units='number/year', type='ARRAY', group='Battery', required='batt_replacement_option=2')
    batt_replacement_cost: float = INPUT(label='Cost to replace battery per kWh', units='$/kWh', type='NUMBER', group='Battery')
    batt_mass: float = INPUT(label='Battery mass', units='kg', type='NUMBER', group='Battery')
    batt_length: float = INPUT(label='Battery length', units='m', type='NUMBER', group='Battery')
    batt_width: float = INPUT(label='Battery width', units='m', type='NUMBER', group='Battery')
    batt_height: float = INPUT(label='Battery height', units='m', type='NUMBER', group='Battery')
    batt_Cp: float = INPUT(label='Battery specific heat capacity', units='J/KgK', type='NUMBER', group='Battery')
    batt_h_to_ambient: float = INPUT(label='Heat transfer between battery and environment', units='W/m2K', type='NUMBER', group='Battery')
    T_room: float = INPUT(label='Temperature of storage room', units='C', type='NUMBER', group='Battery')
    cap_vs_temp: Matrix = INPUT(label='Effective capacity as function of temperature', units='C,%', type='MATRIX', group='Battery')
    dispatch_manual_charge: Array = INPUT(label='Periods 1-6 charging allowed?', type='ARRAY', group='Battery', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_discharge: Array = INPUT(label='Periods 1-6 discharging allowed?', type='ARRAY', group='Battery', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_gridcharge: Array = INPUT(label='Periods 1-6 grid charging allowed?', type='ARRAY', group='Battery', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_percent_discharge: Array = INPUT(label='Periods 1-6 discharge percent', units='%', type='ARRAY', group='Battery', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_percent_gridcharge: Array = INPUT(label='Periods 1-6 gridcharge percent', units='%', type='ARRAY', group='Battery', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_sched: Matrix = INPUT(label='Battery dispatch schedule for weekday', type='MATRIX', group='Battery', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_sched_weekend: Matrix = INPUT(label='Battery dispatch schedule for weekend', type='MATRIX', group='Battery', required='en_batt=1&batt_dispatch_choice=4')
    batt_target_power: Array = INPUT(label='Grid target power (AC) for every time step', units='kWac', type='ARRAY', group='Battery', required='en_batt=1&batt_meter_position=0&batt_dispatch_choice=2')
    batt_target_power_monthly: Array = INPUT(label='Grid target power (AC) on monthly basis', units='kWac', type='ARRAY', group='Battery', required='en_batt=1&batt_meter_position=0&batt_dispatch_choice=2')
    batt_target_choice: float = INPUT(label='Target power input option', units='0/1', type='NUMBER', group='Battery', required='en_batt=1&batt_meter_position=0&batt_dispatch_choice=2', meta='0=InputMonthlyTarget,1=InputFullTimeSeries')
    batt_custom_dispatch: Array = INPUT(label='Custom battery power (DC) for every time step', units='kWdc', type='ARRAY', group='Battery', required='en_batt=1&batt_dispatch_choice=3')
    batt_dispatch_choice: float = INPUT(label='Battery dispatch algorithm', units='0/1/2/3/4', type='NUMBER', group='Battery', required='en_batt=1', meta='If behind the meter: 0=PeakShavingLookAhead,1=PeakShavingLookBehind,2=InputGridTarget,3=InputBatteryPower,4=ManualDispatch, if front of meter: 0=AutomatedLookAhead,1=AutomatedLookBehind,2=AutomatedInputForecast,3=InputBatteryPower,4=ManualDispatch')
    batt_pv_clipping_forecast: Array = INPUT(label='PV clipping forecast', units='kW', type='ARRAY', group='Battery', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2')
    batt_pv_dc_forecast: Array = INPUT(label='PV dc power forecast', units='kW', type='ARRAY', group='Battery', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2')
    batt_dispatch_auto_can_gridcharge: float = INPUT(label='Grid charging allowed for automated dispatch?', units='kW', type='NUMBER', group='Battery')
    batt_dispatch_auto_can_charge: float = INPUT(label='PV charging allowed for automated dispatch?', units='kW', type='NUMBER', group='Battery')
    batt_dispatch_auto_can_clipcharge: float = INPUT(label='Battery can charge from clipped PV for automated dispatch?', units='kW', type='NUMBER', group='Battery')
    batt_auto_gridcharge_max_daily: float = INPUT(label='Allowed grid charging percent per day for automated dispatch', units='kW', type='NUMBER', group='Battery')
    batt_look_ahead_hours: float = INPUT(label='Hours to look ahead in automated dispatch', units='hours', type='NUMBER', group='Battery')
    batt_dispatch_update_frequency_hours: float = INPUT(label='Frequency to update the look-ahead dispatch', units='hours', type='NUMBER', group='Battery')
    batt_cycle_cost_choice: float = INPUT(label='Use SAM model for cycle costs or input custom', units='0/1', type='NUMBER', group='Battery', meta='0=UseCostModel,1=InputCost')
    batt_cycle_cost: float = INPUT(label='Input battery cycle costs', units='$/cycle-kWh', type='NUMBER', group='Battery')
    en_electricity_rates: float = INPUT(label='Enable Electricity Rates', type='NUMBER', group='0=EnableElectricityRates,1=NoRates', meta='0/1')
    ur_ec_sched_weekday: Matrix = INPUT(label='Energy charge weekday schedule', type='MATRIX', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2', meta='12 x 24 matrix')
    ur_ec_sched_weekend: Matrix = INPUT(label='Energy charge weekend schedule', type='MATRIX', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2', meta='12 x 24 matrix')
    ur_ec_tou_mat: Matrix = INPUT(label='Energy rates table', type='MATRIX', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2')
    ppa_price_input: float = INPUT(label='PPA Price Input', type='NUMBER', group='Time of Delivery', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2')
    ppa_multiplier_model: float = INPUT(label='PPA multiplier model', units='0/1', type='NUMBER', group='Time of Delivery', required='?=0', constraints='INTEGER,MIN=0', meta='0=diurnal,1=timestep')
    dispatch_factors_ts: Array = INPUT(label='Dispatch payment factor time step', type='ARRAY', group='Time of Delivery', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2&ppa_multiplier_model=1')
    dispatch_tod_factors: Array = INPUT(label='TOD factors for periods 1-9', type='ARRAY', group='Time of Delivery', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2&ppa_multiplier_model=0')
    dispatch_sched_weekday: Matrix = INPUT(label='Diurnal weekday TOD periods', units='1..9', type='MATRIX', group='Time of Delivery', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2&ppa_multiplier_model=0', meta='12 x 24 matrix')
    dispatch_sched_weekend: Matrix = INPUT(label='Diurnal weekend TOD periods', units='1..9', type='MATRIX', group='Time of Delivery', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2&ppa_multiplier_model=0', meta='12 x 24 matrix')
    batt_q0: Final[Array] = OUTPUT(label='Battery total charge', units='Ah', type='ARRAY', group='Battery')
    batt_q1: Final[Array] = OUTPUT(label='Battery available charge', units='Ah', type='ARRAY', group='Battery')
    batt_q2: Final[Array] = OUTPUT(label='Battery bound charge', units='Ah', type='ARRAY', group='Battery')
    batt_SOC: Final[Array] = OUTPUT(label='Battery state of charge', units='%', type='ARRAY', group='Battery')
    batt_DOD: Final[Array] = OUTPUT(label='Battery cycle depth of discharge', units='%', type='ARRAY', group='Battery')
    batt_qmaxI: Final[Array] = OUTPUT(label='Battery maximum capacity at current', units='Ah', type='ARRAY', group='Battery')
    batt_qmax: Final[Array] = OUTPUT(label='Battery maximum charge with degradation', units='Ah', type='ARRAY', group='Battery')
    batt_qmax_thermal: Final[Array] = OUTPUT(label='Battery maximum charge at temperature', units='Ah', type='ARRAY', group='Battery')
    batt_I: Final[Array] = OUTPUT(label='Battery current', units='A', type='ARRAY', group='Battery')
    batt_voltage_cell: Final[Array] = OUTPUT(label='Battery cell voltage', units='V', type='ARRAY', group='Battery')
    batt_voltage: Final[Array] = OUTPUT(label='Battery voltage', units='V', type='ARRAY', group='Battery')
    batt_DOD_cycle_average: Final[Array] = OUTPUT(label='Battery average cycle DOD', type='ARRAY', group='Battery')
    batt_cycles: Final[Array] = OUTPUT(label='Battery number of cycles', type='ARRAY', group='Battery')
    batt_temperature: Final[Array] = OUTPUT(label='Battery temperature', units='C', type='ARRAY', group='Battery')
    batt_capacity_percent: Final[Array] = OUTPUT(label='Battery capacity percent for lifetime', units='%', type='ARRAY', group='Battery')
    batt_capacity_thermal_percent: Final[Array] = OUTPUT(label='Battery capacity percent for temperature', units='%', type='ARRAY', group='Battery')
    batt_bank_replacement: Final[Array] = OUTPUT(label='Battery bank replacements per year', units='number/year', type='ARRAY', group='Battery')
    batt_power: Final[Array] = OUTPUT(label='Electricity to/from battery', units='kW', type='ARRAY', group='Battery')
    grid_power: Final[Array] = OUTPUT(label='Electricity to/from grid', units='kW', type='ARRAY', group='Battery')
    pv_to_load: Final[Array] = OUTPUT(label='Electricity to load from PV', units='kW', type='ARRAY', group='Battery')
    batt_to_load: Final[Array] = OUTPUT(label='Electricity to load from battery', units='kW', type='ARRAY', group='Battery')
    grid_to_load: Final[Array] = OUTPUT(label='Electricity to load from grid', units='kW', type='ARRAY', group='Battery')
    pv_to_batt: Final[Array] = OUTPUT(label='Electricity to battery from PV', units='kW', type='ARRAY', group='Battery')
    grid_to_batt: Final[Array] = OUTPUT(label='Electricity to battery from grid', units='kW', type='ARRAY', group='Battery')
    pv_to_grid: Final[Array] = OUTPUT(label='Electricity to grid from PV', units='kW', type='ARRAY', group='Battery')
    batt_to_grid: Final[Array] = OUTPUT(label='Electricity to grid from battery', units='kW', type='ARRAY', group='Battery')
    batt_conversion_loss: Final[Array] = OUTPUT(label='Electricity loss in battery power electronics', units='kW', type='ARRAY', group='Battery')
    batt_system_loss: Final[Array] = OUTPUT(label='Electricity loss from battery ancillary equipment', units='kW', type='ARRAY', group='Battery')
    grid_power_target: Final[Array] = OUTPUT(label='Electricity grid power target for automated dispatch', units='kW', type='ARRAY', group='Battery')
    batt_power_target: Final[Array] = OUTPUT(label='Electricity battery power target for automated dispatch', units='kW', type='ARRAY', group='Battery')
    batt_cost_to_cycle: Final[Array] = OUTPUT(label='Battery computed cost to cycle', units='$/cycle', type='ARRAY', group='Battery')
    market_sell_rate_series_yr1: Final[Array] = OUTPUT(label='Market sell rate (Year 1)', units='$/MWh', type='ARRAY', group='Battery')
    monthly_pv_to_load: Final[Array] = OUTPUT(label='Energy to load from PV', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_batt_to_load: Final[Array] = OUTPUT(label='Energy to load from battery', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_grid_to_load: Final[Array] = OUTPUT(label='Energy to load from grid', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_pv_to_grid: Final[Array] = OUTPUT(label='Energy to grid from PV', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_batt_to_grid: Final[Array] = OUTPUT(label='Energy to grid from battery', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_pv_to_batt: Final[Array] = OUTPUT(label='Energy to battery from PV', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_grid_to_batt: Final[Array] = OUTPUT(label='Energy to battery from grid', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    batt_annual_charge_from_pv: Final[Array] = OUTPUT(label='Battery annual energy charged from PV', units='kWh', type='ARRAY', group='Battery')
    batt_annual_charge_from_grid: Final[Array] = OUTPUT(label='Battery annual energy charged from grid', units='kWh', type='ARRAY', group='Battery')
    batt_annual_charge_energy: Final[Array] = OUTPUT(label='Battery annual energy charged', units='kWh', type='ARRAY', group='Battery')
    batt_annual_discharge_energy: Final[Array] = OUTPUT(label='Battery annual energy discharged', units='kWh', type='ARRAY', group='Battery')
    batt_annual_energy_loss: Final[Array] = OUTPUT(label='Battery annual energy loss', units='kWh', type='ARRAY', group='Battery')
    batt_annual_energy_system_loss: Final[Array] = OUTPUT(label='Battery annual system energy loss', units='kWh', type='ARRAY', group='Battery')
    annual_export_to_grid_energy: Final[Array] = OUTPUT(label='Annual energy exported to grid', units='kWh', type='ARRAY', group='Battery')
    annual_import_to_grid_energy: Final[Array] = OUTPUT(label='Annual energy imported from grid', units='kWh', type='ARRAY', group='Battery')
    average_battery_conversion_efficiency: Final[float] = OUTPUT(label='Battery average cycle conversion efficiency', units='%', type='NUMBER', group='Annual')
    average_battery_roundtrip_efficiency: Final[float] = OUTPUT(label='Battery average roundtrip efficiency', units='%', type='NUMBER', group='Annual')
    batt_pv_charge_percent: Final[float] = OUTPUT(label='Battery percent energy charged from PV', units='%', type='NUMBER', group='Annual')
    batt_bank_installed_capacity: Final[float] = OUTPUT(label='Battery bank installed capacity', units='kWh', type='NUMBER', group='Annual')
    batt_dispatch_sched: Final[Matrix] = OUTPUT(label='Battery dispatch schedule', type='MATRIX', group='Battery')

    def __init__(self, *args: Mapping[str, Any],
                 solar_resource_file: str = ...,
                 solar_resource_data: Table = ...,
                 transformer_no_load_loss: float = ...,
                 transformer_load_loss: float = ...,
                 system_use_lifetime_output: float = ...,
                 analysis_period: float = ...,
                 dc_degradation: Array = ...,
                 en_dc_lifetime_losses: float = ...,
                 dc_lifetime_losses: Array = ...,
                 en_ac_lifetime_losses: float = ...,
                 ac_lifetime_losses: Array = ...,
                 en_snow_model: float = ...,
                 system_capacity: float = ...,
                 use_wf_albedo: float = ...,
                 albedo: Array = ...,
                 irrad_mode: float = ...,
                 sky_model: float = ...,
                 inverter_count: float = ...,
                 enable_mismatch_vmax_calc: float = ...,
                 subarray1_nstrings: float = ...,
                 subarray1_modules_per_string: float = ...,
                 subarray1_mppt_input: float = ...,
                 subarray1_tilt: float = ...,
                 subarray1_tilt_eq_lat: float = ...,
                 subarray1_azimuth: float = ...,
                 subarray1_track_mode: float = ...,
                 subarray1_rotlim: float = ...,
                 subarray1_shade_mode: float = ...,
                 subarray1_gcr: float = ...,
                 subarray1_monthly_tilt: Array = ...,
                 subarray1_shading_string_option: float = ...,
                 subarray1_shading_timestep: Matrix = ...,
                 subarray1_shading_mxh: Matrix = ...,
                 subarray1_shading_azal: Matrix = ...,
                 subarray1_shading_diff: float = ...,
                 subarray1_soiling: Array = ...,
                 subarray1_rear_irradiance_loss: float = ...,
                 subarray1_mismatch_loss: float = ...,
                 subarray1_diodeconn_loss: float = ...,
                 subarray1_dcwiring_loss: float = ...,
                 subarray1_tracking_loss: float = ...,
                 subarray1_nameplate_loss: float = ...,
                 subarray2_rear_irradiance_loss: float = ...,
                 subarray2_mismatch_loss: float = ...,
                 subarray2_diodeconn_loss: float = ...,
                 subarray2_dcwiring_loss: float = ...,
                 subarray2_tracking_loss: float = ...,
                 subarray2_nameplate_loss: float = ...,
                 subarray3_rear_irradiance_loss: float = ...,
                 subarray3_mismatch_loss: float = ...,
                 subarray3_diodeconn_loss: float = ...,
                 subarray3_dcwiring_loss: float = ...,
                 subarray3_tracking_loss: float = ...,
                 subarray3_nameplate_loss: float = ...,
                 subarray4_rear_irradiance_loss: float = ...,
                 subarray4_mismatch_loss: float = ...,
                 subarray4_diodeconn_loss: float = ...,
                 subarray4_dcwiring_loss: float = ...,
                 subarray4_tracking_loss: float = ...,
                 subarray4_nameplate_loss: float = ...,
                 dcoptimizer_loss: float = ...,
                 acwiring_loss: float = ...,
                 transmission_loss: float = ...,
                 subarray1_mod_orient: float = ...,
                 subarray1_nmodx: float = ...,
                 subarray1_nmody: float = ...,
                 subarray1_backtrack: float = ...,
                 subarray2_enable: float = ...,
                 subarray2_modules_per_string: float = ...,
                 subarray2_nstrings: float = ...,
                 subarray2_mppt_input: float = ...,
                 subarray2_tilt: float = ...,
                 subarray2_tilt_eq_lat: float = ...,
                 subarray2_azimuth: float = ...,
                 subarray2_track_mode: float = ...,
                 subarray2_rotlim: float = ...,
                 subarray2_shade_mode: float = ...,
                 subarray2_gcr: float = ...,
                 subarray2_monthly_tilt: Array = ...,
                 subarray2_shading_string_option: float = ...,
                 subarray2_shading_timestep: Matrix = ...,
                 subarray2_shading_mxh: Matrix = ...,
                 subarray2_shading_azal: Matrix = ...,
                 subarray2_shading_diff: float = ...,
                 subarray2_soiling: Array = ...,
                 subarray2_mod_orient: float = ...,
                 subarray2_nmodx: float = ...,
                 subarray2_nmody: float = ...,
                 subarray2_backtrack: float = ...,
                 subarray3_enable: float = ...,
                 subarray3_modules_per_string: float = ...,
                 subarray3_nstrings: float = ...,
                 subarray3_mppt_input: float = ...,
                 subarray3_tilt: float = ...,
                 subarray3_tilt_eq_lat: float = ...,
                 subarray3_azimuth: float = ...,
                 subarray3_track_mode: float = ...,
                 subarray3_rotlim: float = ...,
                 subarray3_shade_mode: float = ...,
                 subarray3_gcr: float = ...,
                 subarray3_monthly_tilt: Array = ...,
                 subarray3_shading_string_option: float = ...,
                 subarray3_shading_timestep: Matrix = ...,
                 subarray3_shading_mxh: Matrix = ...,
                 subarray3_shading_azal: Matrix = ...,
                 subarray3_shading_diff: float = ...,
                 subarray3_soiling: Array = ...,
                 subarray3_mod_orient: float = ...,
                 subarray3_nmodx: float = ...,
                 subarray3_nmody: float = ...,
                 subarray3_backtrack: float = ...,
                 subarray4_enable: float = ...,
                 subarray4_modules_per_string: float = ...,
                 subarray4_nstrings: float = ...,
                 subarray4_mppt_input: float = ...,
                 subarray4_tilt: float = ...,
                 subarray4_tilt_eq_lat: float = ...,
                 subarray4_azimuth: float = ...,
                 subarray4_track_mode: float = ...,
                 subarray4_rotlim: float = ...,
                 subarray4_shade_mode: float = ...,
                 subarray4_gcr: float = ...,
                 subarray4_monthly_tilt: Array = ...,
                 subarray4_shading_string_option: float = ...,
                 subarray4_shading_timestep: Matrix = ...,
                 subarray4_shading_mxh: Matrix = ...,
                 subarray4_shading_azal: Matrix = ...,
                 subarray4_shading_diff: float = ...,
                 subarray4_soiling: Array = ...,
                 subarray4_mod_orient: float = ...,
                 subarray4_nmodx: float = ...,
                 subarray4_nmody: float = ...,
                 subarray4_backtrack: float = ...,
                 module_model: float = ...,
                 module_aspect_ratio: float = ...,
                 spe_area: float = ...,
                 spe_rad0: float = ...,
                 spe_rad1: float = ...,
                 spe_rad2: float = ...,
                 spe_rad3: float = ...,
                 spe_rad4: float = ...,
                 spe_eff0: float = ...,
                 spe_eff1: float = ...,
                 spe_eff2: float = ...,
                 spe_eff3: float = ...,
                 spe_eff4: float = ...,
                 spe_reference: float = ...,
                 spe_module_structure: float = ...,
                 spe_a: float = ...,
                 spe_b: float = ...,
                 spe_dT: float = ...,
                 spe_temp_coeff: float = ...,
                 spe_fd: float = ...,
                 spe_vmp: float = ...,
                 spe_voc: float = ...,
                 spe_is_bifacial: float = ...,
                 spe_bifacial_transmission_factor: float = ...,
                 spe_bifaciality: float = ...,
                 spe_bifacial_ground_clearance_height: float = ...,
                 cec_area: float = ...,
                 cec_a_ref: float = ...,
                 cec_adjust: float = ...,
                 cec_alpha_sc: float = ...,
                 cec_beta_oc: float = ...,
                 cec_gamma_r: float = ...,
                 cec_i_l_ref: float = ...,
                 cec_i_mp_ref: float = ...,
                 cec_i_o_ref: float = ...,
                 cec_i_sc_ref: float = ...,
                 cec_n_s: float = ...,
                 cec_r_s: float = ...,
                 cec_r_sh_ref: float = ...,
                 cec_t_noct: float = ...,
                 cec_v_mp_ref: float = ...,
                 cec_v_oc_ref: float = ...,
                 cec_temp_corr_mode: float = ...,
                 cec_is_bifacial: float = ...,
                 cec_bifacial_transmission_factor: float = ...,
                 cec_bifaciality: float = ...,
                 cec_bifacial_ground_clearance_height: float = ...,
                 cec_standoff: float = ...,
                 cec_height: float = ...,
                 cec_mounting_config: float = ...,
                 cec_heat_transfer: float = ...,
                 cec_mounting_orientation: float = ...,
                 cec_gap_spacing: float = ...,
                 cec_module_width: float = ...,
                 cec_module_length: float = ...,
                 cec_array_rows: float = ...,
                 cec_array_cols: float = ...,
                 cec_backside_temp: float = ...,
                 _6par_celltech: float = ...,
                 _6par_vmp: float = ...,
                 _6par_imp: float = ...,
                 _6par_voc: float = ...,
                 _6par_isc: float = ...,
                 _6par_bvoc: float = ...,
                 _6par_aisc: float = ...,
                 _6par_gpmp: float = ...,
                 _6par_nser: float = ...,
                 _6par_area: float = ...,
                 _6par_tnoct: float = ...,
                 _6par_standoff: float = ...,
                 _6par_mounting: float = ...,
                 _6par_is_bifacial: float = ...,
                 _6par_bifacial_transmission_factor: float = ...,
                 _6par_bifaciality: float = ...,
                 _6par_bifacial_ground_clearance_height: float = ...,
                 snl_module_structure: float = ...,
                 snl_a: float = ...,
                 snl_b: float = ...,
                 snl_dtc: float = ...,
                 snl_ref_a: float = ...,
                 snl_ref_b: float = ...,
                 snl_ref_dT: float = ...,
                 snl_fd: float = ...,
                 snl_a0: float = ...,
                 snl_a1: float = ...,
                 snl_a2: float = ...,
                 snl_a3: float = ...,
                 snl_a4: float = ...,
                 snl_aimp: float = ...,
                 snl_aisc: float = ...,
                 snl_area: float = ...,
                 snl_b0: float = ...,
                 snl_b1: float = ...,
                 snl_b2: float = ...,
                 snl_b3: float = ...,
                 snl_b4: float = ...,
                 snl_b5: float = ...,
                 snl_bvmpo: float = ...,
                 snl_bvoco: float = ...,
                 snl_c0: float = ...,
                 snl_c1: float = ...,
                 snl_c2: float = ...,
                 snl_c3: float = ...,
                 snl_c4: float = ...,
                 snl_c5: float = ...,
                 snl_c6: float = ...,
                 snl_c7: float = ...,
                 snl_impo: float = ...,
                 snl_isco: float = ...,
                 snl_ixo: float = ...,
                 snl_ixxo: float = ...,
                 snl_mbvmp: float = ...,
                 snl_mbvoc: float = ...,
                 snl_n: float = ...,
                 snl_series_cells: float = ...,
                 snl_vmpo: float = ...,
                 snl_voco: float = ...,
                 sd11par_nser: float = ...,
                 sd11par_area: float = ...,
                 sd11par_AMa0: float = ...,
                 sd11par_AMa1: float = ...,
                 sd11par_AMa2: float = ...,
                 sd11par_AMa3: float = ...,
                 sd11par_AMa4: float = ...,
                 sd11par_glass: float = ...,
                 sd11par_tnoct: float = ...,
                 sd11par_standoff: float = ...,
                 sd11par_mounting: float = ...,
                 sd11par_Vmp0: float = ...,
                 sd11par_Imp0: float = ...,
                 sd11par_Voc0: float = ...,
                 sd11par_Isc0: float = ...,
                 sd11par_alphaIsc: float = ...,
                 sd11par_n: float = ...,
                 sd11par_Il: float = ...,
                 sd11par_Io: float = ...,
                 sd11par_Egref: float = ...,
                 sd11par_d1: float = ...,
                 sd11par_d2: float = ...,
                 sd11par_d3: float = ...,
                 sd11par_c1: float = ...,
                 sd11par_c2: float = ...,
                 sd11par_c3: float = ...,
                 mlm_N_series: float = ...,
                 mlm_N_parallel: float = ...,
                 mlm_N_diodes: float = ...,
                 mlm_Width: float = ...,
                 mlm_Length: float = ...,
                 mlm_V_mp_ref: float = ...,
                 mlm_I_mp_ref: float = ...,
                 mlm_V_oc_ref: float = ...,
                 mlm_I_sc_ref: float = ...,
                 mlm_S_ref: float = ...,
                 mlm_T_ref: float = ...,
                 mlm_R_shref: float = ...,
                 mlm_R_sh0: float = ...,
                 mlm_R_shexp: float = ...,
                 mlm_R_s: float = ...,
                 mlm_alpha_isc: float = ...,
                 mlm_beta_voc_spec: float = ...,
                 mlm_E_g: float = ...,
                 mlm_n_0: float = ...,
                 mlm_mu_n: float = ...,
                 mlm_D2MuTau: float = ...,
                 mlm_T_mode: float = ...,
                 mlm_T_c_no_tnoct: float = ...,
                 mlm_T_c_no_mounting: float = ...,
                 mlm_T_c_no_standoff: float = ...,
                 mlm_T_c_fa_alpha: float = ...,
                 mlm_T_c_fa_U0: float = ...,
                 mlm_T_c_fa_U1: float = ...,
                 mlm_AM_mode: float = ...,
                 mlm_AM_c_sa0: float = ...,
                 mlm_AM_c_sa1: float = ...,
                 mlm_AM_c_sa2: float = ...,
                 mlm_AM_c_sa3: float = ...,
                 mlm_AM_c_sa4: float = ...,
                 mlm_AM_c_lp0: float = ...,
                 mlm_AM_c_lp1: float = ...,
                 mlm_AM_c_lp2: float = ...,
                 mlm_AM_c_lp3: float = ...,
                 mlm_AM_c_lp4: float = ...,
                 mlm_AM_c_lp5: float = ...,
                 mlm_IAM_mode: float = ...,
                 mlm_IAM_c_as: float = ...,
                 mlm_IAM_c_sa0: float = ...,
                 mlm_IAM_c_sa1: float = ...,
                 mlm_IAM_c_sa2: float = ...,
                 mlm_IAM_c_sa3: float = ...,
                 mlm_IAM_c_sa4: float = ...,
                 mlm_IAM_c_sa5: float = ...,
                 mlm_IAM_c_cs_incAngle: Array = ...,
                 mlm_IAM_c_cs_iamValue: Array = ...,
                 mlm_groundRelfectionFraction: float = ...,
                 inverter_model: float = ...,
                 mppt_low_inverter: float = ...,
                 mppt_hi_inverter: float = ...,
                 inv_num_mppt: float = ...,
                 inv_snl_c0: float = ...,
                 inv_snl_c1: float = ...,
                 inv_snl_c2: float = ...,
                 inv_snl_c3: float = ...,
                 inv_snl_paco: float = ...,
                 inv_snl_pdco: float = ...,
                 inv_snl_pnt: float = ...,
                 inv_snl_pso: float = ...,
                 inv_snl_vdco: float = ...,
                 inv_snl_vdcmax: float = ...,
                 inv_cec_cg_c0: float = ...,
                 inv_cec_cg_c1: float = ...,
                 inv_cec_cg_c2: float = ...,
                 inv_cec_cg_c3: float = ...,
                 inv_cec_cg_paco: float = ...,
                 inv_cec_cg_pdco: float = ...,
                 inv_cec_cg_pnt: float = ...,
                 inv_cec_cg_psco: float = ...,
                 inv_cec_cg_vdco: float = ...,
                 inv_cec_cg_vdcmax: float = ...,
                 inv_ds_paco: float = ...,
                 inv_ds_eff: float = ...,
                 inv_ds_pnt: float = ...,
                 inv_ds_pso: float = ...,
                 inv_ds_vdco: float = ...,
                 inv_ds_vdcmax: float = ...,
                 inv_pd_paco: float = ...,
                 inv_pd_pdco: float = ...,
                 inv_pd_partload: Array = ...,
                 inv_pd_efficiency: Array = ...,
                 inv_pd_pnt: float = ...,
                 inv_pd_vdco: float = ...,
                 inv_pd_vdcmax: float = ...,
                 ond_PNomConv: float = ...,
                 ond_PMaxOUT: float = ...,
                 ond_VOutConv: float = ...,
                 ond_VMppMin: float = ...,
                 ond_VMPPMax: float = ...,
                 ond_VAbsMax: float = ...,
                 ond_PSeuil: float = ...,
                 ond_ModeOper: str = ...,
                 ond_CompPMax: str = ...,
                 ond_CompVMax: str = ...,
                 ond_ModeAffEnum: str = ...,
                 ond_PNomDC: float = ...,
                 ond_PMaxDC: float = ...,
                 ond_IMaxDC: float = ...,
                 ond_INomDC: float = ...,
                 ond_INomAC: float = ...,
                 ond_IMaxAC: float = ...,
                 ond_TPNom: float = ...,
                 ond_TPMax: float = ...,
                 ond_TPLim1: float = ...,
                 ond_TPLimAbs: float = ...,
                 ond_PLim1: float = ...,
                 ond_PLimAbs: float = ...,
                 ond_VNomEff: Array = ...,
                 ond_NbInputs: float = ...,
                 ond_NbMPPT: float = ...,
                 ond_Aux_Loss: float = ...,
                 ond_Night_Loss: float = ...,
                 ond_lossRDc: float = ...,
                 ond_lossRAc: float = ...,
                 ond_effCurve_elements: float = ...,
                 ond_effCurve_Pdc: Matrix = ...,
                 ond_effCurve_Pac: Matrix = ...,
                 ond_effCurve_eta: Matrix = ...,
                 ond_doAllowOverpower: float = ...,
                 ond_doUseTemperatureLimit: float = ...,
                 inv_tdc_cec_db: Matrix = ...,
                 inv_tdc_cec_cg: Matrix = ...,
                 inv_tdc_ds: Matrix = ...,
                 inv_tdc_plc: Matrix = ...,
                 en_batt: float = ...,
                 load: Array = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...,
                 dc_adjust_constant: float = ...,
                 dc_adjust_hourly: Array = ...,
                 dc_adjust_periods: Matrix = ...,
                 batt_chem: float = ...,
                 inv_snl_eff_cec: float = ...,
                 inv_pd_eff: float = ...,
                 inv_cec_cg_eff_cec: float = ...,
                 batt_ac_or_dc: float = ...,
                 batt_dc_dc_efficiency: float = ...,
                 batt_dc_ac_efficiency: float = ...,
                 batt_ac_dc_efficiency: float = ...,
                 batt_meter_position: float = ...,
                 batt_losses: Array = ...,
                 batt_losses_charging: Array = ...,
                 batt_losses_discharging: Array = ...,
                 batt_losses_idle: Array = ...,
                 batt_loss_choice: float = ...,
                 batt_current_choice: float = ...,
                 batt_computed_strings: float = ...,
                 batt_computed_series: float = ...,
                 batt_computed_bank_capacity: float = ...,
                 batt_current_charge_max: float = ...,
                 batt_current_discharge_max: float = ...,
                 batt_power_charge_max: float = ...,
                 batt_power_discharge_max: float = ...,
                 batt_voltage_choice: float = ...,
                 batt_Vfull: float = ...,
                 batt_Vexp: float = ...,
                 batt_Vnom: float = ...,
                 batt_Vnom_default: float = ...,
                 batt_Qfull: float = ...,
                 batt_Qfull_flow: float = ...,
                 batt_Qexp: float = ...,
                 batt_Qnom: float = ...,
                 batt_C_rate: float = ...,
                 batt_resistance: float = ...,
                 batt_voltage_matrix: Matrix = ...,
                 LeadAcid_q20_computed: float = ...,
                 LeadAcid_q10_computed: float = ...,
                 LeadAcid_qn_computed: float = ...,
                 LeadAcid_tn: float = ...,
                 batt_initial_SOC: float = ...,
                 batt_minimum_SOC: float = ...,
                 batt_maximum_SOC: float = ...,
                 batt_minimum_modetime: float = ...,
                 batt_lifetime_matrix: Matrix = ...,
                 batt_calendar_choice: float = ...,
                 batt_calendar_lifetime_matrix: Matrix = ...,
                 batt_calendar_q0: float = ...,
                 batt_calendar_a: float = ...,
                 batt_calendar_b: float = ...,
                 batt_calendar_c: float = ...,
                 batt_replacement_capacity: float = ...,
                 batt_replacement_option: float = ...,
                 batt_replacement_schedule: Array = ...,
                 batt_replacement_cost: float = ...,
                 batt_mass: float = ...,
                 batt_length: float = ...,
                 batt_width: float = ...,
                 batt_height: float = ...,
                 batt_Cp: float = ...,
                 batt_h_to_ambient: float = ...,
                 T_room: float = ...,
                 cap_vs_temp: Matrix = ...,
                 dispatch_manual_charge: Array = ...,
                 dispatch_manual_discharge: Array = ...,
                 dispatch_manual_gridcharge: Array = ...,
                 dispatch_manual_percent_discharge: Array = ...,
                 dispatch_manual_percent_gridcharge: Array = ...,
                 dispatch_manual_sched: Matrix = ...,
                 dispatch_manual_sched_weekend: Matrix = ...,
                 batt_target_power: Array = ...,
                 batt_target_power_monthly: Array = ...,
                 batt_target_choice: float = ...,
                 batt_custom_dispatch: Array = ...,
                 batt_dispatch_choice: float = ...,
                 batt_pv_clipping_forecast: Array = ...,
                 batt_pv_dc_forecast: Array = ...,
                 batt_dispatch_auto_can_gridcharge: float = ...,
                 batt_dispatch_auto_can_charge: float = ...,
                 batt_dispatch_auto_can_clipcharge: float = ...,
                 batt_auto_gridcharge_max_daily: float = ...,
                 batt_look_ahead_hours: float = ...,
                 batt_dispatch_update_frequency_hours: float = ...,
                 batt_cycle_cost_choice: float = ...,
                 batt_cycle_cost: float = ...,
                 en_electricity_rates: float = ...,
                 ur_ec_sched_weekday: Matrix = ...,
                 ur_ec_sched_weekend: Matrix = ...,
                 ur_ec_tou_mat: Matrix = ...,
                 ppa_price_input: float = ...,
                 ppa_multiplier_model: float = ...,
                 dispatch_factors_ts: Array = ...,
                 dispatch_tod_factors: Array = ...,
                 dispatch_sched_weekday: Matrix = ...,
                 dispatch_sched_weekend: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
