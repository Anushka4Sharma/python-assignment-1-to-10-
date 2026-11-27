import math

def calculate_area(shape, *args):
    if shape == "circle":
        return math.pi * args[0] ** 2

    elif shape == "rectangle":
        return args[0] * args[1]

    elif shape == "triangle":
        return 0.5 * args[0] * args[1]

    else:
        return "Invalid shape"

shape = input("Enter shape (circle/rectangle/triangle): ").lower()

try:
    if shape == "circle":
        r = float(input("Enter radius: "))
        print("Area =", calculate_area(shape, r))

    elif shape == "rectangle":
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        print("Area =", calculate_area(shape, l, b))

    elif shape == "triangle":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print("Area =", calculate_area(shape, b, h))

    else:
        print("Invalid shape")

except ValueError:
    print("Invalid input")