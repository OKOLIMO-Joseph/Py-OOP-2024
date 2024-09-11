# Define a class named Car
class Okolimo:
    # Initialize the attributes of the class
    def __init__(self, gender, course, age):
        self.gender = gender
        self.course = course
        self.age = age

    # Define a method to display the car's details
    def display_details(self):
        print("I am a ", self.gender,)
        print("My course is ", self.course)
        print("I am ", self.age, "years old")

# Create an object of the Car class
mybio = Okolimo('male', 'BSIT', 21)

# Call the method to display the car's details
mybio.display_details()
