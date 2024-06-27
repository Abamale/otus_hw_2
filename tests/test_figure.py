from src.figure import Figure
import pytest


def test_add_area_positive(figure_triangle, figure_square):
    assert figure_triangle.get_area + figure_square.get_area == figure_triangle.add_area(figure_square)


def test_add_area_negative(figure_triangle):
    with pytest.raises(ValueError):
        figure_triangle.add_area(1)
