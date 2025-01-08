import random
import os
from hangman_words import word_list
from hangman_art import (stages, logo)

# test word list
# word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# testing code
# print(f"Psst, the solution is {chosen_word}.")
print(logo)
display = ["_" for i in chosen_word]
print(f"{' '.join(display)}")
print("\n")
lives = 6
end_of_game = False
while not end_of_game:
    letter = input("Guess a letter: ").lower()
    os.system('cls')
    if letter not in chosen_word:
        lives -= 1
        print(f"You guessed {letter}, it is not in the word. You lose a life.")
    elif letter in display:
        print(f"You have already guessed the letter {letter}")
    else:
        for i in range(len(chosen_word)):
            if chosen_word[i] == letter:
                display[i] = letter
    print(f"{' '.join(display)}")
    print(stages[lives])
    if lives == 0:
        end_of_game = True
        print(f"The chosend word was : {chosen_word}")
        print("You lose!")
    if "_" not in display:
        end_of_game = True
        print("You win!")
