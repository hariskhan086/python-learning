
name1 = input("What is your name? ")
name2 = input("What is his/her name? ")

combined_string = (name1 + name2).lower()

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

true_score = t + r + u + e

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")

love_score = l + o + v + e

score = int(str(true_score) + str(love_score))

if score < 10 or score > 90:
    print(f"Your score is {score}, and you go together like Coke and Mentos!")
elif 40 <= score <= 50:
    print(f"Your score is {score}, and you are alright together.")
else:
    print(f"Your love score is {score}.")