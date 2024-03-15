#!/usr/bin/env python3
"""module to define element_length"""
import typing

def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.Tuple[typing.Sequence]:
    """return length of lst"""
    return [(i, len(i)) for i in lst]