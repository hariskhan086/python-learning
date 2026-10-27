# Day 10: Python Dictionaries


student = {
    "name": "Haris",
    "age": 20,
    "marks": 85
}

print(student)

print(student["name"])
print(student["marks"])


student["city"] = "Peshawar"
print(student)


student["marks"] = 90
print(student)


student.pop("age")
print(student)


for key, value in student.items():
    print(key, ":", value)


if "name" in student:
    print("Name exists in the dictionary")
    