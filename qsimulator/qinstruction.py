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

    def check_is_instance(self, obj, expected_type):
        if not isinstance(obj, expected_type):
            raise TypeError("Expecting an object of type '{0}'"
                            "but an object of type '{1}' was found instead"
                            .format(expected_type, type(obj))
                            )


class Initialize(Instruction):

    def __init__(self, register, bitstring=None):
        self.check_is_instance(register, Register)
        if bitstring is not None:
            self.check_is_instance(bitstring, BitString)

        self._register = register
        self._bitstring = bitstring

    def __str__(self):
        string = "Initialize {0}".format(self.register)
        if self.bitstring is not None:
            string += " with value '{0}'".format(self.bitstring.value)
        return string

    @property
    def register(self):
        return self._register.number

    @property
    def bitstring(self):
        if self._bitstring is None:
            return None

        return self._bitstring.value


class Select(Instruction):
    def __init__(self, variable, register, offset, limit):
        self.variable = variable
        self.register = register
        self.offset = offset
        self.limit = limit

    def __str__(self):
        string = "Select {0} from {1} to {2} into {3}".format(self.register,
                                                              self.offset,
                                                              self.limit,
                                                              self.variable)
        return string


class Apply(Instruction):
    def __init__(self, matrix, register):
        self.matrix = matrix
        self.register = register

    def __str__(self):
        string = "Apply {0} to {1}".format(self.matrix, self.register)
        return string


class Concat(Instruction):
    def __init__(self, variable, matrix1, matrix2):
        self.variable = variable
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def __str__(self):
        string = "Concat {0} and {1} into {2}".format(self.matrix1,
                                                      self.matrix2,
                                                      self.variable)
        return string


class Measure(Instruction):
    def __init__(self, register, realvar):
        self.register = register
        self.realvar = realvar

    def __str__(self):
        string = "Measure {0} and put it into {1}".format(self.register,
                                                          self.realvar)
        return string


class Tensor(Instruction):
    def __init__(self, variable, op1, op2):
        self.variable = variable
        self.op1 = op1
        self.op2 = op2

    def __str__(self):
        string = "Tensor {0} with {1} and put it into {2}".format(self.op1,
                                                                  self.op2,
                                                                  self.variable)
        return string


class Inverse(Instruction):
    def __init__(self, variable, matrix):
        self.variable = variable
        self.matrix = matrix

    def __str__(self):
        string = "Reverse {0} and put it into {1}".format(self.matrix,
                                                          self.variable)
        return string


#########
# Types #
#########


class Variable(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Var[{0}]".format(self.name)


class BitString(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "BitString[{0}]".format(self.value)


class Digit(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Digit[{0}]".format(self.value)


class Register(object):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return "R[{0}]".format(self.number)


class Matrix(object):
    def __init__(self, value):
        self.value = value


class Gate(Matrix, metaclass=ABCMeta):
    pass


class CNot(Gate):
    def __init__(self):
        pass

    def __str__(self):
        return "CNOT"


class H(Gate):
    def __init__(self):
        pass

    def __str__(self):
        return "H"


class Identity(Gate):
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return "I{0}".format(self.size)
