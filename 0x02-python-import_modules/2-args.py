#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    nargs = len(sys.argv) - 1

    if nargs == 0:
        print("{} arguments.".format(nargs))
    elif nargs == 1:
        print("{} argument:".format(nargs))
    else:
        print("{} arguments:".format(nargs))

    if nargs >= 1:
        nargs = 0
        for arg in sys.argv:
            if nargs != 0:
                print("{}: {}".format(nargs, arg))
            nargs += 1
