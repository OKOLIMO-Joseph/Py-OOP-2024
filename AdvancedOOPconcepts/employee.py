class Employee:
    def __init__(self, salary, department):
        self.__salary = salary
        self.__department = department

    def getSalary(self):
        return self.__salary

    def getDepartment(self):
        return self.__department

emp1 = Employee(550000.8885, 'Computing')
print(emp1.getSalary())
print(emp1.getDepartment())