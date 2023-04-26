def fun(od, do):
    return [x for x in range(od, do+1) if x % 4 == 0 and x % 100 != 0 or x % 400 == 0]


def main():
    print("Lata przestępne >>", fun(1900, 2000))


main()
