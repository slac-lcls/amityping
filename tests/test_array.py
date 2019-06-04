import numpy as np
from amitypes import ArrayMeta, Array1d, Array2d, Array3d


def test_array_dim():
    d1 = np.zeros(5)
    d2 = np.zeros((5, 5))
    d3 = np.zeros((5, 5, 5))

    # check that the array pass the expected isinstance
    assert isinstance(d1, Array1d)
    assert isinstance(d2, Array2d)
    assert isinstance(d3, Array3d)

    # check that d1 is only a Array1d
    assert not isinstance(d1, Array2d)
    assert not isinstance(d1, Array3d)

    # check that d2 is only a Array2d
    assert not isinstance(d2, Array1d)
    assert not isinstance(d2, Array3d)

    # check that d3 is only a Array3d
    assert not isinstance(d3, Array1d)
    assert not isinstance(d3, Array2d)


def test_array_subclass():
    # test that the ArrayNd are subclasses of ArrayMeta
    for cls in [Array1d, Array2d, Array3d]:
        assert issubclass(type(cls), ArrayMeta)
