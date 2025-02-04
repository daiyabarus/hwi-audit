from dataclasses import dataclass
from typing import Optional


@dataclass
class CellAttributes:
    LocalCellId: Optional[str] = None
    CellName: Optional[str] = None
    DlEarfcn: Optional[str] = None
    UlBandWidth: Optional[str] = None
    DlBandWidth: Optional[str] = None
    CellId: Optional[str] = None
    PhyCellId: Optional[str] = None
    FddTddInd: Optional[str] = None
    SubframeAssignment: Optional[str] = None
    SpecialSubframePatterns: Optional[str] = None
    CellSpecificOffset: Optional[str] = None
    TxRxMode: Optional[str] = None


@dataclass
class Cell:
    attributes: CellAttributes


@dataclass
class NENAMEAttributes:
    NENAME: Optional[str] = None
    LMTVERSION: Optional[str] = None


@dataclass
class NENAME:
    attributes: NENAMEAttributes
