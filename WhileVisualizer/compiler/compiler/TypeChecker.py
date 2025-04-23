import sys
from antlr4 import *
sys.path.append('./')
from grammar.TypeWhileLexer import TypeWhileLexer
from grammar.TypeWhileParser import TypeWhileParser
from grammar.TypeWhileVisitor import TypeWhileVisitor
import logging
from textwrap import indent, dedent

symtab = {}  # E - environment

def check(condition, message):
    if not condition:
        sys.stderr.write(f"type error: {message}\n")
        exit(1)
    else:
        # no type error
        pass

class TypeChecker(TypeWhileVisitor):
  
    # Visit a parse tree produced by TypeWhileParser#Assignment.
    def visitAssignment(self, ctx:TypeWhileParser.AssignmentContext):
        name = ctx.ID().getText()
        assigned_val = self.visit(ctx.e())
        check(name in symtab, f"undeclared variable {name}")
        check(symtab[name] == assigned_val, f"incorrectly assigned type. {name} is not {assigned_val}")


    # Visit a parse tree produced by TypeWhileParser#Skip.
    def visitSkip(self, ctx:TypeWhileParser.SkipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeWhileParser#Compound.
    def visitCompound(self, ctx:TypeWhileParser.CompoundContext):
        for stmt in ctx.s():
            self.visit(stmt)


    # Visit a parse tree produced by TypeWhileParser#If.
    def visitIf(self, ctx:TypeWhileParser.IfContext):
        etype = self.visit(ctx.e())
        check(etype == "bool", "If condition must be bool.")
        self.visit(ctx.s(0))
        self.visit(ctx.s(1))

    # Visit a parse tree produced by TypeWhileParser#While.
    def visitWhile(self, ctx:TypeWhileParser.WhileContext):
        etype = self.visit(ctx.e())
        check(etype == "bool", "If condition must be bool.")
        self.visit(ctx.s())

    # Visit a parse tree produced by TypeWhileParser#Declaration.
    def visitDeclaration(self, ctx:TypeWhileParser.DeclarationContext):
        name  = ctx.ID().getText()
        type_declaration = ctx.typeName.text

        check(type_declaration in ["int", "bool"], f"invalid type {type_declaration} for variable {name}")

        symtab[name] = type_declaration      


    # Visit a parse tree produced by TypeWhileParser#Not.
    def visitNot(self, ctx:TypeWhileParser.NotContext):
        ntype = self.visit(ctx.e())
        check(ntype == "bool", "Not operator requires bool")
        return "bool"

    # Visit a parse tree produced by TypeWhileParser#Var.
    def visitVar(self, ctx:TypeWhileParser.VarContext):
        name = ctx.ID().getText()
        check(name in symtab, f"{name} not in symtab.")
        return symtab[name]


    # Visit a parse tree produced by TypeWhileParser#Num.
    def visitNum(self, ctx:TypeWhileParser.NumContext):
        return "int"

    # Visit a parse tree produced by TypeWhileParser#True.
    def visitTrue(self, ctx:TypeWhileParser.TrueContext):
        return "bool"


    # Visit a parse tree produced by TypeWhileParser#False.
    def visitFalse(self, ctx:TypeWhileParser.FalseContext):
        return "bool"


    # Visit a parse tree produced by TypeWhileParser#BinOp.
    def visitBinOp(self, ctx:TypeWhileParser.BinOpContext):
        left_type = self.visit(ctx.e(0))
        right_type = self.visit(ctx.e(1))

        op = ctx.op.text
        if op in ['+', '-', '*', '/']:
            check(left_type == "int" and right_type == "int", f"int operands are needed for {op}")
            return  "int"
        elif op in ['<', '<=', '=', '>', '>=']:
            check (left_type == "int" and right_type == "int", f"int operands are needed for {op}")
            return "bool"
        elif op in ["and", "or"]:
            check(left_type == "bool" and right_type == "bool", f"Bool operands are needed for {op}")
            return "bool"
        else:
            check(False, "Unknown operator.")       


    # Visit a parse tree produced by TypeWhileParser#Paren.
    def visitParen(self, ctx:TypeWhileParser.ParenContext):
        return self.visitChildren(ctx)

input_stream = StdinStream()
lexer = TypeWhileLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = TypeWhileParser(stream)
tree = parser.s()
if parser.getNumberOfSyntaxErrors() > 0:
  print("syntax errors")
  exit(1)
typechecker = TypeChecker()
typechecker.visit(tree)
print("\n".join([ f"symtab[{name}]: {symtab[name]}" for name in symtab ]))
