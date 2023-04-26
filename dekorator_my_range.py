from time import perf_counter


def time_wrapper(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"Czas wykonania funkcji {func.__name__}: {end - start:.6f} sekund")
        return result
    return wrapper


@time_wrapper
def my_range(*args):
    arg_len = len(args)
    if arg_len == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    elif arg_len == 2:
        start = args[0]
        stop = args[1]
        step = 1.0
    elif arg_len == 1:
        start = 0.0
        stop = args[0]
        step = 1.0
    else:
        raise ValueError("Illegal arg count")
    result = []
    while start < stop:
        result.append(start)
        start += step
    return result


def main():
    try:
        print(my_range(1.1, 50, 0.5))
        print(my_range(1.1, 500, 0.1))
        print(my_range(1.1, 4444))
        print(my_range(2.2))
    except ValueError as ve:
        print(ve)


if __name__ == "__main__":
    main()
