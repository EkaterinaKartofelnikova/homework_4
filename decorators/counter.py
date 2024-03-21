def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    """
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Функция была вызвана {count} раз(а)')
        return func(*args, **kwargs)

    return wrapper
