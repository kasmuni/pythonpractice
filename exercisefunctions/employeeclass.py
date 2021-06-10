# Code practice from Corey Schafer tutorial series

class Employee:
    #class variables
    num_of_emps = 0
    raise_amount = 1.04

    #constructor method
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    # returns fullname of the employee
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # applies pay raise with amount based on class variable of raise %
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # alternate constructor method
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

    # Creating a static method that tells if date is workday
    # Static methods do not need class instance as input
    @staticmethod
    def isworkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True