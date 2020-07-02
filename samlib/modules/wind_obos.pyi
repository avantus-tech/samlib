
# This is a generated file

"""wind_obos - Wind Offshore Balance of System cost model"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'turbCapEx': float,
        'nTurb': float,
        'turbR': float,
        'rotorD': float,
        'hubH': float,
        'waterD': float,
        'distShore': float,
        'distPort': float,
        'distPtoA': float,
        'distAtoS': float,
        'substructure': float,
        'anchor': float,
        'turbInstallMethod': float,
        'towerInstallMethod': float,
        'installStrategy': float,
        'cableOptimizer': float,
        'moorLines': float,
        'buryDepth': float,
        'arrayY': float,
        'arrayX': float,
        'substructCont': float,
        'turbCont': float,
        'elecCont': float,
        'interConVolt': float,
        'distInterCon': float,
        'scrapVal': float,
        'projLife': float,
        'inspectClear': float,
        'plantComm': float,
        'procurement_contingency': float,
        'install_contingency': float,
        'construction_insurance': float,
        'capital_cost_year_0': float,
        'capital_cost_year_1': float,
        'capital_cost_year_2': float,
        'capital_cost_year_3': float,
        'capital_cost_year_4': float,
        'capital_cost_year_5': float,
        'tax_rate': float,
        'interest_during_construction': float,
        'mpileCR': float,
        'mtransCR': float,
        'mpileD': float,
        'mpileL': float,
        'mpEmbedL': float,
        'jlatticeCR': float,
        'jtransCR': float,
        'jpileCR': float,
        'jlatticeA': float,
        'jpileL': float,
        'jpileD': float,
        'spStifColCR': float,
        'spTapColCR': float,
        'ballCR': float,
        'deaFixLeng': float,
        'ssStifColCR': float,
        'ssTrussCR': float,
        'ssHeaveCR': float,
        'sSteelCR': float,
        'moorDia': float,
        'moorCR': float,
        'scourMat': float,
        'number_install_seasons': float,
        'pwrFac': float,
        'buryFac': float,
        'catLengFac': float,
        'exCabFac': float,
        'subsTopFab': float,
        'subsTopDes': float,
        'topAssemblyFac': float,
        'subsJackCR': float,
        'subsPileCR': float,
        'dynCabFac': float,
        'shuntCR': float,
        'highVoltSG': float,
        'medVoltSG': float,
        'backUpGen': float,
        'workSpace': float,
        'otherAncillary': float,
        'mptCR': float,
        'arrVoltage': float,
        'cab1CR': float,
        'cab2CR': float,
        'cab1CurrRating': float,
        'cab2CurrRating': float,
        'arrCab1Mass': float,
        'arrCab2Mass': float,
        'cab1TurbInterCR': float,
        'cab2TurbInterCR': float,
        'cab2SubsInterCR': float,
        'expVoltage': float,
        'expCurrRating': float,
        'expCabMass': float,
        'expCabCR': float,
        'expSubsInterCR': float,
        'arrayCables': str,
        'exportCables': str,
        'moorTimeFac': float,
        'moorLoadout': float,
        'moorSurvey': float,
        'prepAA': float,
        'prepSpar': float,
        'upendSpar': float,
        'prepSemi': float,
        'turbFasten': float,
        'boltTower': float,
        'boltNacelle1': float,
        'boltNacelle2': float,
        'boltNacelle3': float,
        'boltBlade1': float,
        'boltBlade2': float,
        'boltRotor': float,
        'vesselPosTurb': float,
        'vesselPosJack': float,
        'vesselPosMono': float,
        'subsVessPos': float,
        'monoFasten': float,
        'jackFasten': float,
        'prepGripperMono': float,
        'prepGripperJack': float,
        'placePiles': float,
        'prepHamMono': float,
        'prepHamJack': float,
        'removeHamMono': float,
        'removeHamJack': float,
        'placeTemplate': float,
        'placeJack': float,
        'levJack': float,
        'hamRate': float,
        'placeMP': float,
        'instScour': float,
        'placeTP': float,
        'groutTP': float,
        'tpCover': float,
        'prepTow': float,
        'spMoorCon': float,
        'ssMoorCon': float,
        'spMoorCheck': float,
        'ssMoorCheck': float,
        'ssBall': float,
        'surfLayRate': float,
        'cabPullIn': float,
        'cabTerm': float,
        'cabLoadout': float,
        'buryRate': float,
        'subsPullIn': float,
        'shorePullIn': float,
        'landConstruct': float,
        'expCabLoad': float,
        'subsLoad': float,
        'placeTop': float,
        'pileSpreadDR': float,
        'pileSpreadMob': float,
        'groutSpreadDR': float,
        'groutSpreadMob': float,
        'seaSpreadDR': float,
        'seaSpreadMob': float,
        'compRacks': float,
        'cabSurveyCR': float,
        'cabDrillDist': float,
        'cabDrillCR': float,
        'mpvRentalDR': float,
        'diveTeamDR': float,
        'winchDR': float,
        'civilWork': float,
        'elecWork': float,
        'nCrane600': float,
        'nCrane1000': float,
        'crane600DR': float,
        'crane1000DR': float,
        'craneMobDemob': float,
        'entranceExitRate': float,
        'dockRate': float,
        'wharfRate': float,
        'laydownCR': float,
        'estEnMFac': float,
        'preFEEDStudy': float,
        'feedStudy': float,
        'stateLease': float,
        'outConShelfLease': float,
        'saPlan': float,
        'conOpPlan': float,
        'nepaEisMet': float,
        'physResStudyMet': float,
        'bioResStudyMet': float,
        'socEconStudyMet': float,
        'navStudyMet': float,
        'nepaEisProj': float,
        'physResStudyProj': float,
        'bioResStudyProj': float,
        'socEconStudyProj': float,
        'navStudyProj': float,
        'coastZoneManAct': float,
        'rivsnHarbsAct': float,
        'cleanWatAct402': float,
        'cleanWatAct404': float,
        'faaPlan': float,
        'endSpecAct': float,
        'marMamProtAct': float,
        'migBirdAct': float,
        'natHisPresAct': float,
        'addLocPerm': float,
        'metTowCR': float,
        'decomDiscRate': float,
        'hubD': float,
        'bladeL': float,
        'chord': float,
        'nacelleW': float,
        'nacelleL': float,
        'rnaM': float,
        'towerD': float,
        'towerM': float,
        'subTotM': float,
        'subTotCost': float,
        'moorCost': float,
        'systAngle': float,
        'freeCabLeng': float,
        'fixCabLeng': float,
        'nExpCab': float,
        'cab1Leng': float,
        'cab2Leng': float,
        'expCabLeng': float,
        'subsTopM': float,
        'arrCab1Cost': float,
        'arrCab2Cost': float,
        'expCabCost': float,
        'subsSubM': float,
        'subsPileM': float,
        'totElecCost': float,
        'moorTime': float,
        'floatPrepTime': float,
        'turbDeckArea': float,
        'nTurbPerTrip': float,
        'turbInstTime': float,
        'subDeckArea': float,
        'nSubPerTrip': float,
        'subInstTime': float,
        'arrInstTime': float,
        'expInstTime': float,
        'subsInstTime': float,
        'totInstTime': float,
        'totAnICost': float,
        'cabSurvey': float,
        'turbine_install_cost': float,
        'substructure_install_cost': float,
        'electrical_install_cost': float,
        'mob_demob_cost': float,
        'array_cable_install_cost': float,
        'export_cable_install_cost': float,
        'substation_install_cost': float,
        'totPnSCost': float,
        'totEnMCost': float,
        'totDevCost': float,
        'commissioning': float,
        'decomCost': float,
        'bos_capex': float,
        'soft_costs': float,
        'total_contingency_cost': float,
        'construction_insurance_cost': float,
        'construction_finance_cost': float,
        'construction_finance_factor': float,
        'total_bos_cost': float
}, total=False)

class Data(ssc.DataDict):
    turbCapEx: float = INPUT(label='Turbine Capital Cost', units='$/kW', type='NUMBER', group='wobos', required='?=1605')
    nTurb: float = INPUT(label='Number of Turbines', type='NUMBER', group='wobos', required='?=20', constraints='MIN=2,MAX=200')
    turbR: float = INPUT(label='Turbine Rating', units='MW', type='NUMBER', group='wobos', required='?=5', constraints='MIN=1,MAX=15')
    rotorD: float = INPUT(label='Rotor Diameter', units='m', type='NUMBER', group='wobos', required='?=120')
    hubH: float = INPUT(label='Hub Height', units='m', type='NUMBER', group='wobos', required='?=90')
    waterD: float = INPUT(label='Max Water Depth', units='m', type='NUMBER', group='wobos', required='?=30', constraints='MIN=3,MAX=1000')
    distShore: float = INPUT(label='Distance to Landfall', units='km', type='NUMBER', group='wobos', required='?=90', constraints='MIN=5,MAX=1000')
    distPort: float = INPUT(label='Distance from Installation Port to Site', units='km', type='NUMBER', group='wobos', required='?=90', constraints='MIN=5,MAX=1000')
    distPtoA: float = INPUT(label='Distance from Installation Port to Inshore Assembly Area', units='km', type='NUMBER', group='wobos', required='?=90', constraints='MIN=5,MAX=1000')
    distAtoS: float = INPUT(label='Distance form Inshore Assembly Area to Site', units='km', type='NUMBER', group='wobos', required='?=90', constraints='MIN=5,MAX=1000')
    substructure: float = INPUT(label='Substructure Type', type='NUMBER', group='wobos', required='?=MONOPILE', constraints='INTEGER')
    anchor: float = INPUT(label='Anchor Type', type='NUMBER', group='wobos', required='?=DRAGEMBEDMENT', constraints='INTEGER')
    turbInstallMethod: float = INPUT(label='Turbine Installation Method', type='NUMBER', group='wobos', required='?=INDIVIDUAL', constraints='INTEGER')
    towerInstallMethod: float = INPUT(label='Tower Installation Method', type='NUMBER', group='wobos', required='?=ONEPIECE', constraints='INTEGER')
    installStrategy: float = INPUT(label='Installation Vessel Strategy', type='NUMBER', group='wobos', required='?=PRIMARYVESSEL', constraints='INTEGER')
    cableOptimizer: float = INPUT(label='Electrical Cable Cost Optimization', type='NUMBER', group='wobos', required='?=FALSE', constraints='INTEGER')
    moorLines: float = INPUT(label='Number Of Mooring Lines', type='NUMBER', group='wobos', required='?=3')
    buryDepth: float = INPUT(label='Electrical Cable Burial Depth', units='m', type='NUMBER', group='wobos', required='?=2', constraints='MIN=0,MAX=15')
    arrayY: float = INPUT(label='Spacing Between Turbines in Rows', units='rotor diameters', type='NUMBER', group='wobos', required='?=9', constraints='MIN=1')
    arrayX: float = INPUT(label='Spacing Between Turbine Rows', units='rotor diameters', type='NUMBER', group='wobos', required='?=9', constraints='MIN=1')
    substructCont: float = INPUT(label='Substructure Install Weather Contingency', units='%', type='NUMBER', group='wobos', required='?=0.3')
    turbCont: float = INPUT(label='Turbine Install Weather Contingency', units='%', type='NUMBER', group='wobos', required='?=0.3')
    elecCont: float = INPUT(label='Electrical Install Weather Contingency', units='%', type='NUMBER', group='wobos', required='?=0.3')
    interConVolt: float = INPUT(label='Grid Interconnect Voltage', units='kV', type='NUMBER', group='wobos', required='?=345')
    distInterCon: float = INPUT(label='Distance Over Land to Grid Interconnect', units='miles', type='NUMBER', group='wobos', required='?=3')
    scrapVal: float = INPUT(label='Total Scrap Value of Decommissioned Components', units='$', type='NUMBER', group='wobos', required='?=0')
    projLife: float = INPUT(label='Project Economic Life', units='years', type='NUMBER', group='wobos', required='?=20')
    inspectClear: float = INPUT(label='Inspection Clearance', units='m', type='NUMBER', group='wobos', required='?=2')
    plantComm: float = INPUT(label='Plant Commissioning Cost Factor', type='NUMBER', group='wobos', required='?=0.01')
    procurement_contingency: float = INPUT(label='Procurement Contingency', type='NUMBER', group='wobos', required='?=0.05')
    install_contingency: float = INPUT(label='Installation Contingency', type='NUMBER', group='wobos', required='?=0.3')
    construction_insurance: float = INPUT(label='Insurance During Construction (% of ICC)', type='NUMBER', group='wobos', required='?=0.01')
    capital_cost_year_0: float = INPUT(label='Capital cost spent in year 0', type='NUMBER', group='wobos', required='?=0.2')
    capital_cost_year_1: float = INPUT(label='Capital cost spent in year 1', type='NUMBER', group='wobos', required='?=0.6')
    capital_cost_year_2: float = INPUT(label='Capital cost spent in year 2', type='NUMBER', group='wobos', required='?=0.1')
    capital_cost_year_3: float = INPUT(label='Capital cost spent in year 3', type='NUMBER', group='wobos', required='?=0.1')
    capital_cost_year_4: float = INPUT(label='Capital cost spent in year 4', type='NUMBER', group='wobos', required='?=0')
    capital_cost_year_5: float = INPUT(label='Capital cost spent in year 5', type='NUMBER', group='wobos', required='?=0')
    tax_rate: float = INPUT(label='Effective Tax Rate', type='NUMBER', group='wobos', required='?=0.4')
    interest_during_construction: float = INPUT(label='Interest During Construction', type='NUMBER', group='wobos', required='?=0.08')
    mpileCR: float = INPUT(label='Monopile Cost Rate', units='$/tonne', type='NUMBER', group='wobos', required='?=2250')
    mtransCR: float = INPUT(label='Monopile Transition Piece Cost Rate', units='$/tonne', type='NUMBER', group='wobos', required='?=3230')
    mpileD: float = INPUT(label='Monopile Diameter', units='m', type='NUMBER', group='wobos', required='?=0', constraints='MIN=0.01')
    mpileL: float = INPUT(label='Monopile Length', units='m', type='NUMBER', group='wobos', required='?=0', constraints='MIN=0.01')
    mpEmbedL: float = INPUT(label='Monopile Embedment Length', units='m', type='NUMBER', group='wobos', required='?=30')
    jlatticeCR: float = INPUT(label='Jacket Main Lattice Cost Rate', units='$/tonne', type='NUMBER', group='wobos', required='?=4680')
    jtransCR: float = INPUT(label='Jacket Transition Piece Cost Rate', units='$/tonne', type='NUMBER', group='wobos', required='?=4500')
    jpileCR: float = INPUT(label='Jacket Pile Cost Rate', units='$/tonne', type='NUMBER', group='wobos', required='?=2250')
    jlatticeA: float = INPUT(label='Jacket Main Lattice Footprint Area', units='m^2', type='NUMBER', group='wobos', required='?=26')
    jpileL: float = INPUT(label='Jacket Pile Length', units='m', type='NUMBER', group='wobos', required='?=47.5')
    jpileD: float = INPUT(label='Jacket Pile Diameter', units='m', type='NUMBER', group='wobos', required='?=1.6')
    spStifColCR: float = INPUT(label='Spar Stiffened Column Cost Rate', units='$/tonne', type='NUMBER', group='wobos', required='?=3120')
    spTapColCR: float = INPUT(label='Spar Tapered Column Cost Rate', units='$/tonne', type='NUMBER', group='wobos', required='?=4220')
    ballCR: float = INPUT(label='Floating Ballast Cost Rate', units='$/tonne', type='NUMBER', group='wobos', required='?=100')
    deaFixLeng: float = INPUT(label='Fixed Mooring Length for Drag Embedment Anchors', units='m', type='NUMBER', group='wobos', required='?=500')
    ssStifColCR: float = INPUT(label='Semi-submersible Stiffened Column Cost Rate', units='$/tonne', type='NUMBER', group='wobos', required='?=3120')
    ssTrussCR: float = INPUT(label='Semi-submersible Truss Cost Rate', units='$/tonne', type='NUMBER', group='wobos', required='?=6250')
    ssHeaveCR: float = INPUT(label='Semi-submersible Heave Plate Cost Rate', units='$/tonne', type='NUMBER', group='wobos', required='?=6250')
    sSteelCR: float = INPUT(label='Secondary/Outfitting Steel Cost Rate', units='$/tonne', type='NUMBER', group='wobos', required='?=7250')
    moorDia: float = INPUT(label='Mooring Line Diameter', units='m', type='NUMBER', group='wobos', required='?=0', constraints='MIN=0.09')
    moorCR: float = INPUT(label='Mooring Line Cost Rate', units='$/m', type='NUMBER', group='wobos', required='?=0', constraints='MIN=399')
    scourMat: float = INPUT(label='Scour Protection Material Cost', units='$/location', type='NUMBER', group='wobos', required='?=250000')
    number_install_seasons: float = INPUT(label='Number of Installation Seasons', type='NUMBER', group='wobos', required='?=1')
    pwrFac: float = INPUT(label='Power Transfer Efficiency Factor', type='NUMBER', group='wobos', required='?=0.95')
    buryFac: float = INPUT(label='Cable Burial Depth Factor', units='1/m', type='NUMBER', group='wobos', required='?=0.1')
    catLengFac: float = INPUT(label='Catenary Cable Length Factor', type='NUMBER', group='wobos', required='?=0.04')
    exCabFac: float = INPUT(label='Excess Cable Factor', type='NUMBER', group='wobos', required='?=0.1')
    subsTopFab: float = INPUT(label='Offshore Substation Fabrication Cost', units='$/tonne', type='NUMBER', group='wobos', required='?=14500')
    subsTopDes: float = INPUT(label='Offshore Substation Design Cost', units='$', type='NUMBER', group='wobos', required='?=4500000')
    topAssemblyFac: float = INPUT(label='Offshore Substation Land-based Assembly Factor', type='NUMBER', group='wobos', required='?=0.075')
    subsJackCR: float = INPUT(label='Offshore Substation Jacket Lattice Cost Rate', units='$/tonne', type='NUMBER', group='wobos', required='?=6250')
    subsPileCR: float = INPUT(label='Offshore Substation Jacket Pile Cost Rate', units='$/tonne', type='NUMBER', group='wobos', required='?=2250')
    dynCabFac: float = INPUT(label='Dynamic Cable Cost Premium Factor', type='NUMBER', group='wobos', required='?=2')
    shuntCR: float = INPUT(label='Shunt Reactor Cost Rate', units='$/MVA', type='NUMBER', group='wobos', required='?=35000')
    highVoltSG: float = INPUT(label='High Voltage Switchgear Cost', units='$', type='NUMBER', group='wobos', required='?=950000')
    medVoltSG: float = INPUT(label='Medium Voltage Switchgear Cost', units='$', type='NUMBER', group='wobos', required='?=500000')
    backUpGen: float = INPUT(label='Back up Diesel Generator Cost', units='$', type='NUMBER', group='wobos', required='?=1000000')
    workSpace: float = INPUT(label='Offshore Substation Workspace & Accommodations Cost', units='$', type='NUMBER', group='wobos', required='?=2000000')
    otherAncillary: float = INPUT(label='Other Ancillary Systems Costs', units='$', type='NUMBER', group='wobos', required='?=3000000')
    mptCR: float = INPUT(label='Main Power Transformer Cost Rate', units='$/MVA', type='NUMBER', group='wobos', required='?=12500')
    arrVoltage: float = INPUT(label='Array cable voltage', units='kV', type='NUMBER', group='wobos', required='?=33')
    cab1CR: float = INPUT(label='Array cable 1 Cost Rate', units='$/m', type='NUMBER', group='wobos', required='?=185.889')
    cab2CR: float = INPUT(label='Array cable 2 Cost Rate', units='$/m', type='NUMBER', group='wobos', required='?=202.788')
    cab1CurrRating: float = INPUT(label='Array cable 1 current rating', units='A', type='NUMBER', group='wobos', required='?=300')
    cab2CurrRating: float = INPUT(label='Array cable 2 current rating', units='A', type='NUMBER', group='wobos', required='?=340')
    arrCab1Mass: float = INPUT(label='Array cable 1 mass', units='kg/m', type='NUMBER', group='wobos', required='?=20.384')
    arrCab2Mass: float = INPUT(label='Array cable 2 mass', units='kg/m', type='NUMBER', group='wobos', required='?=21.854')
    cab1TurbInterCR: float = INPUT(label='Cable 1 turbine interface cost', units='$/interface', type='NUMBER', group='wobos', required='?=8410')
    cab2TurbInterCR: float = INPUT(label='Cable 2 turbine interface cost', units='$/interface', type='NUMBER', group='wobos', required='?=8615')
    cab2SubsInterCR: float = INPUT(label='Cable 2 substation interface cost', units='$/interface', type='NUMBER', group='wobos', required='?=19815')
    expVoltage: float = INPUT(label='Export cable voltage', units='kV', type='NUMBER', group='wobos', required='?=220')
    expCurrRating: float = INPUT(label='Export cable current rating', units='A', type='NUMBER', group='wobos', required='?=530')
    expCabMass: float = INPUT(label='Export cable mass', units='kg/m', type='NUMBER', group='wobos', required='?=71.9')
    expCabCR: float = INPUT(label='Export cable cost rate', units='$/m', type='NUMBER', group='wobos', required='?=495.411')
    expSubsInterCR: float = INPUT(label='Export cable substation interface cost', units='$/interface', type='NUMBER', group='wobos', required='?=57500')
    arrayCables: str = INPUT(label='Inter-array cables to consider by voltage', units='kV', type='STRING', group='wobos', required='?=33 66')
    exportCables: str = INPUT(label='Export cables to consider by voltage', units='kV', type='STRING', group='wobos', required='?=132 220')
    moorTimeFac: float = INPUT(label='Anchor & Mooring Water Depth Time Factor', type='NUMBER', group='wobos', required='?=0.005')
    moorLoadout: float = INPUT(label='Anchor & Mooring Loadout Time', units='hours', type='NUMBER', group='wobos', required='?=5')
    moorSurvey: float = INPUT(label='Survey Mooring Lines & Anchor Positions Time', units='hours', type='NUMBER', group='wobos', required='?=4')
    prepAA: float = INPUT(label='Prepare Inshore Assembly Area For Turbine Installation', units='hours', type='NUMBER', group='wobos', required='?=168')
    prepSpar: float = INPUT(label='Prepare Spar for Tow to Inshore Assembly Area', units='hours', type='NUMBER', group='wobos', required='?=18')
    upendSpar: float = INPUT(label='Upend and Ballast Spar', units='hours', type='NUMBER', group='wobos', required='?=36')
    prepSemi: float = INPUT(label='Prepare Semi-submersible for Turbine Installation', units='hours', type='NUMBER', group='wobos', required='?=12')
    turbFasten: float = INPUT(label='Prepare and Fasten Turbine for Transport', units='hours/turbine', type='NUMBER', group='wobos', required='?=8')
    boltTower: float = INPUT(label='Lift and Bolt Tower Section', units='hours', type='NUMBER', group='wobos', required='?=7')
    boltNacelle1: float = INPUT(label='Lift and Bolt Nacelle Individual Components Method', units='hours', type='NUMBER', group='wobos', required='?=7')
    boltNacelle2: float = INPUT(label='Lift and Bolt Nacelle Bunny Ears Method', units='hours', type='NUMBER', group='wobos', required='?=7')
    boltNacelle3: float = INPUT(label='Lift and Bolt Nacelle Fully Assembled Rotor Method', units='hours', type='NUMBER', group='wobos', required='?=7')
    boltBlade1: float = INPUT(label='Lift and Bolt Blade Individual Components Method', units='hours', type='NUMBER', group='wobos', required='?=3.5')
    boltBlade2: float = INPUT(label='Lift and Bolt Blade Bunny Ears Method', units='hours', type='NUMBER', group='wobos', required='?=3.5')
    boltRotor: float = INPUT(label='Lift and Bolt Rotor Fully Assembled Rotor Method', units='hours', type='NUMBER', group='wobos', required='?=7')
    vesselPosTurb: float = INPUT(label='Vessel Positioning Time Turbine Installation', units='hours', type='NUMBER', group='wobos', required='?=2')
    vesselPosJack: float = INPUT(label='Vessel Positioning Time Jacket Installation', units='hours', type='NUMBER', group='wobos', required='?=8')
    vesselPosMono: float = INPUT(label='Vessel Positioning Time Monopile Installation', units='hours', type='NUMBER', group='wobos', required='?=3')
    subsVessPos: float = INPUT(label='Vessel Positioning Time Offshore Substation Installation', units='hours', type='NUMBER', group='wobos', required='?=6')
    monoFasten: float = INPUT(label='Prepare and Fasten Monopile for Transport', units='hours/unit', type='NUMBER', group='wobos', required='?=12')
    jackFasten: float = INPUT(label='Prepare and Fasten Jacket for Transport', units='hours/unit', type='NUMBER', group='wobos', required='?=20')
    prepGripperMono: float = INPUT(label='Prepare Monopile Gripper and Upender', units='hours', type='NUMBER', group='wobos', required='?=1.5')
    prepGripperJack: float = INPUT(label='Prepare Jacket Gripper and Upender', units='hours', type='NUMBER', group='wobos', required='?=8')
    placePiles: float = INPUT(label='Place Jacket Piles', units='hours', type='NUMBER', group='wobos', required='?=12')
    prepHamMono: float = INPUT(label='Prepare Hammer for Monopile Installation', units='hours', type='NUMBER', group='wobos', required='?=2')
    prepHamJack: float = INPUT(label='Prepare Hammer for jacket Piles Installation', units='hours', type='NUMBER', group='wobos', required='?=2')
    removeHamMono: float = INPUT(label='Remove Hammer for Monopile Installation', units='hours', type='NUMBER', group='wobos', required='?=2')
    removeHamJack: float = INPUT(label='Remove Hammer for Jacket Piles Installation', units='hours', type='NUMBER', group='wobos', required='?=4')
    placeTemplate: float = INPUT(label='Place Jacket Pile Template on Seabed', units='hours', type='NUMBER', group='wobos', required='?=4')
    placeJack: float = INPUT(label='Place Jacket Main Lattice onto Piles', units='hours', type='NUMBER', group='wobos', required='?=12')
    levJack: float = INPUT(label='Level Jacket Main Lattice', units='hours', type='NUMBER', group='wobos', required='?=24')
    hamRate: float = INPUT(label='Pile Hammer Rate', units='m/hour', type='NUMBER', group='wobos', required='?=20')
    placeMP: float = INPUT(label='Lift and Place Monopile for Hammering', units='hours', type='NUMBER', group='wobos', required='?=3')
    instScour: float = INPUT(label='Install Scour Protection Around Monopile Base', units='hours', type='NUMBER', group='wobos', required='?=6')
    placeTP: float = INPUT(label='Place Transition Piece onto Monopile', units='hours', type='NUMBER', group='wobos', required='?=3')
    groutTP: float = INPUT(label='Grout Transition Piece/Monopile Interface', units='hours', type='NUMBER', group='wobos', required='?=8')
    tpCover: float = INPUT(label='Install Transition Piece Cover', units='hours', type='NUMBER', group='wobos', required='?=1.5')
    prepTow: float = INPUT(label='Prepare Floating Substructure for Tow to Site', units='hours', type='NUMBER', group='wobos', required='?=12')
    spMoorCon: float = INPUT(label='Connect Mooring Lines to Spar', units='hours', type='NUMBER', group='wobos', required='?=20')
    ssMoorCon: float = INPUT(label='Connect Mooring Lines to Semi-Submersible', units='hours', type='NUMBER', group='wobos', required='?=22')
    spMoorCheck: float = INPUT(label='Survey Spar Mooring Lines and Connections', units='hours', type='NUMBER', group='wobos', required='?=16')
    ssMoorCheck: float = INPUT(label='Survey Semi-submersible Mooing Lines and Connections', units='hours', type='NUMBER', group='wobos', required='?=12')
    ssBall: float = INPUT(label='Ballast Semi-submersible', units='hours', type='NUMBER', group='wobos', required='?=6')
    surfLayRate: float = INPUT(label='Cable Surface Lay Rate', units='m/hour', type='NUMBER', group='wobos', required='?=375')
    cabPullIn: float = INPUT(label='Array Cable Pull in to Interfaces', units='hours', type='NUMBER', group='wobos', required='?=5.5')
    cabTerm: float = INPUT(label='Cable Termination and Testing', units='hours', type='NUMBER', group='wobos', required='?=5.5')
    cabLoadout: float = INPUT(label='Array Cable Loadout for Installation', units='hours', type='NUMBER', group='wobos', required='?=14')
    buryRate: float = INPUT(label='Cable Burial Rate', units='m/hour', type='NUMBER', group='wobos', required='?=125')
    subsPullIn: float = INPUT(label='Cable Pull in to Offshore Substation', units='hours', type='NUMBER', group='wobos', required='?=48')
    shorePullIn: float = INPUT(label='Cable Pull in to Onshore Infrastructure', units='hours', type='NUMBER', group='wobos', required='?=96')
    landConstruct: float = INPUT(label='Onshore Infrastructure Construction', units='days', type='NUMBER', group='wobos', required='?=7')
    expCabLoad: float = INPUT(label='Export Cable Loadout for Installation', units='hours', type='NUMBER', group='wobos', required='?=24')
    subsLoad: float = INPUT(label='Offshore Substation Loadout for Installation', units='hours', type='NUMBER', group='wobos', required='?=60')
    placeTop: float = INPUT(label='Lift and Place Offshore Substation Topside', units='hours', type='NUMBER', group='wobos', required='?=24')
    pileSpreadDR: float = INPUT(label='Piling Spread Day Rate', units='$/day', type='NUMBER', group='wobos', required='?=2500')
    pileSpreadMob: float = INPUT(label='Piling Spread Mobilization Cost', units='$', type='NUMBER', group='wobos', required='?=750000')
    groutSpreadDR: float = INPUT(label='Grouting Spread Day Rate', units='$/day', type='NUMBER', group='wobos', required='?=3000')
    groutSpreadMob: float = INPUT(label='Grouting Spread Mobilization Cost', units='$', type='NUMBER', group='wobos', required='?=1000000')
    seaSpreadDR: float = INPUT(label='Suction Pile Anchor Spread Day Rate', units='$/day', type='NUMBER', group='wobos', required='?=165000')
    seaSpreadMob: float = INPUT(label='Suction Pile Anchor Spread Mobilization Cost', units='$', type='NUMBER', group='wobos', required='?=4500000')
    compRacks: float = INPUT(label='Component Racks Cost', units='$', type='NUMBER', group='wobos', required='?=1000000')
    cabSurveyCR: float = INPUT(label='Cable Route Survey Cost', units='$/m', type='NUMBER', group='wobos', required='?=240')
    cabDrillDist: float = INPUT(label='Horizontal Drilling distance for Cable Landfall', units='m', type='NUMBER', group='wobos', required='?=500')
    cabDrillCR: float = INPUT(label='Cost Rate for Horizontal Drilling', units='$/m', type='NUMBER', group='wobos', required='?=3200')
    mpvRentalDR: float = INPUT(label='MPV Rental Day Rate', units='$/day', type='NUMBER', group='wobos', required='?=72000')
    diveTeamDR: float = INPUT(label='Cable Landfall Dive Team Day Rate', units='$/day', type='NUMBER', group='wobos', required='?=3200')
    winchDR: float = INPUT(label='Cable Landfall Winch Day Rate', units='$/day', type='NUMBER', group='wobos', required='?=1000')
    civilWork: float = INPUT(label='Onshore Infrastructure Civil Work Cost', units='$', type='NUMBER', group='wobos', required='?=40000')
    elecWork: float = INPUT(label='Onshore Infrastructure Electrical Work Cost', units='$', type='NUMBER', group='wobos', required='?=25000')
    nCrane600: float = INPUT(label='Number of 600 t Crawler Cranes', type='NUMBER', group='wobos', required='?=0')
    nCrane1000: float = INPUT(label='Number of 1000 t Crawler Cranes', type='NUMBER', group='wobos', required='?=0')
    crane600DR: float = INPUT(label='600 t Crawler Crane Day Rate', units='$/day', type='NUMBER', group='wobos', required='?=5000')
    crane1000DR: float = INPUT(label='1000 t Crawler Crane Day Rate', units='$/day', type='NUMBER', group='wobos', required='?=8000')
    craneMobDemob: float = INPUT(label='Port Crane Mobilization/Demobilization Cost', units='$', type='NUMBER', group='wobos', required='?=150000')
    entranceExitRate: float = INPUT(label='Port Entrance and Exit Cost Rate', units='$/occurrence', type='NUMBER', group='wobos', required='?=0.525')
    dockRate: float = INPUT(label='Quayside Docking Cost Rate', units='$/day', type='NUMBER', group='wobos', required='?=3000')
    wharfRate: float = INPUT(label='Wharf Loading and Unloading Cost Rate', units='$/tonne', type='NUMBER', group='wobos', required='?=2.75')
    laydownCR: float = INPUT(label='Laydown and Storage Cost Rate', units='$/m^2/day', type='NUMBER', group='wobos', required='?=0.25')
    estEnMFac: float = INPUT(label='Estimated Engineering & Management Cost Factor', type='NUMBER', group='wobos', required='?=0.04')
    preFEEDStudy: float = INPUT(label='Pre-FEED study Cost', units='$', type='NUMBER', group='wobos', required='?=5000000')
    feedStudy: float = INPUT(label='FEED Study Cost', units='$', type='NUMBER', group='wobos', required='?=10000000')
    stateLease: float = INPUT(label='State Leasing and Permitting Cost', units='$', type='NUMBER', group='wobos', required='?=250000')
    outConShelfLease: float = INPUT(label='Outer Continental Shelf Lease Cost', units='$', type='NUMBER', group='wobos', required='?=1000000')
    saPlan: float = INPUT(label='Site Assessment Plan Cost', units='$', type='NUMBER', group='wobos', required='?=500000')
    conOpPlan: float = INPUT(label='Construction Operations Plan Cost', units='$', type='NUMBER', group='wobos', required='?=1000000')
    nepaEisMet: float = INPUT(label='NEPA Environmental Impact Statement Met Tower Cost', units='$', type='NUMBER', group='wobos', required='?=2000000')
    physResStudyMet: float = INPUT(label='Physical Resource Study Met Tower Cost', units='$', type='NUMBER', group='wobos', required='?=1500000')
    bioResStudyMet: float = INPUT(label='Biological Resource Study Met Tower Cost', units='$', type='NUMBER', group='wobos', required='?=1500000')
    socEconStudyMet: float = INPUT(label='Socioeconomic and Land use Study Met Tower Cost', units='$', type='NUMBER', group='wobos', required='?=500000')
    navStudyMet: float = INPUT(label='Navigation and Transport Study Met Tower Cost', units='$', type='NUMBER', group='wobos', required='?=500000')
    nepaEisProj: float = INPUT(label='NEPA Environmental Impact Study Project Cost', units='$', type='NUMBER', group='wobos', required='?=5000000')
    physResStudyProj: float = INPUT(label='Physical Resource Study Project Cost', units='$', type='NUMBER', group='wobos', required='?=500000')
    bioResStudyProj: float = INPUT(label='Biological Resource Study Porject Cost', units='$', type='NUMBER', group='wobos', required='?=500000')
    socEconStudyProj: float = INPUT(label='Socioeconomic and Land use Study Project Cost', units='$', type='NUMBER', group='wobos', required='?=200000')
    navStudyProj: float = INPUT(label='Navigation and Transport Study Project Cost', units='$', type='NUMBER', group='wobos', required='?=250000')
    coastZoneManAct: float = INPUT(label='Coastal Zone Management Act Compliance Cost', units='$', type='NUMBER', group='wobos', required='?=100000')
    rivsnHarbsAct: float = INPUT(label='Rivers & Harbors Act Section 10 Compliance Cost', units='$', type='NUMBER', group='wobos', required='?=100000')
    cleanWatAct402: float = INPUT(label='Clean Water Act Section 402 Compliance Cost', units='$', type='NUMBER', group='wobos', required='?=100000')
    cleanWatAct404: float = INPUT(label='Clean Water Act Section 404 Compliance Cost', units='$', type='NUMBER', group='wobos', required='?=100000')
    faaPlan: float = INPUT(label='Federal Aviation Administration Plans & Mitigation Cost', units='$', type='NUMBER', group='wobos', required='?=10000')
    endSpecAct: float = INPUT(label='Endangered Species Act Compliance Cost', units='$', type='NUMBER', group='wobos', required='?=500000')
    marMamProtAct: float = INPUT(label='Marine Mammal Protection Act Compliance Cost', units='$', type='NUMBER', group='wobos', required='?=500000')
    migBirdAct: float = INPUT(label='Migratory Bird Treaty Compliance Cost', units='$', type='NUMBER', group='wobos', required='?=500000')
    natHisPresAct: float = INPUT(label='National Historic Preservation Act Compliance Cost', units='$', type='NUMBER', group='wobos', required='?=250000')
    addLocPerm: float = INPUT(label='Additional State and Local Permitting Cost', units='$', type='NUMBER', group='wobos', required='?=200000')
    metTowCR: float = INPUT(label='Meteorological (Met Tower Fabrication & Install Cost', units='$/MW', type='NUMBER', group='wobos', required='?=11518')
    decomDiscRate: float = INPUT(label='Decommissioning Cost Discount Rate', type='NUMBER', group='wobos', required='?=0.03')
    hubD: float = INPUT(label='Hub Diameter', units='m', type='NUMBER', group='wobos', required='?=0')
    bladeL: float = INPUT(label='Blade Length', units='m', type='NUMBER', group='wobos', required='?=0')
    chord: float = INPUT(label='Blade Max Chord', units='m', type='NUMBER', group='wobos', required='?=0')
    nacelleW: float = INPUT(label='Nacelle Width', units='m', type='NUMBER', group='wobos', required='?=0')
    nacelleL: float = INPUT(label='Nacelle Length', units='m', type='NUMBER', group='wobos', required='?=0')
    rnaM: float = INPUT(label='Rotor-Nacelle Assembly Mass', units='tonne', type='NUMBER', group='wobos', required='?=0')
    towerD: float = INPUT(label='Tower Base Diameter', units='m', type='NUMBER', group='wobos', required='?=0')
    towerM: float = INPUT(label='Tower Mass', units='tonne', type='NUMBER', group='wobos', required='?=0')
    subTotM: float = INPUT(label='Total Substructure Mass per Turbine', units='tonne', type='NUMBER', group='wobos', required='?=0')
    subTotCost: float = INPUT(label='Substructure & Foundation Total Cost', units='$', type='NUMBER', group='wobos', required='?=0')
    moorCost: float = INPUT(label='Capital cost of mooring lines and anchors', units='$', type='NUMBER', group='wobos', required='?=0')
    systAngle: Final[float] = OUTPUT(label='Floating System Angle', units='degrees', type='NUMBER', group='wobos')
    freeCabLeng: Final[float] = OUTPUT(label='Free Hanging Cable Length', units='m', type='NUMBER', group='wobos')
    fixCabLeng: Final[float] = OUTPUT(label='Fixed Cable Length', units='m', type='NUMBER', group='wobos')
    nExpCab: Final[float] = OUTPUT(label='Number of Export Cables', type='NUMBER', group='wobos')
    cab1Leng: Final[float] = OUTPUT(label='Array Cable #1 Length', units='m', type='NUMBER', group='wobos')
    cab2Leng: Final[float] = OUTPUT(label='Array Cabel #2 Length', units='m', type='NUMBER', group='wobos')
    expCabLeng: Final[float] = OUTPUT(label='Export Cable Length', units='m', type='NUMBER', group='wobos')
    subsTopM: Final[float] = OUTPUT(label='Substation Topside Mass', units='tonne', type='NUMBER', group='wobos')
    arrCab1Cost: Final[float] = OUTPUT(label='Array Cable #1 and Ancillary Cost', units='$', type='NUMBER', group='wobos')
    arrCab2Cost: Final[float] = OUTPUT(label='Array Cable #2 and Ancillary Cost', units='$', type='NUMBER', group='wobos')
    expCabCost: Final[float] = OUTPUT(label='Export Cable and Ancillary Cost', units='$', type='NUMBER', group='wobos')
    subsSubM: Final[float] = OUTPUT(label='Offshore Substation Substructure Mass', units='tonne', type='NUMBER', group='wobos')
    subsPileM: Final[float] = OUTPUT(label='Offshore Substation Jacket Piles Mass', units='tonne', type='NUMBER', group='wobos')
    totElecCost: Final[float] = OUTPUT(label='Total Electrical Infrastructure Cost', units='$', type='NUMBER', group='wobos')
    moorTime: Final[float] = OUTPUT(label='Mooring and Anchor System Installation Time', units='days', type='NUMBER', group='wobos')
    floatPrepTime: Final[float] = OUTPUT(label='Floating Preparation Time', units='days', type='NUMBER', group='wobos')
    turbDeckArea: Final[float] = OUTPUT(label='Deck Area Required per Turbine', units='m^2', type='NUMBER', group='wobos')
    nTurbPerTrip: Final[float] = OUTPUT(label='Maximum Number of Turbines per Vessel Trip', type='NUMBER', group='wobos')
    turbInstTime: Final[float] = OUTPUT(label='Turbine Installation Time', units='days', type='NUMBER', group='wobos')
    subDeckArea: Final[float] = OUTPUT(label='Deck Area Required per Substructure', units='m^2', type='NUMBER', group='wobos')
    nSubPerTrip: Final[float] = OUTPUT(label='Maximum Number of Substructures per Vessel Trip', type='NUMBER', group='wobos')
    subInstTime: Final[float] = OUTPUT(label='Substructure Installation Time', units='days', type='NUMBER', group='wobos')
    arrInstTime: Final[float] = OUTPUT(label='Array Cable System Installation Time', units='days', type='NUMBER', group='wobos')
    expInstTime: Final[float] = OUTPUT(label='Export Cable Installation Time', units='days', type='NUMBER', group='wobos')
    subsInstTime: Final[float] = OUTPUT(label='Offshore Substation Installation Time', units='days', type='NUMBER', group='wobos')
    totInstTime: Final[float] = OUTPUT(label='Total Installation Time', units='days', type='NUMBER', group='wobos')
    totAnICost: Final[float] = OUTPUT(label='Total Assembly & Installation Cost', units='$', type='NUMBER', group='wobos')
    cabSurvey: Final[float] = OUTPUT(label='Cable Route Survey Cost', units='$', type='NUMBER', group='wobos')
    turbine_install_cost: Final[float] = OUTPUT(label='Turbine Install Cost', units='$', type='NUMBER', group='wobos')
    substructure_install_cost: Final[float] = OUTPUT(label='Substructure Install Cost', units='$', type='NUMBER', group='wobos')
    electrical_install_cost: Final[float] = OUTPUT(label='Electrical Install Cost', units='$', type='NUMBER', group='wobos')
    mob_demob_cost: Final[float] = OUTPUT(label='Mobilization/Demobilization Cost', units='$', type='NUMBER', group='wobos')
    array_cable_install_cost: Final[float] = OUTPUT(label='Array Cable Installation Cost', units='$', type='NUMBER', group='wobos')
    export_cable_install_cost: Final[float] = OUTPUT(label='Export Cable Installation Cost', units='$', type='NUMBER', group='wobos')
    substation_install_cost: Final[float] = OUTPUT(label='Substation Installation Cost', units='$', type='NUMBER', group='wobos')
    totPnSCost: Final[float] = OUTPUT(label='Total Port & Staging Cost', units='$', type='NUMBER', group='wobos')
    totEnMCost: Final[float] = OUTPUT(label='Total Engineering & Management Cost', units='$', type='NUMBER', group='wobos')
    totDevCost: Final[float] = OUTPUT(label='Total Development Cost', units='$', type='NUMBER', group='wobos')
    commissioning: Final[float] = OUTPUT(label='Plant Commissioning Cost', units='$', type='NUMBER', group='wobos')
    decomCost: Final[float] = OUTPUT(label='Plant Decommissioning Cost', units='$', type='NUMBER', group='wobos')
    bos_capex: Final[float] = OUTPUT(label='BOS Capital Expenditures', units='$', type='NUMBER', group='wobos')
    soft_costs: Final[float] = OUTPUT(label='Soft Costs', units='$', type='NUMBER', group='wobos')
    total_contingency_cost: Final[float] = OUTPUT(label='Total Contingency Cost', units='$', type='NUMBER', group='wobos')
    construction_insurance_cost: Final[float] = OUTPUT(label='Construction Insurance Cost', units='$', type='NUMBER', group='wobos')
    construction_finance_cost: Final[float] = OUTPUT(label='Construction Finance Cost', units='$', type='NUMBER', group='wobos')
    construction_finance_factor: Final[float] = OUTPUT(label='Construction Finance Factor', type='NUMBER', group='wobos')
    total_bos_cost: Final[float] = OUTPUT(label='Total Balance of System Cost', units='$', type='NUMBER', group='wobos')

    def __init__(self, *args: Mapping[str, Any],
                 turbCapEx: float = ...,
                 nTurb: float = ...,
                 turbR: float = ...,
                 rotorD: float = ...,
                 hubH: float = ...,
                 waterD: float = ...,
                 distShore: float = ...,
                 distPort: float = ...,
                 distPtoA: float = ...,
                 distAtoS: float = ...,
                 substructure: float = ...,
                 anchor: float = ...,
                 turbInstallMethod: float = ...,
                 towerInstallMethod: float = ...,
                 installStrategy: float = ...,
                 cableOptimizer: float = ...,
                 moorLines: float = ...,
                 buryDepth: float = ...,
                 arrayY: float = ...,
                 arrayX: float = ...,
                 substructCont: float = ...,
                 turbCont: float = ...,
                 elecCont: float = ...,
                 interConVolt: float = ...,
                 distInterCon: float = ...,
                 scrapVal: float = ...,
                 projLife: float = ...,
                 inspectClear: float = ...,
                 plantComm: float = ...,
                 procurement_contingency: float = ...,
                 install_contingency: float = ...,
                 construction_insurance: float = ...,
                 capital_cost_year_0: float = ...,
                 capital_cost_year_1: float = ...,
                 capital_cost_year_2: float = ...,
                 capital_cost_year_3: float = ...,
                 capital_cost_year_4: float = ...,
                 capital_cost_year_5: float = ...,
                 tax_rate: float = ...,
                 interest_during_construction: float = ...,
                 mpileCR: float = ...,
                 mtransCR: float = ...,
                 mpileD: float = ...,
                 mpileL: float = ...,
                 mpEmbedL: float = ...,
                 jlatticeCR: float = ...,
                 jtransCR: float = ...,
                 jpileCR: float = ...,
                 jlatticeA: float = ...,
                 jpileL: float = ...,
                 jpileD: float = ...,
                 spStifColCR: float = ...,
                 spTapColCR: float = ...,
                 ballCR: float = ...,
                 deaFixLeng: float = ...,
                 ssStifColCR: float = ...,
                 ssTrussCR: float = ...,
                 ssHeaveCR: float = ...,
                 sSteelCR: float = ...,
                 moorDia: float = ...,
                 moorCR: float = ...,
                 scourMat: float = ...,
                 number_install_seasons: float = ...,
                 pwrFac: float = ...,
                 buryFac: float = ...,
                 catLengFac: float = ...,
                 exCabFac: float = ...,
                 subsTopFab: float = ...,
                 subsTopDes: float = ...,
                 topAssemblyFac: float = ...,
                 subsJackCR: float = ...,
                 subsPileCR: float = ...,
                 dynCabFac: float = ...,
                 shuntCR: float = ...,
                 highVoltSG: float = ...,
                 medVoltSG: float = ...,
                 backUpGen: float = ...,
                 workSpace: float = ...,
                 otherAncillary: float = ...,
                 mptCR: float = ...,
                 arrVoltage: float = ...,
                 cab1CR: float = ...,
                 cab2CR: float = ...,
                 cab1CurrRating: float = ...,
                 cab2CurrRating: float = ...,
                 arrCab1Mass: float = ...,
                 arrCab2Mass: float = ...,
                 cab1TurbInterCR: float = ...,
                 cab2TurbInterCR: float = ...,
                 cab2SubsInterCR: float = ...,
                 expVoltage: float = ...,
                 expCurrRating: float = ...,
                 expCabMass: float = ...,
                 expCabCR: float = ...,
                 expSubsInterCR: float = ...,
                 arrayCables: str = ...,
                 exportCables: str = ...,
                 moorTimeFac: float = ...,
                 moorLoadout: float = ...,
                 moorSurvey: float = ...,
                 prepAA: float = ...,
                 prepSpar: float = ...,
                 upendSpar: float = ...,
                 prepSemi: float = ...,
                 turbFasten: float = ...,
                 boltTower: float = ...,
                 boltNacelle1: float = ...,
                 boltNacelle2: float = ...,
                 boltNacelle3: float = ...,
                 boltBlade1: float = ...,
                 boltBlade2: float = ...,
                 boltRotor: float = ...,
                 vesselPosTurb: float = ...,
                 vesselPosJack: float = ...,
                 vesselPosMono: float = ...,
                 subsVessPos: float = ...,
                 monoFasten: float = ...,
                 jackFasten: float = ...,
                 prepGripperMono: float = ...,
                 prepGripperJack: float = ...,
                 placePiles: float = ...,
                 prepHamMono: float = ...,
                 prepHamJack: float = ...,
                 removeHamMono: float = ...,
                 removeHamJack: float = ...,
                 placeTemplate: float = ...,
                 placeJack: float = ...,
                 levJack: float = ...,
                 hamRate: float = ...,
                 placeMP: float = ...,
                 instScour: float = ...,
                 placeTP: float = ...,
                 groutTP: float = ...,
                 tpCover: float = ...,
                 prepTow: float = ...,
                 spMoorCon: float = ...,
                 ssMoorCon: float = ...,
                 spMoorCheck: float = ...,
                 ssMoorCheck: float = ...,
                 ssBall: float = ...,
                 surfLayRate: float = ...,
                 cabPullIn: float = ...,
                 cabTerm: float = ...,
                 cabLoadout: float = ...,
                 buryRate: float = ...,
                 subsPullIn: float = ...,
                 shorePullIn: float = ...,
                 landConstruct: float = ...,
                 expCabLoad: float = ...,
                 subsLoad: float = ...,
                 placeTop: float = ...,
                 pileSpreadDR: float = ...,
                 pileSpreadMob: float = ...,
                 groutSpreadDR: float = ...,
                 groutSpreadMob: float = ...,
                 seaSpreadDR: float = ...,
                 seaSpreadMob: float = ...,
                 compRacks: float = ...,
                 cabSurveyCR: float = ...,
                 cabDrillDist: float = ...,
                 cabDrillCR: float = ...,
                 mpvRentalDR: float = ...,
                 diveTeamDR: float = ...,
                 winchDR: float = ...,
                 civilWork: float = ...,
                 elecWork: float = ...,
                 nCrane600: float = ...,
                 nCrane1000: float = ...,
                 crane600DR: float = ...,
                 crane1000DR: float = ...,
                 craneMobDemob: float = ...,
                 entranceExitRate: float = ...,
                 dockRate: float = ...,
                 wharfRate: float = ...,
                 laydownCR: float = ...,
                 estEnMFac: float = ...,
                 preFEEDStudy: float = ...,
                 feedStudy: float = ...,
                 stateLease: float = ...,
                 outConShelfLease: float = ...,
                 saPlan: float = ...,
                 conOpPlan: float = ...,
                 nepaEisMet: float = ...,
                 physResStudyMet: float = ...,
                 bioResStudyMet: float = ...,
                 socEconStudyMet: float = ...,
                 navStudyMet: float = ...,
                 nepaEisProj: float = ...,
                 physResStudyProj: float = ...,
                 bioResStudyProj: float = ...,
                 socEconStudyProj: float = ...,
                 navStudyProj: float = ...,
                 coastZoneManAct: float = ...,
                 rivsnHarbsAct: float = ...,
                 cleanWatAct402: float = ...,
                 cleanWatAct404: float = ...,
                 faaPlan: float = ...,
                 endSpecAct: float = ...,
                 marMamProtAct: float = ...,
                 migBirdAct: float = ...,
                 natHisPresAct: float = ...,
                 addLocPerm: float = ...,
                 metTowCR: float = ...,
                 decomDiscRate: float = ...,
                 hubD: float = ...,
                 bladeL: float = ...,
                 chord: float = ...,
                 nacelleW: float = ...,
                 nacelleL: float = ...,
                 rnaM: float = ...,
                 towerD: float = ...,
                 towerM: float = ...,
                 subTotM: float = ...,
                 subTotCost: float = ...,
                 moorCost: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
