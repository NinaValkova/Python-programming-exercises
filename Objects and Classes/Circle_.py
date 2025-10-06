class Circle:
    pi = 3.14

    def __init__(self, new_radius):
        self.set_radius(new_radius)

    def set_radius(self, new_radius):
        self.radius = new_radius

    @property
    def radius(self):
        return self._radius    

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    def get_area(self):
        return Circle.pi * self.radius * self.radius

    def get_circumference(self):
        return 2 * Circle.pi * self.radius


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
