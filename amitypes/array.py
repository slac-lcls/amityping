import numpy
import typing
import inspect


__all__ = [
    'NumPyTypeDict',
    'Array',
    'ArrayMeta',
    'Array1d',
    'Array2d',
    'Array3d',
]


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
