import pytest
import pickle
import dataclasses
import amitypes as at


TEST_PARAMS = [
    at.DataSource({'type': 'psana'}, 'fake_run', 'fake_step', 'fake_evt'),
    at.Group('mygrp', 'hdf5', 'cspad_1234'),
    at.Detector('xtcav', 'psana', 'camera', [1, 2, 3, 4]),
]


@pytest.fixture(scope='function')
def serializers():
    return [lambda x: pickle.loads(pickle.dumps(x)), lambda x: x._deserialize(x._serialize())]


@pytest.mark.parametrize('obj', TEST_PARAMS)
def test_fields(obj):
    assert obj.fields == dataclasses.fields(obj)


@pytest.mark.parametrize('orig', TEST_PARAMS)
def test_serialize(orig, serializers):

    for func in serializers:
        loaded = func(orig)

        # check that the loaded version has the correct values
        assert loaded.fields == orig.fields
        for field in orig.fields:
            assert hasattr(loaded, field.name)
            if field.metadata.get('drop', False):
                assert getattr(loaded, field.name) == field.default
            else:
                assert getattr(loaded, field.name) == getattr(orig, field.name)

        reloaded = func(loaded)

        # check that the reloaded version has the correct values
        assert reloaded.fields == orig.fields
        for field in orig.fields:
            assert hasattr(reloaded, field.name)
            if field.metadata.get('drop', False):
                assert getattr(reloaded, field.name) == field.default
            else:
                assert getattr(reloaded, field.name) == getattr(orig, field.name)


@pytest.mark.parametrize('data', [{}, {'cat': 'bat', 'goat': 'boat'}])
def test_group(data):
    grp = at.Group('mygrp', 'hdf5', 'cspad_1234', data)

    assert bool(grp) is bool(data)

    assert len(grp) == len(data)

    for key in data:
        assert key in grp
        assert grp[key] == data[key]
