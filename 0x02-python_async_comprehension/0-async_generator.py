#!/usr/bin/env python3
"""
A python module to loop 10 times
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async_generator function to loop 10 times
    Args:
        No arguments
    Returns:
        No return value
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
