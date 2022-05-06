from unittest import TestCase
from parsero import *

class TestParser(TestCase):
    def test_error(self):
        parser = Parser()
        position = ''
        error_message = "ERROR at [11, 28]: Synthax error"
        self.assertEqual(parser.error("Synthax error"))

    def test_peek(self):
        self.fail()

    def test_expect(self):
        self.fail()

    def test_accept(self):
        self.fail()

    def test_remove_comments(self):
        self.fail()

    def test_parse(self):
        self.fail()

    def test_parse_program(self):
        self.fail()

    def test_parse_statement(self):
        self.fail()

    def test_parse_assignment(self):
        self.fail()

    def test_parse_for(self):
        self.fail()

    def test_parse_wtf(self):
        self.fail()

    def test_parse_rtfm(self):
        self.fail()

    def test_parse_brb(self):
        self.fail()

    def test_parse_stfu(self):
        self.fail()

    def test_parse_tldr(self):
        self.fail()

    def test_parse_other(self):
        self.fail()

    def test_parse_unary(self):
        self.fail()

    def test_parse_identifier(self):
        self.fail()

    def test_parse_number(self):
        self.fail()
