import re
import sys

from lexer import Lexer
from parsero import *
A = [1,2,3]
B = sum(A)
print('B',B)
inputText = open("examples/example_basic").readlines()
lexer = Lexer()
lexems = lexer.lex(inputText)
print(lexems[9].value, lexems[9].tag, lexems[9].position[0])
print('done')


parseur = Parser()
print('________________________________________ printing ast ________________________________________ ')
ast = parseur.parse(lexems)

print('ast \n ',ast)


