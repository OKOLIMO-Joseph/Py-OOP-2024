class Student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
    def student_info(self):
        print(f'Name: {self.name} ')
        print(f'Gender: {self.gender}')

charity = Student('Charity', 'Female')
charity.student_info()