# Tip Calculator

# ----- Greeting -----
print('Welcome to the tip calculator')

# ----- Assign cost to variable -----
cost = input('What was the total bill? $')

# ----- Assign n people paying -----
split = input('How many people to split the bill? ')

# ----- Assign tip percentage -----
tip = input('What percentage tip would you like to give? ')

# ----- Calculate tip amount -----
split_Amount = cost / split

calculated_Tip = str((split_Amount * tip) / 100)


# ----- Output tip amount -----
if split == 1:
    print('You should pay: $' + calculated_Tip)
    
else:
    print('Each person should pay: $' + calculated_Tip)