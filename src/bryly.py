from figury import *


class Shape_mixin:

    def get_area(self):
        return sum([_wall.get_area() for _wall in self._walls])

    def get_walls(self):
        return self._walls


class Tetrahedron(Shape_mixin, Shape):

    def __init__(self, _name, _x):
        super().__init__(_name)
        self._walls = [Eq_triangle(_name + "_wall_" + str(_i), _x) for _i in range(1, 5)]


class Pyramid(Shape_mixin, Shape):

    def __init__(self, _name, _x):
        super().__init__(_name)
        self._walls = []
        for _i in range(1, 5):
            self._walls.append(Eq_triangle(_name + "_wall_" + str(_i), _x))
        self._walls.append(Square(_name + "_base", _x))


class Cube(Shape_mixin, Shape):

    def __init__(self, _name, _x):
        super().__init__(_name)
        self._walls = [Square(_name + "_wall_" + str(_i), _x) for _i in range(1, 7)]


def main():
    for x in [Tetrahedron("Czworościan", 5), Pyramid("Piramida", 6), Cube("Sześcian", 7)]:
        print(x.name, x.get_area())
        for y in x.get_walls():
            print(y.name, y.get_area())


if __name__ == "__main__":
    main()
