class Student:
    def __init__(self, name, reg_number):
        self.name = name
        self.reg_number = reg_number
        self.registrations = []

    def add_registration(self, reg_number):
        self.registrations.append(reg_number)

    def display_registrations(self):
        print(f"Registrations for {self.name}:")
        for reg in self.registrations:
            print(reg)

# Example usage:
student = Student("John Doe", "2024-001")
student.add_registration("2024-002")
student.add_registration("2024-003")
student.display_registrations()
