#!/usr/bin/env python3
"""definition of async_comprehension"""

import asyncio
import typing
async_g = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """collects a list of integers from a generators and returns them"""
    return [i async for i in async_g()]
