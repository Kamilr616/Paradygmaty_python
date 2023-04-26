def main():
    xRange = int(input("Podaj do jakiej liczby wypisać liczby pierwsze >>"))
    for x in range(xRange + 1):
        if x == 0 or x == 1:
            continue
        for y in range(x):
            if y == 0 or y == 1:
                continue
            if x % y == 0:
                break
        else:
            print(x)


main()
