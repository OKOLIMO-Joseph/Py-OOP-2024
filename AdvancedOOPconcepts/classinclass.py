class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(f'{self.name} : {self.rollno}')
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'Lenovo'
            self.cpu = 'i7'
            self.ram = '16gb'

        def  show(self):
            print(f'Brand: {self.brand} CPU: {self.cpu} RAM: {self.ram}')

stud1 = Student('OKOLIMO Joseph', 'B22562')
stud2 = Student('Nakacwa Emelda', 'B23456')
stud1.show()
stud2.show()