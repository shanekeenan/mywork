# This program reads in 
# a students percentage 
# and prints out the 
# corresponding grade

# modified - 

# In practice the percentages are rounded ie 69.5 gets rounded to 70 so is 
# equal to a Distinction. 
# How would you modify the program in 1 to deal with this?
# I see two ways.

# solution - with the function round() floats are rounded up from X.5 - X.9 so need to round down - coverting to an int 
#  help from https://www.pythonpool.com/python-round-down/

# also don't round the input !? 

# Author: Shane Keenan


import math
percentage = float(input("Enter the percentage: "))


#percentage = round(percentage)

#      converting to an int will round down 
 
#percentage = int(percentage)

#       using math.floor() with import math also works here 

# percentage = math.floor(percentage)

#passing the absolute value into the if/else statement seems to do the trick as well 
#percentage = abs(percentage)

print ('{} {}' .format((percentage), type(percentage))) # this is for dubugging

# Be careful with the or operator boolean algebra can be tricky
if percentage < 0 or percentage > 100:
    # Later we will show you error handling
    # This should really throw an error
    print ("Please enter a number between 0 and 100")
elif percentage < 40: # we know it is greater than 0
    print ("Fail")
elif percentage < 50: # between 40 and 49
    print ("Pass")
elif percentage < 60: # between 50 and 59
    print ("Merit1")
elif percentage < 70: # between 60 and 69
    print ("Merit2")
else: # the only option left is betwen 70 and 100
    print ("Distinction")