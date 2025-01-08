from art import logo
import os
print(logo)

print("Welcome to the secret auction program")

bidding_dict = {}

bidding = True

def find_highest_bidder(bidding_dict):
    id = ""
    val = 0
    for key in bidding_dict:
        if bidding_dict[key] > val:
            id = key
            val = bidding_dict[key]
    # print(bidding_dict)
    print(f"The winner is {id} with a bid of ${val}")

while bidding:
    name = input("What is your name?: ")
    bid = int(input("What is you bid? $"))
    bidding_dict[name] = bid
    rebid = input("Are there any other bidders? Type 'yes' or 'no'.")
    if rebid == "no":
        bidding = False
    os.system('cls')


find_highest_bidder(bidding_dict=bidding_dict)