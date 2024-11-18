class Lenovo:
    def __init__(self, brand):
        self.brand = brand

    def len_info(self):
        print(f'Brand: {self.brand}')

class ThinkPad(Lenovo):
    def __init__(self, brand, model, color):
        super().__init__(brand)
        self.model = model
        self.color = color

    def len_info(self):
        Lenovo.len_info(self)
        print(f'Mode: {self.model}')
        print(f'Color: {self.color}')

thinkpd1 = ThinkPad('Lenovo', 'ThinkPad', 'Black')
thinkpd1.len_info()
print(sep='\n')

class ThinkBook(Lenovo):
    def __init__(self, brand, model, color):
        super().__init__(brand)
        self.model = model
        self.color = color

    def len_info(self):
        Lenovo.len_info(self)
        print(f'Mode: {self.model}')
        print(f'Color: {self.color}')

thinkbk1 = ThinkBook('Lenovo', 'ThinkBook', 'Silver')
thinkbk1.len_info()
print(sep='\n')

class Yoga(Lenovo):
    def __init__(self, brand, model, color):
        super().__init__(brand)
        self.model = model
        self.color = color

    def len_info(self):
        Lenovo.len_info(self)
        print(f'Mode: {self.model}')
        print(f'Color: {self.color}')  

yoga1 = Yoga('Lenovo', 'Yoga', 'Silver-black')
yoga1.len_info()