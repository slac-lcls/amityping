import typing
import dataclasses


__all__ = [
    'Detector',
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

    def _serialize(self) -> typing.Dict:
        state = self.__dict__.copy()
        for field in self._dropped():
            del state[field.name]
        return state

    @classmethod
    def _deserialize(cls: typing.Type[T], data: typing.Dict) -> T:
        return cls(**data)

    def __getstate__(self) -> typing.Dict:
        return self._serialize()

    def __setstate__(self, state: typing.Dict) -> None:
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
class DataSource(Serializable):
    cfg: typing.Dict
    key: int = 0
    run: typing.Any = dataclasses.field(default=None, metadata={'drop': True})
    evt: typing.Any = dataclasses.field(default=None, metadata={'drop': True})


PyArrowTypes = {Detector, DataSource}