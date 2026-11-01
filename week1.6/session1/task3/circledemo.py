# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
from shapes import Circle
from point import Point

# Create a Circle object
circle = Circle(2.5, Point(0.0, 0.0), "blue")

# Print the Circle's details
print(f"Circle details: Radius = {circle.radius}, Position = {circle.position}, Colour = {circle.colour}")

# Move the Circle to a new position
new_position = Point(1.0, 1.0)
circle.set_position(new_position)
print(f"Circle moved to new position: {circle.position}")

# Change the Circle's colour
circle.set_colour("green")
print(f"Circle colour changed to: {circle.colour}")

# Change the Circle's radius
circle.set_radius(3.0)
print(f"Circle radius changed to: {circle.radius}")



