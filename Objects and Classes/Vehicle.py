class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, mileage):
        self._mileage = mileage


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append("Hudly Wireless")
print(car.gadgets)
