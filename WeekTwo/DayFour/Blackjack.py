# ===== Blackjack =====

# ===== import =====
import random

# ===== Deck of cards =====
deck = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

# ===== Players hand =====
players_hand = []

# ===== Computers hand =====
dealers_hand = []

# ===== Deal a card =====
def deal(num_of_cards, user):
    cards_dealt = 0
    while cards_dealt < num_of_cards:
        card = random.choice(list(deck))
        user.append(card)
        cards_dealt += 1
        
# ===== Opening Deal =====
def openingDeal():
    # ===== Starting deal =====
    deal(2, dealers_hand)
    deal(2, players_hand)
    compare(dealers_hand, players_hand)
    # ===== Show players hand =====
    print("\nYour Hand: ")
    print(players_hand)
 

# ===== Compare hands =====
def compare(hand1, hand2):
    hand1_value = 0
    hand2_value = 0
    for card in hand1:
        hand1_value += deck[card]
    print(hand1_value)
        
    for card in hand2:
        hand2_value += deck[card]
    print(hand2_value)
        
# ===== Hit function =====
def hit():
    deal(1, players_hand)        
    
# ===== Game function =====
def blackjack():
    openingDeal()
    # ===== Ask to hit or stand =====
    hit_or_stay = raw_input("\n Would you like to 'hit' or 'stay'?: ")
    if hit_or_stay == 'hit':
        hit()
    print(players_hand)    
    

# ===== Prompt user to play =====    
play = raw_input("Would you like to play a game of blackjack? 'y' or 'n'?: ")


# ===== Start the game =====
if play == "y":
    blackjack()
