def list_sum(lst):
    if not lst:
        return 0
    return list_sum(lst[1:]) + lst[0]


def list_sum_tail(lst, suma=0):
    if not lst:
        return suma
    return list_sum_tail(lst[1:], lst[0] + suma)


def main():
    lst1 = [1, 2, 3, 4]
    lst2 = []
    print(list_sum(lst1))
    print(list_sum(lst2))

    print(list_sum_tail(lst1))
    print(list_sum_tail(lst2))


if __name__ == "__main__":
    main()
