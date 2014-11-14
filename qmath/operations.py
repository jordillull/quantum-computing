'''
Implements some operations over quantum systems

@author: Jordi Llull
'''
import os
import sys
import inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from complex import ComplexM


def q_observe(vector: 'ComplexM', hmatrix: 'ComplexM'):
    '''
    Simulates an observation in a quantum system.

    Given a vector of size n representing a quantum system and a hermitian
    matrix of size n×n it will return the mean value and the variance of the
    observable on the given state
    '''
    if not isinstance(vector, ComplexM) or not isinstance(hmatrix, ComplexM):
        raise TypeError("The parameters should be of type ComplexM")

    if not hmatrix.is_hermitian():
        raise ValueError("The second parameter shoudl be a hermitian matrix")

    return hmatrix * vector
