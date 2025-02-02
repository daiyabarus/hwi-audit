from dataclasses import dataclass
from typing import Optional


@dataclass
class CellAttributes:
    LocalCellId: Optional[str] = None
    CellName: Optional[str] = None
    CsgInd: Optional[str] = None
    UlCyclicPrefix: Optional[str] = None
    DlCyclicPrefix: Optional[str] = None
    FreqBand: Optional[str] = None
    UlEarfcnCfgInd: Optional[str] = None
    DlEarfcn: Optional[str] = None
    UlBandWidth: Optional[str] = None
    DlBandWidth: Optional[str] = None
    CellId: Optional[str] = None
    PhyCellId: Optional[str] = None
    AdditionalSpectrumEmission: Optional[str] = None
    CellActiveState: Optional[str] = None
    CellAdminState: Optional[str] = None
    FddTddInd: Optional[str] = None
    SubframeAssignment: Optional[str] = None
    SpecialSubframePatterns: Optional[str] = None
    CellSpecificOffset: Optional[str] = None
    QoffsetFreq: Optional[str] = None
    RootSequenceIdx: Optional[str] = None
    HighSpeedFlag: Optional[str] = None
    PreambleFmt: Optional[str] = None
    CellRadius: Optional[str] = None
    CustomizedBandWidthCfgInd: Optional[str] = None
    UePowerMaxCfgInd: Optional[str] = None
    MultiRruCellFlag: Optional[str] = None
    CPRICompression: Optional[str] = None
    CrsPortNum: Optional[str] = None
    TxRxMode: Optional[str] = None
    UserLabel: Optional[str] = None
    WorkMode: Optional[str] = None
    EuCellStandbyMode: Optional[str] = None
    NbCellFlag: Optional[str] = None
    CellSlaveBand: Optional[str] = None
    CnOpSharingGroupId: Optional[str] = None
    IntraFreqRanSharingInd: Optional[str] = None
    IntraFreqAnrInd: Optional[str] = None
    CellRadiusStartLocation: Optional[str] = None
    SpecifiedCellFlag: Optional[str] = None
    MultiCellShareMode: Optional[str] = None
    objId: Optional[str] = None


@dataclass
class Cell:
    attributes: CellAttributes
