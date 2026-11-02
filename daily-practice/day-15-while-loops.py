# Day 15: Python While Loops


number = 1

while number <= 5:
    print(number)
    number += 1


count = 5

while count > 0:
    print(count)
    count -= 1

print("Finished!")


password = ""

while password != "python123":
    password = input("Enter the password: ")

print("Access granted!")



number = 1
total = 0

while number <= 5:
    total += number
    number += 1

print("Total:", total)



number = 1

while number <= 10:
    if number == 6:
        break

    print(number)
    number += 1
    