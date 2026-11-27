try:
    n = int(input("Enter number of students: "))

    if n <= 0:
        print("Number of students must be positive")
    else:
        total = 0

        for i in range(1, n + 1):
            print("Student", i)
            student_total = 0

            for j in range(1, 6):
                marks = float(input("Enter marks for test " + str(j) + ": "))
                student_total += marks

            average = student_total / 5
            total += student_total

            print("Average of student", i, "=", round(average, 2))

        class_average = total / (n * 5)

        print("Overall class average =", round(class_average, 2))

except ValueError:
    print("Invalid input")