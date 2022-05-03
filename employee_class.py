class Employee:

    def __init__(self, first, last, annual_salary):
        self.first = first
        self.last = last
        self.annual_salary = annual_salary

    def give_raise(self, salary_increase):
        if salary_increase:
            self.annual_salary += salary_increase
        else:
            self.annual_salary += 5000
