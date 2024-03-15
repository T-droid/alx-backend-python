#!/usr/bin/env python3
"""module too define aum_mixed_list"""
import typing

def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """adds all elements of the list and return the sum as a float"""
    sum = 0
    for num in mxd_lst:
        sum += num
    return sum