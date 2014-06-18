'''
Created on Jun 15, 2014

@author: Jordi Llull
'''
import unittest

from complex import Complex, ComplexM
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

    def testPolarRepresentation(self):
        test_numbers = [
                        Complex(0, 0),
                        Complex(0, 1),
                        Complex(0, -1),
                        Complex(1, 0),
                        Complex(0, 2.3),
                        Complex(0, -2.7),
                        Complex(4.3, 0),
                        Complex(3.2, 0),
                        Complex(2.4, -3.2),
                        Complex(2.4, -3.2),
                        Complex(-3.2, 3.8),
                        Complex(-1.2, -2.6),
                       ]

        for cartesian in test_numbers:
            polar = Complex().setValueFromPolar(cartesian.getValueAsPolar()[0], cartesian.getValueAsPolar()[1])

            # We have to round the values due to the unavoidable loss of precision
            c_a = round(cartesian.getRealValue(), 12)
            c_b = round(cartesian.getImaginaryValue(), 12)
            p_a = round(polar.getRealValue(), 12)
            p_b = round(polar.getImaginaryValue(), 12)

            self.assertEqual(c_a, p_a, "{0} is not equal to {1}".format(cartesian, polar))
            self.assertEqual(c_b, p_b, "{0} is not equal to {1}".format(cartesian, polar))

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

class ComplexVTest(unittest.TestCase):
    def testAdd(self):
        v = ComplexM(1, 4, [[(5,13), (6,2), (0.54,-6), 12]])
        w = ComplexM(1, 4, [[(7, -8), (0,4), 2, (9.4,3)]])
        res = ComplexM(1, 4, [[(12,5), (6,6), (2.54,-6), (21.4, 3)]])

        self.assertEqual(res, v + w)

        vzero = ComplexM(1, 4, [[0, 0, 0, 0]])
        self.assertEqual(v, vzero + v)
        self.assertEqual(w, vzero + w)
        self.assertEqual(v, v + vzero)
        self.assertEqual(w, w + vzero)

        with self.assertRaises(ValueError):
            ComplexM(1, 3, [[(1,0),2,(3-1)]]) + ComplexM(1, 2, [[(1,0),2]])

    def testMul(self):
        c = Complex(8, -2)
        v = ComplexM(1, 4, [[(16,2.4), (0,-7), (6,0), (5, -4)]])
        res = ComplexM(1, 4, [[(132.8,-12.8), (-14,-56), (48,-12), (32,-42)]])
        self.assertEqual(res, c * v)
        self.assertEqual(v, Complex(1) * v)

    def testComparison(self):
        self.assertEqual( ComplexM(1, 1, [[(1,2)]]), ComplexM(1, 1, [[(1,2)]]) )
        self.assertEqual( ComplexM(1, 2, [[Complex(1,2), Complex(3,4)]]), ComplexM(1, 2, [[(1,2), (3,4)]]) )
        self.assertNotEqual(ComplexM(1, 2, [[1,2]]), ComplexM(1, 1, [[(1,2)]]) )
        self.assertNotEqual(ComplexM(1, 2, [[1,2]]), ComplexM(1, 2, [[(1,-1),(2,-1)]]) )

    def testNegate(self):
        v = ComplexM(1, 3, [[(1,2), (-1,-2), (4,-2.5)]])
        w = ComplexM(1, 3, [[(-1,-2), (1,2), (-4,2.5)]])

        self.assertEqual(w, -v)
        self.assertEqual(v, -w)
        self.assertNotEqual(v, -v)
        self.assertNotEqual(w, -w)

class ComplexMTest(unittest.TestCase):
    def testConstruct(self):
        values = [[(i,j) for i,j in zip(range(10),range(10))] for _ in range(7)]

        v = ComplexM(7,10, values)
        self.assertIsInstance(v, ComplexM)
        self.assertEqual(v.getSize(), (7,10))

        with self.assertRaises(ValueError):
            ComplexM(10,7, values)

    def testAdd(self):
        v = ComplexM(3, 2, [ [(5,13), (6,2)], [(0.54,-6), 12], [3,0] ])
        w = ComplexM(3, 2, [ [(7, -8), (0,4)], [2, (9.4,3)],  [(0,1), (-3,-2)] ])
        res = ComplexM(3,2, [ [(12,5), (6,6)], [(2.54,-6), (21.4, 3)], [(3,1), (-3,-2)]])

        self.assertEqual(res, v + w)
        self.assertEqual(res, w + v)

        vzero = ComplexM(3,2, [ [0,0], [0,0], [0,0] ])
        self.assertEqual(v, vzero + v)
        self.assertEqual(w, vzero + w)
        self.assertEqual(v, v + vzero)
        self.assertEqual(w, w + vzero)

        with self.assertRaises(ValueError):
            ComplexM(1,2, [[1], [2]]) + ComplexM(2,1, [1,2])

    def testMul(self):
        c1 = Complex(0, 2)
        c2 = Complex(1, 2)
        v  = ComplexM(2, 2, [ [(1, -1), 3], [(2,2), (4,1)] ])
        res1 = ComplexM(2, 2, [ [(-2, 6), (-12, 6)], [(-12, -4), (-18,4)] ])
        res2 = ComplexM(2, 2, [ [(5, 3), (3, 12)], [(-6, 10), (0,17)] ])

        self.assertEqual(res1, c1*(c2 * v))
        self.assertEqual(c1*(c2*v), c1*(c2 * v))

        self.assertEqual(res2, (c1+c2) * v)
        self.assertEqual((c1*v) + (c2*v), (c1+c2) * v)

    def testNegate(self):
        v = ComplexM(2, 2, [ [(2, -6), (12, -6)], [(12, 4), (18,-4)] ])
        w = ComplexM(2, 2, [ [(-2, 6), (-12, 6)], [(-12, -4), (-18,4)] ])

        self.assertEqual(w, -v)
        self.assertEqual(v, -w)
        self.assertNotEqual(v, -v)
        self.assertNotEqual(w, -w)

if __name__ == "__main__":
    unittest.main()
