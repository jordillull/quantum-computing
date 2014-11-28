'''
Created on Nov 28, 2014

@author: Jordi Llull
'''


def bitstring_to_matrix(bitstring, sqrt_size):
    matrix = []
    for i in range(sqrt_size):
        s1 = i * sqrt_size
        s2 = (i+1) * sqrt_size
        matrix.append(list(map(int, list(bitstring[s1:s2]))))

    return matrix

