print('Welcome to the Tip Calculator')
bill = input('What was the total bill? \n')
tip = input('What percentage tip would you like to give?  10, 12, or 15 \n')
people = input('How many people to split the bill? \n')

itip = int(tip) / 100 + 1
ibill = int(bill)
ipeople = int(people)

till = ibill * itip
total = till / ipeople
stotal = str(total)
print('Each person should pay: ' + stotal)

###

# Lesson 1 -
# String and Int Conversion
# Lesson 2 -
# Concatenation of Strings opposed to INT and Float
# Lesson 3 -
# Cutting Down