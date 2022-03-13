# ===== Blackjack =====

# ===== Deck of cards =====
deck = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',    
]


# ===== Deal a card =====
def deal():
    print("dealing cards...")

def blackjack():
    print("welcome to blackjack")

# ===== Prompt user to play =====    
play = raw_input("Would you like to play a game of blackjack? 'y' or 'n'?: ")

# ===== Players hand =====
players_hand = []

# ===== Computers hand =====
computers_hand = []

# ===== Start the game =====
if play == "y":
    blackjack()
