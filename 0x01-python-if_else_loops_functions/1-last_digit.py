#!/usr/bin/python3
import random
number = random. randint(-10000, 10000)
_digit = abs(number) % 10
if number < 0:
    _digit = -_digit
print("Last digit of {} is {} and is ".format(number, _digit), end="")
if _digit > 5:
    print("greater than 5")
elif _digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
