from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    ("side_a", "side_b", "area"),
    [
        (7, 3, 21),
        (7.3, 3.4, 24.82)
    ],
    ids=["integer", "float"]
)
def test_rectangle_get_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area == area


@pytest.mark.parametrize(
    ("side_a", "side_b", "perimeter"),
    [
        (7, 3, 20),
        (7.3, 3.4, 21.4)
    ],
    ids=["integer", "float"]
)
def test_rectangle_get_perimeter_positive(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.get_perimeter == perimeter


@pytest.mark.parametrize(
    ("side_a", "side_b"),
    [
        (0, 5),
        (5.5, -1)
    ],
    ids=["zero value", "negative value"]
)
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
