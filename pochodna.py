from math import sin


def kwadrat(z):
    return z ** 2


def derivative(f, x, h=0.0001):
    return (f(x + h) - f(x)) / h


def main():
    a = derivative(sin, 1)
    b = derivative(sin, 0)
    c = derivative(kwadrat, 1, 0.00001)
    print(a, b, c)


if __name__ == "__main__":
    main()
