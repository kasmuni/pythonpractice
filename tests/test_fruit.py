import pytest
from exercisefunctions import fruits

# The unit tests
@pytest.fixture
def apple():
    return fruits.fruit("Apple","Green","Large")

def test_get_fruit_name(apple):
    assert apple.get_fruit_name() == "Apple"

def test_get_fruit_color(apple):
    assert apple.get_fruit_color() == "Green"

def test_get_fruit_size(apple):
    assert apple.get_fruit_size() == "Large"

def test_bite_percentage(apple):
    apple.bite()
    assert apple.get_balance() == 90
