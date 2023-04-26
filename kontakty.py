def fun(spis, nazwisko):
    numery = []
    for nazwa in spis:
        if nazwa[1] == nazwisko:
            numery.append(spis[nazwa])
    return numery


def main():
    kontakty = {('Jan', 'Kowalski'): "123456789", ('Adam', 'Nowak'): "987654321", ('Adam', 'Kowalski'): "600300900"}

    print("Numer telefonu Jana Kowalskiego >>", kontakty['Jan', 'Kowalski'])
    print("Numery telefonu Kowalskich >>", fun(kontakty, "Kowalski"))


main()
