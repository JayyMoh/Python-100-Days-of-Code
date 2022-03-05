# Treasure Island

# ----- Greeting -----
print("Welcome to Treasure Island. Your mission is to find the treasure!\n")

# ----- Prompt starting direction -----
user_action = raw_input("Left or right: ").lower()
# print(user_action)

# ----- First Decision -----
if (user_action == "left"):
    user_action = raw_input("Swim or wait: ").lower()
else:
    print("You have fallen into a hole. Looks like it's game over.") 
    
# ----- Second Decision -----
if (user_action == "wait"):
    user_action = raw_input("You are faced with three doors. Which would you like to go through? Red, blue, or yellow: ").lower()
else:
    print("You've been attacked by trout! Game Over.")    
    
# ----- Third Decision -----
if (user_action == "blue"):
    print("Eaten by beasts! Game Over.")
elif (user_action == "red"):
    print("Burned by fire! Game Over.")
elif (user_action == "yellow"):
    print("You have found the treasure! You win!")
else:
    print("Game Over.")                
    
       