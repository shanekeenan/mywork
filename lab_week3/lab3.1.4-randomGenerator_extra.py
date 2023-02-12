# randomGenerator.py
#  program that prints out a random number between 1 and 10
# Author: Andrew Beatty

import random

max_range = int(input("Enter the upper range for the random number generator: "))


number = random.randint(1, max_range)


print("here is a random number {}".format(number))

