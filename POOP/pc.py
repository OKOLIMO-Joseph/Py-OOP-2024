# Define a class named Car
class Computer:
    # Initialize the attributes of the class
    def __init__(self, brand, model, ram):
        self.brand = brand
        self.model = model
        self.ram = ram

    # Define a method to display the car's details
    def display_details(self):
        print("My PC has a RAM of", self.ram, "gb")
        print("It's model is ", self.model)
        print("The brand is ", self.brand)

# Create an object of the Car class
pc1 = Computer('Lenovo', 'Thinkpad', 16)

# Call the method to display the car's details
pc1.display_details()
