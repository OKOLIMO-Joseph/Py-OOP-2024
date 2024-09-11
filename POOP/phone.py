# Define a class named Car
class Phone:
    # Initialize the attributes of the class
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    # Define a method to display the car's details
    def display_details(self):
        print("My phone is ", self.color)
        print("The phone is a ", self.model)
        print("The phone's brand is ", self.brand)

# Create an object of the Car class
phone1 = Phone('Infinix', 'HOTi', "silver")

# Call the method to display the car's details
phone1.display_details()
