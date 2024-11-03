class Student:

    def __init__ (self, name, course, gender, residence):
        self.name = name
        self.course = course
        self.gender = gender
        self.residence = residence

    def display_bio(self):
        print('My name is ', self.name)
        print('I do ', self.course)
        print('I am a ', self.gender, 'Ugandan')
        print('I reside in ',self.residence, 'hostel')

okolimo = Student('OKOLIMO','BSIT','male','PDR')

okolimo.display_bio()