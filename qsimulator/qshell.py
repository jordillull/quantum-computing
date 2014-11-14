#!/usr/bin/env python3
'''
Interpreter for our custom Quantum Assembler Language

@author: jllull
'''

from ply import yacc
from qlex import tokens


def p_initialize(p):
    '''op_initialize : INITIALIZE REGISTER
                   | INITIALIZE REGISTER BITSTRING'''
    print("op_initialize: not implemeted yet")


def p_select(p):
    '''op_select : SELECT VARIABLE REGISTER DIGIT DIGIT'''
    print("op_select: not implemeted yet")


def p_apply(p):
    '''op_apply : APPLY matrix REGISTER'''
    print("op_apply: not implemeted yet")


def op_concat(p):
    '''op_concat : VARIABLE CONCAT matrix matrix'''
    print("op_concat: not implemeted yet")


def op_tensor(p):
    '''op_tensor : VARIABLE TENSOR matrix'''
    print("op_tensor: not implemeted yet")


def op_measure(p):
    '''op_measure : MEASURE VARIABLE VARIABLE'''
    print("op_measure: not implemeted yet")


def p_matrix(p):
    '''matrix : gate
              | VARIABLE'''
    p[0] = p[1]


def p_gate(p):
    '''gate : CNOT
            | H
            | identity '''
    p[0] = p[1]


def p_identity(p):
    '''identity : IMATRIX'''
    p[0] = p[1]

if __name__ == "__main__":
    parser = yacc.yacc()
    print("Quantum Assembler interpreter. Write an expression or type 'exit' to end the program.")

    while True:
        try:
            s = input(' >>> ')
        except EOFError:
            break

        if not s:
            continue
        result = parser.parse(s)
        print(result)
