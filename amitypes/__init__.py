import typing
import numpy as np
from mypy_extensions import TypedDict


__version__ = '1.0.5'


__all__ = [
    'dumps',
    'loads',
    'Array',
    'Array1d',
    'Array2d',
    'Array3d',
    'Peaks',
    'HSDSegmentPeaks',
    'HSDPeaks',
    'HSDSegmentWaveforms',
    'HSDWaveforms',
    'HSDAssemblies',
    'HSDTypes',
]


def dumps(cls):
    if type(cls) == type:
        if cls.__module__ in ['builtins', '__main__']:
            return cls.__name__
        else:
            return "%s.%s" % (cls.__module__, cls.__name__)
    elif issubclass(type(cls), ArrayMeta):
        return "%s.%s" % (cls.__module__, cls.__name__)
    else:
        return str(cls)


def loads(type_str):
    return eval(type_str.replace('amitypes.', ''))


class ArrayMeta(type):
    pass


class Array1dMeta(ArrayMeta):

    @classmethod
    def __instancecheck__(cls, inst) -> bool:
        if not isinstance(inst, np.ndarray):
            return False

        if inst.ndim != 1:
            return False

        return True


class Array2dMeta(ArrayMeta):

    @classmethod
    def __instancecheck__(cls, inst) -> bool:
        if not isinstance(inst, np.ndarray):
            return False

        if inst.ndim != 2:
            return False

        return True


class Array3dMeta(ArrayMeta):

    @classmethod
    def __instancecheck__(cls, inst) -> bool:
        if not isinstance(inst, np.ndarray):
            return False

        if inst.ndim != 3:
            return False

        return True


class Array1d(metaclass=Array1dMeta):
    pass


class Array2d(metaclass=Array2dMeta):
    pass


class Array3d(metaclass=Array3dMeta):
    pass


Array = typing.Union[Array3d, Array2d, Array1d, typing.List[float]]


Peaks = typing.Tuple[typing.List[int], typing.List[Array1d]]


HSDSegmentPeaks = TypedDict(
                    "HSDSegmentPeaks",
                    {
                       '0': Peaks,
                       '1': Peaks,
                       '2': Peaks,
                       '3': Peaks,
                       '4': Peaks,
                       '5': Peaks,
                       '6': Peaks,
                       '7': Peaks,
                       '8': Peaks,
                       '9': Peaks,
                       '10': Peaks,
                       '11': Peaks,
                       '12': Peaks,
                       '13': Peaks,
                       '14': Peaks,
                       '15': Peaks,
                    },
                    total=False)


HSDPeaks = typing.Dict[int, HSDSegmentPeaks]


HSDSegmentWaveforms = TypedDict(
                        "HSDSegmentWaveforms",
                        {
                          'times': Array1d,
                          '0': Array1d,
                          '1': Array1d,
                          '2': Array1d,
                          '3': Array1d,
                          '4': Array1d,
                          '5': Array1d,
                          '6': Array1d,
                          '7': Array1d,
                          '8': Array1d,
                          '9': Array1d,
                          '10': Array1d,
                          '11': Array1d,
                          '12': Array1d,
                          '13': Array1d,
                          '14': Array1d,
                          '15': Array1d,
                        },
                        total=False)


HSDWaveforms = typing.Dict[int, HSDSegmentWaveforms]


HSDAssemblies = typing.TypeVar('HSDAssemblies')


HSDTypes = {HSDPeaks, HSDWaveforms, HSDAssemblies}
