import re
import sys

from lexer import Lexer
# from parser import Parser

regexExpressions = [


    (r'\/\b', 'SLASH'),
    (r'\\\b', 'BACKSLASH'),
    (r'\?\b', 'ASKPOINT'),
    (r'\!\b', 'EXCPOINT'),
    (r'\,\b', 'COMA'),
    (r'\.\b', 'PERIOD'),
    (r'\:\b', 'COLUMN'),
    (r'\;\b', 'SEMICOLUMN'),
    (r'\'\b', 'APOSTROPHE'),
    (r'\"\b', 'QUOTE'),
    (r'\-\b', 'SUB'),
    (r'\+\b', 'ADD'),
    (r'\_\b', 'UNDERSCORE'),
    (r'\=\b', 'EQUAL'),
    (r'\#\b', 'HASHTAG'),
    (r'\>\b', 'GREATERTHAN'),
    (r'\<\b', 'LOWERTHAN'),

    (r'\b4\b', 'FOR'),
    (r'wtf\b', 'IF'),
    (r'rtfm\b', 'WHILE'),
    (r'stfu\b', 'STOP'),
    (r'stfw\b', 'STFW'),
    (r'iz\b', 'IZ'),
    (r'brb\b', 'BRB'),
    (r'uber\b', 'GREATERTHAN'),
    (r'liek\b', 'EQUAL'),
    (r'2\b', 'TWO'),
    (r'afk\b', 'AFK'),
    (r'w00t\b', 'W00T'),
    (r'lmao\b', 'LMAO'),
    (r'roflmao\b', 'ROFLMAO'),
    (r'rofl\b', 'ROFL'),
    (r'n00b\b', 'N00B'),
    (r'l33t\b', 'L33T'),
    (r'haxor\b', 'HAXOR'),
    (r'tldr\b', 'TLDR'),

    (r'[ \n\t]+', None),
    (r'#[^\n]*', None),
    (r'[l]o+[l]\b', 'IDENTIFIER'),
    (r'[a-zA-Z0-9]\D+\w*', 'COMMENT'),
    (r'[0-9]', 'DIGIT'),
]


inputText = open("examples/example").readlines()
A = Lexer()
B = A.lex(inputText)
#
# C = Parser()




print(A.lexems)
# print(B)
print('done')
# print(B)
#
# print([B[i].tag for i in range(6)])