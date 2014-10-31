#!/usr/bin/env python3
'''
Lexical Analyser for our custom Quantum Assembler Language

@author: jllull
'''

from ply import lex

operations = {
    'INITIALIZE' : 'INITIALIZE',
    'APPLY'      : 'APPLY',
    'SELECT'     : 'SELECT',
    'CONCAT'     : 'CONCAT',
    'MEASURE'    : 'MEASURE',
}
gates = {
    'TENSOR'     : 'TENSOR',
    'CNOT'       : 'CNOT',
    'H'          : 'H',
}

tokens = [
    'REGISTER',
    'IDENTITY_MATRIX',
    'DIGIT',
    'IDENTIFIER',
]

tokens = tokens + list(operations.values()) + list(gates.values())

t_REGISTER        = r'R\d+' # R followed by a digit
t_IDENTITY_MATRIX = r'I\d+'
t_DIGIT           = r'\d+'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'

    # Either operations and gates are reserved words
    t.type = operations.get(t.value)

    if (t.type == None):
        t.type = gates.get(t.value)

    if (t.type == None):
        t.type = 'IDENTIFIER'

    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '{0}'".format(t.value[0]))
    t.lexer.skip(1)

t_ignore = ' \t'

if __name__ == "__main__":
    lexer = lex.lex()
    print("Lexycal Analyser for the custom Quantum Assembler Language.")
    print("  Enter a line input to see its lexycal analysis. Type 'exit' to end.")
    while True:
        print(">>> ", end="")
        inp = input()
        if (inp == "exit"):
            break
        lexer.input(inp)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
