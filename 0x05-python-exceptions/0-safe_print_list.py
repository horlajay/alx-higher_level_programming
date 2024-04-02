#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        printed_count = 0  # Initialize a counter for the number of integers printed
        for item in my_list:
            if count < x:
                try:
                    integer_value = int(item)  # Attempt to convert the item to an integer
                    print("{:d}".format(integer_value), end="")  # Print the integer
                    printed_count += 1  # Increment the printed count
                    count += 1
                except ValueError:
                    pass  # Skip non-integer values silently
            else:
                break  # Exit the loop if we have printed x elements
        print()  # Print a newline after printing all elements
        return printed_count  # Return the number of integers printed
    except TypeError:
        print("An exception occurred: x is bigger than the length of my_list")
        return 0  # Return 0 if x is bigger than the length of my_list
