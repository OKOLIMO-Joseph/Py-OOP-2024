class Vehicle:
    def __init__(self, color):
        self.color = color
        self.tyres = self.Car()
        self.trailer = self.Truck()
        # self.garage = self.Garage()

    def getColor(self):
        return self.color

    def toString(self):
        print(f'This vehicle is {self.color}')
        self.tyres.toString()
        self.trailer.toString()
        # self.garage.toString()

    class Car:
        def __init__(self,has_winter_tyre=False):
            self.has_winter_tyre = has_winter_tyre

        def toString(self):
            print(f'Has winter tyres: {self.has_winter_tyre}')

    class Truck:
        def __init__(self, has_trailer=False):
            self.has_trailer = has_trailer


        def toString(self):
            print(f'Has trailer: {self.has_trailer}')

class Garage(Vehicle):
    def __init__(self):
        super().__init__()

    def setvehicle(self):
        print(f'The vehicle is parked!')

    def toString(self):
        print(f'Description of the parked vehicle... {super.__init__()}')

Romeo = Vehicle('Silver-vlack') 
print(Romeo.getColor())
Romeo.toString()