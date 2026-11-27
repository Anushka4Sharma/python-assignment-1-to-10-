while True:
    password = input("Enter password: ")

    if password.lower() == "stop":
        break

    upper = False
    lower = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True

    if len(password) >= 8 and upper and lower:
        print("Strong password")
    else:
        print("Weak password")