import pytest
import numpy
import typing
import amitypes


@pytest.fixture(scope='function')
def flattener():
    def flattener_func(cls):
        if hasattr(cls, "__name__"):
            if cls.__module__ in ['builtins', '__main__']:
                return cls, cls.__name__
            else:
                return cls, "%s.%s" % (cls.__module__, cls.__name__)
        else:
            return cls, str(cls)
    return flattener_func


@pytest.fixture(scope='function')
def types():
    return [
        amitypes.Array1d,
        amitypes.Array2d,
        amitypes.Array3d,
        amitypes.Peaks,
        amitypes.HSDPeaks,
        amitypes.HSDSegmentPeaks,
        amitypes.HSDWaveforms,
        amitypes.HSDSegmentWaveforms,
        amitypes.HSDAssemblies,
        amitypes.MultiChannelInt,
        amitypes.MultiChannelFloat,
        amitypes.MultiChannelScalar,
        amitypes.AcqirisTimes,
        amitypes.AcqirisWaveforms,
        amitypes.AcqirisChannel,
        amitypes.GenericWfTimes,
        amitypes.GenericWfWaveforms,
        amitypes.GenericWfChannel,
        amitypes.MultiChannelWaveform,
        amitypes.ScanControls,
        amitypes.ScanMonitors,
        amitypes.ScanLabels,
        int,
        list,
        numpy.float64,
        typing.Union,
    ]


@pytest.fixture(scope='function')
def type_map(types, flattener):
    return [flattener(t) for t in types]


def test_dumps(type_map):
    for obj, expected in type_map:
        # check that the object dumps as expected
        assert amitypes.dumps(obj) == expected


def test_loads(type_map):
    for expected, objstr in type_map:
        # check that the object loads as expected
        assert amitypes.loads(objstr) == expected


def test_dumps_and_loads(types):
    for obj in types:
        assert amitypes.loads(amitypes.dumps(obj)) == obj
