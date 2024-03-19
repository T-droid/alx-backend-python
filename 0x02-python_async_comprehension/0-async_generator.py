#!/usr/bin/env python3
"""defines the coroutine async_generator"""

import random
import asyncio
import typing


async def async_generator() -> typing.Iterator[float]:  # type: ignore
    """yields a random number after one second"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
