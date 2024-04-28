#Q1_class Rectangle

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

---------------------------------------------------------------------------

#Q2_class School

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

-----------------------------------------------------

#Q3_class Shape

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def calculate_area(self):
        return self.width ** 2

rectangle = Rectangle(7, 10)
square = Square(5, 5)


print(f"Area of the Rectangle: {rectangle.calculate_area()}")
print(f"Area of the Square: {square.calculate_area()}")

---------------------------------------------------
#Q4_class Vehicle

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class SUV(Vehicle):
    def __init__(self, brand, model, year, four_wheel_drive):
        super().__init__(brand, model, year)
        self.four_wheel_drive = four_wheel_drive

class SportsCar(Vehicle):
    def __init__(self, brand, model, year, max_speed):
        super().__init__(brand, model, year)
        self.max_speed = max_speed


suv = SUV("Subaru", "Forester", 2022, True)
sports_car = SportsCar("Ferrari", "488 GTB", 2020, 345)


print("SUV:")
print(f"Brand: {suv.brand}")
print(f"Model: {suv.model}")
print(f"Year: {suv.year}")
print(f"Four-wheel drive: {suv.four_wheel_drive}")

print("\nSports Car:")
print(f"Brand: {sports_car.brand}")
print(f"Model: {sports_car.model}")
print(f"Year: {sports_car.year}")
print(f"Max speed: {sports_car.max_speed} km/h")

----------------------------------------------------------------
#Q5_class Customer
class Customer:
    def __init__(self, name, surname, BSN, mobile):
        self.name = name
        self.surname = surname
        self.BSN = BSN
        self.mobile = mobile

    def display_customer_info(self):
        print("Customer Information:")
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("BSN:", self.BSN)
        print("Phone:", self.mobile)


class Account(Customer):
    def __init__(self, customer, iban, balance=0):
        super().__init__(customer.name, customer.surname, customer.BSN, customer.mobile)
        self.customer = customer
        self.balance = balance
        self.iban = iban

    def display_balance(self):
        print(f"Account Balance: {self.balance} EUR")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} EUR to the account.")
        self.display_balance()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} EUR from the account.")
        else:
            print("Insufficient balance. Withdrawal unsuccessful.")

        self.display_balance()


customer1 = Customer("Jack", "Smith", "12345678", "0687689784")
account1 = Account(customer1, "NLINGB67898758", 1000)

customer1.display_customer_info()
account1.display_balance()

account1.deposit(400)
account1.withdraw(300)


