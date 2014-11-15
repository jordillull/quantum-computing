#!/usr/bin/env python3
'''
Quantum Computer instructions and types

@author: jllull
'''

from abc import ABCMeta

################
# Instructions #
################


class Instruction(metaclass=ABCMeta):
    pass


class Initialize(Instruction):

    def __init__(self, register, bitstring=None):
        self.register = register
        self.bitstring = bitstring
        self.isexecuted = False


class Select(Instruction):
    def __init__(self, variable, register, offset, limit):
        self.variable = variable
        self.register = register
        self.offset = offset
        self.limit = limit


class Apply(Instruction):
    def __init__(self, matrix, register):
        self.matrix = matrix
        self.register = register


class Concat(Instruction):
    def __init__(self, variable, matrix1, matrix2):
        self.variable = matrix1
        self.variable = matrix2


class Measure(Instruction):
    def __init__(self, register, realvar):
        self.register = register
        self.realvar = realvar


class Tensor(Instruction):
    def __init__(self, variable, op1, op2):
        self.variable = variable
        self.op1 = op1
        self.op2 = op2


class Inverse(Instruction):
    def __init__(self, variable, matrix):
        self.variable = variable
        self.matrix = matrix


#########
# Types #
#########


class Variable(object):
    def __init__(self, name):
        self.name = name


class BitString(object):
    def __init__(self, value):
        self.value = value


class Digit(object):
    def __init__(self, value):
        self.value = value


class Register(object):
    def __init__(self, number):
        self.number = number


class Matrix(object):
    def __init__(self, value):
        self.value = value


class Gate(Matrix, metaclass=ABCMeta):
    pass


class CNot(Gate):
    def __init__(self):
        pass


class H(Gate):
    def __init__(self):
        pass


class Identity(Gate):
    def __init__(self, size):
        self.size = size
