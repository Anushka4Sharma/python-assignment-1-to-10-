try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Addition =", a + b)
    elif choice == 2:
        print("Subtraction =", a - b)
    elif choice == 3:
        print("Multiplication =", a * b)
    elif choice == 4:
        if b != 0:
            print("Division =", a / b)
        else:
            print("Error: Division by zero")

    else:
        print("Invalid choice")

    ch = input("Do you want advanced calculations? (yes/no): ")

    if ch.lower() == "yes":
        print("1. Exponentiation")
        print("2. Modulus")
        print("3. Floor Division")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Exponentiation =", a ** b)
        elif choice == 2:
            if b != 0:
                print("Modulus =", a % b)
            else:
                print("Error: Modulus by zero")
        elif choice == 3:
            if b != 0:
                print("Floor Division =", a // b)
            else:
                print("Error: Division by zero")
        else:
            print("Invalid choice")

except ValueError:
    print("Error: Please enter valid numbers and choices")