class Appliance:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

    def show_details(self):
        print(f'Brand: {self.brand}')
        print(f'Power: {self.power} watts')

class WashingMachine(Appliance):
    def __init__(self, brand, power, drum_size):
        super().__init__(brand, power)
        self.drum_size = drum_size

    def show_details(self):
        super().show_details()
        print(f'Drum Size: {self.drum_size} cu ft')

WashingMachine1 = WashingMachine('Samsung', 1000, 6)
WashingMachine1.show_details()