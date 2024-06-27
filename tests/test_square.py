from src.square import Square
import pytest


@pytest.mark.parametrize(
    ("side_a", "area"),
    [
        (7, 49),
        (7.3, 53.29)
    ],
    ids=["integer", "float"]
)
def test_square_get_area_positive(side_a, area):
    sq = Square(side_a)
    assert sq.get_area == area


@pytest.mark.parametrize(
    ("side_a", "perimeter"),
    [
        (7, 28),
        (7.3, 29.2)
    ],
    ids=["integer", "float"]
)
def test_square_get_perimeter_positive(side_a, perimeter):
    sq = Square(side_a)
    assert sq.get_perimeter == perimeter
