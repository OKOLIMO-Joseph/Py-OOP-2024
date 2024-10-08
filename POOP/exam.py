class Exam:
    course = 'BSIT'
    def  __init__(self, name, m1,  m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def stud_avg(self):
        print(f'{self.name}s average :')
        return (self.m1 +  self.m2 + self.m3) / 3

    @classmethod
    def course_info(cls):
        return cls.course

    @staticmethod
    def uni_info():
        print('BSIT has 3 intakes at UCU')


stud1 = Exam('John', 80, 67, 89)
stud2 = Exam('Joseph', 89, 98, 75)
print(stud1.stud_avg())
print(Exam.course_info())
Exam.uni_info()

