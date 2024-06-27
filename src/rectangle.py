from src.figure import Figure
from typing import Union


class Rectangle(Figure):

    def __init__(self, side_a: Union[int, float], side_b: Union[int, float]):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Длина стороны должна быть больше 0")
        self.side_a = side_a
        self.__side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.__side_b

    @property
    def get_perimeter(self):
        return (self.side_a + self.__side_b) * 2
