import re
import sys

from lexer import Lexer
from parsero import *

inputText = open("examples/example_basic").readlines()
lexer = Lexer()
lexems = lexer.lex(inputText)
print(lexems[3].value, lexems[3].tag, lexems[3].position[0])
print('done')


parseur = Parser()
print('________________________________________ printing ast ________________________________________ ')
ast = parseur.parse(lexems)

print('ast',ast)


