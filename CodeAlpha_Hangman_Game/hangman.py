# Hangman Game

import random

word_list = ["python", "computer", "student", "project", "coding"]


secret_word = random.choice(word_list)


display_word = []

for letter in secret_word:
    display_word.append("_")


wrong_guesses = 0
max_wrong_guesses = 6

guessed_letters = []

print("=================================")
print("      WELCOME TO HANGMAN")
print("=================================")


while wrong_guesses < max_wrong_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)
    print("Guessed letters:", guessed_letters)

    
    guess = input("Enter a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    
    if guess in secret_word:

        print("Correct Guess!")

        
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess

    else:
        print("Wrong Guess!")
        wrong_guesses += 1

print("\n=================================")

if "_" not in display_word:
    print("Congratulations! You Won!")
    print("The word was:", secret_word)
else:
    print("Game Over!")
    print("You Lost!")
    print("The word was:", secret_word)

print("=================================")