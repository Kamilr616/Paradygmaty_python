# gotowe
from abc import ABC, abstractmethod
from math import pi, sqrt


class Shape(ABC):

    def __init__(self, _name):
        self.__name = _name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):

    def __init__(self, _name, _radius):
        super().__init__(_name)
        self._radius = _radius

    def get_area(self):
        return pi * self._radius ** 2


class Triangle(Shape):

    def __init__(self, _name, _side_a, _side_b, _side_c):
        super().__init__(_name)
        self._side_a = _side_a
        self._side_b = _side_b
        self._side_c = _side_c

    def get_area(self):
        _p = (self._side_a + self._side_b + self._side_c) / 2
        return sqrt((_p * (_p - self._side_a) * (_p - self._side_b) * (_p - self._side_c)))


class Rectangle(Shape):

    def __init__(self, _name, _side_a, _side_b):
        super().__init__(_name)
        self._side_a = _side_a
        self._side_b = _side_b

    def get_area(self):
        return self._side_a * self._side_b


class Square(Rectangle):

    def __init__(self, _name, _side_a):
        super().__init__(_name, _side_a, _side_a)


class Eq_triangle(Triangle):

    def __init__(self, _name, _side_a):
        super().__init__(_name, _side_a, _side_a, _side_a)


def main():

    for x in [Circle("Koło", 5), Triangle("Trójkąt", 3, 4, 6), Rectangle("Prostokąt", 5, 4), Square("Kwadrat", 6),
              Eq_triangle("Trójkąt równoboczny", 7)]:
        print(x.name, x.get_area())


if __name__ == "__main__":
    main()
