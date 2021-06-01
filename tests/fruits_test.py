import pytest
from exercisefunctions import fruits

# The unit tests
@pytest.fixture
def setup():
    return fruits.fruit("Apple","Green","Large")

def test_get_fruit_name(setup):
    assert setup.get_fruit_name() == "Apple"


