'''
Created on Nov 28, 2014

@author: Jordi Llull
'''

from qcomputer import QComputer
from qinstrhandler import InitializeHandler
from qmath import ComplexM
from qinstruction import Initialize, \
                         Select

from qinstruction import Register, \
                         BitString, \
                         Digit, \
                         Variable


def get_dummy_computer(nregisters=4, sqrt_size=3):
    qcomp = QComputer(handlers=[], sqrt_size=sqrt_size, nregisters=nregisters)

    return qcomp


def get_functional_computer(nregisters=4, sqrt_size=3):
    handlers = [InitializeHandler]
    qcomp = QComputer(handlers=handlers,
                      sqrt_size=sqrt_size,
                      nregisters=nregisters
                      )

    return qcomp


def zero_matrix(sqrt_size):
    value = [[0 for _ in range(sqrt_size)] for _ in range(sqrt_size)]
    return ComplexM(sqrt_size, sqrt_size, value)


def instr_initialize(reg_num, value=None):
    instr = Initialize(Register(reg_num), BitString(value))
    return instr


def instr_select(var_name, reg_num, offset, numqbits):
    instr = Select(Variable(var_name),
                   Register(reg_num),
                   Digit(offset),
                   Digit(numqbits)
                   )

    return instr
