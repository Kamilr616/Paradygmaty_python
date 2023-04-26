#poprawione
class Fraction:

    counter = 0

    def __init__(self, *args):
        arg_len = len(args)
        if arg_len == 2:
            self.l1 = args[0]
            self.m = args[1]
        elif arg_len == 1:
            self.l1, self.m = args[0].as_integer_ratio()
        elif arg_len == 0:
            self.l1 = 0
            self.m = 1
        else:
            raise ValueError("Too many arguments")
        Fraction.counter += 1

    def __mul__(self, other):
        return Fraction(self.l1 * other.l1, self.m * other.m)

    def __add__(self, other):
        result = Fraction(self.l1 * other.m + other.l1 * self.m, self.m * other.m)
        result.reduction()
        return result

    def __sub__(self, other):
        result = Fraction(self.l1 * other.m - other.l1 * self.m, self.m * other.m)
        result.reduction()
        return result

    def __str__(self):
        return str(self.l1) + "/" + str(self.m)

    def __del__(self):
        Fraction.counter -= 1

    @staticmethod
    def nww(a, b):
        return a * b // Fraction.nwd(a, b)

    @staticmethod
    def nwd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def reduction(self):
        nwd = Fraction.nwd(self.l1, self.m)
        self.l1 = self.l1 // nwd
        self.m = self.m // nwd


def main():
    a = Fraction(6, 12)
    b = Fraction(5.5)
    c = a + b
    print(c)
    print(b)
    c.reduction()
    print(c)
    print("Counter:", c.counter)


if __name__ == "__main__":
    main()
