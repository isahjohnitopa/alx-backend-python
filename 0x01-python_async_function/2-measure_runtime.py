#!/usr/bin/env python3
"""
Contains a method that measure the total execution time of a function
"""
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total time of a function
    Args:
        n: The number of coroutines to lunch
        max_delay: The maimum amout of time to wait for each coroutine
    Return:
        Elapsed time in seconds
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n
