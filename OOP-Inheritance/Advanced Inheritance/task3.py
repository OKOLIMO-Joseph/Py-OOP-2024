class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def start(self):
        print(f'{self.vehicle_type} has started!')

class Car(Vehicle):
    def __init__(self, vehicle_type, number_of_doors):
        super().__init__(vehicle_type)
        self.number_of_doors = number_of_doors

    def start(self):
        super().start()
        print(f'{self.vehicle_type} has {self.number_of_doors}doors')

class ElectricCar(Car):
    def __init__(self, vehicle_type, number_of_doors, battery_capacity):
        super().__init__(vehicle_type, number_of_doors)
        self.battery_capacity = battery_capacity

    def start(self):
        super().start()
        print(f'Battery Capacity: {self.battery_capacity}Ah')

ecar1 = ElectricCar('Bugatti', 2, 50000)
ecar1.start()