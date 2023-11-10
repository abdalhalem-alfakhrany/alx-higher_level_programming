#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    v1 = 0
    v2 = 0
    for i in my_list:
        v1 += i[0] * i[1]
        v2 += i[1]
    return v1/v2
