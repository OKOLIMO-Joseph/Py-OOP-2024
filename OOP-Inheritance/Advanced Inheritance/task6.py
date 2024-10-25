class Animal:
    def sound(self):
        print('Some generic animal sound')

class Dog(Animal):
    def sound(self):
        print('Bark!')

class Cat(Animal):
    def sound(self):
        print('Meow!')

def make_animal_sound(animal):
    animal.sound()

Dog1 = Dog()
make_animal_sound(Dog1)

Cat1 = Cat()
make_animal_sound(Cat1)