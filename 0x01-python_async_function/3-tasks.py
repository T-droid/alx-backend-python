#!/usr/bin/python3
"""module to define task_wait_random"""
import asyncio
wait_r = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    """returns a asyncio.Task"""
    task = asyncio.create_task(wait_r(max_delay))
    return task