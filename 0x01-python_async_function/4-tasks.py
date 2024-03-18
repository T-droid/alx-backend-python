#!/usr/bin/env python3
"""module to define a function that uses the function wait_random
and compiles a list of delay times in ascending order"""
import typing
wait_r = __import__('0-basic_async_syntax').wait_random
task_wait_r = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """uses wait_rondom to compile a list af delay times"""
    myList = []
    for i in range(n):
        task = task_wait_r(await wait_r(max_delay))
        result = await task
        myList.append(result)

    return myList
