


# QUESTION 1: CREATE A SIMPLE FUNCTION

print("\n--- Question 1: Simple Function ---")

def greet():
    print("Hello, Python learner!")

greet()
greet()
greet()


# QUESTION 2: FUNCTION WITH PARAMETERS


print("\n--- Question 2: Parameters ---")

def greet_user(name):
    print("Hello,", name + "! Welcome to Python.")

greet_user("Haris")
greet_user("Ali")
greet_user("Ahmed")


# QUESTION 3: FUNCTION WITH RETURN VALUE


print("\n--- Question 3: Return Values ---")

def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)


# QUESTION 4: ARITHMETIC FUNCTIONS


print("\n--- Question 4: Arithmetic Functions ---")

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

print("Addition:", addition(15, 5))
print("Subtraction:", subtraction(15, 5))
print("Multiplication:", multiplication(15, 5))
print("Division:", division(15, 5))
print("Division by zero:", division(15, 0))


# QUESTION 5: CHECK EVEN OR ODD


print("\n--- Question 5: Even or Odd ---")

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("10 is:", check_even_odd(10))
print("7 is:", check_even_odd(7))
print("0 is:", check_even_odd(0))


# QUESTION 6: FIND THE LARGEST NUMBER IN A LIST


print("\n--- Question 6: Largest Number ---")

def find_largest(numbers):
    if len(numbers) == 0:
        return None

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest

values = [25, 78, 12, 95, 43]

print("Numbers:", values)
print("Largest number:", find_largest(values))
print("Empty list:", find_largest([]))


# QUESTION 7: CALCULATE THE AVERAGE


print("\n--- Question 7: Calculate Average ---")

def calculate_average(numbers):
    if len(numbers) == 0:
        return None

    total = sum(numbers)
    average = total / len(numbers)

    return average

marks = [80, 75, 90, 65, 85]

print("Marks:", marks)
print("Average:", calculate_average(marks))
print("Empty list:", calculate_average([]))


# QUESTION 8: DEFAULT PARAMETERS


print("\n--- Question 8: Default Parameters ---")

def greet_user_with_message(name, greeting="Hello"):
    return greeting + ", " + name + "!"

print(greet_user_with_message("Haris"))
print(greet_user_with_message("Ali", "Good morning"))
print(greet_user_with_message("Ahmed", "Welcome"))


# QUESTION 9: COUNT EVEN NUMBERS


print("\n--- Question 9: Count Even Numbers ---")

def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1

    return count

numbers = [10, 15, 22, 33, 40, 51, 64]

print("Numbers:", numbers)
print("Count of even numbers:", count_even(numbers))


# QUESTION 10: MINI PROJECT — STUDENT MARKS ANALYZER


print("\n--- Question 10: Student Marks Analyzer ---")

def calculate_total(marks):
    return sum(marks)

def calculate_average_mark(marks):
    if len(marks) == 0:
        return None

    return calculate_total(marks) / len(marks)

def find_highest_mark(marks):
    if len(marks) == 0:
        return None

    return max(marks)

def check_result(marks):
    average = calculate_average_mark(marks)

    if average is None:
        return "No marks available"

    if average >= 50:
        return "PASS"
    else:
        return "FAIL"


student_marks = [78, 65, 90, 45, 82]

print("Student marks:", student_marks)
print("Total marks:", calculate_total(student_marks))
print("Average marks:", calculate_average_mark(student_marks))
print("Highest mark:", find_highest_mark(student_marks))
print("Final result:", check_result(student_marks))




