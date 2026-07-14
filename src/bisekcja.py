from math import sin


def wielomian(x):
    return x ** 3 - 2 * x ** 2 + 4 * x - 1


def bisekcja(f, x1, x2, eps=0.001):
    fx1 = f(x1)
    fx2 = f(x2)
    if fx1 * fx2 > 0:
        return "Błąd: Funkcja nie ma różnych znaków na krańcach przedziału"
    while True:
        x0 = (x1 + x2) / 2
        if abs(x1 - x0) < eps:
            break
        fx = f(x0)
        if abs(fx) == 0:
            break
        if fx * fx1 < 0:
            x2 = x0
        else:
            x1 = x0
            fx1 = fx
    return x0


def main():
    print("Bisekcja sinusa >>", bisekcja(sin, -1.5, 1))
    print("Bisekcja wielomianu >>", bisekcja(wielomian, -10, 10, 0.001))


if __name__ == "__main__":
    main()
