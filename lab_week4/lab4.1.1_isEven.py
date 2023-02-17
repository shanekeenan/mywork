# Program prompts the user for an number 
# and indicates if the number is odd or even
# Author: Shane Keenan

number = int(input("enter an integer:"))
if (number % 2) == 0:
    print (f"{number} is an even number")
else:
    print(f"{number} is an odd number")