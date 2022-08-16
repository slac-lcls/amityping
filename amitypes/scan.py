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


class ScanMeta(type):

    @classmethod
    def __instancecheck__(cls, inst) -> bool:
        if not isinstance(inst, list) and not isinstance(inst, Array1d):
            return False

        return True


class ScanControls(metaclass=ScanMeta):
    pass


class ScanMonitors(metaclass=ScanMeta):
    pass


class ScanLabels(metaclass=ScanMeta):
    pass


ScanTypes = {ScanControls, ScanMonitors, ScanLabels}


ScanControlType = float


ScanMonitorType = typing.Tuple[float, float]


ScanLabelType = str
