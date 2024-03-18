#!/usr/bin/python3
"""module to define a function that uses the function wait_random
and compiles a list of delay times in ascending order"""
import random
import asyncio
wait_r = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """uses wait_rondom to compile a list af delay times"""
    myList = [await wait_r(max_delay) for i in range(n)]
    return myList
