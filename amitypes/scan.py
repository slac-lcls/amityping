import typing
from amitypes.array import Array1d


__all__ = [
    'ScanControls',
    'ScanMonitors',
    'ScanLabels',
    'ScanTypes',
    'ScanControlType',
    'ScanMonitorType',
    'ScanLabelType',
]


class ScanControls(Array1d):
    pass


class ScanMonitors(Array1d):
    pass


class ScanLabels(Array1d):
    pass


ScanTypes = {ScanControls, ScanMonitors, ScanLabels}


ScanControlType = float


ScanMonitorType = typing.Tuple[float, float]


ScanLabelType = str
