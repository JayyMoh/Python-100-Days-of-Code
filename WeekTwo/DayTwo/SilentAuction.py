# ===== Silent Auction =====
print("Welcome to the silent auction program.")

# ===== Continue auction condition =====
continue_auction = True

# ===== Bids list =====
bids = {}

while continue_auction is True:
    # ===== Get name =====
    user_name = raw_input("What is your name?: ")
    print(user_name)
    # ===== Get bid =====
    user_bid = int(raw_input("What is your bid?: "))
    print(user_bid)
    # ===== Add bid to bids list =====
    bids[user_name] = user_bid
    print(bids)
    # ===== Check for more bidders =====
    more_bidders = raw_input("Are there any more bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == "no":
        continue_auction = False
        # Find the winning bid and print it out
        winner = max(bids, key=bids.get)
        winning_bid = bids[winner]
        print("The winner is " + winner + " with a bid of $" + winning_bid + ".")
        
    elif more_bidders == "yes":
        # clear the console    
        print("You need to clear the console")
