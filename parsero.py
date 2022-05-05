
import sys

from ast import *


class ProgramNode:
    '''
    AST du programme
    '''

    def __init__(self):
        self.statements = []

    def __str__(self):
        return [self.statements[i].__str__() for i in range(len(self.statements))].__str__()



class StatementNode:

    def __init__(self):
        self.expression =  []
        self.loop_counter = 0
        self.loop_breaker_needed = 0

    def __str__(self):

        return self.expression[0].__str__()



class ExpressionNode:

    def __init__(self):
        self.operator = None
        self.lhs = None
        self.rhs = None

    def __str__(self):
        if self.operator != None:
            return "{} {} {}".format(self.lhs.__str__(),self.operator.tag,self.rhs.__str__())
        else :
            return self.lhs.__str__()



class NumberNode:

    def __init__(self):
        self.tag = "NUMBER"
        self.value = None
    #
    # def __str__(self):
    #
    #     return "Number"
    #

class IdentifierNode:

    def __init__(self):
        self.tag = "IDENTIFIER"
        self.value = None

    # def __str__(self):
    #
    #     return "Identifier"
    #
    #


class UnaryNode:

    def __init__(self):
        self.value = 0

    def __str__(self):

        return self.value.tag




class Parser:

    def __init__(self):
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
            return None
            # self.error('No more lexems left.')


    def expect(self, tag):
        '''
        Pops the next token from the lexems list and tests its type through the tag.
        '''
        next_lexem = self.peek()
        if next_lexem.tag == tag:
            return self.accept()
        else:
            # self.error('Expected {}, got {} instead'.format(tag, next_lexem.tag))
            return None


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
            Identifier, '=', Expression ';' // EXAMPLE

        '''
        '''
            Un statement correspond à une ligne donc 
            on va déterminer quelle est l'expression de chaque ligne/statement
        '''
        print('parsing statement')

        statement_node = StatementNode()
        # statement_node.expression = self.parse_expression()
        # self.expect('TERMINATOR')







        if self.peek().tag == 'WHILE':
            statement_node.expression.append(self.accept())
            statement_node.loop_counter += 1
            statement_node.loop_breaker_needed += 1
            # expect(TLDR) to break the loop
            # expect(BRB to close the loop)

        elif self.peek().tag == "FOR":
            statement_node.expression.append(self.parse_for())

        elif self.peek().tag in ["STFW", "ROFL", "N00B", "L33T", "HAXOR", "AFK", "LMAO", "ROFLMAO"]:
            statement_node.expression.append(self.parse_other())
            # expect(identifier)

        elif self.peek().tag == "IDENTIFIER":
            statement_node.expression.append( self.parse_expression())

        return statement_node




    def parse_expression(self):
        '''
        Parses an expression that looks like:

            Unary, {[ "/" | "+" | "-" | "*" ], Expression}
        '''
        print('parsing expression')
        expression_node = ExpressionNode()
        expression_node.lhs,unary_lign = self.parse_unary()
        # print('xpression_node.lhs.value.name',expression_node.lhs.value.name)

        # To check the type of the expression, we look for a ';' after the first identifier or number

        # #D'abord, on regarde quelle est le nombre de lexeme de la ligne
        # line_number = self.peek().position[0]
        # index = 1
        # self.accept()
        # if self.peek(index).position[0] == line_number:
        #     index+=1
        #     print('index',index)
        #


        if not self.peek().tag == 'TERMINATOR':

        # if (self.peek() != None) and (unary_lign == self.peek().position[0]): #si c'est dans la meme ligne
            # Binary operation so operator and another expression
            if self.peek().tag in ['IZ', 'TODEVNULL']:
                # - Une affectation (lol iz 4)
                # - Une remise à zéro (lol to /dev/null\)
                expression_node.operator = self.accept()
            else:
                self.error("Missing operator in expression.")

        else :
            self.accept()
            return expression_node
        expression_node.rhs = self.parse_expression()

        return expression_node


    def parse_unary(self):
        '''
        Parses an unary that looks like:
            Identifier | Number
        '''
        unary_node = UnaryNode()
        if self.peek() != None :
            if self.peek().tag == 'IDENTIFIER':
                unary_node.value, unary_lign = self.parse_identifier()
            elif self.peek().tag == 'NUMBER':
                unary_node.value, unary_lign = self.parse_number()
            else:
                self.error("Unary is either identifier or number")
        else:
            print('No more peeking nbecause no more token')
        return unary_node, unary_lign

    def parse_identifier(self):
        '''
        Parses an identifier that looks like:
            Character, {Character | Digit}
        '''

        identifier_node = IdentifierNode()
        token = self.expect('IDENTIFIER')
        identifier_node.value = token.value
        return identifier_node, token.position[0]


    def parse_number(self):
        '''
        Parses a number that looks like:
            Digit, {Digit}
        '''
        number_node = NumberNode()
        token = self.expect('NUMBER')
        number_node.value = token.value
        return number_node, token.position[0]

    # def parse_condition(self):
    #     '''
    #     Parses a condition that looks like:
    #         Character, {Character | Digit}
    #     '''
    #     condition_node = ConditionNode()
    #     token = self.expect('CONDITION')
    #     condition_node.type = token.value
    #     return condition_node