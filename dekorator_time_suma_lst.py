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
def list_sum(lst):
    if not lst:
        return 0
    return list_sum(lst[1:]) + lst[0]


@time_wrapper
def list_sum_tail(lst, suma=0):
    if not lst:
        return suma
    return list_sum_tail(lst[1:], lst[0] + suma)

@time_wrapper
def list_sum_iter(lst):
    suma = 0
    for x in lst:
        suma += x
    return suma


def main():
    lst1 = [1, 2, 3, 4]
    lst2 = []

    print("Rekurencja")
    print(list_sum(lst1))
    print(list_sum(lst2))

    print("Rekurencja ogonowa")
    print(list_sum_tail(lst1))
    print(list_sum_tail(lst2))

    print("Iteracja")
    print(list_sum_iter(lst1))
    print(list_sum_iter(lst2))


if __name__ == "__main__":
    main()


