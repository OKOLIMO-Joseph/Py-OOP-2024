class Pizza:

    def __init__ (self,recipe,price,size):
        self.recipe = recipe
        self.price = price
        self.size = size

    def ready(self):
        print('The pizza is ready for eating!')

    def eaten(self):
        print('The pizza has been eaten already')