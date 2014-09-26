'''
Implements some operations over quantum systems

@author: Jordi Llull
'''
import os, sys, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from complex import ComplexM

'''
Simulates an observation in a quantum system.

Given a vector of size n representing a quantum system and a hermitian
matrix of size n×n it will return the mean value and the variance of the
observable on the given state
'''
def qObserve(vector: 'ComplexM', hmatrix: 'ComplexM'):
    if not isinstance(vector, ComplexM) or not isinstance(hmatrix, ComplexM):
        raise TypeError("The parameters should be of type ComplexM")

    if not hmatrix.isHermitian():
        raise ValueError("The second parameter shoudl be a hermitian matrix")

    return hmatrix * vector
