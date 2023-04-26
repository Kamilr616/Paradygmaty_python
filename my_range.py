def my_range(*args):
    arg_len = len(args)
    if arg_len == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
        if step == 0.0:
            raise ValueError("Step == 0")
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

    if step < 0.0:
        while stop > start:
            result.append(stop)
            stop += step
    else:
        while start < stop:
            result.append(start)
            start += step
    return result


def main():
    try:
        print(my_range(1.1, 2.1, 0.5, 1))
    except ValueError as ve:
        print(ve)
    try:
        print(my_range(1.1, 2, 0.0))
    except ValueError as ve:
        print(ve)
    try:
        print(my_range(1.1, 4, 0.5))
    except ValueError as ve:
        print(ve)
    try:
        print(my_range(1.1, 2.2, -0.5))
    except ValueError as ve:
        print(ve)


if __name__ == "__main__":
    main()
