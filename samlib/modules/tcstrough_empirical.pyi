
# This is a generated file

"""tcstrough_empirical - CSP model using the emperical trough TCS types."""

# VERSION: 4

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'file_name': str,
        'track_mode': float,
        'tilt': float,
        'azimuth': float,
        'system_capacity': float,
        'weekday_schedule': Matrix,
        'weekend_schedule': Matrix,
        'i_SfTi': float,
        'SfPipeHl300': float,
        'SfPipeHl1': float,
        'SfPipeHl2': float,
        'SfPipeHl3': float,
        'Stow_Angle': float,
        'DepAngle': float,
        'Distance_SCA': float,
        'Row_Distance': float,
        'NumScas': float,
        'Solar_Field_Area': float,
        'Solar_Field_Mult': float,
        'SfInTempD': float,
        'SfOutTempD': float,
        'MinHtfTemp': float,
        'HtfGalArea': float,
        'SFTempInit': float,
        'HTFFluid': float,
        'IamF0': float,
        'IamF1': float,
        'IamF2': float,
        'Ave_Focal_Length': float,
        'ScaLen': float,
        'SCA_aper': float,
        'SfAvail': float,
        'TrkTwstErr': float,
        'GeoAcc': float,
        'MirRef': float,
        'MirCln': float,
        'ConcFac': float,
        'NumHCETypes': float,
        'HCEtype': Array,
        'HCEFrac': Array,
        'HCEdust': Array,
        'HCEBelShad': Array,
        'HCEEnvTrans': Array,
        'HCEabs': Array,
        'HCEmisc': Array,
        'PerfFac': Array,
        'RefMirrAper': Array,
        'HCE_A0': Array,
        'HCE_A1': Array,
        'HCE_A2': Array,
        'HCE_A3': Array,
        'HCE_A4': Array,
        'HCE_A5': Array,
        'HCE_A6': Array,
        'TurbOutG': float,
        'TurbEffG': float,
        'PTTMAX': float,
        'PTTMIN': float,
        'MaxGrOut': float,
        'MinGrOut': float,
        'TurSUE': float,
        'T2EPLF0': float,
        'T2EPLF1': float,
        'T2EPLF2': float,
        'T2EPLF3': float,
        'T2EPLF4': float,
        'E2TPLF0': float,
        'E2TPLF1': float,
        'E2TPLF2': float,
        'E2TPLF3': float,
        'E2TPLF4': float,
        'TempCorrF': float,
        'TempCorr0': float,
        'TempCorr1': float,
        'TempCorr2': float,
        'TempCorr3': float,
        'TempCorr4': float,
        'LHVBoilEff': float,
        'TurTesEffAdj': float,
        'TurTesOutAdj': float,
        'TnkHL': float,
        'PTSmax': float,
        'PFSmax': float,
        'TSHOURS': float,
        'NUMTOU': float,
        'TSLogic': Matrix,
        'FossilFill': Array,
        'E_tes_ini': float,
        'SfPar': float,
        'SfParPF': float,
        'ChtfPar': float,
        'ChtfParPF': float,
        'CHTFParF0': float,
        'CHTFParF1': float,
        'CHTFParF2': float,
        'AntiFrPar': float,
        'BOPPar': float,
        'BOPParPF': float,
        'BOPParF0': float,
        'BOPParF1': float,
        'BOPParF2': float,
        'CtOpF': float,
        'CtPar': float,
        'CtParPF': float,
        'CtParF0': float,
        'CtParF1': float,
        'CtParF2': float,
        'HtrPar': float,
        'HtrParPF': float,
        'HtrParF0': float,
        'HtrParF1': float,
        'HtrParF2': float,
        'HhtfPar': float,
        'HhtfParPF': float,
        'HhtfParF0': float,
        'HhtfParF1': float,
        'HhtfParF2': float,
        'PbFixPar': float,
        'month': Array,
        'hour': Array,
        'solazi': Array,
        'solzen': Array,
        'beam': Array,
        'tdry': Array,
        'twet': Array,
        'wspd': Array,
        'pres': Array,
        'tou_value': Array,
        'TrackAngle': Array,
        'Theta': Array,
        'CosTheta': Array,
        'IAM': Array,
        'RowShadow': Array,
        'EndLoss': Array,
        'QnipCosTh': Array,
        'Ftrack': Array,
        'ColEff': Array,
        'Qdni': Array,
        'Qsfnipcosth': Array,
        'QsfAbs': Array,
        'RecHl': Array,
        'QsfHceHL': Array,
        'QsfPipeHL': Array,
        'Qsf': Array,
        'QsfWarmup': Array,
        'SfMassFlow': Array,
        'o_SfTi': Array,
        'SfTo': Array,
        'AveSfTemp': Array,
        'Qtts': Array,
        'Qfts': Array,
        'Ets': Array,
        'QTsHl': Array,
        'Enet': Array,
        'Egr': Array,
        'EgrSol': Array,
        'EgrFos': Array,
        'Qtpb': Array,
        'QTurSu': Array,
        'QTsFull': Array,
        'Qmin': Array,
        'Qdump': Array,
        'Qgas': Array,
        'QhtfFpHtr': Array,
        'EparCHTF': Array,
        'EparHhtf': Array,
        'EparSf': Array,
        'EparBOP': Array,
        'EparPB': Array,
        'EparHtr': Array,
        'EparCT': Array,
        'EparAnti': Array,
        'QhtfFreezeProt': Array,
        'QhtfFpTES': Array,
        'EparOffLine': Array,
        'EparOnLine': Array,
        'Epar': Array,
        'system_use_lifetime_output': float,
        'annual_energy': float,
        'annual_W_cycle_gross': float,
        'conversion_factor': float,
        'capacity_factor': float,
        'kwh_per_kw': float,
        'system_heat_rate': float,
        'annual_fuel_usage': float,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix,
        'gen': Array
}, total=False)

