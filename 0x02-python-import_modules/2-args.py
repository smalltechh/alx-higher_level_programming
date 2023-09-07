#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    varCount = len(sys.argv) - 1

    if varCount == 0:
        print("0 arguments.")

    elif varCount == 1:
        print("1 argument:")

    else:
        print("{} arguments:".format(varCount))

    for c in range(varCount):
        print("{}: {}".format(c + 1, sys.argv[c + 1]))
