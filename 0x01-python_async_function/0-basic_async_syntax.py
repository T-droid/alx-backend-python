#!/usr/bin/env python3
"""asynchromous coroutine that waits for a random delay"""
import random
import asyncio

async def wait_random(max_delay=10):
    """function uses random module to wait for a random delay
    and returns it"""
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time