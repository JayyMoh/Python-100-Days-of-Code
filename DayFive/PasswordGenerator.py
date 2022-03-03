import random

# ----- Starting lists -----
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ----- Prompt the user and store input -----
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# ----- Password Variables ----- 
password_list = []
password_str=''

# ----- Get a random letter from the letters list -----
def getRandLetter():
    rand_letter = random.randrange(0, len(letters) - 1)
    password_list.append(letters[rand_letter])
    return password_list

# ----- Get a random number from the numbers list -----
def getRandNum():
    rand_number = random.randrange(0, len(numbers) - 1)
    password_list.append(numbers[rand_number])
    return password_list

# ----- Get a random symbol from the symbols list -----
def getRandSymbol():
    rand_symbol = random.randrange(0, len(symbols) - 1)
    password_list.append(symbols[rand_symbol])
    return password_list

# ----- Allows users input to determine how many times the function runs -----
for letter in range(0, nr_letters):
    getRandLetter()

for symbol in range(0, nr_symbols):
    getRandSymbol()

for number in range(0, nr_numbers):
    getRandNum()

# ----- Shuffle the password list -----
random.shuffle(password_list)

# ----- Convert password list to string -----
for item in password_list:
    password_str += item

# ----- Print password for the user -----
print(f"Generated Password: {password_str}")