'''
Created on Jun 15, 2014

@author: Jordi Llull
'''
import os, sys, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]) + "/..")
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

import unittest

from complex import ComplexM
from operations import qObserve
from math import sqrt

class ComplexTest(unittest.TestCase):

    def testQObserve(self):
        # Bad input
        with self.assertRaises(TypeError):
            qObserve(1,1)

        # Different length matrix/vector
        a = ComplexM(3,1, [ [1], [0], [2]])
        b = ComplexM(2,2, [ [1, 0], [0, 1]])
        with self.assertRaises(TypeError):
            qObserve(a,b)

        #Non hermitian matrix
        a = ComplexM(2,1, [ [1], [0]])
        b = ComplexM(2,2, [ [1, 4], [2, 1]])
        with self.assertRaises(ValueError):
            qObserve(a,b)

        a = ComplexM(2,1, [ [1], [0]])
        b = ComplexM(2,2, [ [0, 1], [1,0] ])
        res = ComplexM(2,1, [ [0], [1]])
        self.assertEqual(res, qObserve(a,b))


if __name__ == "__main__":
    unittest.main()
