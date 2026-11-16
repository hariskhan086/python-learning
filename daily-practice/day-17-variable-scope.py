# Day 17: Python Variable Scope

# 1. Global variable
name = "Haris"

def greet():
    print("Hello", name)

greet()


# 2. Local variable
def student():
    age = 20
    print("Age:", age)

student()


# 3. Local and global variables
name = "Haris"

def show_name():
    name = "Ali"
    print("Inside function:", name)

show_name()
print("Outside function:", name)


# 4. Using the global keyword
score = 10

def update_score():
    global score
    score = 20

update_score()
print("Updated score:", score)


# 5. Using a local variable in a calculation
def calculate():
    number = 10
    result = number * 5
    return result

answer = calculate()
print("Answer:", answer)
