from src.figure import Figure
from typing import Union


class Triangle(Figure):

    def __init__(self, side_a: Union[int, float], side_b: Union[int, float], side_c: Union[int, float]):
        if (side_a + side_b) <= side_c and (side_a + side_c) <= side_b and (side_b + side_c) <= side_a:
            raise ValueError("Это не треугольник")
        elif side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Длина стороны должна быть больше 0")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def get_area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

