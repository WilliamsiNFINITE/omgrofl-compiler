import re
import sys

from lexer import Lexer
from parsero import *

inputText = open("examples/example_basic").readlines()
lexer = Lexer()
lexems = lexer.lex(inputText)
# print(lexems[0].value, lexems[0].tag)
# print('done')


parseur = Parser()
stNode = StatementNode()
stNode.expression = ExpressionNode()
stNode.expression.type = 'NUMBER'
print('stNode',stNode)


ast = parseur.parse(lexems)

print('ast',ast)
