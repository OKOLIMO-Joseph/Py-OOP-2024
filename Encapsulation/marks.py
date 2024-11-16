class Marks:
    def __init__(self, name, access_no, course, course_marks, exam_mark):
        self.name = name
        self.access_no = access_no
        self.course = course
        self.course_marks = course_marks
        self.exam_mark = exam_mark
        
    def grade(self):
        total_marks = (self.course_marks + self.exam_mark)
        print(f'Name: {self.name}')
        print(f'Access Number: {self.access_no}')
        print(f'Course: {self.course}')
        print(f'Coursework: {self.course_marks}')
        print(f'Exam: {self.exam_mark}')
        print(f'Total Marks: {total_marks}')

stud1 = Marks('Jos OKOLIMO', 'B22562', 'BSIT', 55, 35)
stud1.grade()
print(sep='\n')
stud2 = Marks('Job OKULLO', 'B25634', 'CS', 54, 33)
stud2.grade()
