def main():
    count = 0
    int(count)
    phrase = input("Wprowadź napis >>")
    for count, x in enumerate(phrase):
        if x == 'A' or x == 'a':
            print("Index to:", count, "Znak to:", x)


main()
