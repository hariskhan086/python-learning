# Day 11: Functions with Arguments

# 1. Function with one argument
def greet(name):
    print("Hello", name)

greet("Haris")


# 2. Function with two arguments
def add(a, b):
    print("Sum:", a + b)

add(10, 5)


# 3. Function with a return value
def multiply(a, b):
    return a * b

result = multiply(4, 3)
print("Result:", result)


# 4. Function with a default argument
def welcome(name="Student"):
    print("Welcome", name)

welcome()
welcome("Haris")


# 5. Function with arguments and conditions
def check_number(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

check_number(8)
check_number(7)
