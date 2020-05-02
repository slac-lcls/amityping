import typing
from mypy_extensions import TypedDict

from amitypes.array import Array1d


__all__ = [
    'TypedDict',
    'Peaks',
    'HSDSegmentPeaks',
    'HSDPeaks',
    'HSDSegmentWaveforms',
    'HSDWaveforms',
    'HSDAssemblies',
    'HSDTypes',
]


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
