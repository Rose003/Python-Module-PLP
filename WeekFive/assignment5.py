# Assignment 1: Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.
# Activity 2: Polymorphism Challenge! 🎭

# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_status = False

    def start_engine(self):
        self.engine_status = True
        return f"{self.brand} {self.model}'s engine is running"

    def stop_engine(self):
        self.engine_status = False
        return f"{self.brand} {self.model}'s engine is off"

    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.wheels = 4

    def move(self):
        return f"{self.brand} {self.model} is cruising on {self.wheels} wheels"

class Plane(Vehicle):
    def __init__(self, brand, model, year, wingspan):
        super().__init__(brand, model, year)
        self.wingspan = wingspan
        self.altitude = 0

    def move(self):
        return f"{self.brand} {self.model} is soaring through the clouds with {self.wingspan}m wingspan"

    def change_altitude(self, feet):
        self.altitude += feet
        return f"Altitude changed to {self.altitude} feet"

# Create and test vehicles
tesla = Car("Tesla", "Model S", 2023, "Electric")
boeing = Plane("Boeing", "747", 2020, 68)

print(tesla.start_engine())
print(tesla.move())
print(boeing.start_engine())
print(boeing.move())
print(boeing.change_altitude(35000))
