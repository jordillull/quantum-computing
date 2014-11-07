#!/usr/bin/env python3
'''
Lexical Analyser for our custom Quantum Assembler Language

@author: jllull
'''

from ply import lex

operations = {
    'INITIALIZE' : 'INITIALIZE',
    'TENSOR'     : 'TENSOR',
    'APPLY'      : 'APPLY',
    'SELECT'     : 'SELECT',
    'CONCAT'     : 'CONCAT',
    'MEASURE'    : 'MEASURE',
}
gates = {
    'CNOT'       : 'CNOT',
    'H'          : 'H',
}

tokens = [
    'IMATRIX',
    'REGISTER',
    'BITSTRING',
    'DIGIT',
    'VARIABLE',
]

tokens = tokens + list(operations.values()) + list(gates.values())

def QLexer():
    t_ignore = ' \t'

    def t_REGISTER(t):
        r'R\d+'
        t.type = 'REGISTER'
        return t


    def t_GT_IMATRIX(t):
        r'I\d+'
        t.type = 'GT_IMATRIX'
        return t

    def t_BITSTRING(t):
        r'\[[01]+\]'
        t.type = 'BITSTRING'
        return t

    def t_DIGIT(t):
        r'\d+'
        t.type = 'DIGIT'
        return t


    def t_VARIABLE(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'

        # Either operations and gates are reserved words
        t.type = operations.get(t.value)

        if t.type == None:
            t.type = gates.get(t.value)

        if t.type == None:
            t.type = 'VARIABLE'

        return t

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Error handling rule
    def t_error(t):
        print("Illegal character '{0}'".format(t.value[0]))
        t.lexer.skip(1)

    return lex.lex()

lexer = QLexer()

if __name__ == "__main__":
    lexer = QLexer()
    print("Lexical Analyser for the custom Quantum Assembler Language.")
    print("  Enter a line input to see its lexical analysis. Type 'exit' to end.")
    while True:
        print(">>> ", end="")
        inp = input()
        if inp == "exit":
            break
        lexer.input(inp)
        for tok in lexer:
            print(tok)

