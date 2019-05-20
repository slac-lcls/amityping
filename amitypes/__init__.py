import numpy as np
from typing import Union, List, Tuple
from mypy_extensions import TypedDict


__version__ = '1.0.3'


class Array1d(type):

    @classmethod
    def __instancecheck__(cls, inst) -> bool:
        if not isinstance(inst, np.ndarray):
            return False

        if inst.ndim != 1:
            return False

        return True


class Array2d(type):

    @classmethod
    def __instancecheck__(cls, inst) -> bool:
        if not isinstance(inst, np.ndarray):
            return False

        if inst.ndim != 2:
            return False

        return True


class Array3d(type):

    @classmethod
    def __instancecheck__(cls, inst) -> bool:
        if not isinstance(inst, np.ndarray):
            return False

        if inst.ndim != 3:
            return False

        return True


Array = Union[Array2d, Array1d, List[float]]


Peaks = Tuple[List[int], List[Array1d]]


HSDPeaks = TypedDict("HSDPeaks",
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


HSDWaveforms = TypedDict("HSDWaveforms",
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


HSDTypes = {HSDPeaks, HSDWaveforms}
