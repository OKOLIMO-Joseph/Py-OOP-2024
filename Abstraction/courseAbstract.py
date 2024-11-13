from abc import ABC, abstractmethod

class Assignment(ABC):
    @abstractmethod
    def my_assignments(self, course_unit):
        pass

class SAD(Assignment):
    def my_assignments(self, course_unit):
        print(f'Course Unit: {course_unit}')

class AdvancedLAN(Assignment):
    def my_assignments(self, course_unit, work):
        print(f'Course Unit: {course_unit}')
        print(f'Assigment: {work}')

class OOP(Assignment):
    def my_assignments(self, course_unit, concept):
        print(f'Course Uinit: {course_unit}')
        print(f'Concept: {concept}')

assignment1 = SAD()
assignment1.my_assignments('System Analysis and Design')
print(sep='\n')

assignment2 = AdvancedLAN()
assignment2.my_assignments('Advanced Computer Networks', 'Full network project')
print(sep='\n')

assignment3 = OOP()
assignment3.my_assignments('Object Oriented Programming in Python', 'Abstraction')
