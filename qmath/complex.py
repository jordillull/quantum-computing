'''
Handles complex numbers

@author: Jordi Llull
'''

from math import sqrt

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
        other = Complex(other)

        real = (self.getRealValue() * other.getRealValue()) - (self.getImaginaryValue() * other.getImaginaryValue())
        imaginary = (self.getRealValue() * other.getImaginaryValue()) + (self.getImaginaryValue() * other.getRealValue())

        return Complex(real, imaginary)

    def __div__(self, other):
        return self.__truediv__(other)

    def __truediv__(self, other):
        other = Complex(other)
        dividend = other.getRealValue() ** 2 + other.getImaginaryValue() ** 2
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
