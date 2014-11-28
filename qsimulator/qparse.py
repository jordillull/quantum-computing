#!/usr/bin/env python3
'''
Interpreter for our custom Quantum Assembler Language

@author: jllull
'''

from ply import yacc
from qlex import tokens
from qinstruction import Instruction, Select, Initialize, Apply, Concat, \
                         Measure, Tensor, Inverse
from qinstruction import Variable, BitString, Digit, Register, CNot, H, Identity
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
    import sys
    from qcomputer import QComputer
    from qinstrhandler import DummyPrintHandler, InitializeHandler

    parser = yacc.yacc()
    qcomp = QComputer([DummyPrintHandler, InitializeHandler])

    print("\n\n"
          "Quantum Assembler shell. "
          "Type any instruction or write STATUS to view the current status"
          " of the computer"
          "\n"
          "Type CTRL+D to exit.\n\n"
          "{0}".format(qcomp.get_status_info())
          )

    while True:
        try:
            s = input('[qparse] >>> ')
        except EOFError:
            break

        if not s:
            continue

        # STATUS is not a valid assembler instruction but we'll use it to
        # display the quantum computer state
        if s == "STATUS":
            print(qcomp.get_status_info())
            continue

        result = parser.parse(s)
        if isinstance(result, (Instruction)):
            try:
                qcomp.execute(result)
            except Exception as e:
                print('  Error executing instruction: "{0}"'.format(e))
        else:
            print("  Invalid instruction")
