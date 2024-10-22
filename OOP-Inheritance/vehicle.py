class Vehicle:
    def start_engine(self):
        return "Starting engine... generic vehicle."

class Car(Vehicle):
    def start_engine(self):
        return "Starting engine... vroom! It's a car."

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Starting engine... brap brap! It's a motorcycle."

# Create instances
generic_vehicle = Vehicle()
my_car = Car()
my_motorcycle = Motorcycle()

# Call the start_engine method on each instance
print(generic_vehicle.start_engine())  # Output: Starting engine... generic vehicle.
print(my_car.start_engine())           # Output: Starting engine... vroom! It's a car.
print(my_motorcycle.start_engine())    # Output: Starting engine