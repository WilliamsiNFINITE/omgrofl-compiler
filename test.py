import re
import sys

from lexer import Lexer
from parsero import *

inputText = open("examples/example_basic").readlines()
lexer = Lexer()
lexems = lexer.lex(inputText)
print(lexems[10].value, lexems[10].tag, lexems[10].position[0])
print('done')


parseur = Parser()
print('________________________________________ printing ast ________________________________________ ')
ast = parseur.parse(lexems)

print('ast \n ',ast)


