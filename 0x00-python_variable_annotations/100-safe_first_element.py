#!/usr/bin/env python3
"""module to define safe_first_element func"""
import typing

def safe_first_element(lst: typing.Iterable[typing.Any]) -> typing.Union[typing.Any, None]:
    if lst:
        return lst[0]
    else:
        return None