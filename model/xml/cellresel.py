from dataclasses import dataclass, field


@dataclass
class CellReselAttributes:
    LocalCellId: str = field(default="", metadata={"xml": "LocalCellId"})
    Qhyst: str = field(default="", metadata={"xml": "Qhyst"})
    SpeedDepReselCfgInd: str = field(
        default="", metadata={"xml": "SpeedDepReselCfgInd"}
    )
    SNonIntraSearchCfgInd: str = field(
        default="", metadata={"xml": "SNonIntraSearchCfgInd"}
    )
    SNonIntraSearch: str = field(default="", metadata={"xml": "SNonIntraSearch"})
    ThrshServLow: str = field(default="", metadata={"xml": "ThrshServLow"})
    CellReselPriority: str = field(default="", metadata={"xml": "CellReselPriority"})
    QRxLevMin: str = field(default="", metadata={"xml": "QRxLevMin"})
    PMaxCfgInd: str = field(default="", metadata={"xml": "PMaxCfgInd"})
    SIntraSearchCfgInd: str = field(default="", metadata={"xml": "SIntraSearchCfgInd"})
    SIntraSearch: str = field(default="", metadata={"xml": "SIntraSearch"})
    MeasBandWidthCfgInd: str = field(
        default="", metadata={"xml": "MeasBandWidthCfgInd"}
    )
    TReselEutran: str = field(default="", metadata={"xml": "TReselEutran"})
    SpeedStateSfCfgInd: str = field(default="", metadata={"xml": "SpeedStateSfCfgInd"})
    TReselEutranSfMedium: str = field(
        default="", metadata={"xml": "TReselEutranSfMedium"}
    )
    TReselEutranSfHigh: str = field(default="", metadata={"xml": "TReselEutranSfHigh"})
    NeighCellConfig: str = field(default="", metadata={"xml": "NeighCellConfig"})
    PresenceAntennaPort1: str = field(
        default="", metadata={"xml": "PresenceAntennaPort1"}
    )
    SIntraSearchQ: str = field(default="", metadata={"xml": "SIntraSearchQ"})
    SNonIntraSearchQ: str = field(default="", metadata={"xml": "SNonIntraSearchQ"})
    ThrshServLowQCfgInd: str = field(
        default="", metadata={"xml": "ThrshServLowQCfgInd"}
    )
    QQualMinCfgInd: str = field(default="", metadata={"xml": "QQualMinCfgInd"})
    QQualMin: str = field(default="", metadata={"xml": "QQualMin"})
    TReselForNb: str = field(default="", metadata={"xml": "TReselForNb"})
    TReselInterFreqForNb: str = field(
        default="", metadata={"xml": "TReselInterFreqForNb"}
    )
    TReselEutranCE: str = field(default="", metadata={"xml": "TReselEutranCE"})
    EmtcCellReselPriority: str = field(
        default="", metadata={"xml": "EmtcCellReselPriority"}
    )
    PwrOffsetForReselToIntraNb: str = field(
        default="", metadata={"xml": "PwrOffsetForReselToIntraNb"}
    )
    QQualMinForCeModeA: str = field(default="", metadata={"xml": "QQualMinForCeModeA"})
    QQualMinForCeModeB: str = field(default="", metadata={"xml": "QQualMinForCeModeB"})
    QRxLevMinForCeModeA: str = field(
        default="", metadata={"xml": "QRxLevMinForCeModeA"}
    )
    QRxLevMinForCeModeB: str = field(
        default="", metadata={"xml": "QRxLevMinForCeModeB"}
    )
    NbReselRelaxedMonMeasThld: str = field(
        default="", metadata={"xml": "NbReselRelaxedMonMeasThld"}
    )
    NbReselRelaxedMonMeasThld: str = field(
        default="", metadata={"xml": "NbReselRelaxedMonMeasThld"}
    )
