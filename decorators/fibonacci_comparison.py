import time
from memo import memo


def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


# измерение времени выполнения без декоратора
time_in = time.time()
fib(30)
time_out = time.time()
print(f'Время выполнения функции: {time_out - time_in}')

fib = memo(fib)

# измерение времени выполнения с декоратором
time_in = time.time()
fib(30)
time_out = time.time()
print(f'Время выполнения функции: {time_out - time_in}')
