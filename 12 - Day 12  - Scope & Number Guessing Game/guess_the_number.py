from art import logo
import random
print(
    "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
)

print(logo)

easy = 10
hard = 5


def difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    no_of_attempts = 0
    if difficulty == "easy":
        no_of_attempts = easy
    elif difficulty == "hard":
        no_of_attempts = hard
    return no_of_attempts


def random_guess():
    return random.randint(1, 100)


def compare(user, guess):
    if user > guess:
        return "Too high"
    elif user < guess:
        return "Too low"


guess = random_guess()
no_of_attempts = difficulty()


while no_of_attempts:
    print(f"You have {no_of_attempts} remaining to guess the number")
    user = int(input("Make a guess: "))

    if user == guess:
        print("You guessed it!! Congrats you win!!")
        break
    else:
        print(compare(user, guess))

    no_of_attempts -= 1

    if no_of_attempts != 0:
        print("Guess again")

else:
    print("You have run out of guesses, you lose")
