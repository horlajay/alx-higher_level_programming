#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    sec_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            sec_list.append(True)
        else:
            sec_list.append(False)
    return sec_list
