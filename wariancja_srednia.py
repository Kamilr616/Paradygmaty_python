def fun(lista):
    x = 0
    y = 0
    for i in lista:
        x = x + i
    srednia = x / len(lista)
    for i in lista:
        y = y + (i - srednia) ** 2
    wariancja = y / (len(lista) - 1)
    return srednia, wariancja


def odp(abc):
    wynik = fun(abc)
    print("Srednia wynosi:", wynik[0], ", wariancja wynosi:", wynik[1])


def main():
    lista = []
    while True:
        wart_tablicy = int(input("Podaj liczbę: "))
        if wart_tablicy == 0:
            break
        else:
            lista.append(wart_tablicy)
    odp(lista)
    odp([3, 3, 3, 3])
    odp([5, 6, 7, 8, 9])


if __name__ == "__main__":
    main()
