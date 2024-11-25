class Course:
    def __init__(self, course_name, course_code, duration, department):
        self.course_name = course_name
        self.course_code = course_code
        self.duration =duration
        self.department = department

    def info(self):
        print(f'Course: {self.course_name}')
        print(f'Course Code: {self.course_code}')
        print(f'Duration: {self.duration}')
        print(f'Department: {self.department}')

course1 = Course('BSIT', 'B13', '3 Years', 'Department of Computing')
course1.info()

print(sep='\n')

class Teacher(Course):
    def __init__(self, tr_name, course_name, department):
        super().__init__(course_name, department)
        self.tr_name = tr_name

    def info(self):
        super().info(self.department, self.course_name)
        print(f'Lecturer: {self.tr_name}')

tr1 = Teacher('OKOLIMO Joseph', 'BSIT', 'Department of Computing')
tr1.info()