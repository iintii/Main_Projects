# Generated from While.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WhileParser import WhileParser
else:
    from WhileParser import WhileParser

# This class defines a complete generic visitor for a parse tree produced by WhileParser.

class WhileVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WhileParser#Assignment.
    def visitAssignment(self, ctx:WhileParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Skip.
    def visitSkip(self, ctx:WhileParser.SkipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Compound.
    def visitCompound(self, ctx:WhileParser.CompoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#If.
    def visitIf(self, ctx:WhileParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#While.
    def visitWhile(self, ctx:WhileParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Not.
    def visitNot(self, ctx:WhileParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#ROp.
    def visitROp(self, ctx:WhileParser.ROpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Or.
    def visitOr(self, ctx:WhileParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#And.
    def visitAnd(self, ctx:WhileParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#True.
    def visitTrue(self, ctx:WhileParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#False.
    def visitFalse(self, ctx:WhileParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#BParen.
    def visitBParen(self, ctx:WhileParser.BParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#AOp.
    def visitAOp(self, ctx:WhileParser.AOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Var.
    def visitVar(self, ctx:WhileParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#Num.
    def visitNum(self, ctx:WhileParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#AParen.
    def visitAParen(self, ctx:WhileParser.AParenContext):
        return self.visitChildren(ctx)



del WhileParser