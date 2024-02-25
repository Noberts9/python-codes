
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# Input radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Create an instance of Circle
circle = Circle(radius)

# Calculate and display the area and perimeter
area = circle.calculate_area()
perimeter = circle.calculate_perimeter()

print(f"The area of the circle is: {area:.2f}")
print(f"The perimeter of the circle is: {perimeter:.2f}")