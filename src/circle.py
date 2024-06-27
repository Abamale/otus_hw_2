from src.figure import Figure
from typing import Union
from math import pi


class Circle(Figure):
    def __init__(self, radius: Union[int, float]):
        if radius <= 0:
            raise ValueError("Радиус должен быть больше 0")
        self.radius = radius

    @property
    def get_area(self):
        return pi * self.radius * self.radius

    @property
    def get_perimeter(self):
        return 2 * pi * self.radius
