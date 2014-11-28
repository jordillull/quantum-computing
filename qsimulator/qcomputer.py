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

        self._sqrt_size = sqrt_size 
        self._registers = [QRegister(sqrt_size) for _ in range(nregisters)]
        self._variables = {}

        self._handlers = {}
        self._instr_handlers = {}

        for handler in handlers:
            self.register_handler(handler)

    @property
    def size(self):
        return self._sqrt_size ** 2

    @property
    def sqrt_size(self):
        return self._sqrt_size

    @property
    def registers(self):
        return self._registers

    @property
    def variables(self):
        return self._variables

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

    def get_status_info(self):
        info = ("Quantum Computer with {nregs} registers of {nqbits} qbits\n"
                "====== Registers ======\n"
                "{reginfo}\n"
                "====== Variables ======\n"
                "{varinfo}\n"

                .format(nregs   = len(self.registers),
                        nqbits  = self.size,
                        reginfo = self.get_register_info(),
                        varinfo = self.get_variables_info()
                        )
                )

        return info

    def get_register_info(self):
        info = "" 
        for i, reg in enumerate(self.registers): 
            if not reg.is_initialized:
                reg_info = "R{0}: Not initialized\n".format(i)
            else:
                reg_info = "R{0}: {1}\n".format(i, str(reg.value))

            info += reg_info
        return info

    def get_variables_info(self):
        info = ""
        for k, v in self.variables.items():
            info += "Var({0}): {1}".format(k, v)
        return info

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
    def is_initialized(self): 
        return self._value is not None

    @property
    def value(self):
        if not self.is_initialized:
            raise UnboundLocalError("Can't access the value of a not initialized register")
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

