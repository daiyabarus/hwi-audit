from dataclasses import dataclass
from typing import Optional


@dataclass
class CaMgtCfgAttibutes:
    LocalCellId: Optional[str] = None
    CarrAggrA2ThdRsrp: Optional[str] = None
    CarrAggrA4ThdRsrp: Optional[str] = None
    CarrierMgtSwitch: Optional[str] = None
    ActiveBufferLenThd: Optional[str] = None
    DeactiveBufferLenThd: Optional[str] = None
    ActiveBufferDelayThd: Optional[str] = None
    DeactiveThroughputThd: Optional[str] = None
    CarrAggrA6Offset: Optional[str] = None
    SCellAgingTime: Optional[str] = None
    CaA6ReportAmount: Optional[str] = None
    CaA6ReportInterval: Optional[str] = None
    SccDeactCqiThd: Optional[str] = None
    SccCfgInterval: Optional[str] = None
    CellCaAlgoSwitch: Optional[str] = None
    UlCaActiveTimeToTrigger: Optional[str] = None
    MeasCycleSCell: Optional[str] = None
    CellMaxPccNumber: Optional[str] = None
    PccUserNumberOffloadThd: Optional[str] = None
    EnhancedPccAnchorA1ThdRsrp: Optional[str] = None
    AddedMeasCfg: Optional[str] = None
    BlindScellSampleNum: Optional[str] = None
    OptMode: Optional[str] = None
    SleepPeriod: Optional[str] = None
    StatPeriod: Optional[str] = None
    RelaxedBHSccDeactCqiThd: Optional[str] = None
    RelaxedBackhaulCaMaxCcNum: Optional[str] = None
    DisCloudBBCaMaxCcNum: Optional[str] = None
    CaA2TimeToTrigger: Optional[str] = None
    CaA6TimeToTrigger: Optional[str] = None
    CaA1TimeToTrigger: Optional[str] = None
    CaA4TimeToTrigger: Optional[str] = None
    SccQuietTime: Optional[str] = None
    FTRelaxedBHCaDLMaxCcNum: Optional[str] = None
    FddTddCaUlMaxCcNum: Optional[str] = None
    FddTddCaDlMaxCcNum: Optional[str] = None
    FTCA2CCAnchorPolicy: Optional[str] = None
    FTCAMultiCCAnchorPolicy: Optional[str] = None
    UlHeavyTrafficMlbTFCAOptSw: Optional[str] = None
    SccReactivationTime: Optional[str] = None
    FTRelaxedBHCaUlMaxCcNum: Optional[str] = None
    RelaxedBHCaUlMaxCcNum: Optional[str] = None
    CaTrafficDirectionPref: Optional[str] = None
    CaMimoPriorityStrategySw: Optional[str] = None
    EnhancedSccSelA1ThldRsrp: Optional[str] = None
    FastScellSelAftScellRmvSw: Optional[str] = None
    SrsBasedLowEffSinrThld: Optional[str] = None
    RsrpOffset: Optional[str] = None
    SpectrumCoordSinrThld: Optional[str] = None
    MinDlAvgToBeScheduledUeNum: Optional[str] = None
    SmartCaPccAnchoringHyst: Optional[str] = None
    ScellHeavyLoadUeNumThld: Optional[str] = None
    CellCaAlgoExtSwitch: Optional[str] = None
    CaPreallocationSccUeCount: Optional[str] = None
    MassiveMimoGainCoefficient: Optional[str] = None
    ScellNoActivationUeNumThld: Optional[str] = None
    HLUeCntThldForScellConfig: Optional[str] = None
    CaSccFreqMeasOptSw: Optional[str] = None
    VolteCaA2RsrpThld: Optional[str] = None
    MinRsvRouteNumberForLAA: Optional[str] = None
    HighLoadCellTypeNotAsScell: Optional[str] = None
    SccDetectCqiDecreaseStep: Optional[str] = None
    RelaxedBhSccDlTargetIbler: Optional[str] = None
    CaRouteConfigPenaltyWeight: Optional[str] = None
    CaRouteConfigPenaltyOfs: Optional[str] = None
    UlCaA1RsrpThld: Optional[str] = None
    UlCaA2RsrpThld: Optional[str] = None
    UlCaLargePacketDataVoThld: Optional[str] = None
    FddTddCaMaxFrameOfsDiff: Optional[str] = None


@dataclass
class CaMgtCfg:
    attributes: CaMgtCfgAttibutes
