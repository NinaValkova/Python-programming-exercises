from abc import ABC, abstractmethod

# ABC stands for Abstract Base Class.
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

class Car(Vehicle):
    FUEL_CONSUMPTION_SUMMER = 0.9
    def __init__(self, fuel_quantity, fuel_consumption ):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumes = Car.FUEL_CONSUMPTION_SUMMER + self.fuel_consumption
        needed_fuel = distance * consumes

        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):  
    FUEL_CONSUMPTION_SUMMER = 1.6
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumes = Truck.FUEL_CONSUMPTION_SUMMER + self.fuel_consumption
        needed_fuel = distance * consumes

        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        curr_fuel = 0.95 * fuel
        self.fuel_quantity += curr_fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
