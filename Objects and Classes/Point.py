class Point:
    def __init__(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    @property
    def x(self):
        return self._x    

    @x.setter
    def x(self, x):
        self._x = x 

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
        
    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"

p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)

# _x, _y	Actual internal storage of the values
# x, y	Properties for controlled access → call getter/setter when read/write
# set_x(), set_y()	Convenience methods to update x and y (optional, could assign p.x = 3 directly)