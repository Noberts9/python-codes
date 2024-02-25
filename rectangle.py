class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Input length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Create an instance of Rectangle
rectangle = Rectangle(length, width)

# Calculate and display the area and perimeter
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")