import re
import sys

regexExpressions = [
    (r'w00t [\s\S]*\n', 'COMMENT'),

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
    (r'\\n', 'TERMINATORBIS'),


    (r'\b4\b', 'FOR'),
    (r'wtf\b', 'WTF'),
    (r'rtfm\b', 'WHILE'),
    (r'rtfm', 'WHILE'),
    (r'stfu\b', 'STFU'),
    (r'stfw\b', 'STFW'),
    (r'iz\b', 'IZ'),
    (r'brb\b', 'BRB'),
    (r'uber\b', 'UBER'),
    (r'liek\b', 'LIEK'),
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
    (r'[0-9]+', 'NUMBER'),
]


class Lexem:

    def __init__(self, tag, value, position):
        self.tag = tag
        self.value = value
        self.position = position

    def __str__(self):
        return("lexem de tag {} de valeur {} en pos {}".format(self.tag, self.value, self.position))


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
                    print("error in matching lexem at :", lineNumber, position)
                    sys.exit(1)
                else:
                    position = match.end(0)

            # self.lexems.append(Lexem("TERMINATORBIS","\n",[lineNumber,position]))
        print("lexer: analysis successful!")
        return self.lexems
