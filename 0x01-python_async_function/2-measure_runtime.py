#!/usr/bin/env python3
"""asynchronous function and import modules"""
import asyncio
import time
from typing import List
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    counter = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - counter
    return total_time / n
