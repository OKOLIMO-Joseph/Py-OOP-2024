class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self._model = model
        self.__year = year

    # def info(self):
    #     print(f'Brand: {self.brand}')l
    #     print(f'Model: {self._model}')
    #     print(f'Year: {self.__year}')
    def get_year(self): # getter method
        return self.__year

    def set_year(self, year): #setter method
        self.__year = year

car1 = Car('Toyota', 'Rumion', 2022)
car1.brand = 'Volkswagen'
car1._model = 'Eagler'
car1.set_year(2020)

print(f'Brand: {car1.brand}')
print(f'Model: {car1._model}')
print(f'Year: {car1.get_year()}')