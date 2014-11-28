'''
Created on Nov 28, 2014

@author: Jordi Llull
'''

from qcomputer import QComputer
from qinstrhandler import InitializeHandler
from qinstruction import Initialize
from qmath import ComplexM


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


def initialize_instruction(register, value=None):
    instr = Initialize(register, value)
    return instr


def zero_matrix(sqrt_size):
    value = [[0 for _ in range(sqrt_size)] for _ in range(sqrt_size)]
    return ComplexM(sqrt_size, sqrt_size, value)
