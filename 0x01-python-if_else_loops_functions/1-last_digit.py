#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_digit = number % 10
elif number < 0:
    last_digit = number % -10

if last_digit > 5:
    string = 'Last digit of {0} is {1} and is greater 5'
elif last_digit < 6 and last_digit != 0:
    string = 'Last digit of {0} is {1} and is less than 6 and not 0'
elif last_digit == 0:
    string = 'Last digit of {0} is {1} and is 0'

print(string.format(number, last_digit))
