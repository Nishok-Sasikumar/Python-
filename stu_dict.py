student = {
    "name": "John",
    "age": 20,
    "grade": "B",
    "subject": "Python"
}

for key, value in student.items():
    print(key, ":", value)

student["grade"] = "A"
student["passed"] = True

print("Updated Dictionary:")
for key, value in student.items():
    print(key, ":", value)