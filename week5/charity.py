class Charity:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def charity_info(self):
        print(f"My name is: {self.name}")
        print(self.color)
        print(self.size)
aber = Charity('Aber Mercy', 'Chocolate', 'Fat')
# aber.charity_info
print(aber)
