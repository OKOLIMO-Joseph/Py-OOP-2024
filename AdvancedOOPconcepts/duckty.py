class Dog:
    def speak(self):
        return "Bark!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_speak(animal):
    print(animal.speak())

# Both Dog and Cat have a `speak` method
animal_speak(Dog())  # Output: Bark!
animal_speak(Cat())  # Output: Meow!
