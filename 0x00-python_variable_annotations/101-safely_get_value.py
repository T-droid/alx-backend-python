#!/usr/bin/python3
"""module to define safely_get_value"""
import typing

def safely_get_value(dct: typing.Dict[typing.Any, typing.Any], key: typing.Any, default: typing.Union[typing.Any, None] = None) -> typing.Union[typing.Any, typing.Any]:
    """checks if a key is in dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default