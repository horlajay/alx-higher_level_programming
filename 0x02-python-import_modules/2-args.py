#!/usr/bin/python3
from sys import argv


def main():

    arg_len = len(argv) - 1

    if arg_len == 0:
        print("0 arguments.")
    elif arg_len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_len))
        for i, arg in enumerate(args, 1):
            print("{}: {}".format(i + 1, argv[i + 1]))


if __name__ == "__main__":
    main()
