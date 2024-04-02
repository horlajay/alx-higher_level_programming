#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_count = 0
    try:
        for item in my_list[:x]:
            try:
                print("{:d}".format(int(item)), end=" ")
                printed_count += 1
            except ValueError:
                pass
        print()
        return printed_count
    except TypeError:
        print("An exception occurred: x is bigger than the length of my_list")
        return 0
