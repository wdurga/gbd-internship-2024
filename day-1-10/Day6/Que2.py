
# 2. create a base class called Shape and then create child classes 
# like Circle and Rectangle. Implement methods for calculating 
# area and perimeter, and show how inheritance can be used effectively.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle with radius {self.radius}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height}"

circle = Circle(5)
rectangle = Rectangle(4, 7)

# Calculate and print area and perimeter for Circle
print(circle)
print(f"Area: {circle.area()}")
print(f"Perimeter: {circle.perimeter()}")

# Calculate and print area and perimeter for Rectangle
print(rectangle)
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")
