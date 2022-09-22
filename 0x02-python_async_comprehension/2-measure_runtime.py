#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension



async def measure_runtime() -> float:
    counter = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    j = time.time()
    return j - counter

