import typing
from amitypes.array import Array1d, Array2d


__all__ = [
    'MultiChannelInt',
    'MultiChannelFloat',
    'MultiChannelScalar',
    'MultiChannelScalarTypes',
    'AcqirisTimes',
    'AcqirisWaveforms',
    'AcqirisChannel',
    'AcqirisTypes',
    'GenericWfTimes',
    'GenericWfWaveforms',
    'GenericWfChannel',
    'GenericWfTypes',
    'MultiChannelWaveform',
    'MultiChannelWaveformTypes',
]


class MultiChannelInt(Array1d):
    pass


class MultiChannelFloat(Array1d):
    pass


MultiChannelScalar = typing.Union[MultiChannelInt, MultiChannelFloat, Array1d]


MultiChannelScalarTypes = {MultiChannelInt, MultiChannelFloat}


class AcqirisTimes(Array2d):
    pass


class AcqirisWaveforms(Array2d):
    pass


AcqirisChannel = Array1d


AcqirisTypes = {AcqirisTimes, AcqirisWaveforms}


GenericWfTimes = typing.List[Array1d]


GenericWfWaveforms = typing.List[Array1d]


GenericWfChannel = Array1d


GenericWfTypes = {GenericWfTimes, GenericWfWaveforms}


MultiChannelWaveform = typing.Union[AcqirisTimes, AcqirisWaveforms, GenericWfTimes, GenericWfWaveforms, Array2d]


MultiChannelWaveformTypes = AcqirisTypes | GenericWfTypes
