# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py
import math
# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle
class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

class Circle:
    """
    A Circle in 2D space.
    """

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius