#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_value = sorted(a_dictionary.values())[-1]
        key = list(filter(lambda x: a_dictionary[x] == max_value, a_dictionary))[0]
        return key
    else:
        return None
