#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function task_wait_n"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_n"""
    wList = []
    for i in range(n):
        wList.append(await task_wait_random(max_delay))
    return sorted(wList)
    