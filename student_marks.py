name = input("Enter student name: ")
mark1 = float(input("Enter mark 1: "))
mark2 = float(input("Enter mark 2: "))
mark3 = float(input("Enter mark 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total)
print("Average:", round(average, 2))