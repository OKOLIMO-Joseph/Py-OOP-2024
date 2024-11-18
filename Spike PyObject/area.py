class Shape:
    def __init__(self, type, sides):
        self.type = type
        self.sides = sides

    def area(self):
        print('Calculating Area')

class Square(Shape):
    def __init__(self, type, sides, length):
        super().__init__(type, sides)
        self.length = length

    def area(self):
        sq_area = (self.length ** 2)
        print('Area of Square =', sq_area,'cm')

sq1 = Square('Square', 4, 9)
sq1.area()

class Rectangle(Shape):
    def __init__(self, type, sides, length, width):
        super().__init__(type, sides)
        self.length = length
        self.width = width

    def area(self):
        sq_rectangle = (self.length * self.width)
        print('Area of Rectangle =', sq_rectangle,'cm')

rectangle1 = Rectangle('Rectangle', 4, 9, 5)
rectangle1.area()

class Circle(Shape):
    def __init__(self, type, sides, radius):
        super().__init__(type, sides)
        self.radius = radius

    def area(self):
        Circle_area = (3.014 * self.radius**2)
        print('Area of Circle =', Circle_area,'cm')

Circle1 = Circle('Circle',  0, 9)
Circle1.area()
