class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return(f'Student added successfully!')

        return(f'Max number of students reached!')

    def get_avg_grade(self):
        avg_grade = 0
        for student in self.students:
            avg_grade += student.get_grade()

        return avg_grade/len(self.students)

stud1 = Student('Joseph', 21, 90)
stud2 = Student('John', 20, 88)
stud3 = Student('Jessy', 23, 64)

course1 = Course('IT', 2)
print(course1.add_student(stud1))
print(course1.add_student(stud2))
print(course1.add_student(stud3))
print(course1.students[0].name)

print(course1.get_avg_grade())