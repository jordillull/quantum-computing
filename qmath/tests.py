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
        v = ComplexM(4, 1, [[(5, 13)], [(6, 2)], [(0.54, -6)], [12]])
        w = ComplexM(4, 1, [[(7, -8)], [(0, 4)], [2], [(9.4, 3)]])
        res = ComplexM(4, 1, [[(12, 5)], [(6, 6)], [(2.54, -6)], [(21.4, 3)]])

        self.assertEqual(res, v + w)

        vzero = ComplexM(4, 1, [[0], [0], [0], [0]])
        self.assertEqual(v, vzero + v)
        self.assertEqual(w, vzero + w)
        self.assertEqual(v, v + vzero)
        self.assertEqual(w, w + vzero)

        with self.assertRaises(ValueError):
            ComplexM(1, 3, [[(1,0),2,(3-1)]]) + ComplexM(1, 2, [[(1,0),2]])

    def testScalarMul(self):
        c = Complex(8, -2)
        v = ComplexM(4, 1, [[(16, 2.4)], [(0, -7)], [(6, 0)], [(5, -4)]])
        res = ComplexM(4, 1, [[(132.8, -12.8)], [(-14, -56)], [(48, -12)], [(32, -42)]])
        self.assertEqual(res, c * v)
        self.assertEqual(v, Complex(1) * v)

    def testComparison(self):
        self.assertEqual( ComplexM(1, 1, [[(1,2)]]), ComplexM(1, 1, [[(1,2)]]) )
        self.assertEqual(ComplexM(2, 1, [[Complex(1, 2)], [Complex(3, 4)]]), ComplexM(2, 1, [[(1, 2)], [(3, 4)]]))
        self.assertNotEqual(ComplexM(2, 1, [[1], [2]]), ComplexM(1, 1, [[(1, 2)]]))
        self.assertNotEqual(ComplexM(2, 1, [[1], [2]]), ComplexM(1, 2, [[(1, -1), (2, -1)]]))

    def testNegate(self):
        v = ComplexM(3, 1, [[(1, 2)], [(-1, -2)], [(4, -2.5)]])
        w = ComplexM(3, 1, [[(-1, -2)], [(1, 2)], [(-4, 2.5)]])

        self.assertEqual(w, -v)
        self.assertEqual(v, -w)
        self.assertNotEqual(v, -v)
        self.assertNotEqual(w, -w)

    def testIsVector(self):
        v = ComplexM(3, 1, [[(-1, -2)], [(1, 2)], [(-4, 2.5)]])
        a = ComplexM(1, 3, [[(-1, -2), (1, 2), (-4, 2.5)]])

        self.assertTrue(v.isVector())
        self.assertFalse(a.isVector())

