# Generated from TypeWhile.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TypeWhileParser import TypeWhileParser
else:
    from TypeWhileParser import TypeWhileParser

# This class defines a complete generic visitor for a parse tree produced by TypeWhileParser.

class TypeWhileVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TypeWhileParser#Assignment.
    def visitAssignment(self, ctx:TypeWhileParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeWhileParser#Skip.
    def visitSkip(self, ctx:TypeWhileParser.SkipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeWhileParser#Compound.
    def visitCompound(self, ctx:TypeWhileParser.CompoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeWhileParser#If.
    def visitIf(self, ctx:TypeWhileParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeWhileParser#While.
    def visitWhile(self, ctx:TypeWhileParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeWhileParser#Declaration.
    def visitDeclaration(self, ctx:TypeWhileParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeWhileParser#Not.
    def visitNot(self, ctx:TypeWhileParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeWhileParser#Var.
    def visitVar(self, ctx:TypeWhileParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeWhileParser#Num.
    def visitNum(self, ctx:TypeWhileParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeWhileParser#True.
    def visitTrue(self, ctx:TypeWhileParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeWhileParser#False.
    def visitFalse(self, ctx:TypeWhileParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeWhileParser#BinOp.
    def visitBinOp(self, ctx:TypeWhileParser.BinOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeWhileParser#Paren.
    def visitParen(self, ctx:TypeWhileParser.ParenContext):
        return self.visitChildren(ctx)



del TypeWhileParser