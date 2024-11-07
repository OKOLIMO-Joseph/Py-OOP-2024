class Employee:
    rate = 250000
    def __init__(self, name, salary, overtime):
        self.name = name
        self.salary = salary
        self.overtime = overtime

    def my_salary(self):
        emp_salary = self.salary + (Employee.rate * self.overtime)
        print(f'{self.name} earns:  {emp_salary}')

emp1 = Employee('Joseph', 2000000, 20)
emp2 = Employee('Harold', 3500000, 45)
emp1.my_salary()
emp2.my_salary()


# OR
#     def my_salary(self):
#         return self.salary + (self.overtime*Employee.rate)

# john = Employee('John', 4500000, 10)
# print(f'John earns Shs. {john.my_salary()}')
