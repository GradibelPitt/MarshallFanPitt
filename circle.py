import math

radius_input = input("Please enter the radius of the circle:")

r = float(radius_input)
p = round(2 * r * math.pi, 2)
area = round(math.pi * r ** 2, 3)

print(f"The circle with radius {r} has an area of {area} and a perimeter of {p}.")
