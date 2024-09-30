import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        result = random.randint(1, self.sides)
        print(f"The die shows: {result}")

# Example usage
die = Die()
die.roll()
