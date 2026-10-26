# Week 1.5, Session 1: Task 3

class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Add constructor here

    # Add distance() method here
    def distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


# Finally, add code here to demonstrate use of Point
