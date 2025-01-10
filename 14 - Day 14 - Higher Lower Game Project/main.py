import os
from art import logo
from art import vs
import random
from game_data import data





def compare_choice(choice):
    if  A["follower_count"] > B["follower_count"]:
        return choice == "A"
    else:
        return choice == "B"



B = random.choice(data)


count = 0
will_continue = True
while will_continue:
    A = B
    B = random.choice(data)
    if A==B:
        B = random.choice(data)

    print(logo)
    if count:
        print(f"You are right and the current score is {count}")

    print(f"Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}.")

    print(vs)

    print(f"Against B: {B["name"]}, a {B["description"]}, from {B["country"]}.")
    choice = input("Who has more followers? Type 'A' or 'B': ")

    os.system('clear')

    result = compare_choice(choice)
    if result:
        count +=1

    else:
        will_continue = False
        print(logo)
        print(f"Sorry thay was wrong, Your final score is {count}")
