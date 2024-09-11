# Define a class named Car
class Food:
    # Initialize the attributes of the class
    def __init__(self, size, recipe, price):
        self.size = size
        self.recipe = recipe
        self.price = price

    # Define a method to display the car's details
    def display_details(self):
        print("This pizza is", self.size, "in size")
        print("This is a ", self.recipe, "pizza")
        print("The pizza costs $ ", self.price)

# Create an object of the Car class
pizza = Food("10", 'Chicken', "small")

# Call the method to display the car's details
pizza.display_details()
