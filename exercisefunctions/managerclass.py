from exercisefunctions import employeeclass


class Manager(employeeclass.Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def get_emps(self):
        emplist = []
        for emp in self.employees:
            emplist.append(emp.fullname())

        return emplist

