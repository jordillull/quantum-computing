#!/usr/bin/env python3
'''
Quantum Computer simulator

@author: jllull
'''

from qmath.complex import ComplexM
from qinstruction import *
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
        return (Initialize)

    def execute(self, computer):
        '''
        @computer: QComputer
        '''
        ri = self.instruction.register
        bitstring = self.instruction.bitstring
        computer.registers[ri].initialize(bitstring)


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
        message += " on a computer with {0} registers of {1} qbits".format(len(computer.registers), computer.size)
        print(message)
