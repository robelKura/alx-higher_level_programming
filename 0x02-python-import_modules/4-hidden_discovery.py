#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    # dir() is used to find out which names a module defines
    for name in names:
        if name[:2] != "__":
            print(name)
