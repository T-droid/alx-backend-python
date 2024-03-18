#!/usr/bin/env python3
"""module to define task_wait_random"""
import asyncio
import typing
wait_r = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> typing.Any:
    """creates and returns a asyncio.Task"""
    task = asyncio.create_task(wait_r(max_delay))
    return task
