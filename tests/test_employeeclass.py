from exercisefunctions import employeeclass
import pytest
import datetime


@pytest.fixture
def emp_1():
    return employeeclass.Employee("James", "Anderson", 50000)



def test_fullname(emp_1):
    assert emp_1.fullname() == "James Anderson"


def test_email(emp_1):
    assert emp_1.email == "James.Anderson@company.com"


def test_apply_raise(emp_1):
    assert emp_1.pay == 50000
    emp_1.apply_raise()
    assert emp_1.pay == 52000


def test_set_raise_amt():
    emp_str_1 = 'Eoin-Morgan-70000'
    emp_str_2 = 'Adil-Rashid-50000'
    emp_str_3 = 'Ben-Stokes-100000'

    new_emp_1 = employeeclass.Employee.from_string(emp_str_1)
    new_emp_2 = employeeclass.Employee.from_string(emp_str_2)
    new_emp_3 = employeeclass.Employee.from_string(emp_str_3)

    assert new_emp_1.email == "Eoin.Morgan@company.com"
    assert new_emp_2.email == "Adil.Rashid@company.com"
    assert new_emp_3.email == "Ben.Stokes@company.com"

    assert new_emp_1.pay == 70000
    assert new_emp_2.pay == 50000
    assert new_emp_3.pay == 100000


def test_isworkday(emp_1):
    mydate1 = datetime.date(2016, 7, 10)
    mydate2 = datetime.date(2016, 7, 11)

    assert emp_1.isworkday(mydate1) == False
    assert emp_1.isworkday(mydate2) == True
