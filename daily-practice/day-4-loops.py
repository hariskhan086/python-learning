
# Day 4: Python Loops

# Example 1: A simple for loop
for i in range(1, 6):
    print(i)


# Example 2: Loop through a list
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# Example 3: A while loop
count = 1

while count <= 5:
    print(count)
    count += 1


# Example 4: Sum of numbers from 1 to 10
total = 0

for number in range(1, 11):
    total += number

print("Total:", total)


# Example 5: Print a multiplication table
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

