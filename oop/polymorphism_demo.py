import math
class Shape:
    def area(self):
        return f"NotImplementedError"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return ("%.2d" %float(self.width * self.length))

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return float(math.pi * self.radius*self.radius)
