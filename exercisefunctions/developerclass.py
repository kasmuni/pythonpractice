# Corey Schafer OOP Tutorials
from exercisefunctions import employeeclass


class Developer(employeeclass.Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
