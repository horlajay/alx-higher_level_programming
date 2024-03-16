#!/usr/bin/python3
import sys


if __name__ == "__main__":
    number = 0

    for arg in sys.argv[1:]:
        number += int(arg)
    print(f"{number}")
