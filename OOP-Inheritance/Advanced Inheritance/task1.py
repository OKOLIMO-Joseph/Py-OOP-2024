class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def show_info(self):
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')

class Smartphone(Device):
    def __init__(self, brand, model, storage_capacity):
        super().__init__(brand, model)
        self.storage_capacity = storage_capacity

    def  show_info(self):
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Storage Capacity: {self.storage_capacity}')

smartphone1 = Smartphone('Infinix', 'HOT10i', '64gb')
smartphone1.show_info()
