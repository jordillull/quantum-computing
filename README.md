# Quantum Computing
[![Build Status](https://travis-ci.org/jordillull/quantum-computing.svg?branch=master)](https://travis-ci.org/jordillull/quantum-computing)

This project aims to build a quantum computer emulator from scratch, including
all the mathematical foundations that supports a quantum computer.

Since I'm using my own module for handling complex numbers it will be extremely
inefficient. However, having a complex matrix object with methods such as
``is_hermitian()`` or ``normalize()`` allows us to easily understand the
underlying math in quantum computing.

## Requirements
* [PLY](https://pypi.python.org/pypi/ply) Used for the lexical and syntactic
analyzer of the quantum computer assembly language.
* [PrettyTables](https://pypi.python.org/pypi/PrettyTable) _(optional)_ for
cool printing of complex matrices.

## Usage
From the root of the project type ``make qparse``. This starts a quantum
computer with 16 registers of 9 qubits and prompts a shell expecting
instructions.

### Quantum Computer internal status
You can call STATUS from a shell to see the current internal values of the
quantum registers and quantum variables. Note that this is **not** the same as
calling the instruction MEASURE. The status instruction will display the
current status of the quantum computer including the matrix representing the
quantum state of its registers without affecting its internal state.

Obviously, we can only do it because we are emulating the quantum computer, this
wouldn't be possible with a real quantum system.


### Instructions
As per the current release only the initialize instruction is implemented.
* ``INITIALIZE Rn`` Initialize register n. You can call it with a bitstring to
initialize it to a given value (_e.g. ``INITIALIZE R6 [100010001]`` will
 initialize R6 to the identity matrix_).
* ``SELECT`` _Not implemented yet_
* ``CONCAT `` _Not implemented yet_
* ``APPLY`` _Not implemented yet_
* ``TENSOR`` _Not implemented yet_
* ``MEASURE`` _Not implemented yet_


## References

Most of the concepts used are extracted from the book [Quantum computing for
Computer Scientists](http://www.amazon.com/Quantum-Computing-Computer-Scientists-Yanofsky/dp/0521879965/)
by _Noson S. Yanofsky_ and _Mirco A. Mannucci_.


Both [Quantum Computing since
Democritus](http://www.amazon.com/Quantum-Computing-since-Democritus-Aaronson-ebook/dp/B00B4V6IZK/)
and its [lecture notes](http://www.scottaaronson.com/democritus/) by _Scott
Aaronson_ were of big help to understand quantum mechanics and an invaluable
source of inspiration

If you are, like me, just a computer scientist without any clue about physics
but you really want to understand all this sh*t I'd encourage you to start by
reading [Decoding the
Universe](http://www.amazon.com/Decoding-Universe-Information-Explaining-Everything-ebook/dp/B000O76NFK)
by _Charles Seife_. This book makes a gently introduction to modern physics from
an information theory perspective.
