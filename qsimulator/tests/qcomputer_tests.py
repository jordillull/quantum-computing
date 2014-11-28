'''
Created on Nov 28, 2014

@author: Jordi Llull
'''
import os
import sys
import inspect
cmd_folder = os.path.realpath(os.path.abspath(
    os.path.split(inspect.getfile(inspect.currentframe()))[0]) + "/..")
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

import unittest

from qcomputer import QComputer
from qmath import ComplexM
from utils import bitstring_to_matrix
from test_utils import get_dummy_computer, get_functional_computer, initialize_instruction, zero_matrix


class QComputerTest(unittest.TestCase):

    def testQuantumComputerStartsWithoutInitializedRegisters(self):
        qcomp = get_dummy_computer()
        for register in qcomp.registers:
            self.assertFalse(register.is_initialized)

    def testRegisterInitializationOnlyInitializedTheGivenRegister(self):
        qcomp = get_functional_computer(nregisters=4)
        qcomp.execute(initialize_instruction(1))

        self.assertTrue(qcomp.registers[1].is_initialized)
        self.assertFalse(qcomp.registers[0].is_initialized)
        self.assertFalse(qcomp.registers[2].is_initialized)
        self.assertFalse(qcomp.registers[3].is_initialized)

    def testRegistersAreInitializedToTheZeroMatrixByDefault(self):
        qcomp = get_functional_computer(nregisters=4, sqrt_size=3)
        qcomp.execute(initialize_instruction(2))

        self.assertEqual(zero_matrix(qcomp.sqrt_size), qcomp.registers[2].value)

    def testInitializeRegisterWithBitString(self):
        qcomp = get_functional_computer(nregisters=4, sqrt_size=3)
        value = "101100010"
        qcomp.execute(initialize_instruction(0, value))

        cvalue = ComplexM(3, 3, bitstring_to_matrix(value, 3))

        print(type(cvalue))
        print(cvalue)
        print(type(qcomp.registers[0].value))
        print(qcomp.registers[0].value)
        self.assertEquals(cvalue, qcomp.registers[0].value)

    def testInitializeRegisterWithTooLongBitstringRaisesAnError(self):
        qcomp = get_functional_computer(nregisters=4, sqrt_size=3)
        value = "00101010001"
        with self.assertRaises(ValueError):
            qcomp.execute(initialize_instruction(0, value))

    def testInitializeRegisterWithInvalidBitstringRaisesAnError(self):
        qcomp = get_functional_computer(nregisters=4, sqrt_size=3)
        value = "00102010001"
        with self.assertRaises(ValueError):
            qcomp.execute(initialize_instruction(0, value))



if __name__ == "__main__":
    unittest.main()
