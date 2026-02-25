# dineshkate_stage3_python_file
# Stage 3 --> Student Grade Calculator program

name = input("Enter student name: ")

mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))

total = mark1 + mark2 + mark3
percentage = (total / 300) * 100

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

print("\n--- RESULT ---")
print("Name:", name)
print("Total:", total, "/300")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)