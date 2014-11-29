# Quantum Computing
[![Build Status](https://travis-ci.org/jordillull/quantum-computing.svg?branch=master)]
(https://travis-ci.org/jordillull/quantum-computing)

This project aims to build a quantum computer emulator from scratch, including
all the mathematical foundations that supports a quantum computer.

Since I'm using my own module for handling complex numbers it will be extremely
inefficient. However, having a complex matrix object with methods such as
``is_hermitian()`` or ``normalize()`` allows us to easily understand the
underlying math in quantum computing.

## Requirements
* Python3
* [PLY](https://pypi.python.org/pypi/ply) Used for the lexical and syntactic
analyzer of the quantum computer assembly language.
* [PrettyTables](https://pypi.python.org/pypi/PrettyTable) *(optional)* for
cool printing of complex matrices.

## Usage
Run ``pip3 install -r requirements.txt`` to install requirements.

From the root of the project type ``python3 qsimulator/qparse.py``. This starts
a quantum computer with 16 registers of 9 qubits and prompts a shell expecting
instructions.

### Quantum Computer internal status
You can call STATUS from a shell to see the current internal values of the
quantum registers and quantum variables. Note that this is **not** the same as
calling the instruction MEASURE. The status instruction will display the
current status of the quantum computer including the matrix representing the
quantum state of its registers without affecting its internal state.

Obviously, we can only do it because we are emulating the quantum computer, this
wouldn't be possible with a real quantum system.

### Assembler Instructions
As per the current release only the initialize and select instructions are
implemented.

#### 1. INITIALIZE
The instruction ``INTIALIZE RN [01..01]`` will initialize the Nth register to
the given bitstring. If you don't provide a bitstring it will be initialized
with zeros.

**Example:** ``INITIALIZE R6 [100010001]`` will initialize R6 to the identity matrix.

Note that when the quantum computer is started all its quantum registers are in
a uninitialized status. Trying to access an uninitialized register will cause an
exception.

It can be discussed whether this uninitialized behavior is a good choice or not.
My guess is that future real quantum computers would still need a big amount of
energy to start and maintain a register so it makes sense to force programmers
to explicitly initialized the registers when they need it.

#### 2. SELECT
``SELECT V RN X Y`` Puts _Y_ qubits from the Nth register into the variable _V_
starting from _X_

**Example:**
```
INITIALIZE R0 [010010011]
SELECT MYVAR R0 3 6
```
MYVAR will contain qubits of R0 from 3 to 9.
```
[qparse] >>> STATUS
Quantum Computer with 16 registers of 9 qbits
====== Registers ======
R0:
+---+---+---+
| 0 | 1 | 0 |
| 0 | 1 | 0 |
| 0 | 1 | 1 |
+---+---+---+
R1...R15: Not initialized

====== Variables ======
MYVAR:
+---+---+---+---+---+---+
| 0 | 1 | 0 | 0 | 1 | 1 |
+---+---+---+---+---+---+
```

#### 3. CONCAT
*Not implemented yet*

#### 4. APPLY
*Not implemented yet*

#### 5. TENSOR
*Not implemented yet*

#### 6. MEASURE
*Not implemented yet*



## References

Most of the concepts used are extracted from the book [*Quantum computing for
Computer Scientists*](http://www.amazon.com/Quantum-Computing-Computer-Scientists-Yanofsky/dp/0521879965/)
by *Noson S. Yanofsky* and *Mirco A. Mannucci*.


Both [*Quantum Computing since
Democritus*](http://www.amazon.com/Quantum-Computing-since-Democritus-Aaronson-ebook/dp/B00B4V6IZK/)
and its [lecture notes](http://www.scottaaronson.com/democritus/) by *Scott
Aaronson* were of big help to understand quantum mechanics and an invaluable
source of inspiration

If you are, like me, just a computer scientist without any clue about physics
but you really want to understand all this sh*t I'd encourage you to start by
reading [*Decoding the
Universe*](http://www.amazon.com/Decoding-Universe-Information-Explaining-Everything-ebook/dp/B000O76NFK)
by *Charles Seife*. This book makes a gently introduction to modern physics from
an information theory perspective.
