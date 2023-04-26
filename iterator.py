# poprawione
class My_range:

    def __init__(self, *args):

        arg_len = len(args)
        if arg_len == 3:
            if args[2] == 0.0:
                raise ValueError("Error: Step = 0")
            else:
                self.step = args[2]
            self.start = args[0]
            self.stop = args[1]
        elif arg_len == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1.0
        elif arg_len == 1:
            self.start = 0.0
            self.stop = args[0]
            self.step = 1.0
        else:
            raise ValueError("Error: Too many arguments")

    def __iter__(self):

        if self.step < 0.0:
            self.n = self.stop
        else:
            self.n = self.start
        return self

    def __next__(self):

        if self.n > self.start and self.step < 0.0:
            result = self.n
            self.n += self.step
            return result

        elif self.n < self.stop and self.step > 0.0:
            result = self.n
            self.n += self.step
            return result
        else:
            raise StopIteration


def main():

    try:
        for x in My_range(1.1, 3, 0.0):
            print(x)
    except ValueError as ve:
        print(ve)
    try:
        for x in My_range(1.1, 3, 0.1, 2):
            print(x)
    except ValueError as ve:
        print(ve)
    try:
        for x in My_range(1.1, 2, -0.1):
            print(x)
    except ValueError as ve:
        print(ve)
    try:
        for x in My_range(1.1, 2, 0.1):
            print(x)
    except ValueError as ve:
        print(ve)


if __name__ == "__main__":
    main()
