'''
Handles complex numbers

@author: Jordi Llull
'''

from math import sqrt
from math import sin, cos, atan, pi
from prettytable import PrettyTable

class Complex(object):

    def __init__(self, real=None, imaginary=None):
        if imaginary == None:
            value = real
            if value == None:
                self.setValue(0, 0)
            elif isinstance(value, (int, float)):
                self.setValue(value, 0)
            elif isinstance(value, Complex):
                self.setValue(value.getRealValue(), value.getImaginaryValue())
            elif isinstance(value, (tuple, list)) and len(value) == 2:
                self.setValue(value[0], value[1])
            else:
                raise TypeError("Cannot make a complex number from an object of class {0}".format(value.__class__.__name__))
        else:
            self.setValue(real, imaginary)


    def __str__(self):
        return self.toString()

    def __add__(self, other):
        other = Complex(other)

        real = self.getRealValue() + other.getRealValue()
        imaginary = self.getImaginaryValue() + other.getImaginaryValue()

        return Complex(real, imaginary)

    def __sub__(self, other):
        other = Complex(other)

        return self.__add__(-other)

    def __mul__(self, other):
        if isinstance(other, ComplexM):
            return other * self
        else:
            other = Complex(other)

            real = (self.getRealValue() * other.getRealValue()) - (self.getImaginaryValue() * other.getImaginaryValue())
            imaginary = (self.getRealValue() * other.getImaginaryValue()) + (self.getImaginaryValue() * other.getRealValue())

            return Complex(real, imaginary)

    def __div__(self, other):
        return self.__truediv__(other)

    def __truediv__(self, other):
        other = Complex(other)
        dividend = other.getRealValue() ** 2.0 + other.getImaginaryValue() ** 2.0
        if dividend == 0:
            raise ZeroDivisionError("Can't divide a complex number by 0")

        real = (self.getRealValue() * other.getRealValue() + self.getImaginaryValue() * other.getImaginaryValue()) / dividend
        imaginary = (self.getImaginaryValue() * other.getRealValue() - self.getRealValue() * other.getImaginaryValue()) / dividend

        return Complex(real, imaginary)

    def __neg__(self):
        return Complex(-self.getRealValue(), -self.getImaginaryValue())

    def __abs__(self):
        '''
        returns the modulus of the complex number
        '''
        return sqrt(self.getRealValue() ** 2 + self.getImaginaryValue() ** 2)

    def __eq__(self, other):
        other = Complex(other)
        return self.getRealValue() == other.getRealValue() and self.getImaginaryValue() == other.getImaginaryValue()

    def setValue(self, real, imaginary):
        if isinstance(real, (int, float)) and isinstance(imaginary, (int, float)):
            self.__value = (real, imaginary)
        else:
            raise TypeError("The real and the imaginary part of a complex number should be valid real numbers")

    def getValue(self):
        return self.__value

    def getRealValue(self):
        return self.__value[0]

    def getImaginaryValue(self):
        return self.__value[1]

    def setValueFromPolar(self, modulus, angle):
        real = modulus * cos(angle)
        imaginary = modulus * sin(angle)
        self.setValue(real, imaginary)
        return self

    def getValueAsPolar(self):
        a = self.getRealValue()
        b = self.getImaginaryValue()
        modulus = abs(self)
        if a == 0:  # Angle in the Y axis
            angle = pi / 2.0 if b >= 0 else 3 * pi / 2.0
        else:
            angle = atan(b / float(a))
            if a < 0:  # Second and third quadrant
                angle = angle + pi

        return (modulus, angle)

    def conjugate(self):
        return Complex(self.getRealValue(), -self.getImaginaryValue())

    def toString(self):
        value = self.getValue()
        string = ""
        if value[0] != 0:
            if value[1] == 0:
                string = "{0}".format(value[0])
            else :
                imaginary_value = abs(value[1]) if abs(value[1]) != 1 else ""
                string = "{real}{sign}{imaginary}i".format(real=value[0], imaginary=imaginary_value, sign='+' if value[1] > 0 else "-")
        elif value[1] != 0:
            sign = "-" if value[1] < 0 else ""
            imaginary = abs(value[1]) if abs(value[1]) != 1 else ""
            string = "{0}{1}i".format(sign, imaginary)
        else:
            string = "0"

        return string

