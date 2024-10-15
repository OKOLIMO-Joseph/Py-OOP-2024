class Animal:
    def __init__(self, name):
        self.name = name
    
    def display_info(self):
        print(f'{self.name}')

    def make_sound(self):
        print(f'{self.name} cries!')

class  Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name)

    def make_sound(self):
        sum
