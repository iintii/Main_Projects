import sys
from antlr4 import *
from grammar.WhileLexer import WhileLexer
from grammar.WhileParser import WhileParser
from grammar.WhileVisitor import WhileVisitor
import logging
from textwrap import indent, dedent

input_stream = StdinStream()
lexer = WhileLexer(input_stream)
stream = CommonTokenStream(lexer)
while True:
    token = stream.LT(1)
    if token.type == Token.EOF:
        break
    print(token.text)
    stream.consume()
