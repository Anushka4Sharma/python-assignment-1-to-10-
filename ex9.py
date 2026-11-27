try:
    filename = input("Enter filename: ")

    with open(filename, "r") as file:
        content = file.read()

    print("File contents:")
    print(content)

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")