#!/usr/bin/python3
from sys import argv


def main():

    arg_len = len(argv[1:])
    args = argv[1:]
    if arg_len == 0:
        print("{} arguments.".format(arg_len))
    elif arg_len == 1:
        print("{} argument:".format(arg_len))
    else:
        print("{} arguments:".format(arg_len))
        for i, arg in enumerate(args, 1):
            print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
