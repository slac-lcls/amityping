import pytest
import numpy as np
from amitypes import NumPyTypeDict


@pytest.mark.parametrize('nptype, pytype',
                         [
                            (np.float64, float),
                            (np.float32, float),
                            (np.int64, int),
                            (np.int32, int),
                            (np.int16, int),
                            (np.int8, int),
                            (np.uint64, int),
                            (np.uint32, int),
                            (np.uint16, int),
                            (np.uint8, int),
                            (int, None),
                            (float, None),
                            (np.number, None),
                            (np.floating, None),
                         ])
def test_numpy_type(nptype, pytype):
    assert NumPyTypeDict.get(nptype) == pytype
