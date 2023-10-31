import sys
import json
import numpy
import typing
import inspect
import importlib

from amitypes.array import NumPyTypeDict
from amitypes.array import *    # noqa ignore=F405
from amitypes.hsd import *      # noqa ignore=F405
from amitypes.waveform import * # noqa ignore=F405
from amitypes.source import *   # noqa ignore=F405
from amitypes.scan import *     # noqa ignore=F405


__version__ = '1.2.1'


def dumps(cls):
    if inspect.isclass(cls):
        if isinstance(cls, typing.GenericAlias):
            return str(cls)
        elif cls.__module__ in ['builtins']:
            return cls.__name__
        else:
            return "%s.%s" % (cls.__module__, cls.__name__)
    elif isinstance(cls, typing.TypeVar):
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

    return cls


class TypeDumper(object):

    def __init__(self, ttype):
        self.ttype = ttype

    def __repr__(self):
        return dumps(self.ttype)


class TypeEncoder(json.JSONEncoder):

    def default(self, obj):
        nptopy = NumPyTypeDict.get(type(obj))
        if nptopy is not None:
            return nptopy(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        elif inspect.isclass(obj):
            if isinstance(obj, typing.GenericAlias):
                return str(obj)
            elif obj.__module__ in ['builtins']:
                return obj.__name__
            else:
                return "%s.%s" % (obj.__module__, obj.__name__)
        elif isinstance(obj, typing.TypeVar):
            return "%s.%s" % (obj.__module__, obj.__name__)
        elif isinstance(obj, (typing._GenericAlias, typing._SpecialForm)):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


T = typing.TypeVar('T')
