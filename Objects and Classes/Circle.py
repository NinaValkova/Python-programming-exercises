class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.Diameter = diameter
        self.Raduis = diameter / 2

    @property
    def Raduis(self):
        return self._raduis

    @Raduis.setter
    def Raduis(self, raduis):
        self._raduis = raduis

    @property
    def Diameter(self):
        return self._diameter

    @Diameter.setter
    def Diameter(self, diameter):
        self._diameter = diameter

    def calculate_circumference(self):
        return Circle.__pi * self.Diameter

    def calculate_area(self):
        return Circle.__pi * self.Raduis * self.Raduis

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * Circle.__pi * self.Raduis * self.Raduis


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
