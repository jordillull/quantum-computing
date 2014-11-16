#!/usr/bin/env python3
'''
Quantum Computer simulator

@author: jllull
'''

from qmath import ComplexM
from qinstrhandler import DummyPrintHandler
from qinstruction import Instruction, Select, Initialize, Apply, Concat, \
                         Measure, Tensor, Inverse


class InstructionHandlerRegisterError(Exception):
    pass

class QComputer(object):

    def __init__(self, handlers, sqrt_size=3, nregisters=16):
        '''Initialize a quantum computer with nregisters of size sqrt_size x sqrt_size'''

        self._size = sqrt_size ** 2
        self._registers = [QRegister(sqrt_size) for _ in range(nregisters)]
        self._variables = {}

        self._handlers = {}
        self._instr_handlers = {}

        for handler in handlers:
            self.register_handler(handler)

    @property
    def size(self):
        return self._size

    @property
    def registers(self):
        return self._registers

    def register_handler(self, handler):
        '''
        @handler: InstructionHandler
        '''
        if handler in self._handlers.keys():
            raise InstructionHandlerRegisterError("The handler is already registered")

        for instruction in handler.get_handled_instructions():
            if instruction not in self._instr_handlers.keys():
                self._instr_handlers[instruction] = [handler]
            else:
                self._instr_handlers[instruction] += [handler]

        self._handlers[handler] = handler.get_handled_instructions()

    def execute_instruction(self, instruction):
        for Handler in self._instr_handlers[type(instruction)]:
            handlerinst = Handler(instruction)
            handlerinst.execute(self)


class QRegister(object):
    def __init__(self, sqrt_size=3):
        self._sqrt_size = sqrt_size
        self._value = None

    def initialize(self, value=None):
        if value is None:
            matrix = [[0 for _ in range(self._sqrt_size)] for _ in range(self._sqrt_size)]
        else:
            raise NotImplementedError("Can't initialize with a custome value")
            matrix = []

        self._value = ComplexM(self._sqrt_size, self._sqrt_size, matrix)

    @property
    def value(self):
        if self._value is None:
            raise UnboundLocalError("Can't access the value of a not initialized register")
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

