# GOTOWE
def fun(lst, length, suma=0):
    if not lst:
        return suma / length, 0
    mean, dev = fun(lst[1:], length, suma + lst[0])
    dev += ((lst[0] - mean) ** 2) / length

    return mean, dev


def main():
    lst1 = [3, 3, 3, 3]
    lst2 = [5, 6, 7, 8, 9]
    print(fun(lst1, len(lst1)))
    print(fun(lst2, len(lst2)))


if __name__ == "__main__":
    main()
