class Student:
    """A class to represent a student."""
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.__enrolled_courses = []  # Private list to track enrolled courses

    def enroll(self, course):
        """Enroll the student in a course."""
        if course not in self.__enrolled_courses:
            self.__enrolled_courses.append(course)
            print(f"{self.name} has been enrolled in {course.name}.")
        else:
            print(f"{self.name} is already enrolled in {course.name}.")

    def get_courses(self):
        """Get the list of enrolled courses."""
        return [course.name for course in self.__enrolled_courses]

    def __str__(self):
        """String representation of a student."""
        return f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}"


class Course:
    """A class to represent a course."""
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.enrolled_students = []

    def add_student(self, student):
        """Add a student to the course."""
        if len(self.enrolled_students) < self.max_students:
            self.enrolled_students.append(student)
            student.enroll(self)
        else:
            print(f"Enrollment failed: {self.name} is full.")

    def list_students(self):
        """List all students enrolled in the course."""
        print(f"Students enrolled in {self.name}:")
        for student in self.enrolled_students:
            print(student)

    def __str__(self):
        """String representation of a course."""
        return f"Course: {self.name}, Max Students: {self.max_students}, Enrolled: {len(self.enrolled_students)}"


# Example usage
# Create courses
cs_course = Course("Computer Science", max_students=2)
math_course = Course("Mathematics", max_students=3)
history_course = Course("History", max_students=1)

# Create students
student1 = Student("Alice", 20, "S001")
student2 = Student("Bob", 22, "S002")
student3 = Student("Charlie", 21, "S003")
student4 = Student("Diana", 23, "S004")

# Enroll students in courses
cs_course.add_student(student1)  # Alice enrolled in CS
cs_course.add_student(student2)  # Bob enrolled in CS
cs_course.add_student(student3)  # Enrollment fails (CS full)

math_course.add_student(student3)  # Charlie enrolled in Math
math_course.add_student(student4)  # Diana enrolled in Math

history_course.add_student(student1)  # Alice enrolled in History
history_course.add_student(student4)  # Enrollment fails (History full)

# List students in each course
cs_course.list_students()
math_course.list_students()
history_course.list_students()

# Check individual student's enrolled courses
print(f"\n{student1.name}'s courses:", student1.get_courses())
print(f"{student3.name}'s courses:", student3.get_courses())
