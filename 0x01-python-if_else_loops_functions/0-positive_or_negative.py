#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if (number > 0) and (number < 10):
    print("is positive")
elif (number > -10) and (number < 0):
    print("is negative")
else:
    print( "is zero")
