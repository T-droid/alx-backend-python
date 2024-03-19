#!/usr/bin/env python3
"""module to define measure_runtime"""

import asyncio
import time
async_c = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures the runtime of running async_comprehension"""
    t1 = time.time()
    batch = await asyncio.gather(async_c(), async_c(), async_c(), async_c())
    t2 = time.time()
    return t2 - t1
