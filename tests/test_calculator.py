import pytest
from exercisefunctions import calculator


# The unit tests
@pytest.fixture
def calsetup():
    return calculator.calculator()


def test_add(calsetup):
    assert calsetup.add(14,5) == 19


def test_subtract(calsetup):
    assert calsetup.subtract(14,5) == 9


def test_divide(calsetup):
    assert calsetup.divide(14,5) == 2.8


def test_multiply(calsetup):
    assert calsetup.multiply(14,5) == 70
