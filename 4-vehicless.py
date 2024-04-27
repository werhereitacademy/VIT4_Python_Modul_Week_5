import json

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class OffRoadVehicle(Vehicle):
        def __init__(self, four_wheel_drive, brand, model, year):
            super().__init__(brand, model, year)
            self.four_wheel_drive = four_wheel_drive

class SportsCar(Vehicle):
        def __init__(self, max_speed, brand, model, year):
            super().__init__(brand, model, year)
            self.max_speed = max_speed

def load_from_json(filename):
    vehicles = []
    try:
        with open(filename, "r") as json_file:
            data = json.load(json_file)
            for item in data:
                if "four_wheel_drive" in item:
                    vehicle = OffRoadVehicle(item["four_wheel_drive"], item["brand"], item["model"], item["year"])
                elif "max_speed" in item:
                    vehicle = SportsCar(item["max_speed"], item["brand"], item["model"], item["year"])
                else:
                    vehicle = Vehicle(item["brand"], item["model"], item["year"])
                vehicles.append(vehicle)
        print("Vehicles loaded from vehicles.json.")
    except FileNotFoundError:
        print("No vehicles.json file found. Starting with an empty list of vehicles.")
    return vehicles

def save_to_json(vehicles, filename):
    data = []
    for vehicle in vehicles:
        vehicle_data = {
            "brand": vehicle.brand,
            "model": vehicle.model,
            "year": vehicle.year,
        }
        if isinstance(vehicle, OffRoadVehicle):
            vehicle_data["four_wheel_drive"] = vehicle.four_wheel_drive
        elif isinstance(vehicle, SportsCar):
            vehicle_data["max_speed"] = vehicle.max_speed
        data.append(vehicle_data)
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print("Vehicles saved to vehicles.json.")

vehicles = load_from_json("vehicles.json")

while True:
    print("\n*** Vehicle Management System ***")
    print("1. Add Off-Road Vehicle")
    print("2. Add Sports Car")
    print("3. View Vehicles Information")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        brand = input("Enter the brand of the off-road vehicle: ")
        model = input("Enter the model of the off-road vehicle: ")
        year = input("Enter the production year of the off-road vehicle: ")
        four_wheel_drive = input("Does it have four-wheel drive? (Yes/No): ").lower() == "yes"
        off_road_vehicle = OffRoadVehicle(four_wheel_drive, brand, model, year)
        vehicles.append(off_road_vehicle)
        print("Off-Road Vehicle added successfully.")

    elif choice == "2":
        brand = input("Enter the brand of the sports car: ")
        model = input("Enter the model of the sports car: ")
        year = input("Enter the production year of the sports car: ")
        max_speed = input("Enter the maximum speed of the sports car (in km/h): ")
        sports_car = SportsCar(max_speed, brand, model, year)
        vehicles.append(sports_car)
        print("Sports Car added successfully.")

    elif choice == "3":
        if not vehicles:
            print("No vehicles added yet.")
        else:
            print("\n*** Vehicles Information ***")
            for idx, vehicle in enumerate(vehicles, start=1):
                print(f"\nVehicle {idx}:")
                print("Brand:", vehicle.brand)
                print("Model:", vehicle.model)
                print("Year:", vehicle.year)
                if isinstance(vehicle, OffRoadVehicle):
                    print("Type: Off-Road Vehicle")
                    print("Four-Wheel Drive:", "Yes" if vehicle.four_wheel_drive else "No")
                elif isinstance(vehicle, SportsCar):
                    print("Type: Sports Car")
                    print("Max Speed:", vehicle.max_speed, "km/h")

    elif choice == "4":
        save_to_json(vehicles, "vehicles.json")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
