#!/usr/bin/env python3
"""module to define sum_list funct"""
import typing

def sum_list(input_list: typing.List[float]) -> float:
    """adds all values in a list"""
    sum = 0
    for num in input_list:
        sum += num
    return sum