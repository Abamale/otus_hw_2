from src.triangle import Triangle
import pytest


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "area"),
    [
        (3, 5, 7, 6.49519052838329),
        (3.5, 5.6, 7.7, 8.98184836211345)
    ],
    ids=["integer", "float"]
)
def test_triangle_get_area_positive(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_area == area


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "perimeter"),
    [
        (3, 5, 7, 15),
        (3.5, 5.6, 7.7, 16.8)
    ],
    ids=["integer", "float"]
)
def test_triangle_get_perimeter_positive(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimeter == perimeter


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [
        (0, 5, 7),
        (5.5, -1, 3),
        (1, 2, 3)
    ],
    ids=["zero value", "negative value", "not a triangle"]
)
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)
