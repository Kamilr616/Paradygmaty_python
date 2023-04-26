def main():
    count = 0
    int(count)
    phrase = input("Wprowadź napis >>")
    for x in phrase:
        if x == 'A' or x == 'a':
            count += 1
    print("Liczba znalezionych znaków to", count)


main()
