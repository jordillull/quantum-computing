'''
Created on Jun 15, 2014

@author: Jordi Llull
'''
import unittest

from complex import Complex
from math import sqrt

class ComplexTest(unittest.TestCase):

    def testCreateNumbers(self):
        self.assertIsInstance(Complex(), Complex)
        self.assertIsInstance(Complex(5), Complex)
        self.assertIsInstance(Complex(-2, 3), Complex)
        self.assertIsInstance(Complex(1.323, 123.00), Complex)
        self.assertIsInstance(Complex((3, 4)), Complex)
        self.assertIsInstance(Complex([4, 5]), Complex)

        with self.assertRaises(TypeError):
            Complex('a', 2)

        with self.assertRaises(TypeError):
            Complex(3, 'b')

    def testComparison(self):
        self.assertEqual(Complex(), 0)
        self.assertEqual(Complex(1, 0), 1)
        self.assertEqual(Complex(4.00, 2.00), Complex(4, 2))

        self.assertNotEqual(Complex(0, -1), 0)
        self.assertNotEqual(Complex(4, 1), Complex(4))

    def testNegate(self):
        self.assertEqual(Complex(-4, -3), -Complex(4, 3))
        self.assertNotEqual(Complex(-4, 3), -Complex(4, 3))
        self.assertEqual(-4, -Complex(4, 0))

    def testSum(self):
        self.assertEqual(Complex(3, -4), Complex(3, -4) + Complex(0, 0))  # (0,0) is the identity
        self.assertEqual(Complex(7), Complex(4) + Complex(3))  # Real numbers addition
        self.assertEqual(Complex(4, 1), Complex(1, 1) + 3)
        self.assertEqual(Complex(4, 1), Complex(1, 1) + 3.00)
        self.assertEqual(Complex(2, 3), Complex(1, 1) - Complex(-1, -2))
        self.assertEqual(Complex(-1, -4), Complex(1, 4) + Complex(-2, -8))

    def testModulus(self):
        self.assertEqual(5, abs(Complex(3, 4)))
        self.assertEqual(2, abs(Complex(2.000)))
        self.assertEqual(sqrt(2), abs(Complex(1, 1)))
        self.assertEqual(1, abs(Complex(0, 1)))
        self.assertEqual(5, abs(Complex(3, -4)))
        self.assertEqual(13, abs(Complex(-5, -12)))

    def testCommutativity(self):
        a = Complex(1, 2)
        b = Complex(3, -4)

        self.assertEqual(a + b, b + a)
        self.assertEqual(a * b, b * a)

    def testAssociativity(self):
        a = Complex(1, 2)
        b = Complex(3, -4)
        c = Complex(-5, -1)

        self.assertEqual((a + b) + c, a + (b + c))
        self.assertEqual((a * b) * c, a * (b * c))

    def testDistributivity(self):
        a = Complex(1, 2)
        b = Complex(3, -4)
        c = Complex(-5, -1)

        self.assertEqual(a * (b + c), (a * b) + (a * c))
        self.assertEqual(b * (a + c), (b * a) + (b * c))
        self.assertEqual(c * (a + b), (c * a) + (c * b))

    def testDiv(self):
        self.assertEqual(Complex(4), Complex(12) / Complex(3))  # real numbers division
        self.assertEqual(Complex(0, 1), Complex(-2, 1) / Complex(1, 2))
        self.assertEqual(Complex(-1.5, -1.5), Complex(0, 3) / Complex(-1, -1))
        self.assertEqual(Complex(-4, 3), Complex(-13, 16) / Complex(4, -1))
        with self.assertRaises(ZeroDivisionError):
            Complex(3, 3) / Complex(0, 0)

    def testConjugation(self):
        self.assertEqual(Complex(), Complex().conjugate())
        self.assertEqual(Complex(3), Complex(3).conjugate())
        self.assertEqual(Complex(4, -3), Complex(4, 3).conjugate())
        self.assertEqual(Complex(-2, 3), Complex(-2, -3).conjugate())
        a = Complex(1, 2)
        self.assertEqual(a, a.conjugate().conjugate())

    def testToString(self):
        self.assertEqual('0', str(Complex()))
        self.assertEqual('3', str(Complex(3)))
        self.assertEqual('i', str(Complex(0, 1)))
        self.assertEqual('-i', str(Complex(0, -1)))
        self.assertEqual('3+4i', str(Complex(3, 4)))
        self.assertEqual('-3-2i', str(Complex(-3, -2)))
        self.assertEqual('-5i', str(Complex(0, -5)))
        self.assertEqual('4+i', str(Complex(4, 1)))
        self.assertEqual('-3.43-i', str(Complex(-3.4300, -1)))

if __name__ == "__main__":
    unittest.main()
