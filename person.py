class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f'Name: {self.name}, Age: {self.age}')

class Student(Person):
    def __init__(self, name, age, accessNumber):
        super().__init__(name, age)
        self.accessNumber = accessNumber
 
    def display_info(self):
        super().display_info()
        print(f'Acess Number: {self.accessNumber}')

student1 = Student('OKOLIMO Joseph', '21', 'B22562')
student1.display_info()
print(sep='\n')

class Staff(Person):
    def __init__(self, name, age, staffId):
        super().__init__(name, age)
        self.staffId = staffId

    def display_info(self):
        super().display_info()
        print(f'Staff ID: {self.staffId}')

staff1 = Staff('Lubambo Simon', '32', 'UCU-001')
staff1.display_info()