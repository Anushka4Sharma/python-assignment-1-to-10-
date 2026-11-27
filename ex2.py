try:
    mass = float(input("Enter mass of object in kg: "))

    if mass < 0:
        print("Mass cannot be negative")
    else:
        earth = mass * 9.81
        moon = mass * 1.62

        print("Weight on Earth =", round(earth, 2), "N")
        print("Weight on Moon =", round(moon, 2), "N")

except ValueError:
    print("Invalid input")
