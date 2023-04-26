def suma(lista):
    wynik = []
    for krotka in lista:
        wynik.append(krotka[0] + krotka[1])
    return wynik


def main():
    lista1 = [(1, 2), (3, 4), (5, 6), (7, 8)]
    lista2 = [('a', 'b'), ('a', 'c'), ('b', 'c')]
    print(lista1, " -> ", suma(lista1))
    print(lista2, " -> ", suma(lista2))


main()
