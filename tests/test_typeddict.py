import pytest
import typing
import pickle
import amitypes


TEST_PARAMS = [
    ('TestDict', {'x': int, 'y': int}),
    ('TestDict', {}),
    ('TestDict', {'x': int, 'y': amitypes.Array3d}),
]


@pytest.fixture(scope='function')
def typed_dict(request):
    print(request.param)
    name, fields = request.param
    return name, fields, amitypes.TypedDict(name, fields)


@pytest.mark.parametrize('typed_dict', TEST_PARAMS, indirect=True)
def test_hints(typed_dict):
    name, fields, cls = typed_dict

    assert cls.__name__ == name
    assert typing.get_type_hints(cls) == fields


@pytest.mark.parametrize('typed_dict', TEST_PARAMS, indirect=True)
def test_serialization(typed_dict):
    name, fields, cls = typed_dict

    reloaded_cls = amitypes.loads(amitypes.dumps(cls))

    assert reloaded_cls.__name__ == name
    assert typing.get_type_hints(reloaded_cls) == fields


@pytest.mark.parametrize('typed_dict', TEST_PARAMS, indirect=True)
def test_pickled(typed_dict):
    name, fields, cls = typed_dict

    reloaded_cls = amitypes.loads(amitypes.dumps(cls))

    assert reloaded_cls.__name__ == name
    assert typing.get_type_hints(reloaded_cls) == fields

    pickled_cls = pickle.loads(pickle.dumps(reloaded_cls))

    assert pickled_cls.__name__ == name
    assert typing.get_type_hints(pickled_cls) == fields
