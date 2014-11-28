'''
Created on Jun 15, 2014

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

from qmath import ComplexM, q_observe


class ComplexOperationsTest(unittest.TestCase):

    def testQObserve(self):
        # Bad input
        with self.assertRaises(TypeError):
            q_observe(1, 1)

        # Different length matrix/vector
        a = ComplexM(3, 1, [[1], [0], [2]])
        b = ComplexM(2, 2, [[1, 0], [0, 1]])
        with self.assertRaises(TypeError):
            q_observe(a, b)

        # Non hermitian matrix
        a = ComplexM(2, 1, [[1], [0]])
        b = ComplexM(2, 2, [[1, 4], [2, 1]])
        with self.assertRaises(ValueError):
            q_observe(a, b)

        a = ComplexM(2, 1, [[1], [0]])
        b = ComplexM(2, 2, [[0, 1], [1, 0]])
        res = ComplexM(2, 1, [[0], [1]])
        self.assertEqual(res, q_observe(a, b))


if __name__ == "__main__":
    unittest.main()
