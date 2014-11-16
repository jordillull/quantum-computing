Quantum Computing
=================

This project aims to build a quantum computer emulator from scratch, including
all the mathematical foundations that supports a quantum computer.

Since I'm using my own module for handling complex numbers it will be extremely
inefficient. However, having a complex matrix object with methods such as
``is_hermitian()`` or ``normalize()`` allows us to easily understand the underlying
math in quantum computing.

Dependencies
------------
* [PLY](https://pypi.python.org/pypi/ply) Used for the lexical and syntactic
analyzer of the quantumc computer assembly language.
* [PrettyTables](https://pypi.python.org/pypi/PrettyTable) _(optional)_ for
cool printing of complex matrices.

References
----------

Most of the concepts used are extracted from the book [Quantum computing for
Computer Scientists](http://www.amazon.com/Quantum-Computing-Computer-Scientists-Yanofsky/dp/0521879965/)
by _Noson S. Yanofsky_ and _Mirco A. Mannucci_.

The [lecture notes](http://www.scottaaronson.com/democritus/) of _Scott
Aaronson_ about quantum computing were also a big help to understand quantum
mechanics and an invaluable source of inspiration.
