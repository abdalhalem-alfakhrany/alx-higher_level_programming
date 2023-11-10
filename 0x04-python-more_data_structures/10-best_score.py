#!/usr/bin/python3
def best_score(a_dictionary):
    max_idx = 0
    max_value = 0
    if a_dictionary == None:
        return None
    for i in a_dictionary.keys():
        if a_dictionary[i] > max_value:
            max_value = a_dictionary[i]
            max_idx = i
    return max_idx
