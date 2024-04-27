class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def area_calculation(self):
        return self.width * self.height

class Square(Shape):
    def area_calculation(self):
        return self.width ** 2

rectangle = Rectangle(3, 4)
print("Rectangle Area:", rectangle.area_calculation())

square = Square(4, 4)
print("Square Area:", square.area_calculation())