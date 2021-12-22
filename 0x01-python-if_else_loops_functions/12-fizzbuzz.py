#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100 +1):
        if i % 3:
            print("Fizz", end=" ")
        elif i % 5:
            print("Buzz", end=" ")
        elif i % 3 and i % 5:
            print("FizzBuzz", end=" ")
        else:
            print("{:d}".format(i), end=" ")
