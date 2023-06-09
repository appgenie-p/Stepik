"""Timer decorator for async functions."""

import functools
import time
from typing import Callable


def timer_async(func: Callable):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        print(f"<Асинхронная func<{func.__name__}> СТАРТ>")
        result = await func(*args, **kwargs)
        end: float = time.perf_counter()
        diff = end - start
        print(f"<Асинхронная func<{func.__name__}> СТОП: {diff:0.2f} sec>")
        return result

    return wrapper


def timer_sync(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        print(f"<Синхронная func<{func.__name__}> СТАРТ>")
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        diff = end_time - start_time
        print(f"<Синхронная func<{func.__name__}> СТОП: {diff:0.2f} sec>")
        return result

    return wrapper
