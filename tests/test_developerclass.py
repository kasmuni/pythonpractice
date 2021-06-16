from exercisefunctions import developerclass
import pytest


@pytest.fixture()
def dev():
    return developerclass.Developer("Ian", "Botham", 60000, "Java")


def test_devfullname(dev):
    assert dev.fullname() == "Ian Botham"

def test_devemail(dev):
    assert dev.email == "Ian.Botham@company.com"


def test_devapply_raise(dev):
    assert dev.pay == 60000
    dev.apply_raise()
    assert dev.pay == 66000

def test_prog_lang(dev):
    assert dev.prog_lang == "Java"
