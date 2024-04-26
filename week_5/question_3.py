class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def area(self):
        return self.width * self.height

class Square(Shape):
    def area(self):
        return self.width ** 2

# Create an instance of a rectangle and a square
rectangle = Rectangle(5, 7)
square = Square(4, 4)

# Calculate the area of each shape and print the results
print("Area of Rectangle:", rectangle.area())
print("Area of Square:", square.area())