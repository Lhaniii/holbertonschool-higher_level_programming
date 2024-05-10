#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    l = len(sys.argv) - 1
    if l == 0:
        print("0 arguments.")
    elif l == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments".format(l))
        for i in range(1, l + 1):
            print("{}: {}".format(i, sys.argv[i]))