#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for index in my_list[:x]:
            try:
                integer_v = int(index)
                print("{}".format(integer_v))
                count += 1
            except ValueError:
                pass
    except TypeError:
        print(" The value x is greater than the list")
        return 0
    print()
    return count
