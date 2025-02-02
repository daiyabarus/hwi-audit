from dataclasses import dataclass, field


@dataclass
class EutranInterNFreqAttributes:
    LocalCellId: str = field(default="", metadata={"xml": "LocalCellId"})
    DlEarfcn: str = field(default="", metadata={"xml": "DlEarfcn"})
    UlEarfcnCfgInd: str = field(default="", metadata={"xml": "UlEarfcnCfgInd"})
    CellReselPriorityCfgInd: str = field(
        default="", metadata={"xml": "CellReselPriorityCfgInd"}
    )
    CellReselPriority: str = field(default="", metadata={"xml": "CellReselPriority"})
    EutranReselTime: str = field(default="", metadata={"xml": "EutranReselTime"})
    SpeedDependSPCfgInd: str = field(
        default="", metadata={"xml": "SpeedDependSPCfgInd"}
    )
    MeasBandWidth: str = field(default="", metadata={"xml": "MeasBandWidth"})
    QoffsetFreq: str = field(default="", metadata={"xml": "QoffsetFreq"})
    ThreshXhigh: str = field(default="", metadata={"xml": "ThreshXhigh"})
    ThreshXlow: str = field(default="", metadata={"xml": "ThreshXlow"})
    QRxLevMin: str = field(default="", metadata={"xml": "QRxLevMin"})
    PmaxCfgInd: str = field(default="", metadata={"xml": "PmaxCfgInd"})
    NeighCellConfig: str = field(default="", metadata={"xml": "NeighCellConfig"})
    PresenceAntennaPort1: str = field(
        default="", metadata={"xml": "PresenceAntennaPort1"}
    )
    InterFreqHoEventType: str = field(
        default="", metadata={"xml": "InterFreqHoEventType"}
    )
    ThreshXhighQ: str = field(default="", metadata={"xml": "ThreshXhighQ"})
    ThreshXlowQ: str = field(default="", metadata={"xml": "ThreshXlowQ"})
    QqualMinCfgInd: str = field(default="", metadata={"xml": "QqualMinCfgInd"})
    ConnFreqPriority: str = field(default="", metadata={"xml": "ConnFreqPriority"})
    MlbTargetInd: str = field(default="", metadata={"xml": "MlbTargetInd"})
    FreqPriBasedHoMeasFlag: str = field(
        default="", metadata={"xml": "FreqPriBasedHoMeasFlag"}
    )
    IdleMlbUEReleaseRatio: str = field(
        default="", metadata={"xml": "IdleMlbUEReleaseRatio"}
    )
    MlbFreqPriority: str = field(default="", metadata={"xml": "MlbFreqPriority"})
    DlFreqOffset: str = field(default="", metadata={"xml": "DlFreqOffset"})
    QoffsetFreqConn: str = field(default="", metadata={"xml": "QoffsetFreqConn"})
    MeasFreqPriority: str = field(default="", metadata={"xml": "MeasFreqPriority"})
    IfHoThdRsrpOffset: str = field(default="", metadata={"xml": "IfHoThdRsrpOffset"})
    IfMlbThdRsrpOffset: str = field(default="", metadata={"xml": "IfMlbThdRsrpOffset"})
    MasterBandFlag: str = field(default="", metadata={"xml": "MasterBandFlag"})
    InterFreqRanSharingInd: str = field(
        default="", metadata={"xml": "InterFreqRanSharingInd"}
    )
    InterFreqHighSpeedFlag: str = field(
        default="", metadata={"xml": "InterFreqHighSpeedFlag"}
    )
    AnrInd: str = field(default="", metadata={"xml": "AnrInd"})
    VoipPriority: str = field(default="", metadata={"xml": "VoipPriority"})
    PsPriority: str = field(default="", metadata={"xml": "PsPriority"})
    VolteHoTargetInd: str = field(default="", metadata={"xml": "VolteHoTargetInd"})
    BackoffTargetInd: str = field(default="", metadata={"xml": "BackoffTargetInd"})
    MlbInterFreqHoEventType: str = field(
        default="", metadata={"xml": "MlbInterFreqHoEventType"}
    )
    MobilityTargetInd: str = field(default="", metadata={"xml": "MobilityTargetInd"})
    MlbInterFreqEffiRatio: str = field(
        default="", metadata={"xml": "MlbInterFreqEffiRatio"}
    )
    SnrBasedUeSelectionMode: str = field(
        default="", metadata={"xml": "SnrBasedUeSelectionMode"}
    )
    UlTrafficMlbTargetInd: str = field(
        default="", metadata={"xml": "UlTrafficMlbTargetInd"}
    )
    UlTrafficMlbPriority: str = field(
        default="", metadata={"xml": "UlTrafficMlbPriority"}
    )
    MlbInterFreqHoA3Offset: str = field(
        default="", metadata={"xml": "MlbInterFreqHoA3Offset"}
    )
    IfSrvHoThdRsrpOffset: str = field(
        default="", metadata={"xml": "IfSrvHoThdRsrpOffset"}
    )
    IfSrvHoThdRsrqOffset: str = field(
        default="", metadata={"xml": "IfSrvHoThdRsrqOffset"}
    )
    MlbFreqUlPriority: str = field(default="", metadata={"xml": "MlbFreqUlPriority"})
    InterFreqMlbDlPrbOffset: str = field(
        default="", metadata={"xml": "InterFreqMlbDlPrbOffset"}
    )
    InterFreqMlbUlPrbOffset: str = field(
        default="", metadata={"xml": "InterFreqMlbUlPrbOffset"}
    )
    NcellNumForAnr: str = field(default="", metadata={"xml": "NcellNumForAnr"})
    MeasPerformanceDemand: str = field(
        default="", metadata={"xml": "MeasPerformanceDemand"}
    )
    IfBackoffThdRsrpOffset: str = field(
        default="", metadata={"xml": "IfBackoffThdRsrpOffset"}
    )
    IfBackoffThdRsrqOffset: str = field(
        default="", metadata={"xml": "IfBackoffThdRsrqOffset"}
    )
    VoLTEQualityIfHoTargetInd: str = field(
        default="", metadata={"xml": "VoLTEQualityIfHoTargetInd"}
    )
    IdleMlbeMtcUEReleaseRatio: str = field(
        default="", metadata={"xml": "IdleMlbeMtcUEReleaseRatio"}
    )
    InterFreqCioAdjLimitCfgInd: str = field(
        default="", metadata={"xml": "InterFreqCioAdjLimitCfgInd"}
    )
    InterFreq4TInd: str = field(default="", metadata={"xml": "InterFreq4TInd"})
    MeasPriorityForFreqPriHo: str = field(
        default="", metadata={"xml": "MeasPriorityForFreqPriHo"}
    )
    EmtcInterFreqCellReselPri: str = field(
        default="", metadata={"xml": "EmtcInterFreqCellReselPri"}
    )
    PwrOffsetForReselToInterNb: str = field(
        default="", metadata={"xml": "PwrOffsetForReselToInterNb"}
    )
    InterFreqHoA5Thd1RsrpOfs: str = field(
        default="", metadata={"xml": "InterFreqHoA5Thd1RsrpOfs"}
    )
    InterFreqHoA5Thd1RsrqOfs: str = field(
        default="", metadata={"xml": "InterFreqHoA5Thd1RsrqOfs"}
    )
    InterFreqPrdcMrFreqGrpId: str = field(
        default="", metadata={"xml": "InterFreqPrdcMrFreqGrpId"}
    )
    InterFreqRedirectionSwitch: str = field(
        default="", metadata={"xml": "InterFreqRedirectionSwitch"}
    )
    PwrOfsForNbInterFreqRedir: str = field(
        default="", metadata={"xml": "PwrOfsForNbInterFreqRedir"}
    )
    QQualMinForCeModeA: str = field(default="", metadata={"xml": "QQualMinForCeModeA"})
    QQualMinForCeModeB: str = field(default="", metadata={"xml": "QQualMinForCeModeB"})
    QRxLevMinForCeModeA: str = field(
        default="", metadata={"xml": "QRxLevMinForCeModeA"}
    )
    QRxLevMinForCeModeB: str = field(
        default="", metadata={"xml": "QRxLevMinForCeModeB"}
    )
    CovIfHoA5VolteThld1RsrpOfs: str = field(
        default="", metadata={"xml": "CovIfHoA5VolteThld1RsrpOfs"}
    )
    CovIfHoA5VolteThld2RsrpOfs: str = field(
        default="", metadata={"xml": "CovIfHoA5VolteThld2RsrpOfs"}
    )
    A3InterFHoServingRsrpOfs: str = field(
        default="", metadata={"xml": "A3InterFHoServingRsrpOfs"}
    )
    NsaCovIfHoServCellRsrpOfs: str = field(
        default="", metadata={"xml": "NsaCovIfHoServCellRsrpOfs"}
    )
    AggregationAttribute: str = field(
        default="", metadata={"xml": "AggregationAttribute"}
    )
    FreqPriHoA4ThldRsrpOffset: str = field(
        default="", metadata={"xml": "FreqPriHoA4ThldRsrpOffset"}
    )
    FreqPriHoA4ThldRsrpOffset: str = field(
        default="", metadata={"xml": "FreqPriHoA4ThldRsrpOffset"}
    )
