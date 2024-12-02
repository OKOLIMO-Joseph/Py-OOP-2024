class Animal:
    def speak(self):
        print("Animal speaks.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

class Cat(Animal):
    def speak(self):
        print("Cat meows.")

# Polymorphism in action
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.speak()

# Output:
# Dog barks.
# Cat meows.
# Animal speaks.
