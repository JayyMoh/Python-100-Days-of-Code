# ===== Silent Auction =====

# ===== Imports =====
import os
from Art import logo

# ===== Clear console function =====
clear = lambda: os.system('cls')

# ===== Continue auction condition =====
continue_auction = True

# ===== Bids list =====
bids = {}

# ===== Auction loop =====
while continue_auction is True:
    # ===== Welcome =====
    print("===============================================================")
    print(logo)
    print("===============================================================\n")
    print("Welcome to the silent auction.\n")
    print("===============================================================")

    # ===== Get name =====
    user_name = input("What is your name?: ")
    # print(user_name)

    # ===== Get bid =====
    user_bid = int(input("What is your bid?: "))
    # print(user_bid)

    # ===== Add bid to bids list =====
    bids[user_name] = user_bid
    # print(bids)

    # ===== Check for more bidders =====
    more_bidders = input("Are there any more bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == "no":
        continue_auction = False
        # ===== Find the winning bid and print it out =====
        winner = max(bids, key=bids.get)
        winning_bid = bids[winner]
        clear()
        print(f"The winner is {winner} with a bid of ${winning_bid}.")
    elif more_bidders == "yes":
        # ===== Clear the console =====
        clear()
