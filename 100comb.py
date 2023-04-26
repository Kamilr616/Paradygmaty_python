#gotowe
def main():
    comb = 0
    int(comb)
    for ten in range(11):
        for five in range(21):
            for two in range(51):
                if two * 2 + five * 5 + ten * 10 == 100:
                    comb += 1
    print("Liczba kombinacji wynosi:", comb)


main()
