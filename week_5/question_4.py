# Question 4
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

# Create instances of SUV and SportsCar
suv = SUV("Toyota", "Land Cruiser", 2022, True)
sports_car = SportsCar("Ferrari", "488 GTB", 2023, 330)

print("SUV Brand:", suv.brand)
print("SUV Model:", suv.model)
print("SUV Year:", suv.year)
print("Four Wheel Drive:", suv.four_wheel_drive)

print("Sports Car Brand:", sports_car.brand)
print("Sports Car Model:", sports_car.model)
print("Sports Car Year:", sports_car.year)
print("Maximum Speed (km/h):", sports_car.max_speed)