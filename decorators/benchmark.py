import time


def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло выполнение декорируемой функции
    """

    def wrapper(*args, **kwargs):
        time_in = time.time()
        ans = func(*args, **kwargs)
        time_out = time.time()
        print(f'Время выполнения функции {func.__name__}: {time_out - time_in}')
        return ans

    return wrapper
