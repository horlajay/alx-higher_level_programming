#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_di = abs(number) % 10
if last_di < 0:
    last_di = -last_di
print("Last digit of {} is {} and is ".format(number, last_di), end="")
if last_di > 5:
    print("greater than 5")
elif last_di == 0:
    print("0")
else:
    print("less than 6 and not 0")
