# ===== Imports =====
import random
import os
# ===== Clear console =====
clear = lambda: os.system('cls')
# ===== Get random number between 1 - 100 =====
numbers = []
for number in range(1, 101):
    numbers.append(number)
def getNumber():
    random_number = random.choice(numbers)
    return random_number
# ===== Get game difficulty =====
def difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_level == "easy":
        guesses = 10
    elif difficulty_level == "hard":
        guesses = 5
    return guesses
# ===== Get users guess =====
def playerGuess():
    user_guess = int(input("Make a guess: "))
    print("==========================================================")
    return user_guess
# ===== Check users guess against number =====
def checkGuess(number, number_of_guesses):
    print("==========================================================")
    print(f"You have {number_of_guesses} attempts remaining to guess the number.")
    guess = playerGuess()
    num_guessed = False
    while number_of_guesses > 0 and not num_guessed:
        if guess > number:
            print(f"{guess} is too high.")
        elif guess < number:
            print(f"{guess} is too low.")
        elif guess == number:
            num_guessed = True
            print(f'{number} is the correct number, Congratulations!')
            print("-----------------------")
            playAgain()
        number_of_guesses -= 1
        if number_of_guesses == 0:
            print("You ran out of attempts.")
            playAgain()
        else:
            checkGuess(number, number_of_guesses)
# ===== Play again =====
def playAgain():
    choice = input("Type 'yes' if you want to play again or type 'no' to exit: ")
    if choice == 'yes':
        clear()
        game()
    elif choice == 'no':
        quit()
# ===== GAME =====
def game():
    # ===== Get random number =====
    random_number = getNumber()
    # ===== Welcome =====
    print("==========================================================")
    print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100")
    # ===== Get difficulty level =====
    number_of_guesses = difficulty()
    # ===== Check guess =====
    checkGuess(random_number, number_of_guesses)

# ===== Calling the game =====
game()