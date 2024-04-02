#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for item in my_list[:x]:
            try:
                print("{:d}".format(int(item)), end="")
                count += 1
            except ValueError:
                pass
        print()
        return count
    except TypeError:
        print("Error: ")
        return 0
