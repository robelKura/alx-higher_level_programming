#!/usr/bin/python3
i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    # the third value in range(1st,2nd.3rd) is weigth of the jump.
    print("{}".format(chr(c - i)), end="")
    # one-liner ternary operator can be use to represent ff
    # if i=0:
    # i=32
    # else:
    # i=0
    i = 32 if i == 0 else 0
