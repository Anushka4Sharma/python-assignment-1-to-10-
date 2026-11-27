assignments = ["Python", "DBMS", "DSA"]

print("Original assignments:", assignments)

new_assignment = input("Enter new assignment: ")
assignments.append(new_assignment)

completed = input("Enter completed assignment: ")

if completed in assignments:
    assignments.remove(completed)
else:
    print("Assignment not found")

print("Updated assignments:", assignments)