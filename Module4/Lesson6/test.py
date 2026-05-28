# Student Grade Book

# Dictionary with student names and scores
students = {
    "Aman": 85,
    "Riya": 92,
    "Karan": 76,
    "Sneha": 88,
    "Rahul": 95
}

print("Student Grade Book")
print(students)

# Calculate class average
total = 0

for score in students.values():
    total += score

average = total / len(students)

print("\nClass Average =", average)

# Find highest scorer
top_student = max(students, key=students.get)
print("\nTop Scorer :", top_student, "-", students[top_student])

# Find lowest scorer
bottom_student = min(students, key=students.get)
print("Bottom Scorer :", bottom_student, "-", students[bottom_student])

# Search for a student
name = input("\nEnter student name to search: ")

grade = students.get(name)

if grade is not None:
    print(name, "scored", grade)
else:
    print("Student not found")