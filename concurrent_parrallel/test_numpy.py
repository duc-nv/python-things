import numpy as np
import time


def execution_time(func):
    def inner(*arg, **kwargs):
        tik = time.perf_counter()
        return_values = func(*arg, **kwargs)
        time_taken = time.perf_counter() - tik
        print(func.__name__, '. Time taken: ', time_taken)
        return return_values
    return inner


@execution_time
def test_numpy():
    x = np.random.rand(1000, 1000)
    y = np.random.rand(1000, 1000)
    for _ in range(10):
        np.matmul(x, y)

print(np.show_config())
test_numpy()
