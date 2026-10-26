# DAY 9: PYTHON SETS



# QUESTION 1: CREATE A SET


print("\n--- Question 1: Create a Set ---")

fruits = {"apple", "banana", "mango", "orange", "grapes"}

print("Fruits:", fruits)
print("Number of fruits:", len(fruits))


# QUESTION 2: REMOVE DUPLICATES


print("\n--- Question 2: Remove Duplicates ---")

numbers = [10, 20, 10, 30, 20, 40, 50, 30]

unique_numbers = set(numbers)

print("Original list:", numbers)
print("Unique numbers:", unique_numbers)
print("Number of unique values:", len(unique_numbers))


# QUESTION 3: ADD ELEMENTS TO A SET


print("\n--- Question 3: Add Elements ---")

colours = {"red", "blue", "green"}

colours.add("yellow")
print("After add:", colours)

colours.update(["black", "white"])
print("After update:", colours)

colours.add("red")
print("After adding red again:", colours)


# QUESTION 4: REMOVE ELEMENTS FROM A SET


print("\n--- Question 4: Remove Elements ---")

animals = {"cat", "dog", "rabbit", "horse"}

animals.remove("dog")
print("After remove:", animals)

animals.discard("lion")
print("After discard of missing item:", animals)

removed_animal = animals.pop()
print("Removed by pop:", removed_animal)
print("Remaining animals:", animals)


animals.clear()
print("After clear:", animals)



# QUESTION 5: CHECK MEMBERSHIP


print("\n--- Question 5: Membership ---")

languages = {"Python", "Java", "C++", "JavaScript"}

print("Python available:", "Python" in languages)
print("Ruby available:", "Ruby" in languages)
print("Ruby not available:", "Ruby" not in languages)



# QUESTION 6: SET UNION


print("\n--- Question 6: Union ---")

python_students = {"Ali", "Haris", "Sara", "Ahmed"}
java_students = {"Sara", "Ahmed", "Usman", "Ayesha"}

all_students = python_students | java_students

print("Python students:", python_students)
print("Java students:", java_students)
print("All unique students:", all_students)








