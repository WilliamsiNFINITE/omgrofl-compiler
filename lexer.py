import re
import sys

regexExpressions = [
    (r'[ \n\t]+', None),
    (r'#[^\n]*', None),
    (r'[l]o+[l]\b', 'IDENTIFIER'),
    (r'[a-zA-Z0-9]\w*', 'COMMENT'),
    (r'[0-9]', 'DIGIT'),

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

]


class Token:

    def __init__(self, tag, value, position):
        self.tag = tag
        self.value = value
        self.position = position


class Lexer:

    def __init__(self):
        self.tokens = []

    def lex(self, inputText):

        lineNumber = 0
        for line in inputText:
            lineNumber += 1
            position = 0
            while position < len(line):
                match = None
                for tokenRegex in regexExpressions:
                    pattern, tag = tokenRegex
                    regex = re.compile(pattern)
                    match = regex.match(line, position)
                    if match:
                        data = match.group(0)
                        if tag:
                            token = Token(tag, data, [lineNumber, position])
                            self.tokens.append(token)
                            print("token value = " + str(token.value))
                        break
                if not match:
                    print(position)
                    print(inputText[position])
                    print("no match")
                    sys.exit(1)
                else:
                    position = match.end(0)
        print("lexer: analysis successful!")
        return self.tokens


inputText = open("example").readlines()
A = Lexer()
B = A.lex(inputText)
# print(B)
print('done')
# print(B)
#
# print([B[i].tag for i in range(6)])
