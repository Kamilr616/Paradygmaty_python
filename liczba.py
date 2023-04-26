#gotowe
def fun(liczba):
    slownik = {
        "dwadzieścia": "2",
        "trzydzieści": "3",
        "czterdzieści": "4",
        "pięćdziesiąt": "5",
        "jeden": "1",
        "dwa": "2",
        "trzy": "3",
        "cztery": "4",
        "pięć": "5",
        "sześć": "6",
        "siedem": "7",
        "osiem": "8",
        "dziewięć": "9", }

    cyfry = liczba.split(' ')
    length = len(cyfry)

    if cyfry[0] not in slownik:
        return "Nieprawidłowe dane"
    wynik = slownik[cyfry[0]]
    if length == 2:
        if cyfry[1] not in slownik:
            return "Nieprawidłowe dane"
        wynik += slownik[cyfry[1]]
    elif length == 1:
        wynik += "0"
    else:
        return "Nieprawidłowe dane"
    return int(wynik)


def main():
    print("Dwadzieścia jeden =", fun("dwadzieścia jeden"))
    print("czterdzieści 1 =", fun("czterdzieści 1"))
    print("test =", fun("test"))
    print("czterdzieści pięć dwa =", fun("czterdzieści pięć dwa"))


main()
