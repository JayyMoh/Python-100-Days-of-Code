import random
import HangmanWords
import HangmanArt
# ===== Welcome to Hangman =====
print('=================================================')
print(HangmanArt.logo)
print('================================================= \n')

# ===== Lives varialbes =====
lives = 6

# ===== Guessed letters =====
guessed_letters = []
# ===== Pull a random word from word list =====
chosen_word = random.choice(HangmanWords.word_list)
# print(f"The chosen word is: {chosen_word}")

# ===== Create the hidden word =====
hidden_word = []
for letter in chosen_word:
    hidden_word.append('_')

# ===== Create loop condition =====
end_of_game = False

# ===== Game loop =====
while not end_of_game:

    # ===== Users guess =====
    guess = input('Guess a letter: ').lower()

    # ===== Catch duiplicate guess =====
    if guess in guessed_letters and guess in chosen_word:
        print(f'You have already guessed: {guess}')
    elif guess in guessed_letters and guess not in chosen_word:
        lives -= 1
        print(f'You have already guessed: {guess}')

    guessed_letters.append(guess)
    
    # ===== Check for matching =====
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            hidden_word[position] = letter

    # ===== Check lives =====
    if guess not in chosen_word:
        lives -= 1
        print(HangmanArt.stages[lives])
    else:
        print(HangmanArt.stages[lives])

    print(hidden_word)
    print('================================================= \n')
    # ===== Check win condition =====
    if '_' not in hidden_word:
        end_of_game = True
        print('You Win!')
    elif lives == 0:
        end_of_game = True
        print(f'Oh no! The correct word was {chosen_word}. Better luck next time.')





