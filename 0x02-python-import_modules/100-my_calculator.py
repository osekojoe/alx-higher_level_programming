#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    nargs = len(sys.argv) - 1

    if nargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    oper = sys.argv[2]
    opers = ['+', '-', '*', '/']

    if oper not in opers:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if oper == opers[0]:
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif oper == opers[1]:
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif oper == opers[2]:
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
