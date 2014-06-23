#!/usr/bin/env python3
'''
Given a matrix that reprensents a graph and a vector that represents the current
state of the system it returns the new state of the system after a given time

@author: Jordi Llull
'''
import os, sys, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]) + "/..")
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from qmath.complex import ComplexM


def main():
    matrix = []
    matrix.append(tuple(map(lambda x: int(x), input().split(" "))))
    m_len = len(matrix[0])

    for _ in range(m_len - 1):
        matrix.append(tuple(map(lambda x: int(x), input().split(" "))))

    vector = []
    for _ in range(m_len):
        vector.append(int(input()))

    vector = tuple(map(lambda x: [x], vector))
    cmatrix = ComplexM(m_len, m_len, matrix)
    cvector = ComplexM(m_len, 1, vector)

    print("Transition matrix")
    print(cmatrix)
    print()
    print("State vector")
    print(cvector)
    print()

    for i in range(1, 10):
        print("t={0}".format(str(i)))
        print(cmatrix * cvector)
        cmatrix = cmatrix * cmatrix




if __name__ == '__main__':
    main()