class Data(ssc.DataDict):
    file_name: str = INPUT(label='local weather file path', type='STRING', group='Weather', required='*', constraints='LOCAL_FILE')
    track_mode: float = INPUT(label='Tracking mode', type='NUMBER', group='Weather', required='*')
    tilt: float = INPUT(label='Tilt angle of surface/axis', type='NUMBER', group='Weather', required='*')
    azimuth: float = INPUT(label='Azimuth angle of surface/axis', type='NUMBER', group='Weather', required='*')
    system_capacity: float = INPUT(label='Nameplate capacity', units='kW', type='NUMBER', group='trough', required='*')
    weekday_schedule: Matrix = INPUT(label='12x24 Time of Use Values for week days', type='MATRIX', group='tou_translator', required='*')
    weekend_schedule: Matrix = INPUT(label='12x24 Time of Use Values for week end days', type='MATRIX', group='tou_translator', required='*')
    i_SfTi: float = INPUT(label='Solar Field HTF inlet Temperature (if -999, calculated)', units='C', type='NUMBER', group='solarfield', required='*')
    SfPipeHl300: float = INPUT(label='Solar field piping heat loss at design', units='W/m2', type='NUMBER', group='solarfield', required='*')
    SfPipeHl1: float = INPUT(label='Solar field piping heat loss at reduced temp. - linear term', units='C^(-1)', type='NUMBER', group='solarfield', required='*')
    SfPipeHl2: float = INPUT(label='Solar field piping heat loss at reduced temp. - quadratic term', units='C^(-2)', type='NUMBER', group='solarfield', required='*')
    SfPipeHl3: float = INPUT(label='Solar field piping heat loss at reduced temp. - cubic term', units='C^(-3)', type='NUMBER', group='solarfield', required='*')
    Stow_Angle: float = INPUT(label='Night-Time Trough Stow Angle', units='deg', type='NUMBER', group='solarfield', required='*')
    DepAngle: float = INPUT(label='Deployment Angle', units='deg', type='NUMBER', group='solarfield', required='*')
    Distance_SCA: float = INPUT(label='Distance between SCAs in Row', units='m', type='NUMBER', group='solarfield', required='*')
    Row_Distance: float = INPUT(label='Distance between Rows of SCAs', units='m', type='NUMBER', group='solarfield', required='*')
    NumScas: float = INPUT(label='Number of SCAs per Row', type='NUMBER', group='solarfield', required='*')
    Solar_Field_Area: float = INPUT(label='Solar Field Area', units='m2', type='NUMBER', group='solarfield', required='*')
    Solar_Field_Mult: float = INPUT(label='Solar Field Multiple', type='NUMBER', group='solarfield', required='*')
    SfInTempD: float = INPUT(label='Solar Field Design Inlet Temperature', units='C', type='NUMBER', group='solarfield', required='*')
    SfOutTempD: float = INPUT(label='Solar Field Design Outlet Temperature', units='C', type='NUMBER', group='solarfield', required='*')
    MinHtfTemp: float = INPUT(label='Minimum Heat Transfer Fluid Temperature', units='C', type='NUMBER', group='solarfield', required='*')
    HtfGalArea: float = INPUT(label='HTF Fluids in Gallons per Field Area', units='gal/m2', type='NUMBER', group='solarfield', required='*')
    SFTempInit: float = INPUT(label='Solar Field Initial Temperature', units='C', type='NUMBER', group='solarfield', required='*')
    HTFFluid: float = INPUT(label='Type of Heat Transfer Fluid used', type='NUMBER', group='solarfield', required='*', constraints='INTEGER')
    IamF0: float = INPUT(label='Label', type='NUMBER', group='sca', required='*')
    IamF1: float = INPUT(label='Label', type='NUMBER', group='sca', required='*')
    IamF2: float = INPUT(label='Label', type='NUMBER', group='sca', required='*')
    Ave_Focal_Length: float = INPUT(label='Label', type='NUMBER', group='sca', required='*')
    ScaLen: float = INPUT(label='Label', type='NUMBER', group='sca', required='*')
    SCA_aper: float = INPUT(label='Label', type='NUMBER', group='sca', required='*')
    SfAvail: float = INPUT(label='Label', type='NUMBER', group='sca', required='*')
    TrkTwstErr: float = INPUT(label='Label', type='NUMBER', group='sca', required='*')
    GeoAcc: float = INPUT(label='Label', type='NUMBER', group='sca', required='*')
    MirRef: float = INPUT(label='Label', type='NUMBER', group='sca', required='*')
    MirCln: float = INPUT(label='Label', type='NUMBER', group='sca', required='*')
    ConcFac: float = INPUT(label='Label', type='NUMBER', group='sca', required='*')
    NumHCETypes: float = INPUT(label='Number of HCE types', type='NUMBER', group='hce', required='*', constraints='INTEGER')
    HCEtype: Array = INPUT(label='Number indicating the receiver type', type='ARRAY', group='hce', required='*')
    HCEFrac: Array = INPUT(label='Fraction of field that is this type of HCE', type='ARRAY', group='hce', required='*')
    HCEdust: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCEBelShad: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCEEnvTrans: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCEabs: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCEmisc: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    PerfFac: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    RefMirrAper: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCE_A0: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCE_A1: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCE_A2: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCE_A3: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCE_A4: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCE_A5: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCE_A6: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    TurbOutG: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    TurbEffG: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    PTTMAX: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    PTTMIN: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    MaxGrOut: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    MinGrOut: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    TurSUE: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    T2EPLF0: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    T2EPLF1: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    T2EPLF2: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    T2EPLF3: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    T2EPLF4: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    E2TPLF0: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    E2TPLF1: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    E2TPLF2: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    E2TPLF3: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    E2TPLF4: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    TempCorrF: float = INPUT(label='Temp Correction Mode (0=wetbulb 1=drybulb basis)', type='NUMBER', group='pwrb', required='*', constraints='INTEGER')
    TempCorr0: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    TempCorr1: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    TempCorr2: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    TempCorr3: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    TempCorr4: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    LHVBoilEff: float = INPUT(label='Label', type='NUMBER', group='pwrb', required='*')
    TurTesEffAdj: float = INPUT(label='Label', type='NUMBER', group='tes', required='*')
    TurTesOutAdj: float = INPUT(label='Label', type='NUMBER', group='tes', required='*')
    TnkHL: float = INPUT(label='Label', type='NUMBER', group='tes', required='*')
    PTSmax: float = INPUT(label='Label', type='NUMBER', group='tes', required='*')
    PFSmax: float = INPUT(label='Label', type='NUMBER', group='tes', required='*')
    TSHOURS: float = INPUT(label='Label', type='NUMBER', group='tes', required='*')
    NUMTOU: float = INPUT(label='Label', type='NUMBER', group='tes', required='*')
    TSLogic: Matrix = INPUT(label='Label', type='MATRIX', group='tes', required='*')
    FossilFill: Array = INPUT(label='Label', type='ARRAY', group='tes', required='*')
    E_tes_ini: float = INPUT(label='Initial TES energy - fraction of max', type='NUMBER', group='tes', required='*')
    SfPar: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    SfParPF: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    ChtfPar: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    ChtfParPF: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    CHTFParF0: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    CHTFParF1: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    CHTFParF2: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    AntiFrPar: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    BOPPar: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    BOPParPF: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    BOPParF0: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    BOPParF1: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    BOPParF2: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    CtOpF: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*', constraints='INTEGER')
    CtPar: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    CtParPF: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    CtParF0: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    CtParF1: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    CtParF2: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    HtrPar: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    HtrParPF: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    HtrParF0: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    HtrParF1: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    HtrParF2: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    HhtfPar: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    HhtfParPF: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    HhtfParF0: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    HhtfParF1: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    HhtfParF2: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    PbFixPar: float = INPUT(label='Label', type='NUMBER', group='parasitic', required='*')
    month: Final[Array] = OUTPUT(label='Resource Month', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    hour: Final[Array] = OUTPUT(label='Resource Hour of Day', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    solazi: Final[Array] = OUTPUT(label='Resource Solar Azimuth', units='deg', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    solzen: Final[Array] = OUTPUT(label='Resource Solar Zenith', units='deg', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    beam: Final[Array] = OUTPUT(label='Resource Beam normal irradiance', units='W/m2', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    tdry: Final[Array] = OUTPUT(label='Resource Dry bulb temperature', units='C', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    twet: Final[Array] = OUTPUT(label='Resource Wet bulb temperature', units='C', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    wspd: Final[Array] = OUTPUT(label='Resource Wind Speed', units='m/s', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    pres: Final[Array] = OUTPUT(label='Resource Pressure', units='mbar', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    tou_value: Final[Array] = OUTPUT(label='Resource time-of-use value', type='ARRAY', group='tou', required='*', constraints='LENGTH=8760')
    TrackAngle: Final[Array] = OUTPUT(label='Field collector tracking angle', units='deg', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    Theta: Final[Array] = OUTPUT(label='Field collector solar incidence angle', units='deg', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    CosTheta: Final[Array] = OUTPUT(label='Field collector cosine efficiency', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    IAM: Final[Array] = OUTPUT(label='Field collector incidence angle modifier', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    RowShadow: Final[Array] = OUTPUT(label='Field collector row shadowing loss', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    EndLoss: Final[Array] = OUTPUT(label='Field collector optical end loss', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    QnipCosTh: Final[Array] = OUTPUT(label='Field collector DNI-cosine product', units='W/m2', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    Ftrack: Final[Array] = OUTPUT(label='Field collector fraction of time period tracking', type='ARRAY', group='other', required='*', constraints='LENGTH=8760')
    ColEff: Final[Array] = OUTPUT(label='Field collector thermal and optical efficiency', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    Qdni: Final[Array] = OUTPUT(label='Field thermal power total incident', units='MWt', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    Qsfnipcosth: Final[Array] = OUTPUT(label='Field thermal power incident after cosine', units='MWt', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    QsfAbs: Final[Array] = OUTPUT(label='Field thermal power absorbed', units='MWt', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    RecHl: Final[Array] = OUTPUT(label='Field thermal power receiver heat loss', units='kJ/hr-m2', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    QsfHceHL: Final[Array] = OUTPUT(label='Field thermal power receiver total loss', units='MWt', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    QsfPipeHL: Final[Array] = OUTPUT(label='Field thermal power pipe losses', units='MWt', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    Qsf: Final[Array] = OUTPUT(label='Field thermal power total produced', units='MWt', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    QsfWarmup: Final[Array] = OUTPUT(label='Field HTF energy inertial (consumed)', units='MWht', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    SfMassFlow: Final[Array] = OUTPUT(label='Field HTF mass flow rate total', units='kg/s', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    o_SfTi: Final[Array] = OUTPUT(label='Field HTF temperature cold header inlet', units='C', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    SfTo: Final[Array] = OUTPUT(label='Field HTF temperature hot header outlet', units='C', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    AveSfTemp: Final[Array] = OUTPUT(label='Field HTF temperature average', units='C', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    Qtts: Final[Array] = OUTPUT(label='TES thermal energy into storage', units='MWt', type='ARRAY', group='type_806', required='*', constraints='LENGTH=8760')
    Qfts: Final[Array] = OUTPUT(label='TES thermal energy from storage', units='MWt', type='ARRAY', group='type_806', required='*', constraints='LENGTH=8760')
    Ets: Final[Array] = OUTPUT(label='TES thermal energy available', units='MWht', type='ARRAY', group='type_806', required='*', constraints='LENGTH=8760')
    QTsHl: Final[Array] = OUTPUT(label='TES thermal losses from tank(s)', units='MWt', type='ARRAY', group='type_806', required='*', constraints='LENGTH=8760')
    Enet: Final[Array] = OUTPUT(label='Cycle electrical power output (net)', units='MWe', type='ARRAY', group='type_807', required='*', constraints='LENGTH=8760')
    Egr: Final[Array] = OUTPUT(label='Cycle electrical power output (gross)', units='MWe', type='ARRAY', group='type_807', required='*', constraints='LENGTH=8760')
    EgrSol: Final[Array] = OUTPUT(label='Cycle electrical power output (gross, solar share)', units='MWe', type='ARRAY', group='type_807', required='*', constraints='LENGTH=8760')
    EgrFos: Final[Array] = OUTPUT(label='Cycle electrical power output (gross, fossil share)', units='MWe', type='ARRAY', group='type_807', required='*', constraints='LENGTH=8760')
    Qtpb: Final[Array] = OUTPUT(label='Cycle thermal power input', units='MWt', type='ARRAY', group='type_806', required='*', constraints='LENGTH=8760')
    QTurSu: Final[Array] = OUTPUT(label='Cycle thermal startup energy', units='MWt', type='ARRAY', group='type_806', required='*', constraints='LENGTH=8760')
    QTsFull: Final[Array] = OUTPUT(label='Cycle thermal energy dumped - TES is full', units='MWt', type='ARRAY', group='type_806', required='*', constraints='LENGTH=8760')
    Qmin: Final[Array] = OUTPUT(label='Cycle thermal energy dumped - min. load requirement', units='MWt', type='ARRAY', group='type_806', required='*', constraints='LENGTH=8760')
    Qdump: Final[Array] = OUTPUT(label='Cycle thermal energy dumped - solar field', units='MWt', type='ARRAY', group='type_806', required='*', constraints='LENGTH=8760')
    Qgas: Final[Array] = OUTPUT(label='Fossil thermal power produced', units='MWt', type='ARRAY', group='type_807', required='*', constraints='LENGTH=8760')
    QhtfFpHtr: Final[Array] = OUTPUT(label='Fossil freeze protection provided', units='MWt', type='ARRAY', group='type_806', required='*', constraints='LENGTH=8760')
    EparCHTF: Final[Array] = OUTPUT(label='Parasitic power solar field HTF pump', units='MWe', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    EparHhtf: Final[Array] = OUTPUT(label='Parasitic power TES and Cycle HTF pump', units='MWe', type='ARRAY', group='type_806', required='*', constraints='LENGTH=8760')
    EparSf: Final[Array] = OUTPUT(label='Parasitic power field collector drives', units='MWe', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    EparBOP: Final[Array] = OUTPUT(label='Parasitic power generation-dependent load', units='MWe', type='ARRAY', group='type_807', required='*', constraints='LENGTH=8760')
    EparPB: Final[Array] = OUTPUT(label='Parasitic power fixed load', units='MWe', type='ARRAY', group='type_807', required='*', constraints='LENGTH=8760')
    EparHtr: Final[Array] = OUTPUT(label='Parasitic power auxiliary heater operation', units='MWe', type='ARRAY', group='type_807', required='*', constraints='LENGTH=8760')
    EparCT: Final[Array] = OUTPUT(label='Parasitic power condenser operation', units='MWe', type='ARRAY', group='type_807', required='*', constraints='LENGTH=8760')
    EparAnti: Final[Array] = OUTPUT(label='Parasitic power freeze protection pump', units='MWe', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    QhtfFreezeProt: Final[Array] = OUTPUT(label='Parasitic thermal field freeze protection', units='MWt', type='ARRAY', group='type_805', required='*', constraints='LENGTH=8760')
    QhtfFpTES: Final[Array] = OUTPUT(label='Parasitic thermal TES freeze protection', units='MWt', type='ARRAY', group='type_806', required='*', constraints='LENGTH=8760')
    EparOffLine: Final[Array] = OUTPUT(label='Parasitic power - offline total', units='MWe', type='ARRAY', group='type_807', required='*', constraints='LENGTH=8760')
    EparOnLine: Final[Array] = OUTPUT(label='Parasitic power - online total', units='MWe', type='ARRAY', group='type_807', required='*', constraints='LENGTH=8760')
    Epar: Final[Array] = OUTPUT(label='Parasitic power total consumption', units='MWe', type='ARRAY', group='type_807', required='*', constraints='LENGTH=8760')
    system_use_lifetime_output: Final[float] = OUTPUT(label='Use lifetime output', units='0/1', type='NUMBER', group='tcs_trough_empirical', required='*', constraints='INTEGER')
    annual_energy: Final[float] = OUTPUT(label='Annual energy', units='kWh', type='NUMBER', group='tcs_trough_empirical', required='*')
    annual_W_cycle_gross: Final[float] = OUTPUT(label='Electrical source - Power cycle gross output', units='kWh', type='NUMBER', group='tcs_trough_empirical', required='*')
    conversion_factor: Final[float] = OUTPUT(label='Gross to Net Conversion Factor', units='%', type='NUMBER', group='Calculated', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', required='*')
    kwh_per_kw: Final[float] = OUTPUT(label='First year kWh/kW', units='kWh/kW', type='NUMBER', required='*')
    system_heat_rate: Final[float] = OUTPUT(label='System heat rate', units='MMBtu/MWh', type='NUMBER', required='*')
    annual_fuel_usage: Final[float] = OUTPUT(label='Annual fuel usage', units='kWh', type='NUMBER', required='*')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    gen: Final[Array] = OUTPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 file_name: str = ...,
                 track_mode: float = ...,
                 tilt: float = ...,
                 azimuth: float = ...,
                 system_capacity: float = ...,
                 weekday_schedule: Matrix = ...,
                 weekend_schedule: Matrix = ...,
                 i_SfTi: float = ...,
                 SfPipeHl300: float = ...,
                 SfPipeHl1: float = ...,
                 SfPipeHl2: float = ...,
                 SfPipeHl3: float = ...,
                 Stow_Angle: float = ...,
                 DepAngle: float = ...,
                 Distance_SCA: float = ...,
                 Row_Distance: float = ...,
                 NumScas: float = ...,
                 Solar_Field_Area: float = ...,
                 Solar_Field_Mult: float = ...,
                 SfInTempD: float = ...,
                 SfOutTempD: float = ...,
                 MinHtfTemp: float = ...,
                 HtfGalArea: float = ...,
                 SFTempInit: float = ...,
                 HTFFluid: float = ...,
                 IamF0: float = ...,
                 IamF1: float = ...,
                 IamF2: float = ...,
                 Ave_Focal_Length: float = ...,
                 ScaLen: float = ...,
                 SCA_aper: float = ...,
                 SfAvail: float = ...,
                 TrkTwstErr: float = ...,
                 GeoAcc: float = ...,
                 MirRef: float = ...,
                 MirCln: float = ...,
                 ConcFac: float = ...,
                 NumHCETypes: float = ...,
                 HCEtype: Array = ...,
                 HCEFrac: Array = ...,
                 HCEdust: Array = ...,
                 HCEBelShad: Array = ...,
                 HCEEnvTrans: Array = ...,
                 HCEabs: Array = ...,
                 HCEmisc: Array = ...,
                 PerfFac: Array = ...,
                 RefMirrAper: Array = ...,
                 HCE_A0: Array = ...,
                 HCE_A1: Array = ...,
                 HCE_A2: Array = ...,
                 HCE_A3: Array = ...,
                 HCE_A4: Array = ...,
                 HCE_A5: Array = ...,
                 HCE_A6: Array = ...,
                 TurbOutG: float = ...,
                 TurbEffG: float = ...,
                 PTTMAX: float = ...,
                 PTTMIN: float = ...,
                 MaxGrOut: float = ...,
                 MinGrOut: float = ...,
                 TurSUE: float = ...,
                 T2EPLF0: float = ...,
                 T2EPLF1: float = ...,
                 T2EPLF2: float = ...,
                 T2EPLF3: float = ...,
                 T2EPLF4: float = ...,
                 E2TPLF0: float = ...,
                 E2TPLF1: float = ...,
                 E2TPLF2: float = ...,
                 E2TPLF3: float = ...,
                 E2TPLF4: float = ...,
                 TempCorrF: float = ...,
                 TempCorr0: float = ...,
                 TempCorr1: float = ...,
                 TempCorr2: float = ...,
                 TempCorr3: float = ...,
                 TempCorr4: float = ...,
                 LHVBoilEff: float = ...,
                 TurTesEffAdj: float = ...,
                 TurTesOutAdj: float = ...,
                 TnkHL: float = ...,
                 PTSmax: float = ...,
                 PFSmax: float = ...,
                 TSHOURS: float = ...,
                 NUMTOU: float = ...,
                 TSLogic: Matrix = ...,
                 FossilFill: Array = ...,
                 E_tes_ini: float = ...,
                 SfPar: float = ...,
                 SfParPF: float = ...,
                 ChtfPar: float = ...,
                 ChtfParPF: float = ...,
                 CHTFParF0: float = ...,
                 CHTFParF1: float = ...,
                 CHTFParF2: float = ...,
                 AntiFrPar: float = ...,
                 BOPPar: float = ...,
                 BOPParPF: float = ...,
                 BOPParF0: float = ...,
                 BOPParF1: float = ...,
                 BOPParF2: float = ...,
                 CtOpF: float = ...,
                 CtPar: float = ...,
                 CtParPF: float = ...,
                 CtParF0: float = ...,
                 CtParF1: float = ...,
                 CtParF2: float = ...,
                 HtrPar: float = ...,
                 HtrParPF: float = ...,
                 HtrParF0: float = ...,
                 HtrParF1: float = ...,
                 HtrParF2: float = ...,
                 HhtfPar: float = ...,
                 HhtfParPF: float = ...,
                 HhtfParF0: float = ...,
                 HhtfParF1: float = ...,
                 HhtfParF2: float = ...,
                 PbFixPar: float = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
