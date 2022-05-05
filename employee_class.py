class Employee:

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, salary_increase=5000):
        self.salary += salary_increase