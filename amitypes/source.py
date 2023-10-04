import typing
import dataclasses
import collections.abc


__all__ = [
    'Detector',
    'Group',
    'DataSource',
    'PyArrowTypes',
]


T = typing.TypeVar('T', bound='Serializable')


class Serializable:
    @property
    def fields(self) -> typing.Iterable[dataclasses.Field]:
        return dataclasses.fields(self)

    def _dropped(self) -> typing.Generator[dataclasses.Field, None, None]:
        for field in self.fields:
            if field.metadata.get('drop', False):
                yield field

    def _undropped(self) -> typing.Generator[dataclasses.Field, None, None]:
        for field in self.fields:
            if not field.metadata.get('drop', False):
                yield field

    def _serialize(self) -> dict:
        state = self.__dict__.copy()
        for field in self._dropped():
            del state[field.name]
        return state

    @classmethod
    def _deserialize(cls: typing.Type[T], data: dict) -> T:
        return cls(**data)

    def __getstate__(self) -> dict:
        return self._serialize()

    def __setstate__(self, state: dict) -> None:
        for field in self._dropped():
            state[field.name] = field.default
        self.__dict__.update(state)


@dataclasses.dataclass
class Detector(Serializable):
    name: str
    src: str
    type: str
    det: typing.Any = dataclasses.field(default=None, metadata={'drop': True})


@dataclasses.dataclass
class Group(Serializable, collections.abc.Mapping):
    name: str
    src: str
    type: str
    data: dict = dataclasses.field(default_factory=dict)

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)


@dataclasses.dataclass
class DataSource(Serializable):
    cfg: dict
    key: int = 0
    run: typing.Any = dataclasses.field(default=None, metadata={'drop': True})
    step: typing.Any = dataclasses.field(default=None, metadata={'drop': True})
    evt: typing.Any = dataclasses.field(default=None, metadata={'drop': True})


PyArrowTypes = {Detector, Group, DataSource}
