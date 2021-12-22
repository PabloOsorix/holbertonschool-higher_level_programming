#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number < 0:
    negative_number = number * -1
    last_digit = negative_number % 10

if last_digit > 5:
    if number < 0:
        last_digit = last_digit * -1
    print("Last digit of {:d} is {:d} and is greather than 5"
          .format(number, last_digit))
if last_digit < 6 and last_digit != 0:
    if number < 0:
        last_digit = last_digit * -1
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, last_digit))
if last_digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last_digit))
