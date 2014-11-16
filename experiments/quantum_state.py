#!/usr/bin/env python3
'''
Simulates a quantum system. It takes two inputs. The first input is a vector
describing the state of the quantum system. The second input might be an index
of the first vector or another vector.

If the second input is an an index it prints the probability of the quantum
system of being found in the given state after making a measurement.

If the second input its a vector it returns the probability of the quantum
system of transitioning to the state represented by the second vector after
measuring it.

@author: Jordi Llull
'''
import os
import sys
import inspect

cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]) + "/..")
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from qsimulator.qmath import ComplexM


def get_vector_or_index():

    vector = []
    element = input('> ')

    while element != '':
        t = element.split(',')
        if len(t) >= 2:
            vector.append([(int(t[0]), int(t[1]))])
        else:
            vector.append([int(t[0])])
        element = input('> ')

    if len(vector) == 1:
        return (vector[0][0], False)
    else:
        return (ComplexM(len(vector), 1, vector), True)


def get_probability_transition(v, w):

    if isinstance(w, ComplexM):
        # This is equivalent to v.normalize().inner_product(w.normalize())
        return v.inner_product(w) / (v.norm() * w.norm())
    else:
        return (abs(v[w][0]) ** 2) / (v.norm() ** 2)


def main():

    print("""Insert a vector describing a quantum state. Each element separated by a new line.""")
    (v, is_vector) = get_vector_or_index()
    if not is_vector:
        raise ValueError("Expected the first input to be a vector")
    print()
    print("""Insert a second vector or an index of the first vector""")
    (w, is_vector) = get_vector_or_index()

    p = get_probability_transition(v, w)
    print()
    if is_vector:
        print("The probability of the system transitioning from the first state to the second is {0}".format(p))
    else:
        print("The probability of the particle being found at state {0} is {1}".format(w, p))

if __name__ == '__main__':
    main()
