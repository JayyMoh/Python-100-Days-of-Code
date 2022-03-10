from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES
from Alphabet import alphabet
from Art import logo

# ===== Caesar Cipher =====
print("======================================================================")
print(logo)
print("====================================================================== \n")

# ===== While loop condition =====
end_cipher = False

while not end_cipher:
    # ===== Get users input choice =====
    user_action = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

    # ===== Get users message =====
    user_message = input("Type your message: ")

    # ===== Get shift amount =====
    shift = int(input("Type the shift number: "))
    
    # ===== Catch numbers greater than alphabet length =====
    shift = shift % 26

    # ===== Decode function =====
    def decode(str):
        decoded_word = ""
        for letter in user_message:
            if letter in alphabet:
                letter_position = alphabet.index(letter)
                new_letter = alphabet[letter_position - shift]
                decoded_word += new_letter
            else:
                decoded_word += letter

        print(decoded_word)

    # ===== Encode function =====
    def encode(str):
        encoded_word = ""
        for letter in user_message:
            if letter in alphabet:
                letter_position = alphabet.index(letter)
                new_letter = alphabet[letter_position + shift]
                encoded_word += new_letter
            else:
                encoded_word += letter

            
        print(encoded_word)

    # ===== Choose encode or decode based on user action =====
    if user_action == 'encode':
        encode(user_message)
    elif user_action == 'decode':
        decode(user_message) 
    
    # ===== Ask the user to go again =====
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no': ")

    # ===== Decide to go again or not =====
    if go_again == 'no':
        end_cipher = True
    elif go_again == 'yes':
        end_cipher = False 

print("\n======================================================================\n")

