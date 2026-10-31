# Hangman Word Guessing Game

import random

word_list = ["apple", "beautiful", "mango"]
lives = 6
chosen_word = random.choice(word_list)

display = ["_"] * len(chosen_word)
guessed_letters = []

print("Welcome to Hangman!")
print(display)

game_over = False

while not game_over:
    guess_letter = input("Guess a letter: ").lower()

    if len(guess_letter) != 1 or not guess_letter.isalpha():
        print("Please enter one letter.")
        continue

    if guess_letter in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess_letter)

    if guess_letter not in chosen_word:
        lives -= 1
        print(f"Wrong guess! Lives remaining: {lives}")
    else:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess_letter:
                display[position] = guess_letter

    print(" ".join(display))

    if "_" not in display:
        print("You win!")
        print(f"The word was: {chosen_word}")
        game_over = True
    elif lives == 0:
        print("You lose!")
        print(f"The word was: {chosen_word}")
        game_over = True
        