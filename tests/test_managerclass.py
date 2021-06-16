from exercisefunctions import managerclass
from exercisefunctions import developerclass
import pytest

@pytest.fixture()
def man():
    dev1 = developerclass.Developer("John", "McEnroe", 50000, "Python")
    return managerclass.Manager("Alec", "Stewart", 90000, [dev1])

@pytest.fixture()
def man2():
    dev1 = developerclass.Developer("John", "McEnroe", 50000, "Python")
    return managerclass.Manager("Alec", "Stewart", 90000, [dev1]),dev1

def test_manfullname(man):
    assert man.fullname() == "Alec Stewart"

def test_manpay_raise(man):
    assert man.pay == 90000
    man.apply_raise()
    assert man.pay == 93600

def test_manemail(man):
    assert man.email == "Alec.Stewart@company.com"

def test_get_emps(man):
    assert man.get_emps() == ["John McEnroe"]


def test_add_emp(man):
    dev_2 = developerclass.Developer("Jim", "Courrier", 40000, "Java")
    man.add_emp(dev_2)
    assert man.get_emps() == ["John McEnroe", "Jim Courrier"]


def test_remove_emp(man2):
    assert man2[0].get_emps() == ["John McEnroe"]
    man2[0].remove_emp(man2[1])
    assert man2[0].get_emps() == []