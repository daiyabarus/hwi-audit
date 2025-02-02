from dataclasses import dataclass, field


@dataclass
class NEAttributes:
    NENAME: str = field(default="", metadata={"xml": "NENAME"})
    HOTPATCHVERSION: str = field(default="", metadata={"xml": "HOTPATCHVERSION"})
    SWVERSION: str = field(default="", metadata={"xml": "SWVERSION"})


@dataclass
class CellAttributes:
    LocalCellId: str = field(default="", metadata={"xml": "LocalCellId"})
    CellName: str = field(default="", metadata={"xml": "CellName"})
    CsgInd: str = field(default="", metadata={"xml": "CsgInd"})
    UlCyclicPrefix: str = field(default="", metadata={"xml": "UlCyclicPrefix"})
    DlCyclicPrefix: str = field(default="", metadata={"xml": "DlCyclicPrefix"})
    FreqBand: str = field(default="", metadata={"xml": "FreqBand"})
    UlEarfcnCfgInd: str = field(default="", metadata={"xml": "UlEarfcnCfgInd"})
    DlEarfcn: str = field(default="", metadata={"xml": "DlEarfcn"})
    UlBandWidth: str = field(default="", metadata={"xml": "UlBandWidth"})
    DlBandWidth: str = field(default="", metadata={"xml": "DlBandWidth"})
    CellId: str = field(default="", metadata={"xml": "CellId"})
    PhyCellId: str = field(default="", metadata={"xml": "PhyCellId"})
    AdditionalSpectrumEmission: str = field(
        default="", metadata={"xml": "AdditionalSpectrumEmission"}
    )
    CellActiveState: str = field(default="", metadata={"xml": "CellActiveState"})
    CellAdminState: str = field(default="", metadata={"xml": "CellAdminState"})
    FddTddInd: str = field(default="", metadata={"xml": "FddTddInd"})
    CellSpecificOffset: str = field(default="", metadata={"xml": "CellSpecificOffset"})
    QoffsetFreq: str = field(default="", metadata={"xml": "QoffsetFreq"})
    RootSequenceIdx: str = field(default="", metadata={"xml": "RootSequenceIdx"})
    HighSpeedFlag: str = field(default="", metadata={"xml": "HighSpeedFlag"})
    PreambleFmt: str = field(default="", metadata={"xml": "PreambleFmt"})
    CellRadius: str = field(default="", metadata={"xml": "CellRadius"})
    CustomizedBandWidthCfgInd: str = field(
        default="", metadata={"xml": "CustomizedBandWidthCfgInd"}
    )
    EmergencyAreaIdCfgInd: str = field(
        default="", metadata={"xml": "EmergencyAreaIdCfgInd"}
    )
    UePowerMaxCfgInd: str = field(default="", metadata={"xml": "UePowerMaxCfgInd"})
    MultiRruCellFlag: str = field(default="", metadata={"xml": "MultiRruCellFlag"})
    CPRICompression: str = field(default="", metadata={"xml": "CPRICompression"})
    AirCellFlag: str = field(default="", metadata={"xml": "AirCellFlag"})
    CrsPortNum: str = field(default="", metadata={"xml": "CrsPortNum"})
    TxRxMode: str = field(default="", metadata={"xml": "TxRxMode"})
    UserLabel: str = field(default="", metadata={"xml": "UserLabel"})
    WorkMode: str = field(default="", metadata={"xml": "WorkMode"})
    EuCellStandbyMode: str = field(default="", metadata={"xml": "EuCellStandbyMode"})
    SfnMasterCellLabel: str = field(default="", metadata={"xml": "SfnMasterCellLabel"})
    CellSlaveBand: str = field(default="", metadata={"xml": "CellSlaveBand"})
    CnOpSharingGroupId: str = field(default="", metadata={"xml": "CnOpSharingGroupId"})
    IntraFreqRanSharingInd: str = field(
        default="", metadata={"xml": "IntraFreqRanSharingInd"}
    )
    IntraFreqAnrInd: str = field(default="", metadata={"xml": "IntraFreqAnrInd"})
    CellScaleInd: str = field(default="", metadata={"xml": "CellScaleInd"})
    FreqPriorityForAnr: str = field(default="", metadata={"xml": "FreqPriorityForAnr"})
    CellRadiusStartLocation: str = field(
        default="", metadata={"xml": "CellRadiusStartLocation"}
    )
    SpecifiedCellFlag: str = field(default="", metadata={"xml": "SpecifiedCellFlag"})
    MultiCellShareMode: str = field(default="", metadata={"xml": "MultiCellShareMode"})
    ObjId: str = field(default="", metadata={"xml": "objId"})
    NbCellFlag: str = field(default="", metadata={"xml": "NbCellFlag"})
    SubframeAssignment: str = field(default="", metadata={"xml": "SubframeAssignment"})
    SpecialSubframePatterns: str = field(
        default="", metadata={"xml": "SpecialSubframePatterns"}
    )
    CrsPortMap: str = field(default="", metadata={"xml": "CrsPortMap"})
    CsiRsPeriod: str = field(default="", metadata={"xml": "CsiRsPeriod"})
    UlEarfcn: str = field(default="", metadata={"xml": "UlEarfcn"})
    UePowerMax: str = field(default="", metadata={"xml": "UePowerMax"})