class ComplexM(object):
    """
    Complex matrix manipulation
    """
    def __init__(self, m, n, matrix):
        len_m = len(matrix)
        len_n = [lx for lx in map(lambda x: len(x), matrix) if lx != n ]

        if len_m != m or len_n != []:
            if len_n != []:
                len_n = len_n[0]
            else:
                len_n = n
            raise ValueError("Expected a bidimensional array of length {0}x{1}. An array of {2}x{3} was given instead".format(m, n, len_m, len_n))

        self.__size = (m,n)

        my_mat = []
        for row in matrix:
            my_mat.append(tuple(map(lambda x: Complex(x), row)))

        self.__matrix = tuple(my_mat)

    def __str__(self):
        return self.toString()

    def __add__(self, other):
        if isinstance(other, ComplexM):
            if self.getSize() != other.getSize():
                self_size = 'x'.join(map(lambda x: str(x), self.getSize()))
                other_size = 'x'.join(map(lambda x: str(x), other.getSize()))
                raise ValueError("Can't sum ComplexM of size {0} with a ComplexM of size {1}".format(self_size, other_size))

            new_values = tuple(map(lambda r1, r2: tuple(map(lambda x, y: x + y, r1, r2)), self, other))
            m,n = self.getSize()
            return ComplexM(m,n, tuple(new_values))
        else:
            raise TypeError("Cannot sum a ComplexM with and object of class {0}".format(other.__class__.__name__))

    def __sub__(self, other):
        return self.__add__(-other)

    def __eq__(self, other):
        if self.getSize() != other.getSize():
            return False

        return self.getMatrix() == other.getMatrix()

    def __scalarmul__(self, other):
        new_values = tuple(map(lambda i: tuple(map(lambda j: other * j, i)), self))
        m,n = self.getSize()
        return ComplexM(m,n, new_values)

    def __matrixmul__(self, other):
        sm, sn = self.getSize()
        om, on = other.getSize()

        if sn != om:
            raise TypeError("Cannot multiply a ComplexM of size {0}x{1} with a ComplexM of size {2}x{3}".format(str(sm),str(sn),str(om),str(on)))

        new_values = [[Complex(0) for _ in range(on)] for _ in range(sm)]

        for i in range(sm):
            for j in range(on):
                for r1,r2 in zip(self.getRow(i), other.getCol(j)):
                    new_values[i][j] += r1*r2

        return ComplexM(sm, on, new_values)



    def __mul__(self, other):
        if isinstance(other, Complex): # Scalar multiplication
            return self.__scalarmul__(other)
        elif isinstance(other, ComplexM):
            return self.__matrixmul__(other)
        else:
            raise TypeError("Cannot sum a complex number with and object of class {0}".format(other.__class__.__name__))

    def __neg__(self):
        new_values = tuple(map(lambda i: tuple(map(lambda j:-j, i)), self))
        m,n = self.getSize()
        return ComplexM(m,n, new_values)

    def __getitem__(self, i):
        return self.getMatrix()[i]

    def innerProduct(self, other):
        if not isinstance(other, ComplexM):
            raise TypeError("Cannot do the innerproduct of ComplexM with an object of class {0}".format(other.__class__.__name__))

        if self.isVector() and other.isVector():
            return (self.adjoint() * other).trace()
        elif self.isSquared() and other.isSquared() and self.getSize()[0] == other.getSize()[0]:
            return (self.transpose() * other).trace()
        else:
            self_size = 'x'.join(map(lambda x: str(x), self.getSize()))
            other_size = 'x'.join(map(lambda x : str(x), other.getSize()))
            raise ValueError("Cannot do the innerproduct of a ComplexM of size {0} with a ComplexM of size {1}".format(self_size, other_size)) 

    def getMatrix(self):
        return self.__matrix

    def getSize(self):
        return self.__size

    def conjugate(self):
        new_values = tuple(map(lambda r: tuple(map(lambda x: x.conjugate(), r)), self))
        m,n = self.getSize()
        return ComplexM(m,n,new_values)

    def transpose(self):
        m,n = self.getSize()
        new_values = [[self[j][i] for j in range(m)] for i in range(n)]

        return ComplexM(n,m,new_values)

    def adjoint(self):
        return self.conjugate().transpose()

    def isVector(self):
        return self.getSize()[1] == 1

    def isSquared(self):
        return self.getSize()[0] == self.getSize()[1]

    def trace(self):
        if not self.isSquared():
            raise ValueError("A matrix of size {0}x{1} is not an squared matrix".format(str(self.getSize()[0]), str(self.getSize()[1])))
        res = Complex(0)
        for i in range(self.getSize()[0]):
            res += self[i][i]

        return res

    def norm(self):
        return sqrt(self.innerProduct(self).getRealValue())

    def distance(self, other):
        return (self - other).norm()

    def tensor(self, other):
        (sm, sn) = self.getSize()
        (m, n) = other.getSize()
        # We are using the formal definition of Tensor here. I.e:
        #     Being size of B m×n
        #     (A ⊗ B)[i, j] = A[i/m, j/n] * B[i % m, j % n]
        tensorFnx = lambda i, j: self[i // m][j // n] * other[i % m][j % n]
        tensor_size = (sm * m, sn * n)
        tensor_matrix = [[tensorFnx(i, j) for j in range(tensor_size[1])] for i in range(tensor_size[0])]

        return ComplexM(tensor_size[0], tensor_size[1], tensor_matrix)

    def isHermitian(self):
        return self.isSquared() and self.adjoint() == self

    def isUnitary(self):
        if not self.isSquared():
            return False
        return self * self.adjoint() == self.getIdentity()

    def normalize(self):
        norm = self.norm()
        (m, n) = self.getSize()
        new_values = [ [self[i][j] / norm for j in range(n)] for i in range(m)]

        return ComplexM(m, n, new_values)

    def getIdentity(self):
        m, n = self.getSize()
        if m != n:
            return None
        values = [[1 if i == j else 0 for i in range(m)] for j in range(n)]
        return ComplexM(m, n, values)

    def getRow(self, i):
        return self[i]

    def getCol(self, j):
        return self.transpose()[j]

    def toString(self):
        t = PrettyTable(header=False)

        for row in self:
            t.add_row(row)

        return str(t)
