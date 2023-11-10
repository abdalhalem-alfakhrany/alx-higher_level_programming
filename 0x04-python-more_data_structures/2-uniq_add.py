#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    uniq = {}

    for i in my_list:
        if uniq.get(i) != None:
            uniq[i] = 1 + uniq.get(i)
        else:
            uniq[i] = 1

    for i in uniq.keys():
        result += i

    return result
