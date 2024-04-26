
# Define the Rectangle class
class Rectangle:
    # Constructor method to initialize width and height
    def __init__(self, width, height): ### anlatimda parametreleri degistir ve nerelerin degistigini goster
        self.width = width
        self.height = height

    # Method to calculate the area of the rectangle
    def area(self):
        return self.width * self.height
    
    # Method to calculate the perimeter of the rectangle
    def perimeter(self):
        return 2 * (self.width + self.height)

# Create an instance of the Rectangle class with width 5 and height 7    
my_rectangle = Rectangle(5, 7)

the_area = my_rectangle.area()
the_perimeter = my_rectangle.perimeter()

print(f"Area of a rectangle with dimensions {my_rectangle.width} by {my_rectangle.height} is: {the_area}")
print(f"Perimeter of a rectangle with dimentions {my_rectangle.width} by {my_rectangle.height} is: {the_perimeter}")
        
