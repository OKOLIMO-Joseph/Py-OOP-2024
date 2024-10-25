class Device:
    def info(self):
        print('Device information')

class Computer(Device):
    def info(self):
        print('Computer Information')

class Laptop(Computer):
    def info(self):
        print('Laptop information')
        super().info()
        super(Computer, self).info()

Laptop1 = Laptop()
Laptop1.info()