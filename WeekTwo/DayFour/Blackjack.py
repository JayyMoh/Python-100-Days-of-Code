# ===== Imports =====
import random
import os
from Cards import deck
from Art import logo

# ===== Players hand =====
players_hand = []
# ===== Computers hand =====
dealers_hand = []
# ===== Clear console =====
clear = lambda: os.system('cls')
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
    # ===== Show table =====
    runningTotal()
    # ===== Run totals =====
    dealers_total(dealers_hand)
    players_total(players_hand)
    # ===== Compare for win in opening deal =====
    checkNatural(dealers_total, players_total)
# ===== Get hand values =====
def dealers_total(hand):
    dealers_hand_value = 0
    for card in hand:
        dealers_hand_value += deck[card]
    return dealers_hand_value

def players_total(hand):
    players_hand_value = 0
    for card in hand:
        players_hand_value += deck[card]
    return players_hand_value
# ===== Give the player their hand value and dealers card =====
def runningTotal():
    # ===== Show players hand =====
    print("================================================================")
    print(f"Your Hand: {players_hand}, current total: {players_total(players_hand)}")
    print(f"Dealers first card: {dealers_hand[0]}")
    print("================================================================")
# ===== Present the player total and dealer full hand =====
def finalShow():
    print("================================================================")
    print(f"Your final hand: {players_hand}, final total: {players_total(players_hand)}")
    print(f"Dealers final hand: {dealers_hand}, final score: {dealers_total(dealers_hand)}")
    print("================================================================")
# ===== Check for natural on opening deal =====
def checkNatural(dealer, player):
    dealer = dealers_total(dealers_hand)
    player = players_total(players_hand)
    if dealer == 21 and player != 21:
        print(f"The dealer wins with a natural: {dealer}")
        playAgain()   
    elif player == 21 and dealer != 21:
        print(f"You win with a natural: {player}")
        playAgain()   
    elif player == 21 and dealer == 21:
        print(f"Stand off with! You both got naturals: {dealer}")
        playAgain()   
    elif player > 21:
        print(f"You busted with a total of {player}. Dealer wins.")
        playAgain()   
    elif dealer > 21:
        print(f"Dealer busted with a total of {dealer}. You win.") 
        playAgain()   
# ===== Hit function =====
def hit(player):
    deal(1, players_hand)
    player = players_total(players_hand)
    if player > 21:
        finalShow()
        print(f"Bust! You lost with a total of: {player}")
        playAgain()   
    else:
        runningTotal()
        hitOrStand()    
# ===== Compare hands =====
def stand(dealer, player):
    # ===== Dealer draws one more if under 17 =====
    if dealers_total(dealers_hand) < 17 and len(dealers_hand) < 3:
        deal(1, dealers_hand)
        dealers_total(dealers_hand)
    # ===== Get and compare totals =====
    dealer = dealers_total(dealers_hand)
    player = players_total(players_hand)
    dealer_to_21 = 21 - dealer
    player_to_21 = 21 - player
    finalShow()
    if dealer_to_21 < player_to_21 and dealer <= 21:
        print(f"You had {player}. The dealer wins with a total of {dealer}.")
    elif player_to_21 < dealer_to_21 and player <= 21:
        print(f"The dealer had {dealer}. You win with a total of {player}!")
    elif player_to_21 == dealer_to_21 and player <= 21 and dealer <= 21:
        print(f"We have a standoff! You both have a total of {dealer}.")
    elif dealer > 21:
        print(f"Dealer bust! You win.")    
    playAgain()  
# ===== Ask the player to hit or stand =====    
def hitOrStand():
    choice = input("Would you like to 'hit' or 'stand'?: ")
    if choice == 'hit':
        hit(players_hand)
    elif choice == 'stand':
        stand(dealers_hand, players_hand)
# ===== Check if player wants to go again =====
def playAgain():
    choice = input("Type 'yes' to play again or 'no' to exit: ")
    if choice == 'yes':
        clearHands(players_hand, dealers_hand)
        clear()
        blackjack()
    elif choice == 'no':
        return 
# ===== Clear the tables hands for new game =====
def clearHands(hand1, hand2):
    hand1.clear()
    hand2.clear()
# ===== Game function =====
def blackjack():
    # ===== Game logo =====
    print("================================================================")
    print(logo)
    # ===== Deal cards =====
    openingDeal()
    # ===== Ask to hit or stand =====
    hitOrStand()
# ===== Prompt user to play =====    
play = input("Would you like to play a game of blackjack? 'y' or 'n'?: ")
# ===== Start the game =====
if play == "y":
    blackjack()
