#!/usr/bin/env python3
'''
A simple experiment displaying how a quantum system evolves over time

@author: Jordi Llull
'''
import os, sys, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]) + "/..")
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from qsimulator.qmath import ComplexM
from math import sqrt

def getProbabilityMatrix(matrix):
    m, n = matrix.size
    norm = matrix.norm()
    probabilities = [[(abs(matrix[i][j]) ** 2) / (norm ** 2) for j in range(n)] for i in range(m)]

    return ComplexM(m, n, probabilities)

def main():

    x = 1 / sqrt(2)
    u = ComplexM(4, 4,
        [
          [(0, 0) , (x, 0) , (x, 0)  , (0, 0) ],
          [(0, x) , (0, 0) , (0, 0)  , (x, 0) ],
          [(x, 0) , (0, 0) , (0, 0)  , (0, x) ],
          [(0, 0) , (x, 0) , (-x, 0) , (0, 0) ],
        ]
    )
    v0 = ComplexM(4, 1, [ [1], [0], [0], [0]])

    v1 = u * v0
    v2 = u * v1
    v3 = u * v2

    print("Probabilities at t=0")
    print(getProbabilityMatrix(v0))
    print("Probabilities at t=1")
    print(getProbabilityMatrix(v1))
    print("Probabilities at t=2")
    print(getProbabilityMatrix(v2))
    print("Probabilities at t=3")
    print(getProbabilityMatrix(v3))

if __name__ == '__main__':
    main()
