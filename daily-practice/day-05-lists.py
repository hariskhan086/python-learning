
# Day 5: Python Lists

# Example 1: Create a list
fruits = ["apple", "banana", "mango", "orange"]
print(fruits)

# Example 2: Access list items
print(fruits[0])   # First item
print(fruits[1])   # Second item
print(fruits[-1])  # Last item

# Example 3: Change an item
fruits[1] = "grapes"
print(fruits)

# Example 4: Add items
fruits.append("banana")
fruits.insert(1, "watermelon")
print(fruits)

# Example 5: Remove items
fruits.remove("mango")
fruits.pop()  # Removes the last item
print(fruits)

# Example 6: Find the length
print("Number of fruits:", len(fruits))

# Example 7: Loop through a list
for fruit in fruits:
    print(fruit)

# Example 8: Numbers in a list
numbers = [10, 20, 30, 40, 50]

print("Total:", sum(numbers))
print("Smallest:", min(numbers))
print("Largest:", max(numbers))


