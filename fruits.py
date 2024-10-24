class Tropical:
    def grow_in_tropics(self):
        return "This fruit grows in tropical climates."

class Citrus:
    def is_citrus(self):
        return "This fruit is a type of citrus."

class Fruits(Tropical, Citrus):
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"{self.name} is a fruit. {self.grow_in_tropics()} {self.is_citrus()}"

# Example usage
if __name__ == "__main__":
    mango = Fruits("Mango")
    print(mango.info())
