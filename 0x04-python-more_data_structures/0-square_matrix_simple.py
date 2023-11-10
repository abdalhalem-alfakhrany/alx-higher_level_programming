#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in range(len(matrix)):
        result.append([])
        for col in range(len(matrix[row])):
            result[row].append(matrix[row][col] ** 2)
    
    return result
