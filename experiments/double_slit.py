#!/usr/bin/env python3
'''
It performs a double slit experiment with a quantum particle and with a non quantum particle.

@author: Jordi Llull
'''
import os, sys, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]) + "/..")
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from qmath.complex import ComplexM
from math import sqrt


def getNonQuantumMatrix():
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

def getQuantumMatrix():
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

def getProbabilityMatrix(matrix):
    m, n = matrix.getSize()
    norm = matrix.norm()
    probabilities = [[(abs(matrix[i][j]) ** 2) / (norm ** 2) for j in range(n)] for i in range(m)]

    return ComplexM(m, n, probabilities)


def main():
    a = getNonQuantumMatrix()
    b = getQuantumMatrix()
    v = ComplexM(8, 1, [ [1], [0], [0], [0], [0], [0], [0], [0] ])

    print("The probability vector for a NON quantum particle is:")
    print(a * a * v)
    print("The probability vector for a quantum particle is:")
    print(getProbabilityMatrix(b * b * v))

if __name__ == '__main__':
    main()
