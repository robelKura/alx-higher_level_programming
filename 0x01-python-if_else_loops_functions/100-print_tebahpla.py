#!/usr/bin/python3
i = 0
for c in range(ord('z'), ord('a') - 1, -1):
#the third value in range(1st,2nd.3rd) is weigth of the jump.
    print("{}".format(chr(c - i)), end="")
    i = 32 if i == 0 else 0 
    # the following code is a one-liner ternary operator equivalent to
    # if i=0:
    #	i=32
    # else:
    #	i=0
