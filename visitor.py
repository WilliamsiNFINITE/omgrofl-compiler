from parsero import *


class Visitor:
    def visit(self,program):
        program.accept(self)
        return program
    def visit_program_node(self,program_node):
        for statement in program_node.statements:
            statement.accept(self)

    def visit_statement_node(self,statement_node):
        statement_node.expression.accept(self)
        #statement_node.loop_counter.accept(self)
        #statement_node.loop_breaker_needed.accept(self)

    def visit_assignement_node(self,assignement_node):
        assignement_node.operator.accept(self)
        assignement_node.lhs.accept(self)
        assignement_node.rhs.accept(self)

    #TODO pour faire un rhs/lhs.visit et accept, je sais pas ce que c'est ^^'

    def visit_rtfm_node(self,rtfm_node):
        rtfm_node.operator.accept(self)

    def visit_stfu_node(self,stfu_node):
        stfu_node.end.accept(self)

    def visit_tdlr_node(self,tdlr_node):
        tdlr_node.breaker.accept(self)

    def visit_brb_node(self,brb_node):
        brb_node.loop.accept(self)

    def visit_for_node(self,for_node):
        for_node.variable.accept(self)
        for_node.initial_value.accept(self)

    def visit_wtf_node(self,wtf_node):
        wtf_node.variable1.accept(self)
        wtf_node.operator.accept(self)
        wtf_node.variable2.accept(self)

    def visit_number_node(self,number_node):
        number_node.tag.accept(self)
        number_node.value.accept(self)