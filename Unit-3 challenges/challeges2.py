class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Test cases
students1 = [
    Student("John Doe", "001", 3.8),
    Student("Jane Smith", "002", 3.9),
    Student("Bob Johnson", "003", 3.7)
]

students2 = [
    Student("Alice Lee", "004", 3.6),
    Student("James Brown", "005", 3.5),
    Student("Eva Davis", "006", 4.0)
]

# Sort and print students based on CGPA
sorted_students1 = sort_students(students1)
sorted_students2 = sort_students(students2)

print("Students sorted by CGPA (Descending Order):")
for student in sorted_students1:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

print("\n")

for student in sorted_students2:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
