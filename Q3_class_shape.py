

class Shape:

    def __init__(self, width, height):

        self.width = width
        self.height = height


class Rectangle(Shape):

    def calculate_area(self):
        return self.width * self.height  


class Square(Shape):
    
    def calculate_area(self):
        return self.width * self.height
    

my_rectangle = Rectangle(5, 7)
print(my_rectangle.calculate_area())

my_square = Square(5, 5)
print(my_square.calculate_area())