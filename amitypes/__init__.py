import sys
import json
# import numpy
import typing
import inspect
import importlib

# from amitypes.array import NumPyTypeDict
from amitypes.array import *    # noqa ignore=F405
from amitypes.hsd import *      # noqa ignore=F405
from amitypes.waveform import * # noqa ignore=F405
from amitypes.source import *   # noqa ignore=F405


__version__ = '1.1.8'


def dumps(cls):
    if inspect.isclass(cls):
        if cls.__module__ in ['builtins']:
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


class TypeEncoder(json.JSONEncoder):

    def default(self, obj):
        # nptopy = NumPyTypeDict.get(type(obj))
        # if nptopy is not None:
        #     return nptopy(obj)
        # elif isinstance(obj, numpy.ndarray):
        #     return obj.tolist()
        if inspect.isclass(obj):
            if obj.__module__ in ['builtins']:
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
