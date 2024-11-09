class Sponsor:
    def __init__(self, name, slang):
        self.name = name
        self.slang = slang

    def  display_info(self):
        print(f"Sponsor: {self.name}")
        print(f"Slang: {self.slang}")

Sponsor1 = Sponsor('Nike', 'Just Do It!')
Sponsor1.display_info()
print(sep='\n')

class Shoe(Sponsor):
    def __init__(self, name, slang, model):
        super().__init__(name, slang)
        self.model = model

    def display_info(self):
        super().display_info()
        print(f'Spike Model: {self.model}')

myspike = Shoe('Nike', 'Just DO It!', 'Nike-MaxFLY')
myspike.display_info()
print(sep='\n')

class Vest(Sponsor):
    def __init__(self, name, slang, color, size):
        super().__init__(name, slang)
        self.color = color
        self.size = size

    def display_info(self):
        super().display_info()
        print(f'Vest-Color: {self.color}')
        print(f'Size: {self.size}')

vest1 = Vest('Nike', 'Just DO It!', 'Orange', 'Large(L)')
vest1.display_info()

class Athlete(Sponsor,  Shoe, Vest):
    def __init__(self, name, slang, model, color, size, athlete_name, sport):
        super().__init__(name,  slang, model, color, size)
        self.athlete_name = athlete_name
        self.sport = sport

    def display_info(self):
        super().display_info()
        print(f'Athletes Name: {self.athlete_name}')
        print(f'{self.athlete_name} does {self.sport}')

athlete1 = Athlete('Nike', 'Just DO It!',  'Nike-MaxFLY', 'Orange', 'Large(L)', 'OKOLIMO Joseph', 'Track and Fiekd')
athlete1.display_info()
