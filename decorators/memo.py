def memo(func):
    """
  Декоратор, запоминающий результаты исполнения функции func, чьи аргументы args должны быть хешируемыми
  """
    cache = {}

    def fmemo(arg):
        if arg not in cache:
            cache[arg] = func(arg)
        return cache[arg]

    return fmemo
