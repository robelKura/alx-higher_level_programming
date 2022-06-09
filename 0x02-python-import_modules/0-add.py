#!/usr/bin/python3
if __name__ == "__main__":
    # is used to execute a code only if the file was run directly,not imported.
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
