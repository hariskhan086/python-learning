# DAY 6: PYTHON REVISION AND PRACTICE




# QUESTION 1: VARIABLES AND DATA TYPES
# Create variables for a student's name, age, and marks.
# Print each value and its data type.

print("\n--- Question 1: Variables and Data Types ---")

student_name = "Ali"
age = 20
marks = 85.5
is_passed = True

print("Name:", student_name)
print("Age:", age)
print("Marks:", marks)
print("Passed:", is_passed)

print(type(student_name))
print(type(age))
print(type(marks))
print(type(is_passed))


# QUESTION 2: ARITHMETIC OPERATORS
# A shop sells a product for Rs. 250.
# A customer buys 4 products.
# Calculate the total bill, discount, and final bill.
# The customer receives a 10% discount.

print("\n--- Question 2: Arithmetic Operators ---")

price = 250
quantity = 4

total_bill = price * quantity
discount = total_bill * 0.10
final_bill = total_bill - discount

print("Price per product:", price)
print("Quantity:", quantity)
print("Total bill:", total_bill)
print("Discount:", discount)
print("Final bill:", final_bill)


# QUESTION 3: COMPARISON AND LOGICAL OPERATORS
# A student passes if marks are at least 50.
# A student gets a distinction if marks are at least 80.
# Check whether the student passed and earned distinction.

print("\n--- Question 3: Comparison and Logical Operators ---")

marks = 85

passed = marks >= 50
distinction = marks >= 80

print("Passed:", passed)
print("Distinction:", distinction)
print("Passed and distinction:", passed and distinction)
print("Failed:", marks < 50)


# QUESTION 4: IF, ELIF, AND ELSE
# Write a program to classify a number as positive,
# negative, or zero. Also check whether it is even or odd.

print("\n--- Question 4: Conditionals ---")

number = 17

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# QUESTION 5: NESTED IF
# A person can enter if their age is at least 18.
# If they are eligible, check whether they have an ID card.

print("\n--- Question 5: Nested If ---")

person_age = 21
has_id_card = True

if person_age >= 18:
    if has_id_card:
        print("Entry allowed.")
    else:
        print("Please bring your ID card.")
else:
    print("Entry denied: You must be at least 18.")


# QUESTION 6: FOR LOOP AND RANGE
# Print all numbers from 1 to 20.
# Calculate their sum.

print("\n--- Question 6: For Loop ---")

total = 0

for number in range(1, 21):
    print(number)
    total += number

print("Sum of numbers from 1 to 20:", total)


# QUESTION 7: WHILE LOOP
# Print numbers from 5 down to 1 using a while loop.

print("\n--- Question 7: While Loop ---")

count = 5

while count >= 1:
    print(count)
    count -= 1

print("Countdown complete!")


# QUESTION 8: MULTIPLICATION TABLE
# Print the multiplication table of a given number.

print("\n--- Question 8: Multiplication Table ---")

table_number = 7

for number in range(1, 11):
    result = table_number * number
    print(table_number, "x", number, "=", result)


# QUESTION 9: LIST BASICS
# Create a list of five favorite foods.
# Print the list, first item, last item, and list length.

print("\n--- Question 9: List Basics ---")

foods = ["Biryani", "Pizza", "Burger", "Pasta", "Karahi"]

print("All foods:", foods)
print("First food:", foods[0])
print("Last food:", foods[-1])
print("Number of foods:", len(foods))


# QUESTION 10: LIST METHODS
# Create a shopping list.
# Add an item, insert an item, remove an item,
# and remove the last item using pop().

print("\n--- Question 10: List Methods ---")

shopping_list = ["Milk", "Bread", "Eggs"]

print("Original list:", shopping_list)

shopping_list.append("Rice")
print("After append:", shopping_list)

shopping_list.insert(1, "Butter")
print("After insert:", shopping_list)

shopping_list.remove("Bread")
print("After remove:", shopping_list)

removed_item = shopping_list.pop()
print("Popped item:", removed_item)
print("Final shopping list:", shopping_list)


# QUESTION 11: LIST WITH LOOPS
# Print each number in a list.
# Calculate the total, highest, and lowest numbers.

print("\n--- Question 11: Lists and Loops ---")

numbers = [12, 45, 7, 89, 23]

for number in numbers:
    print("Number:", number)

print("Total:", sum(numbers))
print("Highest:", max(numbers))
print("Lowest:", min(numbers))
print("Length:", len(numbers))


# QUESTION 12: EVEN NUMBERS IN A LIST
# Print only the even numbers from a list.

print("\n--- Question 12: Even Numbers ---")

numbers = [10, 15, 22, 33, 40, 51, 64]

for number in numbers:
    if number % 2 == 0:
        print(number, "is even")


# QUESTION 13: COUNT POSITIVE AND NEGATIVE NUMBERS
# Count how many numbers are positive, negative, and zero.

print("\n--- Question 13: Number Counter ---")

numbers = [10, -5, 0, 8, -2, 15, 0, -7]

positive_count = 0
negative_count = 0
zero_count = 0

for number in numbers:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Zeros:", zero_count)


# QUESTION 14: FIND THE LARGEST NUMBER WITHOUT max()
# Find the largest number in a list using a loop.
# Do not use the built-in max() function.

print("\n--- Question 14: Find Largest Number ---")

numbers = [25, 78, 12, 95, 43]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest number:", largest)


# QUESTION 15: MINI PROJECT — MARKS ANALYZER
# Store five marks in a list.
# Calculate total and average.
# Display the highest and lowest marks.
# Print Pass if average is at least 50; otherwise Fail.

print("\n--- Question 15: Marks Analyzer ---")

marks = [78, 65, 90, 45, 82]

total_marks = sum(marks)
average_marks = total_marks / len(marks)
highest_marks = max(marks)
lowest_marks = min(marks)

print("Marks:", marks)
print("Total marks:", total_marks)
print("Average marks:", average_marks)
print("Highest marks:", highest_marks)
print("Lowest marks:", lowest_marks)

if average_marks >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("\nDay 6 revision completed!")
