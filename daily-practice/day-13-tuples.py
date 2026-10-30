# Day 13: Python Tuples

# 1. Creating a tuple
fruits = ("apple", "banana", "mango")
print(fruits)

# 2. Accessing tuple elements
print(fruits[0])
print(fruits[1])

# 3. Accessing the last element
print(fruits[-1])

# 4. Finding the length
print(len(fruits))

# 5. Looping through a tuple
for fruit in fruits:
    print(fruit)

# 6. Checking if an item exists
if "apple" in fruits:
    print("Apple is available")

# 7. Counting an element
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))

# 8. Finding the index
print(numbers.index(20))

# 9. A tuple with one element
single_item = ("apple",)
print(single_item)

# 10. Converting a list into a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print(my_tuple)