#!/usr/bin/python3
import sys


def main():

    arg_len = len(sys.argv[1:])
    if arg_len == 0:
        print("{} arguments.".format(arg_len))
    elif arg_len == 1:
        print("{} argument:".format(arg_len))
    else:
        print("{} arguments:".format(arg_len))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
