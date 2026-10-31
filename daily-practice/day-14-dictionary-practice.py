# Day 14: Dictionary Practice


student = {
    "name": "Haris",
    "age": 20,
    "marks": 85
}

print(student)

print("Name:", student["name"])
print("Marks:", student["marks"])


student["city"] = "Islamabad"
print(student)


student["marks"] = 95
print(student)


for key, value in student.items():
    print(f"{key}: {value}")


if student["marks"] >= 50:
    print("Student passed!")
else:
    print("Student failed!")
    