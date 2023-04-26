def napis(cyfry):
    slownik = {
        '0': 'zero',
        '1': 'jeden',
        '2': 'dwa',
        '3': 'trzy',
        '4': 'cztery',
        '5': 'pięć',
        '6': 'sześć',
        '7': 'siedem',
        '8': 'osiem',
        '9': 'dziewięć',
    }
    slownie = ""
    for cyfra in cyfry:
        if cyfra in slownik:
            slownie += slownik[cyfra] + " "
    return slownie


def main():
    print(napis(input("Wprowadź liczbę >>")))


main()
