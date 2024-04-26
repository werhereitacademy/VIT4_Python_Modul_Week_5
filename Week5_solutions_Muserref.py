#Question 1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 7)

print(f"Area of Rectangle: {rectangle.area()}")
print(f"Perimeter of Rectangle: {rectangle.perimeter()}")

#Question 2
class School:
    def __init__(self, name, establishment_year):
        self.name = name
        self.establishment_year = establishment_year
        self.students = []
        self.teachers = {}

    def add_student(self, student_name, grade):
        self.students.append({"name": student_name, "grade": grade})

    def add_teacher(self, teacher_name, subject):
        self.teachers[teacher_name] = subject

    def display_student_list(self):
        print("Registered students:")
        for student in self.students:
            print(f"Name: {student['name']}, Grade: {student['grade']}")

    def display_teacher_list(self):
        print("Teachers:")
        for teacher, subject in self.teachers.items():
            print(f"Name: {teacher}, Subject: {subject}")

# Sample usage
school = School("Ede School", 1990)
school.add_student("Ali Er", "10A")
school.add_student("Miriam Son", "11B")
school.add_teacher("Jan Kai", "Mathematics")
school.add_teacher("Regien Woort", "Physics")

school.display_student_list()
print("\n")
school.display_teacher_list()

#Question 3

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

#Q4

#Q5

# Hackerrank 

import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        return Complex(a + c, b + d)

    def __sub__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        return Complex(a - c, b - d)

    def __mul__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        real_mult = (a * c) - (b * d)
        imag_mult = (a * d) + (b * c)
        return Complex(real_mult, imag_mult)

    def __truediv__(self, no):
        a = self.real
        b = self.imaginary
        c = no.real
        d = no.imaginary
        real_numerator = a * c + b * d
        imag_numerator = b * c - a * d
        denom = c * c + d * d
        real_div = real_numerator / denom
        imag_div = imag_numerator / denom
        return Complex(real_div, imag_div)

    def mod(self):
        a = self.real
        b = self.imaginary
        return Complex(math.sqrt(a ** 2 + b ** 2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = '%.2f+0.00i' % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = '0.00+%.2fi' % (self.imaginary)
            else:
                result = '0.00-%.2fi' % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = '%.2f+%.2fi' % (self.real, self.imaginary)
        else:
            result = '%.2f-%.2fi' % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
