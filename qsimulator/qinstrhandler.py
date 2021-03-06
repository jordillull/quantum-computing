#!/usr/bin/env python3
'''
Quantum Computer simulator

@author: jllull
'''

from qinstruction import Instruction, Select, Initialize, Apply, Concat, \
                         Measure, Tensor, Inverse
from qmath import ComplexM
from abc import ABCMeta, abstractmethod


class InstructionHandler(metaclass=ABCMeta):

    def __init__(self, instruction):
        '''
        @instruction: Instruction
        '''
        if not isinstance(instruction, self.get_handled_instructions()):
            raise TypeError("Can't handle instructions of type {0}"
                            .format(type(instruction)))

        self.instruction = instruction

    @classmethod
    def get_handled_instructions(cls):
        return []

    @abstractmethod
    def execute(self, computer):
        '''
        @computer: QComputer
        '''
        return


class InitializeHandler(InstructionHandler):

    @classmethod
    def get_handled_instructions(cls):
        '''
        @return: A tuple of handled instructions
        '''
        return (Initialize,)

    def execute(self, computer):
        '''
        @computer: QComputer
        '''

        register = computer.registers[self.instruction.register]
        register.initialize(self.instruction.bitstring)

class SelectHandler(InstructionHandler):

    @classmethod
    def get_handled_instructions(cls):
        '''
        @return: A tuple of handled instructions
        '''
        return (Select,)

    def execute(self, computer):
        '''
        @computer: QComputer
        '''
        register = computer.registers[self.instruction.register]
        start = self.instruction.offset
        stop = self.instruction.numqubits + start

        if start > register.size or stop > register.size:
            raise IndexError("Unable to select from element {0} to element {1}".format(start, stop))

        # The result of the select is saved as a complex vector
        value = ComplexM(1, stop - start, [register[start:stop]])

        variable = self.instruction.variable

        computer.set_variable(variable, value)


class DummyPrintHandler(InstructionHandler):

    @classmethod
    def get_handled_instructions(cls):
        '''
        @return: A tuple of handled instructions
        '''
        return (Initialize, Select, Apply, Concat, Measure, Tensor, Inverse)

    def execute(self, computer):
        '''
        @computer: QComputer
        '''
        message = "Executing instruction: '{0}'".format(self.instruction)
        print(message)
