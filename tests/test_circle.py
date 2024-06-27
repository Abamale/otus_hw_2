from src.circle import Circle
import pytest


@pytest.mark.parametrize(
    ("radius", "area"),
    [
        (3, 28.274333882308138),
        (3.5, 38.48451000647496)
    ],
    ids=["integer", "float"]
)
def test_circle_get_area_positive(radius, area):
    c = Circle(radius)
    assert c.get_area == area


@pytest.mark.parametrize(
    ("radius", "perimeter"),
    [
        (3, 18.84955592153876),
        (3.5, 21.991148575128552)
    ],
    ids=["integer", "float"]
)
def test_circle_get_perimeter_positive(radius, perimeter):
    c = Circle(radius)
    assert c.get_perimeter == perimeter


@pytest.mark.parametrize(
    ("radius"),
    [
        (0),
        (-1)
    ],
    ids=["zero value", "negative value"]
)
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)
