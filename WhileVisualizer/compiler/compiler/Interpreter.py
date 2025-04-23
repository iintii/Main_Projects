import sys
from antlr4 import *
sys.path.append('./')
from grammar.WhileLexer import WhileLexer
from grammar.WhileParser import WhileParser
from grammar.WhileVisitor import WhileVisitor
import logging
from textwrap import indent, dedent

# Simple helper for debug prints
def debug(msg):
    print(msg)

class Interpreter(WhileVisitor):
    def __init__(self):
        self.symtab = {}
        #debug("Interpreter now empty symbol table.")

    # Visit a parse tree produced by WhileParser#Assignment.
    def visitAssignment(self, ctx:WhileParser.AssignmentContext):
        var_name = ctx.ID().getText()
        #debug(f"visitAssignment: Current_variable '{var_name}'.")
        value = self.visit(ctx.a())
        self.symtab[var_name] = value
        #debug(f"visitAssignment: {value} to variable '{var_name}'.")
        
        return value

    def visitSkip(self, ctx:WhileParser.SkipContext):
        
        return self.visitChildren(ctx)

    # Visit a parse tree produced by WhileParser#If.
    def visitIf(self, ctx:WhileParser.IfContext):
        #debug("visitIf: if stmt")
        cond = self.visit(ctx.b())
        #debug(f"visitIf: Condition is {cond}.")
        if cond:
            #debug("visitIf: Executing then-branch.")
            self.visit(ctx.s(0))
        else:
            #debug("visitIf: Executing else-branch.")
            self.visit(ctx.s(1))

    # Visit a parse tree produced by WhileParser#While.
    def visitWhile(self, ctx:WhileParser.WhileContext):
        while self.visit(ctx.b()):
            
            self.visit(ctx.s())
            
            

    # Visit a parse tree produced by WhileParser#Compound.
    def visitCompound(self, ctx:WhileParser.CompoundContext):
        
        for i, statement in enumerate(ctx.s()):
            
            self.visit(statement)

    # Visit a parse tree produced by WhileParser#Not.
    def visitNot(self, ctx:WhileParser.NotContext):
        
        result = not self.visit(ctx.b())
        
        return result

    # Visit a parse tree produced by WhileParser#ROp.
    def visitROp(self, ctx:WhileParser.ROpContext):
        #debug("visitROp: is relational operator")
        left = self.visit(ctx.a(0))
        right = self.visit(ctx.a(1))
        operation = ctx.op.type
        #debug(f"visitROp: Left = {left} Right = {right} Operator Type = {operation}")
        if operation == WhileParser.EQ:
            result = left == right
        elif operation == WhileParser.LT:
            result = left < right
        elif operation == WhileParser.LE:
            result = left <= right
        elif operation == WhileParser.GT:
            result = left > right
        elif operation == WhileParser.GE:
            result = left >= right
        else:
            raise ValueError("Unknown op")
        #debug(f"visitROp: result is {result}")
        return result
        
    # Visit a parse tree produced by WhileParser#Or.
    def visitOr(self, ctx:WhileParser.OrContext):
        #debug("visitOr: is or operator")
        left = self.visit(ctx.b(0))
        right = self.visit(ctx.b(1))
        result = left or right
        #debug(f"visitOr: Left = {left} Right = {right} Result = {result}")
        return result

    # Visit a parse tree produced by WhileParser#And.
    def visitAnd(self, ctx:WhileParser.AndContext):
        
        left = self.visit(ctx.b(0))
        right = self.visit(ctx.b(1))
        result = left and right
        
        return result

    # Visit a parse tree produced by WhileParser#True.
    def visitTrue(self, ctx:WhileParser.TrueContext):
        #debug("visitTrue: true encountered.")
        return True

    # Visit a parse tree produced by WhileParser#False.
    def visitFalse(self, ctx:WhileParser.FalseContext):
        #debug("visitFalse: false encountered.")
        return False

    # Visit a parse tree produced by WhileParser#BParen.
    def visitBParen(self, ctx:WhileParser.BParenContext):
        
        result = self.visit(ctx.b())
        
        return result

    # Visit a parse tree produced by WhileParser#AOp.
    def visitAOp(self, ctx:WhileParser.AOpContext):
        #debug("visitAOp: is arithmetic.")
        left = self.visit(ctx.a(0))
        right = self.visit(ctx.a(1))
        operation = ctx.op.type
        #debug(f"visitAOp: Left = {left} Right = {right} Operator Type = {operation}")
        if operation == WhileParser.PLUS:
            result = left + right
        elif operation == WhileParser.MINUS:
            result = left - right
        elif operation == WhileParser.MULT:
            result = left * right
        elif operation == WhileParser.DIV:
            result = left // right
        else:
            raise ValueError("Unknown operator in visitAOp.")
        #debug(f"visitAOp: Result is {result}.")
        return result

    # Visit a parse tree produced by WhileParser#Var.
    def visitVar(self, ctx:WhileParser.VarContext):
        var_name = ctx.ID().getText()
        #debug(f"visitVar: accessing variable '{var_name}'")
        value = self.symtab.get(var_name, 0)
        #debug(f"visitVar: returning value {value} for variable '{var_name}'")
        return value

    # Visit a parse tree produced by WhileParser#Num.
    def visitNum(self, ctx:WhileParser.NumContext):
        num_text = ctx.NUM().getText()
        #debug(f"visitNum: found number literal '{num_text}'")
        result = int(num_text)
        #debug(f"visitNum: converted '{num_text}' to {result}")
        return result

    # Visit a parse tree produced by WhileParser#AParen.
    def visitAParen(self, ctx:WhileParser.AParenContext):
        
        result = self.visit(ctx.a())
        
        return result

# Main entry point
debug("Main entry point starting.")
input_stream = StdinStream()
lexer = WhileLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = WhileParser(stream)
tree = parser.s()
debug("Parse tree generated.")

if parser.getNumberOfSyntaxErrors() > 0:
    print("syntax errors")
    exit(1)

interpreter = Interpreter()
debug("Interpreter created, starting to visit the parse tree.")
interpreter.visit(tree)
debug("Finished visiting the parse tree.")

# Print the final symbol table from the interpreter instance
print("\n".join([ f"symtab[{name}]: {interpreter.symtab[name]}" for name in interpreter.symtab ]))
