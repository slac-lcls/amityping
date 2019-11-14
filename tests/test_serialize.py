import pytest
import numpy
import amitypes


@pytest.fixture(scope='function')
def type_map():
    return [
        (amitypes.Array1d, 'amitypes.Array1d'),
        (amitypes.Array2d, 'amitypes.Array2d'),
        (amitypes.Array3d, 'amitypes.Array3d'),
        (amitypes.HSDPeaks, 'typing.Dict[int, amitypes.HSDSegmentPeaks]'),
        (amitypes.HSDWaveforms, 'typing.Dict[int, amitypes.HSDSegmentWaveforms]'),
        (list, 'list'),
        (numpy.float64, 'numpy.float64'),
    ]


def test_dumps(type_map):
    for obj, expected in type_map:
        # check that the object dumps as expected
        assert amitypes.dumps(obj) == expected


def test_loads(type_map):
    for expected, objstr in type_map:
        # check that the object loads as expected
        assert amitypes.loads(objstr) == expected
