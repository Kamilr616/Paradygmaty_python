# gotowe
from functools import reduce


def mean(lst):
    return reduce(lambda x, y: x + y, lst)/len(lst)


def largest_el(lst):
    return reduce(lambda x, y: x if x > y else y, lst)


def splaszcz(lst):
    return list(reduce(lambda x, y: x + y, lst))


def manhattan(lst1, lst2):
    return reduce(lambda x, y: x + abs(y[0] - y[1]), zip(lst1, lst2), 0)


def wspolne_litery(lst1):
    return list(reduce(lambda x, y: x & y, map(set, lst1)))


def list_add(lst1, el):
    return reduce(lambda x, y: x + [el, y] if y >= el and el not in x else x + [y], lst1, [])


def main():
    lst1 = [1, 2, 3, 4, 5, 6]
    lst2 = [[1, 2, 3], [5], [8, 9]]
    lst3 = ['Ala', 'ma', 'kota']
    lst4 = ['mama', 'ma', 'misia']
    lst5 = [5, 4, 8, 2, 1, 6]
    el = 4
    print(splaszcz(lst2))
    print(mean(lst1))
    print(largest_el(lst1))
    print(manhattan(lst1, lst5))
    print(wspolne_litery(lst3))
    print(wspolne_litery(lst4))
    print(list_add(lst1, el))


if __name__ == '__main__':
    main()
