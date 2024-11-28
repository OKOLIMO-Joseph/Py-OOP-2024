class Computer:
#brand is the class variable
    brand = 'Lenovo'
#Constructor with the instance variables
    def __init__(self, core, ram, disk):
        self.core = core
        self.ram = ram
        self.disk = disk
    def _config_(self):
        print(self.core, self.ram, self.disk, self.brand)
    def stat(self):
        print(Computer.brand)

com1 = Computer('i7', '8gb', 'hdd')
com2 = Computer('i5', '16gb', 'ssd')
com1._config_()
com1.stat()
com2._config_()
com2.stat()
Computer._config_(com2)



mthd()
_mthd()
__mthd()