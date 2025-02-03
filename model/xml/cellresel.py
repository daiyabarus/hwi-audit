from dataclasses import dataclass
from typing import Optional


@dataclass
class CellReselAttributes:
    LocalCellId: Optional[str] = None
    Qhyst: Optional[str] = None
    SpeedDepReselCfgInd: Optional[str] = None
    SNonIntraSearchCfgInd: Optional[str] = None
    SNonIntraSearch: Optional[str] = None
    ThrshServLow: Optional[str] = None
    CellReselPriority: Optional[str] = None
    QRxLevMin: Optional[str] = None
    PMaxCfgInd: Optional[str] = None
    SIntraSearchCfgInd: Optional[str] = None
    SIntraSearch: Optional[str] = None
    MeasBandWidthCfgInd: Optional[str] = None
    TReselEutran: Optional[str] = None
    SpeedStateSfCfgInd: Optional[str] = None
    TReselEutranSfMedium: Optional[str] = None
    TReselEutranSfHigh: Optional[str] = None
    NeighCellConfig: Optional[str] = None
    PresenceAntennaPort1: Optional[str] = None
    SIntraSearchQ: Optional[str] = None
    SNonIntraSearchQ: Optional[str] = None
    ThrshServLowQCfgInd: Optional[str] = None
    QQualMinCfgInd: Optional[str] = None
    QQualMin: Optional[str] = None
    TReselForNb: Optional[str] = None
    TReselInterFreqForNb: Optional[str] = None
    TReselEutranCE: Optional[str] = None
    EmtcCellReselPriority: Optional[str] = None
    PwrOffsetForReselToIntraNb: Optional[str] = None
    QQualMinForCeModeA: Optional[str] = None
    QQualMinForCeModeB: Optional[str] = None
    QRxLevMinForCeModeA: Optional[str] = None
    QRxLevMinForCeModeB: Optional[str] = None
    NbReselRelaxedMonMeasThld: Optional[str] = None


@dataclass
class CellResel:
    attributes: CellReselAttributes
