#gotowe
def fun(liczba):
    dziesiatki = {
        "dwadzieścia": 20,
        "trzydzieści": 30,
        "czterdzieści": 40,
        "pięćdziesiąt": 50,
    }
    jednosci = {
        "zero": 0,
        "jeden": 1,
        "dwa": 2,
        "trzy": 3,
        "cztery": 4,
        "pięć": 5,
        "sześć": 6,
        "siedem": 7,
        "osiem": 8,
        "dziewięć": 9,
    }

    cyfry = liczba.split()
    if len(cyfry) == 1:
        return dziesiatki.get(cyfry[0], jednosci.get(cyfry[0], "Nieprawidłowe dane"))
    if len(cyfry) == 2 and cyfry[0] in dziesiatki and cyfry[1] in jednosci:
        return dziesiatki[cyfry[0]] + jednosci[cyfry[1]]
    return "Nieprawidłowe dane"


def main():
    print("Dwadzieścia jeden =", fun("dwadzieścia jeden"))
    print("czterdzieści 1 =", fun("czterdzieści 1"))
    print("test =", fun("test"))
    print("czterdzieści pięć dwa =", fun("czterdzieści pięć dwa"))


if __name__ == "__main__":
    main()
