def main():
    n = 0
    while (n != 7):
        n = int(input("Podaj wysokość choinki: "))
        for i in range(n + 1):
            space = " " * (n - i)
            print(space, end="")
            if n % 2 == 0:
                char = "*" * (i * 2 - 1)
            else:
                char = "#" * (i * 2 - 1)
            print(char)
        print("")


main()
