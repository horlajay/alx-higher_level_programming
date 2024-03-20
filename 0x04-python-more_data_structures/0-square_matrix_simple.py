#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for mat in matrix:
        temp = []
        for i in mat:
            temp.append(i**2)
        result.append(temp)
    return result
