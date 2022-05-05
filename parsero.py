
import sys

from ast import *


indent = "    "

class ProgramNode:
    '''
    AST du programme
    '''

    def __init__(self):
        self.statements = []

    def __str__(self):
        string = ""
        for i in range(len(self.statements)):
            string += self.statements[i].__str__()
        return "{Program : \n " + string + "\n}"



class StatementNode:

    def __init__(self):
        self.expression =  []
        self.loop_counter = 0
        self.loop_breaker_needed = 0

    def __str__(self):

        return 1*indent + "{Statement : \n " + self.expression[0].__str__() + "\n"+\
               1*indent + "}\n"



class AssignmentNode:

    def __init__(self):
        self.operator = None
        self.lhs = None
        self.rhs = None

    def __str__(self):
        if self.operator != None:
            return 2*indent + "{Expression : \n" + \
                   3*indent + "Left :  {}".format(self.lhs.__str__()) + "\n" +\
                   3*indent + "Operator : {}".format(self.operator.tag) + "\n" +\
                   3*indent + "Right : {}".format(self.rhs.__str__()) + "\n" +\
                   2*indent + "}\n"

        else:
            return self.lhs.__str__()

class OtherNode:

    def __init__(self):
        self.operator = None
        self.variable = None

    def __str__(self):
        if self.operator != None:
            return 2*indent + "{Expression : \n" + \
                   3*indent + "Operator : {}".format(self.operator.tag) + "\n" +\
                   3*indent + "Variable : {}".format(self.variable.tag) + "\n" +\
                   2*indent + "}\n"

        else:
            return self.lhs.__str__()

class WhileNode:

    def __init__(self):
        self.operator = None

    def __str__(self):
        return 2 * indent + "{Loop : \n" + \
               3 * indent + "Operator : {}".format(self.operator.tag) + "\n" + \
               2 * indent + "}\n"


class StfuNode:

    def __init__(self):
        self.end = None

    def __str__(self):
        return 2 * indent + "{End of Program\n" + \
               2 * indent + "}\n"




class BrbNode:

    def __init__(self):
        self.loop = None

    def __str__(self):
        return 2 * indent + "{End of loop\n" + \
               2 * indent + "}\n"


class ForNode:
    def __init__(self):
        self.variable = None
        self.initial_value = None
        self.end_value = None

    def __str__(self):
        return 2 * indent + "{Loop : \n" + \
               3 * indent + "Variable :  {}".format(self.variable.tag) + "\n" + \
               3 * indent + "Initial Value : {}".format(self.initial_value.tag) + "\n" + \
               3 * indent + "Ending Value : {}".format(self.end_value.tag) + "\n" +\
               2 * indent + "}\n"


class NumberNode:

    def __init__(self):
        self.tag = "NUMBER"
        self.value = None

class IdentifierNode:

    def __init__(self):
        self.tag = "IDENTIFIER"
        self.value = None

class UnaryNode:

    def __init__(self):
        self.value = None

    def __str__(self):

        return self.value.tag
pass


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
            print("NON'", tag, next_lexem.tag)
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
        Parses a statement that represents a line
        '''

        statement_node = StatementNode()
        # statement_node.expression = self.parse_assignment()
        # self.expect('TERMINATOR')

        if self.peek().tag == 'WHILE':
            statement_node.expression.append(self.parse_while())
            statement_node.loop_counter += 1
            statement_node.loop_breaker_needed += 1
            # expect(TLDR) to break the loop
            # expect(BRB to close the loop)

        elif self.peek().tag == "FOR":
            statement_node.expression.append(self.parse_for())
            statement_node.loop_counter += 1
            statement_node.loop_breaker_needed += 1

        elif self.peek().tag in ["STFW", "ROFL", "N00B", "L33T", "HAXOR", "AFK", "LMAO", "ROFLMAO"]:
            statement_node.expression.append(self.parse_other())

        elif self.peek().tag == "IDENTIFIER":
            statement_node.expression.append( self.parse_assignment())

        elif self.peek().tag == "BRB":
            statement_node.expression.append( self.parse_brb())

        elif self.peek().tag == "STFU":
            statement_node.expression.append( self.parse_stfu())

        elif self.peek().tag == "TLDR":
            statement_node.expression.append( self.parse_stfu())

        else:
            self.error("Synthax error")

        return statement_node




    def parse_assignment(self):
        '''
        Parses an expression that looks like:
            Unary, iz, Expression}
        '''
        expression_node = AssignmentNode()
        expression_node.lhs,unary_lign = self.parse_unary()
        # print('xpression_node.lhs.value.name',expression_node.lhs.value.name)

        # To check the type of the expression, we look for a ';' after the first identifier or number
        if not self.peek().tag == 'TERMINATOR':
            # Binary operation so operator and another expression
            if self.peek().tag in ['IZ', 'TODEVNULL']:
                # - Une assignment (lol iz 4)
                # - Une remise à zéro (lol to /dev/null\)
                expression_node.operator = self.accept()
            else:
                self.error("Missing operator in expression.")

        else :
            self.accept()
            return expression_node
        expression_node.rhs = self.parse_assignment()

        return expression_node

    def parse_for(self):
        '''
        Parses an expression that looks like:
            4, Identifier, iz, Identifier | Number, 2, Identifier | Number
        '''
        for_node = ForNode()
        token = self.expect('FOR')
        token = self.expect('IDENTIFIER'); for_node.variable = token
        token = self.expect('IZ')
        #INITIAL
        if self.peek().tag in ['IDENTIFIER', 'NUMBER']:
            for_node.initial_value = self.accept()
        else:
            self.error('Expected IDENTIFIER or NUMBER, got {} instead'.format(self.peek().tag))

        token = self.expect('TWO')
        #FINAL
        if self.peek().tag in ['IDENTIFIER', 'NUMBER']:
            for_node.end_value = self.accept()
        else:
            self.error('Expected IDENTIFIER or NUMBER, got {} instead'.format(self.peek().tag))

        return for_node

    def parse_while(self):
        '''
        Parses an expression that looks like:
            rtfm
        '''
        while_node = WhileNode()
        while_node.operator = self.accept()
        return while_node

    def parse_brb(self):
        '''
        Parses an expression that looks like:
            brb
        '''
        brb_node = BrbNode()
        brb_node.loop = self.accept()
        return brb_node

    def parse_stfu(self):
        '''
        Parses an expression that looks like:
            stfu
        '''
        stfu_node = StfuNode()
        stfu_node.end = self.accept()
        return stfu_node

    def parse_other(self):
        '''
        Parses an expression that looks like:
            Operator, Identifier
        '''
        other_node = OtherNode()
        other_node.operator = self.accept()
        token = self.expect('IDENTIFIER'); other_node.variable = token
        return other_node

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
                print('voila pourquoi :', self.peek().tag)
                self.error("Unary is either identifier or number")
        else:
            print('No more peeking nbecause no more token')
        return unary_node, unary_lign

    def parse_identifier(self):
        '''
        Parses an identifier that looks like:
            l{o}l
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