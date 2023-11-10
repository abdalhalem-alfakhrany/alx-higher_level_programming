#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_delete = []
    if value in a_dictionary.values():
        for i in a_dictionary.keys():
            if a_dictionary[i] == value:
                keys_to_delete.append(i)
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary
