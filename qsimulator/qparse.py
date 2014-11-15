#!/usr/bin/env python3
'''
Interpreter for our custom Quantum Assembler Language

@author: jllull
'''

from ply import yacc
from qlex import tokens
from qinstruction import *
from qsimulator import qinstruction

def p_instruction(p):
    '''instruction : op_initialize
                   | op_select
                   | op_apply
                   | op_concat
                   | op_tensor
                   | op_measure
                   | op_inverse
    '''
    p[0] = p[1]


def p_initialize(p):
    '''op_initialize : INITIALIZE register
                     | INITIALIZE register bitstring'''
    if len(p) > 3:
        p[0] = Initialize(p[2], p[3])
    else:
        p[0] = Initialize(p[2])


def p_select(p):
    '''op_select : SELECT variable register digit digit'''
    p[0] = Select(p[2], p[3], p[4], p[5])


def p_apply(p):
    '''op_apply : APPLY matrix register'''
    p[0] = Apply(p[2], p[3])


def p_concat(p):
    '''op_concat : variable CONCAT matrix matrix'''
    p[0] = Concat(p[1], p[3], p[4])


def p_tensor(p):
    '''op_tensor : variable TENSOR matrix matrix'''
    p[0] = Tensor(p[1], p[3], p[4])


def p_measure(p):
    '''op_measure : MEASURE register variable'''
    p[0] = Measure(p[2], p[3])


def p_inverse(p):
    '''op_inverse : variable INVERSE matrix'''
    p[0] = Inverse(p[1], p[3])


def p_matrix(p):
    '''matrix : gate
              | variable
              | register'''
    p[0] = p[1]


def p_register(p):
    '''register : REGISTER'''
    p[0] = Register(p[1])


def p_digit(p):
    '''digit : DIGIT'''
    p[0] = Digit(p[1])


def p_bitstring(p):
    '''bitstring : BITSTRING'''
    p[0] = BitString(p[1])


def p_variable(p):
    '''variable : VARIABLE'''
    p[0] = Variable(p[1])


def p_gate(p):
    '''gate : cnot_gate
            | h_gate
            | identity '''
    p[0] = p[1]


def p_cnot_gate(p):
    '''cnot_gate : CNOT'''
    p[0] = CNot()


def p_h_gate(p):
    '''h_gate : H '''
    p[0] = H()


def p_identity(p):
    '''identity : IMATRIX'''
    p[0] = Identity(p[1])


def p_error(p):
    pass


if __name__ == "__main__":
    from qcomputer import QComputer
    from qinstrhandler import DummyPrintHandler

    parser = yacc.yacc()
    print("Quantum Assembler interpreter. Write an instruction.")
    print("Type CTRL+D to exit.")

    qcomp = QComputer([DummyPrintHandler])

    while True:
        try:
            s = input('[qparse] >>> ')
        except EOFError:
            break

        if not s:
            continue

        result = parser.parse(s)
        if isinstance(result, (Instruction)):
            qcomp.execute_instruction(result)
        else:
            print("  Error: Invalid instruction")
