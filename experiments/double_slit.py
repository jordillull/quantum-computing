#!/usr/bin/env python3
'''
It performs a double slit experiment with a quantum particle and with a non quantum particle.

@author: Jordi Llull
'''
import os
import sys
import inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]) + "/..")
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from qsimulator.qmath import ComplexM
from math import sqrt


def get_non_quantum_matrix():
    return ComplexM(8, 8,
            [
             [(0, 0)  , (0, 0)     , (0, 0)     , (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(1 / 2) , (0, 0)     , (0, 0)     , (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(1 / 2) , (0, 0)     , (0, 0)     , (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0)  , (1 / 3, 0) , (0, 0)     , (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0)  , (1 / 3, 0) , (0, 0)     , (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0)  , (1 / 3, 0) , (1 / 3, 0) , (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)],
             [(0, 0)  , (0, 0)     , (1 / 3, 0) , (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)],
             [(0, 0)  , (0, 0)     , (1 / 3, 0) , (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)],
            ]
            )


def get_quantum_matrix():
    s2 = sqrt(2)
    s6 = sqrt(6)
    return ComplexM(8, 8,
            [
             [(0, 0)      , (0, 0)             , (0, 0)             , (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(1 / s2, 0) , (0, 0)             , (0, 0)             , (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(1 / s2, 0) , (0, 0)             , (0, 0)             , (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0)      , (-1 / s6, 1 / s6)  , (0, 0)             , (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0)      , (-1 / s6, -1 / s6) , (0, 0)             , (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0)      , (1 / s6, -1 / s6)  , (-1 / s6, 1 / s6)  , (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)],
             [(0, 0)      , (0, 0)             , (-1 / s6, -1 / s6) , (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)],
             [(0, 0)      , (0, 0)             , (1 / s6, -1 / s6)  , (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)],
            ]
            )


def get_probability_matrix(matrix):
    m, n = matrix.size
    norm = matrix.norm()
    probabilities = [[(abs(matrix[i][j]) ** 2) / (norm ** 2) for j in range(n)] for i in range(m)]

    return ComplexM(m, n, probabilities)


def main():
    a = get_non_quantum_matrix()
    b = get_quantum_matrix()
    v = ComplexM(8, 1, [[1], [0], [0], [0], [0], [0], [0], [0]])

    print("The probability vector for a NON quantum particle is:")
    print(a * a * v)
    print("The probability vector for a quantum particle is:")
    print(get_probability_matrix(b * b * v))

if __name__ == '__main__':
    main()
