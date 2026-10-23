# DAY 8: PYTHON EXERCISE DAY


# QUESTION 1: SIMPLE CALCULATOR

print("\n--- Question 1: Simple Calculator ---")

num1 = 20
num2 = 5

print("First number:", num1)
print("Second number:", num2)
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Cannot divide by zero.")


# QUESTION 2: POSITIVE, NEGATIVE, ZERO, EVEN OR ODD


print("\n--- Question 2: Number Analyzer ---")

def analyze_number(number):
    if number > 0:
        sign = "Positive"
    elif number < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    if number % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    return sign, parity

result = analyze_number(-7)
print("Number analysis:", result)


# QUESTION 3: MULTIPLICATION TABLE

print("\n--- Question 3: Multiplication Table ---")

def multiplication_table(number):
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

multiplication_table(6)


# QUESTION 4: SUM OF NUMBERS


print("\n--- Question 4: Sum of Numbers ---")

def calculate_sum(n):
    total = 0

    for number in range(1, n + 1):
        total += number

    return total

print("Sum from 1 to 10:", calculate_sum(10))


# QUESTION 5: LIST STATISTICS


print("\n--- Question 5: List Statistics ---")

def list_statistics(numbers):
    if len(numbers) == 0:
        return None

    total = sum(numbers)
    average = total / len(numbers)
    highest = max(numbers)
    lowest = min(numbers)

    return total, average, highest, lowest

values = [12, 45, 7, 89, 23]

print("Numbers:", values)
print("Total, average, highest, lowest:")
print(list_statistics(values))


# QUESTION 6: COUNT EVEN AND ODD NUMBERS


print("\n--- Question 6: Count Even and Odd ---")

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

values = [10, 15, 22, 33, 40, 51, 64]

even, odd = count_even_odd(values)

print("Numbers:", values)
print("Even numbers:", even)
print("Odd numbers:", odd)


# QUESTION 7: REMOVE DUPLICATES FROM A LIST


print("\n--- Question 7: Remove Duplicates ---")

def remove_duplicates(items):
    unique_items = []

    for item in items:
        if item not in unique_items:
            unique_items.append(item)

    return unique_items

numbers = [1, 2, 2, 3, 4, 4, 5, 1]

print("Original list:", numbers)
print("Without duplicates:", remove_duplicates(numbers))


# QUESTION 8: STUDENT GRADE CALCULATOR


print("\n--- Question 8: Grade Calculator ---")

def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid marks"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

print("Marks 85:", calculate_grade(85))
print("Marks 74:", calculate_grade(74))
print("Marks 48:", calculate_grade(48))
print("Marks 110:", calculate_grade(110))


# QUESTION 9: PASSWORD ATTEMPT SIMULATOR


print("\n--- Question 9: Password Attempt Simulator ---")

correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password (practice: python123): ")
    attempts += 1

    if password == correct_password:
        print("Access granted!")
        break
    else:
        remaining = max_attempts - attempts

        if remaining > 0:
            print("Incorrect password. Attempts left:", remaining)
        else:
            print("Access denied. No attempts remaining.")


# QUESTION 10: MINI PROJECT — EXPENSE ANALYZER


print("\n--- Question 10: Expense Analyzer ---")

def calculate_total_expenses(expenses):
    return sum(expenses)

def calculate_average_expense(expenses):
    if len(expenses) == 0:
        return 0

    return sum(expenses) / len(expenses)

def find_largest_expense(expenses):
    if len(expenses) == 0:
        return None

    return max(expenses)

def count_large_expenses(expenses):
    count = 0

    for expense in expenses:
        if expense > 1000:
            count += 1

    return count

def check_budget(total):
    if total < 5000:
        return "Under budget"
    elif total == 5000:
        return "Budget reached"
    else:
        return "Over budget"

expenses = [500, 1200, 800, 2500, 600]

total = calculate_total_expenses(expenses)
average = calculate_average_expense(expenses)
largest = find_largest_expense(expenses)
large_expense_count = count_large_expenses(expenses)
budget_status = check_budget(total)

print("Expenses:", expenses)
print("Total expenses:", total)
print("Average expense:", average)
print("Largest expense:", largest)
print("Expenses above 1000:", large_expense_count)
print("Budget status:", budget_status)




print("\nDay 8 exercise practice completed!")