import pytest
from src.triangle import Triangle
from src.rectangle import Rectangle
from src.circle import Circle
from src.square import Square
from src.figure import Figure


@pytest.fixture
def figure_circle():
    return Circle(3)


@pytest.fixture
def figure_triangle():
    return Triangle(3, 5, 7)


@pytest.fixture
def figure_rectangle():
    return Rectangle(3, 5)


@pytest.fixture
def figure_square():
    return Square(5)
