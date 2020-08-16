

# 1
# """
# 容器序列：list, tuple, dict, collections.deque
# 扁平序列：str

# 可变序列：list，dict，collections.deque
# 不可变序列：tuple, str
# """

# 2
def my_map(func, *iterables):
    if hasattr(iterables, '__iter__'):
        for i in iterables:
            yield func(i)
    else:
        raise TypeError(
            f"'{iterables.__class__.__name__}' object is not iterable")



# 3
from functools import wraps
import time


def timer(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start_time)
        return res
    return decorator


@timer
def test(second):
    time.sleep(second)


test(3)
