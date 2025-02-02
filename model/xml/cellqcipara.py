from dataclasses import dataclass, field


@dataclass
class CellQciParaAttributes:
    LocalCellId: str = field(default="", metadata={"xml": "LocalCellId"})
    Qci: str = field(default="", metadata={"xml": "Qci"})
    InterFreqHoGroupId: str = field(default="", metadata={"xml": "InterFreqHoGroupId"})
    InterRatHoCdmaHrpdGroupId: str = field(
        default="", metadata={"xml": "InterRatHoCdmaHrpdGroupId"}
    )
    InterRatHoCommGroupId: str = field(
        default="", metadata={"xml": "InterRatHoCommGroupId"}
    )
    InterRatHoGeranGroupId: str = field(
        default="", metadata={"xml": "InterRatHoGeranGroupId"}
    )
    InterRatHoUtranGroupId: str = field(
        default="", metadata={"xml": "InterRatHoUtranGroupId"}
    )
    IntraFreqHoGroupId: str = field(default="", metadata={"xml": "IntraFreqHoGroupId"})
    DrxParaGroupId: str = field(default="", metadata={"xml": "DrxParaGroupId"})
    SriPeriod: str = field(default="", metadata={"xml": "SriPeriod"})
    RlfTimerConstCfgInd: str = field(
        default="", metadata={"xml": "RlfTimerConstCfgInd"}
    )
    TrafficRelDelay: str = field(default="", metadata={"xml": "TrafficRelDelay"})
    QciPriorityForHo: str = field(default="", metadata={"xml": "QciPriorityForHo"})
    PreallocationParaGroupId: str = field(
        default="", metadata={"xml": "PreallocationParaGroupId"}
    )
    QciPriorityForDrx: str = field(default="", metadata={"xml": "QciPriorityForDrx"})
    QciAlgoSwitch: str = field(default="", metadata={"xml": "QciAlgoSwitch"})
    QciEutranFreqRelationId: str = field(
        default="", metadata={"xml": "QciEutranFreqRelationId"}
    )
    QciUtranFreqRelationId: str = field(
        default="", metadata={"xml": "QciUtranFreqRelationId"}
    )
    QciGeranFreqRelationId: str = field(
        default="", metadata={"xml": "QciGeranFreqRelationId"}
    )
    EmtcModeADrxParaGroupId: str = field(
        default="", metadata={"xml": "EmtcModeADrxParaGroupId"}
    )
    EmtcModeBDrxParaGroupId: str = field(
        default="", metadata={"xml": "EmtcModeBDrxParaGroupId"}
    )
    ServiceFlag: str = field(default="", metadata={"xml": "ServiceFlag"})
    DlAmbrLimitFactor: str = field(default="", metadata={"xml": "DlAmbrLimitFactor"})
    QciAmbrLimitFlag: str = field(default="", metadata={"xml": "QciAmbrLimitFlag"})
    UlAmbrLimitFactor: str = field(default="", metadata={"xml": "UlAmbrLimitFactor"})
    InitDlTargetIbler: str = field(default="", metadata={"xml": "InitDlTargetIbler"})
    SinrAdjustTargetIbler: str = field(
        default="", metadata={"xml": "SinrAdjustTargetIbler"}
    )
    EmtcSriPeriod: str = field(default="", metadata={"xml": "EmtcSriPeriod"})
    UsUeControlRate: str = field(default="", metadata={"xml": "UsUeControlRate"})
    QciPdcchSinrOffset: str = field(default="", metadata={"xml": "QciPdcchSinrOffset"})
    DecreaseInNackCqiAdj: str = field(
        default="", metadata={"xml": "DecreaseInNackCqiAdj"}
    )
    CeuUlPathLossThld: str = field(default="", metadata={"xml": "CeuUlPathLossThld"})
    NrHoParamGroupId: str = field(default="", metadata={"xml": "NrHoParamGroupId"})
    QciSinrThldForTrigTtibB: str = field(
        default="", metadata={"xml": "QciSinrThldForTrigTtibB"}
    )
    LowLatencyFlag: str = field(default="", metadata={"xml": "LowLatencyFlag"})
    NsaDcDefaultBearerMode: str = field(
        default="", metadata={"xml": "NsaDcDefaultBearerMode"}
    )
    LowDelayCeuPreallocOptThld: str = field(
        default="", metadata={"xml": "LowDelayCeuPreallocOptThld"}
    )
    LowDelayUeSrSchMinDataVol: str = field(
        default="", metadata={"xml": "LowDelayUeSrSchMinDataVol"}
    )
    NsaDcGeranHoGroupId: str = field(
        default="", metadata={"xml": "NsaDcGeranHoGroupId"}
    )
    NsaDcInterFreqHoGroupId: str = field(
        default="", metadata={"xml": "NsaDcInterFreqHoGroupId"}
    )
    NsaDcInterRatHoCommGroupId: str = field(
        default="", metadata={"xml": "NsaDcInterRatHoCommGroupId"}
    )
    NsaDcIntraFreqHoGroupId: str = field(
        default="", metadata={"xml": "NsaDcIntraFreqHoGroupId"}
    )
    NsaDcUtranHoGroupId: str = field(
        default="", metadata={"xml": "NsaDcUtranHoGroupId"}
    )
    NsaDcOptSwitch: str = field(default="", metadata={"xml": "NsaDcOptSwitch"})
    NsaDcDrxParaGroupId: str = field(
        default="", metadata={"xml": "NsaDcDrxParaGroupId"}
    )
    EmtcModeACl0DrxParaGroupId: str = field(
        default="", metadata={"xml": "EmtcModeACl0DrxParaGroupId"}
    )
    EmtcModeBCl2DrxParaGroupId: str = field(
        default="", metadata={"xml": "EmtcModeBCl2DrxParaGroupId"}
    )
    NsaDcQciParamGroupId: str = field(
        default="", metadata={"xml": "NsaDcQciParamGroupId"}
    )
    MaximumNumberOfCarriers: str = field(
        default="", metadata={"xml": "MaximumNumberOfCarriers"}
    )
    ServReselTrgDlEarfcn: str = field(
        default="", metadata={"xml": "ServReselTrgDlEarfcn"}
    )
    ServReselTrgDlEarfcn: str = field(
        default="", metadata={"xml": "ServReselTrgDlEarfcn"}
    )
