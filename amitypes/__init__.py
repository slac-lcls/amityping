import sys
import abc
import importlib
from mypy_extensions import _TypedDictMeta

from amitypes.array import ArrayMeta
from amitypes.array import *    # noqa ignore=F405
from amitypes.hsd import *      # noqa ignore=F405
from amitypes.source import *   # noqa ignore=F405


__version__ = '1.1.0'


def dumps(cls):
    if type(cls) in [type, abc.ABCMeta]:
        if cls.__module__ in ['builtins', '__main__']:
            return cls.__name__
        else:
            return "%s.%s" % (cls.__module__, cls.__name__)
    elif issubclass(type(cls), _TypedDictMeta):
        return "TypedDict('%s', %s)" % (cls.__name__, {k: dumps(v) for k, v in cls.__annotations__.items()})
    elif issubclass(type(cls), ArrayMeta):
        return "%s.%s" % (cls.__module__, cls.__name__)
    else:
        return str(cls)


def loads(type_str):
    parts = type_str.split('.')
    if len(parts) > 1 and parts[0] != __name__:
        try:
            mod = importlib.import_module(parts[0])
            setattr(sys.modules[__name__], mod.__name__, mod)
        except ModuleNotFoundError:
            pass

    cls = eval(type_str.replace('amitypes.', ''))

    if issubclass(type(cls), _TypedDictMeta):
        setattr(sys.modules[__name__], cls.__name__, cls)

    return cls
