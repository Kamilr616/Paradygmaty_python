def wspolne(z1, z2):
    return list(set([a for a in z1 if a in z2]))


def main():
    lst1 = [3, 3, 3, 3]
    lst2 = [5, 6, 7, 3, 9]
    print("Lista >>", wspolne(lst1, lst2))

    tup1 = (3, 3, 4, 5)
    tup2 = (3, 3, 2, 5)
    print("Krotka >>", wspolne(tup1, tup2))

    txt1 = "Ala ma kota"
    txt2 = "Ala ma psa"
    print("Tekst >>", wspolne(txt1, txt2))


if __name__ == "__main__":
    main()
