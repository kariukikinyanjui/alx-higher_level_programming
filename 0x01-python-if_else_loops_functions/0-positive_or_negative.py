#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number >= 0:
    if number == 0:
        print(number, 'is zero')
    else:
        print(number, 'is positive')
else:
    print(number, 'is negative')
