import pytest
import json
import amitypes
import numpy as np


TEST_PARAMS = [
    {'ebeam': 7, 'gdet': 5.5, 'pwr': 'off', 'np': np.uint16(102)},
    {'ebeam': [1, 2, np.uint16(5)], 'gdet': np.arange(5), 'pwr': amitypes.DataSource},
    {'ebeam': amitypes.Array2d, 'gdet': amitypes.Peaks, 'pwr': amitypes.HSDAssemblies, 'np': amitypes.Array},
]


@pytest.fixture(scope='function')
def encoder():
    return amitypes.TypeEncoder


@pytest.mark.parametrize('orig', TEST_PARAMS)
def test_json_encoding(encoder, orig):

    # dump and then load the object
    reloaded = json.loads(json.dumps(orig, cls=encoder))

    # check the orig and reloaded have the same keys
    assert set(orig) == set(reloaded)

    for key, expected in orig.items():
        value = reloaded[key]
        if isinstance(expected, np.ndarray):
            assert np.array_equal(value, expected)
        else:
            if isinstance(value, str) and not isinstance(expected, str):
                value = amitypes.loads(value)
            assert value == expected
