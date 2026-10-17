
# Day 3: Python Conditional Statements

# Example 1: if and else
age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# Example 2: if, elif, and else
marks = 75

if marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Needs improvement")


# Example 3: Check even or odd
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Example 4: Nested if
age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("You are too young")

