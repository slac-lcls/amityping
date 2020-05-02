import pytest
import numpy
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
def type_map(flattener):
    return [
        flattener(amitypes.Array1d),
        flattener(amitypes.Array2d),
        flattener(amitypes.Array3d),
        flattener(amitypes.HSDPeaks),
        flattener(amitypes.HSDWaveforms),
        flattener(list),
        flattener(numpy.float64),
    ]


def test_dumps(type_map):
    for obj, expected in type_map:
        # check that the object dumps as expected
        assert amitypes.dumps(obj) == expected


def test_loads(type_map):
    for expected, objstr in type_map:
        # check that the object loads as expected
        assert amitypes.loads(objstr) == expected
