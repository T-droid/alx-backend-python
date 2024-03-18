#!/usr/bin/env python3
"""definition of measure time"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for function wait_n"""

    start_time = time.time()
    asyncio.gather(wait_n(n, max_delay))
    stop_time = time.time()

    elapsed_time = stop_time - start_time
    return elapsed_time / n
