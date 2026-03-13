import time
from typing import Callable

def trace_execution(func: Callable):
    """Decorator for tracing agent execution time and outcomes."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start_time
        print(f"[Trace] Executed {func.__name__} in {duration:.4f}s")
        return result
    return wrapper
