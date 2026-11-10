# Day 16: Functions with Return Values


def greet():
    return "Hello Haris!"

message = greet()
print(message)



def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)


def square(number):
    return number * number

print("Square:", square(5))



def check_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

answer = check_number(7)
print(answer)



def calculate_percentage(obtained, total):
    return (obtained / total) * 100

percentage = calculate_percentage(450, 500)
print(f"Percentage: {percentage}%")
