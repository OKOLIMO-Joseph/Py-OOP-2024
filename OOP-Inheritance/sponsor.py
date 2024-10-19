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