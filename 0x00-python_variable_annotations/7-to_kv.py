#!/usr/bin/env python3
"""module to define to_kv func"""
import typing

def to_kv(k: str, v: typing.List[typing.Union[int, float]]) -> typing.Tuple[str, float]:
    """returns a tuple of string and int/float"""
    return (k,v)