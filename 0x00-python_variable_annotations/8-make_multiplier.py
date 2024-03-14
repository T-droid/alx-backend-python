#!/usr/bin/python3
"""module to define make_multiplier funct"""
import typing

def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """returns a function that multiplies the multiplier"""
    def fun(num: float) -> float:
        """multiplies multiplier with a float"""
        return num * multiplier
    return fun