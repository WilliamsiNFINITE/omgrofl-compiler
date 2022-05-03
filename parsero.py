
import sys

from ast import *


class ProgramNode:
    '''
    AST du programme
    '''

    def __int__(self):
        self.statements = None

    def __str__(self):

        return self.statements



class StatementNode:

    def __int__(self):
        self.condition = None
        self.expression = None

    def __str__(self):

        return self.conditon, self.expression



class ExpressionNode:

    def __int__(self):
        self.type = None
        self.value = None
        self.lhs = None
        self.rhs = None

    def __str__(self):

        return self.type.name, self.value



class NumberNode:

    def __int__(self):
        self.name = "Number"
        self.value = None

    def __str__(self):

        return self.name, self.value


class IdentifierNode:

    def __int__(self):
        self.name = "Identifier"
        self.value = None

    def __str__(self):

        return self.name, self.value


class ConditionNode:

    def __int__(self):
        self.type = None


    def __str__(self):

        return self.type




class UnaryNode:
    pass




class Parser:

    def __int__(self):
        self.test = []


    '''
    OMGROFL language parser.
    '''

    # ==========================
    #      Helper Functions
    # ==========================

    def error(self, message):
        '''
        Error template.
        '''
        print('ERROR at {}:'.format(str(self.peek().position)), message)
        sys.exit(1)

    def peek(self, n=1):
        '''
        Returns the next token in the list WITHOUT popping it.
        '''

        try:
            return self.lexems[n - 1]
        except IndexError:
            self.error('No more lexems left.')


    def expect(self, tag):
        '''
        Pops the next token from the lexems list and tests its type through the tag.
        '''
        next_lexem = self.peek()
        if next_lexem.tag == tag:
            return self.accept()
        else:
            self.error('Expected {}, got {} instead'.format(tag, next_lexem.tag))


    def accept(self):
        '''
        Pops the lexem out of the lexems list and log its tag/value combination.
        '''
        # lexem = self.peek()
        return self.lexems.pop(0)


    def remove_comments(self):
        '''
        Removes the comments from the token list by testing their tags.
        '''
        self.lexems = [lexem for lexem in self.lexems if lexem.tag!="COMMENT"]


    # ==========================
    #      Parse Functions
    # ==========================

    def parse(self, lexems):
        '''
        Main function: launches the parsing operation given a lexem list.
        '''
        self.lexems = lexems
        self.remove_comments()
        ast = self.parse_program()
        return ast


    def parse_program(self):
        '''
        Parses a program which is a succession of statements.
        '''
        program_node = ProgramNode()
        while(len(self.lexems) > 0):
            statement = self.parse_statement()
            program_node.statements.append(statement)
        return program_node


    def parse_statement(self):
        '''
        Parses an statement that looks like:
            Identifier, '=', Expression ';'
        '''
        statement_node = StatementNode()
        # statement_node.condition = self.parse_condition()
        # self.expect('ASSIGN')
        statement_node.expression = self.parse_expression()
        # self.expect('TERMINATOR')
        return statement_node


    def parse_expression(self):
        '''
        Parses an expression that looks like:



            Unary, {[ "/" | "+" | "-" | "*" ], Expression}
        '''
        expression_node = ExpressionNode()

        if self.peek().tag == 'WHILE':
            expression_node.type = self.accept()
            #expect(TLDR) to break the loop
            #expect(BRB to close the loop)

        elif self.peek().tag == "FOR":
            expression_node.type = self.accept()
            # expect(identifier IZ initial_number TWO ending_number)
            # expect(BRB to close the loop)

        elif self.peek().tag in ["STFW", "ROFL", "N00B", "L33T", "HAXOR", "AFK", "LMAO", "ROFLMAO"]:
            expression_node.type = self.accept()
            # expect(identifier)

        elif self.peek().tag == "IDENTIFIER":
            # Il faut peek le token d'après pour savoir si c'est :
            # - Une affectation (lol iz 4)
            # - Une remise à zéro (lol to /dev/null\)



        else:
            self.error("Missing operator in expression.")
            expression_node.rhs = self.parse_expression()


        return expression_node




        expression_node.lhs = self.parse_unary()
        # To check the type of the expression, we look for a ';' after the first identifier or number

        if not self.peek().tag == 'TERMINATOR':
            # Binary operation so operator and another expression
            if self.peek().tag in ['ADD', 'SUB', 'MULTIPLICATION', 'DIVISION']:
                expression_node.operator = self.accept()
            else:
                self.error("Missing operator in expression.")
            expression_node.rhs = self.parse_expression()
        return expression_node


    def parse_unary(self):
        '''
        Parses an unary that looks like:
            Identifier | Number
        '''
        unary_node = UnaryNode()
        if self.peek().tag == 'IDENTIFIER':
            unary_node.value = self.parse_identifier()
        elif self.peek().tag == 'NUMBER':
            unary_node.value = self.parse_number()
        else:
            print('self.peek.tag', self.peek().tag)
            self.error("Unary is either identifier or number")
        return unary_node


    def parse_condition(self):
        '''
        Parses a condition that looks like:
            Character, {Character | Digit}
        '''
        condition_node = ConditionNode()
        token = self.expect('CONDITION')
        condition_node.type = token.value
        return condition_node

    def parse_identifier(self):
        '''
        Parses an identifier that looks like:
            Character, {Character | Digit}
        '''
        identifier_node = IdentifierNode()
        token = self.expect('IDENTIFIER')
        identifier_node.name = token.value
        return identifier_node


    def parse_number(self):
        '''
        Parses a number that looks like:
            Digit, {Digit}
        '''
        number_node = NumberNode()
        token = self.expect('NUMBER')
        number_node.name = token.value
        return number_node
