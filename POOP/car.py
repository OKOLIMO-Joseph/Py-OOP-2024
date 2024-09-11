# Define a class named Car
class Car:
    # Initialize the attributes of the class
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Define a method to display the car's details
    def display_details(self):
        print("The car was made in", self.year)
        print("The car's model is", self.model)
        print("The car's brand is ", self.make)

# Create an object of the Car class
car1 = Car('Toyota', 'Corolla', 2018)

# Call the method to display the car's details
car1.display_details()
