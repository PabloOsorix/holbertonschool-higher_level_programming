#!/usr/bin/python3
def uppercase(str):
   for i in str:
       if ord(i)is not range(97,122):
   	   print("{:c}".format(ord(i)), end="")
       elif ord(i) >= 97 and ord(i) <= 122:
	   print("{:c}".format(ord(i) - 32), end="")
