#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10

print(f"Last digit of {number} is {lastDigit}",end=" and is ")
#the print function appends new lines
#end=" " appends white space instead of a newline

if lastDigit > 5:
    print("greater than 5")
elif lastDigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
