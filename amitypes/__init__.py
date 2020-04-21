import sys
import typing
import numpy
import inspect
from mypy_extensions import TypedDict, _TypedDictMeta


__version__ = '1.0.8'


__all__ = [
    'dumps',
    'loads',
    'NumPyTypeDict',
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
    elif issubclass(type(cls), _TypedDictMeta):
        return "TypedDict('%s', %s)" % (cls.__name__, {k: dumps(v) for k, v in cls.__annotations__.items()})
    elif issubclass(type(cls), ArrayMeta):
        return "%s.%s" % (cls.__module__, cls.__name__)
    else:
        return str(cls)


def loads(type_str):
    cls = eval(type_str.replace('amitypes.', ''))
    if issubclass(type(cls), _TypedDictMeta):
        setattr(sys.modules[__name__], cls.__name__, cls)
    return cls


def _map_numpy_types():
    nptypemap = {}
    for name, dtype in inspect.getmembers(numpy, lambda x: inspect.isclass(x) and issubclass(x, numpy.generic)):
        try:
            ptype = None
            if 'time' in name:
                ptype = type(dtype(0, 'D').item())
            elif 'object' not in name:
                ptype = type(dtype(0).item())

            # if it is still a numpy dtype don't make a mapping
            if not issubclass(ptype, numpy.generic):
                nptypemap[dtype] = ptype
        except TypeError:
            pass

    return nptypemap


NumPyTypeDict = _map_numpy_types()


class ArrayMeta(type):
    pass


class Array1dMeta(ArrayMeta):

    @classmethod
    def __instancecheck__(cls, inst) -> bool:
        if not isinstance(inst, numpy.ndarray):
            return False

        if inst.ndim != 1:
            return False

        return True


class Array2dMeta(ArrayMeta):

    @classmethod
    def __instancecheck__(cls, inst) -> bool:
        if not isinstance(inst, numpy.ndarray):
            return False

        if inst.ndim != 2:
            return False

        return True


class Array3dMeta(ArrayMeta):

    @classmethod
    def __instancecheck__(cls, inst) -> bool:
        if not isinstance(inst, numpy.ndarray):
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
