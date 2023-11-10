#!/usr/bin/python3
def best_score(a_dictionary):
    return None if a_dictionary == None else max(a_dictionary,key=a_dictionary.get)
