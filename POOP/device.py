class Device:
    def operate(self):
        print('Device is operating')

class Perco(Device):
    def operate(self):
        print('Boiling!')
samsung = Perco()
samsung.operate()

class Laptop(Device):
    def operate(self):
        print('Laptop is coding')
thinkad = Laptop()
thinkad.operate()