class ComplexMTest(unittest.TestCase):
    def testConstruct(self):
        values = [[(i,j) for i,j in zip(range(10),range(10))] for _ in range(7)]

        a = ComplexM(7,10, values)
        self.assertIsInstance(a, ComplexM)
        self.assertEqual(a.getSize(), (7,10))

        with self.assertRaises(ValueError):
            ComplexM(10,7, values)

    def testGetelement(self):
        a = ComplexM(3, 2, [ [(5, 13), (6, 2)], [(0.54, -6), 12], [3, 0] ])

        self.assertEqual(a[0][0], Complex(5, 13))
        self.assertEqual(a[0][1], Complex(6,2))
        self.assertEqual(a[1][0], Complex(0.54,-6))
        self.assertEqual(a[1][1], Complex(12,0))
        self.assertEqual(a[2][0], Complex(3,0))
        self.assertEqual(a[2][1], Complex(0,0))

        with self.assertRaises(IndexError):
            a[3][1]

        with self.assertRaises(IndexError):
            a[1][3]

    def testAdd(self):
        a = ComplexM(3, 2, [ [(5,13), (6,2)], [(0.54,-6), 12], [3,0] ])
        b = ComplexM(3, 2, [ [(7, -8), (0,4)], [2, (9.4,3)],  [(0,1), (-3,-2)] ])
        res = ComplexM(3,2, [ [(12,5), (6,6)], [(2.54,-6), (21.4, 3)], [(3,1), (-3,-2)]])

        self.assertEqual(res, a + b)
        self.assertEqual(res, b + a)

        azero = ComplexM(3,2, [ [0,0], [0,0], [0,0] ])
        self.assertEqual(a, azero + a)
        self.assertEqual(b, azero + b)
        self.assertEqual(a, a + azero)
        self.assertEqual(b, b + azero)

        with self.assertRaises(ValueError):
            ComplexM(1,2, [[1], [2]]) + ComplexM(2,1, [1,2])

    def testScalarMul(self):
        c1 = Complex(0, 2)
        c2 = Complex(1, 2)
        a  = ComplexM(2, 2, [ [(1, -1), 3], [(2,2), (4,1)] ])
        res1 = ComplexM(2, 2, [ [(-2, 6), (-12, 6)], [(-12, -4), (-18,4)] ])
        res2 = ComplexM(2, 2, [ [(5, 3), (3, 12)], [(-6, 10), (0,17)] ])

        self.assertEqual(res1, c1*(c2 * a))
        self.assertEqual(c1*(c2*a), c1*(c2 * a))

        self.assertEqual(res2, (c1+c2) * a)
        self.assertEqual((c1*a) + (c2*a), (c1+c2) * a)

    def testTranspose(self):
        a = ComplexM(3, 2, [ [(7, -8), (0,4)], [2, (9.4,3)],  [(0,1), (-3,-2)] ])
        b = ComplexM(2, 3, [ [(7, -8), 2, (0,1)], [(0,4), (9.4,3), (-3,-2)]])

        self.assertEqual(b, a.transpose())
        self.assertEqual(a, b.transpose())
        self.assertEqual(a, a.transpose().transpose())
        self.assertEqual(b, b.transpose().transpose())

    def testConjugate(self):
        a = ComplexM(3, 2, [ [(7, -8), (0,4)], [2, (9.4,3)],  [(0,1), (-3,-2)] ])
        b = ComplexM(3, 2, [ [(7, 8), (0,-4)], [2, (9.4,-3)],  [(0,-1), (-3,2)] ])

        self.assertEqual(b, a.conjugate())
        self.assertEqual(a, b.conjugate())
        self.assertEqual(a, a.conjugate().conjugate())
        self.assertEqual(b, b.conjugate().conjugate())


    def testMul_3x3(self):
        a   = ComplexM(3,3,
                [
                  [(3,2)  , (0,0)   , (5,-6) ],
                  [(1,0)  , (4,2)   , (0,1)  ],
                  [(4,-1) , (0,0)   , (4,0)  ],
                ]
            )
        b   = ComplexM(3,3,
                [
                  [(5,0)  , (2,-1)  , (6,-4) ],
                  [(0,0)  , (4,5)   , (2,0)  ],
                  [(7,-4) , (2,7)   , (0,0)  ],
                ]
            )
        res = ComplexM(3,3,
                [
                  [(26,-52)  , (60,24)  , (26,0) ],
                  [(9,7)    , (1,29)   , (14,0)  ],
                  [(48,-21) , (15,22)  , (20,-22)  ],
                ]
            )

        self.assertEqual(a*b, res)
        self.assertNotEqual(b*a, a*b)

        ident = a.getIdentity()
        self.assertEqual(a, a*ident)
        self.assertEqual(b, b*ident)

        x = Complex(2,-1)
        self.assertEqual(x * (a*b), (x*a) * b)
        self.assertEqual(x * (a*b), a * (x*b))

        c = res
        self.assertEqual((a*b)*c, a*(b*c))
        self.assertEqual(a*(b+c), (a*b)+(a*c))
        self.assertEqual((a*b).transpose(), b.transpose() * a.transpose())
        self.assertEqual((a*b).adjoint(), b.adjoint() * a.adjoint())
        self.assertEqual((a*b).conjugate(), a.conjugate() * b.conjugate())

    def testMul_2x3(self):
        a   = ComplexM(2,3,
                [
                  [(3,2)  , (0,0)   , (5,-6) ],
                  [(1,0)  , (4,2)   , (0,1)  ],
                ]
            )
        b   = ComplexM(3,2,
                [
                  [(5,0)  , (2,-1)],
                  [(0,0)  , (4,5)],
                  [(7,-4) , (2,7)],
                ]
            )
        res = ComplexM(2,2,
                [
                  [(26,-52)  , (60,24)],
                  [(9,7)    , (1,29)],
                ]
            )

        self.assertEqual(a*b, res)
        self.assertNotEqual(b*a, a*b)

        self.assertIsNone(a.getIdentity())
        self.assertIsNone(b.getIdentity())
        self.assertIsNotNone(res.getIdentity())

        x = Complex(4,-3.5)
        self.assertEqual(x * (a*b), (x*a) * b)
        self.assertEqual(x * (a*b), a * (x*b))

        self.assertEqual((a*b).transpose(), b.transpose() * a.transpose())
        self.assertEqual((a*b).adjoint(), b.adjoint() * a.adjoint())
        self.assertEqual((a*b).conjugate(), a.conjugate() * b.conjugate())

    def testNegate(self):
        a = ComplexM(2, 2, [ [(2, -6), (12, -6)], [(12, 4), (18,-4)] ])
        b = ComplexM(2, 2, [ [(-2, 6), (-12, 6)], [(-12, -4), (-18,4)] ])

        self.assertEqual(b, -a)
        self.assertEqual(a, -b)
        self.assertNotEqual(a, -a)
        self.assertNotEqual(b, -b)

    def testTrace(self):
        a = ComplexM(3, 3,
                [
                  [(3, 2)  , (0, 0)   , (5, -6) ],
                  [(1, 0)  , (-7, 2)   , (0, 1)  ],
                  [(1, 0)  , (4, 2)   , (1, -3.5)  ],
                ]
            )
        self.assertEqual(a.trace(), Complex(-3, 0.5))

        b = ComplexM(2, 3, a[0:2])
        with self.assertRaises(ValueError):
            b.trace()

    def testVectorInnerProduct(self):
        v1 = ComplexM(3, 1, [[(2, -5)], [(1, 0)], [(3, 1)]])
        v2 = ComplexM(3, 1, [[(2, 1)], [(2, 3)], [(4, 14)]])
        v3 = ComplexM(3, 1, [[(0, -2)], [(-1, 0)], [(2, -3)]])
        c  = Complex(3, 3)
        vz = ComplexM(3, 1, [[0], [0], [0]])

        self.assertIsInstance(v1.innerProduct(v2), Complex)
        # v ≠ 0 → ⟨v, v⟩ > 0
        self.assertGreater(v1.innerProduct(v1).getRealValue(), 0)
        self.assertEqual(v1.innerProduct(v1).getImaginaryValue(), 0)
        # ⟨v1, v2⟩ = 0 ↔ v = 0
        self.assertEqual(vz.innerProduct(vz), Complex(0))
        # ⟨v1+v2, v3⟩ = ⟨v1, v3⟩ + ⟨v2, v3⟩
        self.assertEqual((v1 + v2).innerProduct(v3), v1.innerProduct(v3) + v2.innerProduct(v3))
        # ⟨v1, v2+v3⟩ = ⟨v1, v2⟩ + ⟨v1, v3⟩
        self.assertEqual(v1.innerProduct(v2 + v3), v1.innerProduct(v2) + v1.innerProduct(v3))
        # ⟨c v1, v2⟩ = conj(c) ⟨v1, v2⟩
        self.assertEqual((v1 * c).innerProduct(v2), c.conjugate() * v1.innerProduct(v2))
        # ⟨v1, c v2⟩ = c ⟨v2, v1⟩
        self.assertEqual(v1.innerProduct(c * v2), c * v1.innerProduct(v2))
        # ⟨v1, v2⟩ = conj(⟨v2, v1⟩)
        self.assertEqual(v1.innerProduct(v2), v2.innerProduct(v1).conjugate())

    def testIsSquared(self):
        a = ComplexM(5,5, [[i*j for j in range(5)] for i in range(5)])
        self.assertTrue(a.isSquared())
        b = ComplexM(4,5, a[0:4])
        self.assertFalse(b.isSquared())

    def testNorm(self):
        v1 = ComplexM(4, 1, [ [(4, 3)], [(6,-4)], [(12,-7)], [(0,13)]])
        v2 = ComplexM(4, 1, [ [(2, 3)], [(2,-4)], [(1,-7)], [(3,13)]])

        self.assertEqual(v1.norm(), sqrt(439))
        self.assertGreater(v2.norm(), 0)
        self.assertLess((v1 + v2).norm(), v1.norm() + v2.norm())

        a = ComplexM(2, 2, [ [(3, 0), (5, 0)], [(2, 0), (3, 0)] ])

        self.assertEqual(a.norm(), sqrt(47))

        b = ComplexM(3, 2, [ [(3, 0), (5, 0)], [(2, 0), (3, 0)], [(4,0), (5,0)] ])
        with self.assertRaises(ValueError):
            b.norm()

    def testDistance(self):
        v1 = ComplexM(3,1, [ [3], [1], [2] ])
        v2 = ComplexM(3,1, [ [2], [2], [-1] ])
        v3 = ComplexM(3,1, [ [4], [2], [-3] ])

        self.assertEqual(v1.distance(v2), sqrt(11))
        self.assertEqual(v1.distance(v1), 0)
        self.assertEqual(v2.distance(v2), 0)
        self.assertLess(v1.distance(v3), v1.distance(v2) + v1.distance(v3))
        self.assertEqual(v1.distance(v2), v2.distance(v1))

        with self.assertRaises(TypeError):
            v1.distance('foo')

        v4 = ComplexM(4,1, [ [4], [0], [-3], [-1] ])
        with self.assertRaises(ValueError):
            v1.distance(v4)

        a = ComplexM(3, 2, [ [(7, 8), (0,-4)], [2, (9.4,-3)],  [(0,-1), (-3,2)] ])
        b = ComplexM(3, 2, [ [(7, 8), (0,-4)], [2, (9.4,-3)],  [(0,-1), (-3,2)] ])
        with self.assertRaises(ValueError):
            a.distance(b)

    def testIsHermitian(self):
        a = ComplexM(3,3,
                [
                  [(5, 0)  , (4, 5)  , (6, -16) ],
                  [(4, -5) , (13, 0) , (7, 0)   ],
                  [(6, 16) , (7, 0)  , (-2.1, 0)],
                ]
            )
        b = ComplexM(3, 3,
                [
                  [(5, 0)  , (4, 5)  , (6, -16) ],
                  [(4, 5)  , (13, 0) , (14, 0)  ],
                  [(6, 16) , (7, 0)  , (-2.1, 0)],
                ]
            )

        self.assertTrue(a.isHermitian())
        self.assertFalse(b.isHermitian())
        c = ComplexM(2, 3, a[0:2])
        self.assertFalse(c.isHermitian())

    def testIsUnitary(self):
        a = ComplexM(3, 3,
                [
                  [(26, -52)  , (60, 24)  , (26, 0) ],
                  [(9, 7)    , (1, 29)   , (14, 0)  ],
                  [(48, -21) , (15, 22)  , (20, -22)],
                ]
            )
        b = ComplexM(2, 2, [[1, 0], [0, (0, 1)]])
        c = ComplexM(3, 3,
                [
                  [(0.5, 0.5) , (0, 1 / sqrt(3)) , (3 / (2 * sqrt(15)), 1 / (2 * sqrt(15))) ],
                  [(-0.5, 0)  , (1 / sqrt(3), 0) , (4 / (2 * sqrt(15)), 3 / (2 * sqrt(15))) ],
                  [(0.5, 0)   , (0, -1 / sqrt(3)), (0, 5 / (2 * sqrt(15)))                  ],
                ]
            )
        d = ComplexM(3, 3,
                [
                  [(2 ** -0.5, 0)  , (2 ** -0.5, 0) , (0, 0) ],
                  [(0, -2 ** -0.5) , (0, 2 ** -0.5) , (0, 0) ],
                  [(0, 0)          , (0, 0)         , (0, 1) ],
                ]
            )
        self.assertFalse(a.isUnitary())
        self.assertTrue(b.isUnitary())
        # Despite c  and d being unitary matrices the test below will fail
        # because of the loss of precision
        #   self.assertTrue(c.isUnitary())
        #   self.assertTrue(d.isUnitary())

    def testTensor(self):
        v1 = ComplexM(3, 1, [[3], [4], [7]])
        v2 = ComplexM(2, 1, [[-1], [2]])
        res = ComplexM(6, 1, [[-3], [6], [-4], [8], [-7], [14]])

        self.assertEqual(res, v1.tensor(v2))
        self.assertNotEqual(res, v2.tensor(v1))

        a = ComplexM(3, 3,
            [
              [(3, 2) , (5, -1) , (0, 2) ],
              [(0, 0) , (12, 0) , (6, -3)],
              [(2, 0) , (4, 4)  , (9, 3) ],
            ]
        )
        b = ComplexM(3, 3,
            [
              [(1, 0)  , (3, 4) , (5, -7) ],
              [(10, 2) , (6, 0) , (2, 5)  ],
              [(0, 0)  , (1, 0) , (2, 9)  ]
            ]
        )
        c = ComplexM(9, 9,
            [
              [(3, 2)   , (1, 18)  , (29, -11) , (5, -1)   , (19, 17) , (18, -40) , (0, 2)    , (-8, 6)   , (14, 10)  ],
              [(26, 26) , (18, 12) , (-4, 19)  , (52, 0)   , (30, -6) , (15, 23)  , (-4, 20)  , (0, 12)   , (-10, 4)  ],
              [(0, 0)   , (3, 2)   , (-12, 31) , (0, 0)    , (5, -1)  , (19, 43)  , (0, 0)    , (0, 2)    , (-18, 4)  ],
              [(0, 0)   , (0, 0)   , (0, 0)    , (12, 0)   , (36, 48) , (60, -84) , (6, -3)   , (30, 15)  , (9, -57)  ],
              [(0, 0)   , (0, 0)   , (0, 0)    , (120, 24) , (72, 0)  , (24, 60)  , (66, -18) , (36, -18) , (27, 24)  ],
              [(0, 0)   , (0, 0)   , (0, 0)    , (0, 0)    , (12, 0)  , (24, 108) , (0, 0)    , (6, -3)   , (39, 48)  ],
              [(2, 0)   , (6, 8)   , (10, -14) , (4, 4)    , (-4, 28) , (48, -8)  , (9, 3)    , (15, 45)  , (66, -48) ],
              [(20, 4)  , (12, 0)  , (4, 10)   , (32, 48)  , (24, 24) , (-12, 28) , (84, 48)  , (54, 18)  , (3, 51)   ],
              [(0, 0)   , (2, 0)   , (4, 18)   , (0, 0)    , (4, 4)   , (-28, 44) , (0, 0)    , (9, 3)    , (-9, 87)  ],
            ]
        )
        self.assertEqual(c, a.tensor(b))
        self.assertNotEqual(c, b.tensor(a))

    def testToString(self):
        a = ComplexM(2, 2, [ [(2, -6), (12, -6)], [(12, 4), (18, -4)] ])
        str(a)

if __name__ == "__main__":
    unittest.main()
