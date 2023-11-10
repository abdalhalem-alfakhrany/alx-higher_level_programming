#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = []
    unqui = []
    for s1 in set_1:
        for s2 in set_2:
            if s1 == s2:
                unqui.append(s1)
    
    for s1 in set_1:
        if s1 not in unqui:
            result.append(s1)
    
    for s2 in set_2:
        if s2 not in unqui:
            result.append(s2)

    return result
