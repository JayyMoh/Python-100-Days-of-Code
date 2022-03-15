############DEBUGGING#####################
#================================================================
# # # Describe Problem # # #
# ---------------------------------------------------------------
# Original function had a range of (1, 20). The print condition
# was to pring if 'i' == 20. Range of (1, 20) is every number from
# 1 - 19 so it excludes the top number. Thus 'i' can never be 20.
# We can change the range to (1, 21) if we want the print to fire
# in our function.
# ---------------------------------------------------------------
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()
#================================================================


#================================================================
# # # Reproduce the Bug # # #
# ---------------------------------------------------------------
# The bug would rancomly happen when running the code. I added a
# print statement to display what the programming was reading for
# dice_num to make sure it was pulling the proper image from the
# list. As was pretty obvious from just looking at the code, it
# was not correct. Changed the randint range from (1,6) to (0,5).
# The original range excluded our 0 index of dice_imgs as well
# as tried to pull from a non existing 6 index
# ---------------------------------------------------------------
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(f"Dice number: {dice_num}")
# print(dice_imgs[dice_num])
#================================================================

#================================================================
# # # Play Computer # # #
# ---------------------------------------------------------------
# The bug is that the year range in the if statement does not
# include the edge cases. You could either add '=' to each gt and
# lt condition or you could adjust the edge cases a year. I will
# be adding '=' to the conditions.
# ---------------------------------------------------------------
# year = int(input("What's your year of birth?"))
# if year >= 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
#================================================================

#================================================================
# # # Fix the Errors # # #
# ---------------------------------------------------------------
# Original print statement needed an indent to properly be inside
# the if statment block. Also need to format the age input as an 
# int so that we can compare it with another int. Lastly, the
# print statement is formatted to be an f string without the f at
# the start. I have added the 'f'. 
# ---------------------------------------------------------------
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")
#================================================================

#================================================================
# # # Print is Your Friend # # #
# ---------------------------------------------------------------
# Used print statements to figure out which value was not storing
# properly. Word_per_page was staying at 0. After evaluating the
# word_per_page line, I realized that there was an extra '='. Once
# removed, things tracked properly.
# ---------------------------------------------------------------
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(f"Pages: {pages}")
# word_per_page = int(input("Number of words per page: "))
# print(f"Words per page: {word_per_page}")
# total_words = pages * word_per_page
# print(total_words)
#================================================================

#================================================================
# # # Use a Debugger # # #
# ---------------------------------------------------------------
# The append statement was not in the for loop block therefore it was
# taking the value of the last new_item and placing it as b_list.
# Indenting the append step into the for loop solved this bug.
# ---------------------------------------------------------------
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
#================================================================
