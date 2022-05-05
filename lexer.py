import re
import sys

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
    (r'\;', 'TERMINATOR'),


    (r'\b4\b', 'FOR'),
    (r'wtf\b', 'IF'),
    (r'rtfm\b', 'WHILE'),
    (r'rtfm', 'WHILE'),
    (r'stfu\b', 'STOP'),
    (r'stfw\b', 'STFW'),
    (r'iz\b', 'IZ'),
    (r'brb\b', 'BRB'),
    (r'uber\b', 'GREATERTHAN'),
    (r'liek\b', 'EQUAL'),
    (r'2\b', 'TWO'),
    (r'afk\b', 'AFK'),
    (r'lmao\b', 'LMAO'),
    (r'roflmao\b', 'ROFLMAO'),
    (r'to /dev/null\b', 'TODEVNULL'),
    (r'rofl\b', 'ROFL'),
    (r'n00b\b', 'N00B'),
    (r'nope\b', 'NOPE'),
    (r'l33t\b', 'L33T'),
    (r'haxor\b', 'HAXOR'),
    (r'tldr\b', 'TLDR'),

    (r'[ \n\t]+', None),
    (r'#[^\n]*', None),
    (r'[l]o+[l]\b', 'IDENTIFIER'),
    (r'w00t [\s\S]*\n', 'COMMENT'),
    (r'[0-9]+', 'NUMBER'),
]


class Lexem:

    def __init__(self, tag, value, position):
        self.tag = tag
        self.value = value
        self.position = position


class Lexer:

    def __init__(self):
        self.lexems = []

    def lex(self, inputText):

        lineNumber = 0
        for line in inputText:
            lineNumber += 1
            position = 0
            while position < len(line):
                match = None
                for lexemRegex in regexExpressions:
                    pattern, tag = lexemRegex
                    regex = re.compile(pattern)
                    match = regex.match(line, position)
                    if match:
                        data = match.group(0)
                        if tag:
                            lexem = Lexem(tag, data, [lineNumber, position])
                            self.lexems.append(lexem)
                            # print("lexem tag = " + str(lexem.tag))
                        break
                if not match:
                    print("pos : ",position)
                    print("input_pos : " ,inputText[position])
                    print("no match")
                    sys.exit(1)
                else:
                    position = match.end(0)
        print("lexer: analysis successful!")
        return self.lexems






