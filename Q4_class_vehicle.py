

class Vehicle:

    def __init__(self, brand, model, year):

        self.brand = brand
        self.model = model
        self.year = year
    def __str__(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}"
        

class SUV(Vehicle):

    def __init__(self,brand, model, year, four_wheel_drive):

        super().__init__(brand, model, year)
        self.four_wheel_drive = four_wheel_drive

    def __str__(self):
        return f"Brand: {super().__str__()}\nFour wheel drive: {self.four_wheel_drive}"


class SportsCar(Vehicle):

    def __init__(self,brand, model, year,  maximum_speed):
        super().__init__(brand, model, year)
        self.maximum_speed = maximum_speed

    def __str__(self):
        return f"Brand: {super().__str__()}\nFour wheel drive: {self.maximum_speed}"


print("\n")
my_SUV = SUV("Toyota", "Land Cruiser", 2022, True)
print(my_SUV)
print("\n")
my_sports_car = SportsCar("Ferrari", "488 GTB", 2023, 330)
print(my_sports_car)
print("\n")

