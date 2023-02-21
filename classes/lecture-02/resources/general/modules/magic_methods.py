# Тут все есть https://habr.com/ru/post/186608/
import copy


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x) -> None:
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y) -> None:
        self._y = new_y

    # def __repr__(self):
    #     return f'Point repr: x = {self.x}; y = {self.y}\n'
    #
    # def __str__(self):
    #     return f'Point str: x = {self.x}; y = {self.y}\n'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __deepcopy__(self, memodict={}):
        return Point(self.x, self.y)


class PointSet:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2


def example():
    # p1 = Point(1, 2)
    # p2 = Point(10, 20)
    #
    # p3 = p1 + p2
    # print(f'add: {p1} + {p2} = {p3}')
    #
    # print(f'not equals: p1 != p2 -> {p1 != p2}')
    #
    # p4 = copy.deepcopy(p3)
    # print(f'equals: p3 == p4 -> {p3 == p4}')
    #
    # print(repr(p1))
    # print(str(p4))
    #
    # ex = PointSet(p1, p4)

    # print(ex.__dict__)

    Class = type('NewClass', (), {
        'a': 1,
        'b': 2,
    })

    r = Class()

    print(r.a)