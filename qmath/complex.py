'''
Handles complex numbers

@author: Jordi Llull
'''

from math import sqrt
from math import sin, cos, atan, pi
from prettytable import PrettyTable


class Complex(object):

    def __init__(self, real=None, imaginary=None):
        if imaginary is None:
            value = real
            if value is None:
                self.value = (0, 0)
            elif isinstance(value, (int, float)):
                self.value = (value, 0)
            elif isinstance(value, Complex):
                self.value = (value.real_value, value.imaginary_value)
            elif isinstance(value, (tuple, list)) and len(value) == 2:
                self.value = (value[0], value[1])
            else:

                raise TypeError("Cannot make a complex number from an object of class {0}"
                                .format(value.__class__.__name__))
        else:
            self.value = (real, imaginary)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, tuple):
            raise ValueError("The complex value should be a tuple of size 2")

        if isinstance(new_value[0], (int, float)) and isinstance(new_value[1], (int, float)):
            self._value = new_value
        else:
            raise TypeError("The real and the imaginary part of a complex number should be valid real numbers")

    @property
    def real_value(self):
        return self.value[0]

    @property
    def imaginary_value(self):
        return self.value[1]

    def __str__(self):
        return self.to_string()

    def __add__(self, other):
        other = Complex(other)

        real = self.real_value + other.real_value
        imaginary = self.imaginary_value + other.imaginary_value

        return Complex(real, imaginary)

    def __sub__(self, other):
        other = Complex(other)

        return self.__add__(-other)

    def __mul__(self, other):
        if isinstance(other, ComplexM):
            return other * self
        else:
            other = Complex(other)

            real = (self.real_value * other.real_value) - (self.imaginary_value * other.imaginary_value)
            imaginary = (self.real_value * other.imaginary_value) + (self.imaginary_value * other.real_value)

            return Complex(real, imaginary)

    def __div__(self, other):
        return self.__truediv__(other)

    def __truediv__(self, other):
        other = Complex(other)
        dividend = other.real_value ** 2.0 + other.imaginary_value ** 2.0
        if dividend == 0:
            raise ZeroDivisionError("Can't divide a complex number by 0")

        real = (self.real_value * other.real_value + self.imaginary_value * other.imaginary_value) / dividend
        imaginary = (self.imaginary_value * other.real_value - self.real_value * other.imaginary_value) / dividend

        return Complex(real, imaginary)

    def __neg__(self):
        return Complex(-self.real_value, -self.imaginary_value)

    def __abs__(self):
        '''
        returns the modulus of the complex number
        '''
        return sqrt(self.real_value ** 2 + self.imaginary_value ** 2)

    def __eq__(self, other):
        other = Complex(other)
        return self.real_value == other.real_value and self.imaginary_value == other.imaginary_value

    def get_value(self):
        return self.__value

    def set_value_from_polar(self, modulus, angle):
        real = modulus * cos(angle)
        imaginary = modulus * sin(angle)
        self.value = (real, imaginary)
        return self

    def get_value_as_polar(self):
        a = self.real_value
        b = self.imaginary_value
        modulus = abs(self)
        if a == 0:  # Angle in the Y axis
            angle = pi / 2.0 if b >= 0 else 3 * pi / 2.0
        else:
            angle = atan(b / float(a))
            if a < 0:  # Second and third quadrant
                angle = angle + pi

        return (modulus, angle)

    def conjugate(self):
        return Complex(self.real_value, -self.imaginary_value)

    def to_string(self):
        string = ""
        if self.real_value != 0:
            if self.imaginary_value == 0:
                string = "{0}".format(self.real_value)
            else:
                i = abs(self.imaginary_value) if abs(self.imaginary_value) != 1 else ""
                string = "{real}{sign}{imaginary}i".format(real=self.real_value,
                                                           imaginary=i,
                                                           sign='+' if self.imaginary_value > 0 else "-")
        elif self.imaginary_value != 0:
            sign = "-" if self.imaginary_value < 0 else ""
            imaginary = abs(self.imaginary_value) if abs(self.imaginary_value) != 1 else ""
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
        len_n = [lx for lx in map(lambda x: len(x), matrix) if lx != n]

        if len_m != m or len_n != []:
            if len_n != []:
                len_n = len_n[0]
            else:
                len_n = n
            raise ValueError("Expected a bidimensional array of length {0}x{1}. An array of {2}x{3} was given instead"
                             .format(m, n, len_m, len_n))

        self._size = (m, n)

        my_mat = []
        for row in matrix:
            my_mat.append(tuple(map(lambda x: Complex(x), row)))

        self._matrix = tuple(my_mat)

    @property
    def matrix(self):
        return self._matrix

    @property
    def size(self):
        return self._size

    def __str__(self):
        return self.to_string()

    def __add__(self, other):
        if isinstance(other, ComplexM):
            if self.size != other.size:
                self_size = 'x'.join(map(lambda x: str(x), self.size))
                other_size = 'x'.join(map(lambda x: str(x), other.size))
                raise ValueError("Can't sum ComplexM of size {0} with a ComplexM of size {1}"
                                 .format(self_size, other_size))

            new_values = tuple(map(lambda r1, r2: tuple(map(lambda x, y: x + y, r1, r2)), self, other))
            m, n = self.size
            return ComplexM(m, n, tuple(new_values))
        else:
            raise TypeError("Cannot sum a ComplexM with and object of class {0}"
                            .format(other.__class__.__name__))

    def __sub__(self, other):
        return self.__add__(-other)

    def __eq__(self, other):
        if self.size != other.size:
            return False

        return self.matrix == other.matrix

    def __scalarmul__(self, other):
        new_values = tuple(map(lambda i: tuple(map(lambda j: other * j, i)), self))
        m, n = self.size
        return ComplexM(m, n, new_values)

    def __matrixmul__(self, other):
        sm, sn = self.size
        om, on = other.size

        if sn != om:
            raise TypeError("Cannot multiply a ComplexM of size {0}x{1} with a ComplexM of size {2}x{3}"
                            .format(str(sm), str(sn), str(om), str(on)))

        new_values = [[Complex(0) for _ in range(on)] for _ in range(sm)]

        for i in range(sm):
            for j in range(on):
                for r1, r2 in zip(self.get_row(i), other.get_col(j)):
                    new_values[i][j] += r1*r2

        return ComplexM(sm, on, new_values)

    def __mul__(self, other):
        if isinstance(other, Complex):  # Scalar multiplication
            return self.__scalarmul__(other)
        elif isinstance(other, ComplexM):
            return self.__matrixmul__(other)
        else:
            raise TypeError("Cannot sum a complex number with and object of class {0}"
                            .format(other.__class__.__name__))

    def __neg__(self):
        new_values = tuple(map(lambda i: tuple(map(lambda j:-j, i)), self))
        m, n = self.size
        return ComplexM(m,n, new_values)

    def __getitem__(self, i):
        return self.matrix[i]

    def inner_product(self, other):
        if not isinstance(other, ComplexM):
            raise TypeError("Cannot do the inner_product of ComplexM with an object of class {0}".format(other.__class__.__name__))

        if self.is_vector() and other.is_vector():
            return (self.adjoint() * other).trace()
        elif self.is_squared() and other.is_squared() and self.size[0] == other.size[0]:
            return (self.transpose() * other).trace()
        else:
            self_size = 'x'.join(map(lambda x: str(x), self.size))
            other_size = 'x'.join(map(lambda x: str(x), other.size))
            raise ValueError("Cannot do the inner_product of a ComplexM of size {0} with a ComplexM of size {1}"
                             .format(self_size, other_size))

    def conjugate(self):
        new_values = tuple(map(lambda r: tuple(map(lambda x: x.conjugate(), r)), self))
        m, n = self.size
        return ComplexM(m, n, new_values)

    def transpose(self):
        m, n = self.size
        new_values = [[self[j][i] for j in range(m)] for i in range(n)]

        return ComplexM(n, m, new_values)

    def adjoint(self):
        return self.conjugate().transpose()

    def is_vector(self):
        return self.size[1] == 1

    def is_squared(self):
        return self.size[0] == self.size[1]

    def trace(self):
        if not self.is_squared():
            raise ValueError("A matrix of size {0}x{1} is not an squared matrix"
                             .format(str(self.size[0]), str(self.size[1])))
        res = Complex(0)
        for i in range(self.size[0]):
            res += self[i][i]

        return res

    def norm(self):
        return sqrt(self.inner_product(self).real_value)

    def distance(self, other):
        return (self - other).norm()

    def tensor(self, other):
        (sm, sn) = self.size
        (m, n) = other.size
        # We are using the formal definition of Tensor here. I.e:
        #     Being size of B m×n
        #     (A ⊗ B)[i, j] = A[i/m, j/n] * B[i % m, j % n]
        tensorFnx = lambda i, j: self[i // m][j // n] * other[i % m][j % n]
        tensor_size = (sm * m, sn * n)
        tensor_matrix = [[tensorFnx(i, j) for j in range(tensor_size[1])] for i in range(tensor_size[0])]

        return ComplexM(tensor_size[0], tensor_size[1], tensor_matrix)

    def is_hermitian(self):
        return self.is_squared() and self.adjoint() == self

    def is_unitary(self):
        if not self.is_squared():
            return False
        return self * self.adjoint() == self.get_identity()

    def normalize(self):
        norm = self.norm()
        (m, n) = self.size
        new_values = [[self[i][j] / norm for j in range(n)] for i in range(m)]

        return ComplexM(m, n, new_values)

    def get_identity(self):
        m, n = self.size
        if m != n:
            return None
        values = [[1 if i == j else 0 for i in range(m)] for j in range(n)]
        return ComplexM(m, n, values)

    def get_row(self, i):
        return self[i]

    def get_col(self, j):
        return self.transpose()[j]

    def to_string(self):
        t = PrettyTable(header=False)

        for row in self:
            t.add_row(row)

        return str(t)
