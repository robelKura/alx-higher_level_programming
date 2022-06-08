#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
#range() works like (first,last]
#The ord() function returns the number representing the unicode code of a specified character.
    if i != ord('q') and i != ord('e'):
        print('{:c}'.format(i), end='')
