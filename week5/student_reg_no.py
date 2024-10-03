class Student_details:
    def __init__(self, name, registration_no, gender, course):
        self.name = name
        self.registration_no = registration_no
        self.gender = gender
        self.course = course

    def student_info(self):
        print(f"Name: {self.name}")
        print(f"Registration No: {self.registration_no}")
        print(f"Gender: {self.gender}")
        print(f"Course: {self.course}")

student1 = Student_details('OKOLIMO Joseph', 'M23B13/008', 'Male', 'BSIT')
student2 = Student_details('LUBONGE Marvin', 'M23B13/034', 'Male', 'Medicine and Surgery')
student3 = Student_details('SHILPAH Sing', 'M23B14/012', 'Female', 'Computer Systems')

student1.student_info()
# student2.student_info()
# student3.student_info()