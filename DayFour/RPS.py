# Rock Paper Scissors

# ----- Imports -----
import random

# ----- Greeting -----
print("Welcome to Rock Paper Scissors!\n\nThe Rules of the game are simple. You will play head-to-head with the computer. You will each choose one of rock, paper, or scissors at the same time.\n\n - Rock wins against Scissors\n - Paper wins against Rock\n - Scissors wins against Paper\n")


# ----- Start game function -----
def startGame():
    # Get the users hand
    users_hand = raw_input("Choose your hand: Type 'R' for Rock, 'P' for Paper, or 'S' for Scissors: ").lower()
    
    # Get the computers hand
    computers_hand = random.choice(['r', 'p', 's'])
    
    # check for win 
    if (computers_hand == users_hand):
        print(f"You both chose {users_hand}. It's a tie.")    
    elif (users_hand == "r" and computers_hand == "s") or (users_hand == "s" and computers_hand == "p") or (users_hand == "p" and computers_hand == "r"):
        print(f"You: {users_hand}\nComputer: {computers_hand}\nYou Win!")
    else:
        print(f"You: {users_hand}\nComputer: {computers_hand}\nThe computer won! Better luck next time.")     
    
        
startGame()    


          
    
