def calculate_calories(carbs, fat, protein):
    return carbs * 4 + fat * 9 + protein * 4

try:
    carbs = float(input("Enter carbohydrates in grams: "))
    fat = float(input("Enter fat in grams: "))
    protein = float(input("Enter protein in grams: "))

    if carbs < 0 or fat < 0 or protein < 0:
        print("Grams cannot be negative")
    else:
        total = calculate_calories(carbs, fat, protein)
        print("Total calorie intake =", total, "calories")

except ValueError:
    print("Invalid input")