# Generated from While.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WhileParser import WhileParser
else:
    from WhileParser import WhileParser

# This class defines a complete listener for a parse tree produced by WhileParser.
class WhileListener(ParseTreeListener):

    # Enter a parse tree produced by WhileParser#Assignment.
    def enterAssignment(self, ctx:WhileParser.AssignmentContext):
        pass

    # Exit a parse tree produced by WhileParser#Assignment.
    def exitAssignment(self, ctx:WhileParser.AssignmentContext):
        pass


    # Enter a parse tree produced by WhileParser#Skip.
    def enterSkip(self, ctx:WhileParser.SkipContext):
        pass

    # Exit a parse tree produced by WhileParser#Skip.
    def exitSkip(self, ctx:WhileParser.SkipContext):
        pass


    # Enter a parse tree produced by WhileParser#Compound.
    def enterCompound(self, ctx:WhileParser.CompoundContext):
        pass

    # Exit a parse tree produced by WhileParser#Compound.
    def exitCompound(self, ctx:WhileParser.CompoundContext):
        pass


    # Enter a parse tree produced by WhileParser#If.
    def enterIf(self, ctx:WhileParser.IfContext):
        pass

    # Exit a parse tree produced by WhileParser#If.
    def exitIf(self, ctx:WhileParser.IfContext):
        pass


    # Enter a parse tree produced by WhileParser#While.
    def enterWhile(self, ctx:WhileParser.WhileContext):
        pass

    # Exit a parse tree produced by WhileParser#While.
    def exitWhile(self, ctx:WhileParser.WhileContext):
        pass


    # Enter a parse tree produced by WhileParser#Not.
    def enterNot(self, ctx:WhileParser.NotContext):
        pass

    # Exit a parse tree produced by WhileParser#Not.
    def exitNot(self, ctx:WhileParser.NotContext):
        pass


    # Enter a parse tree produced by WhileParser#ROp.
    def enterROp(self, ctx:WhileParser.ROpContext):
        pass

    # Exit a parse tree produced by WhileParser#ROp.
    def exitROp(self, ctx:WhileParser.ROpContext):
        pass


    # Enter a parse tree produced by WhileParser#Or.
    def enterOr(self, ctx:WhileParser.OrContext):
        pass

    # Exit a parse tree produced by WhileParser#Or.
    def exitOr(self, ctx:WhileParser.OrContext):
        pass


    # Enter a parse tree produced by WhileParser#And.
    def enterAnd(self, ctx:WhileParser.AndContext):
        pass

    # Exit a parse tree produced by WhileParser#And.
    def exitAnd(self, ctx:WhileParser.AndContext):
        pass


    # Enter a parse tree produced by WhileParser#True.
    def enterTrue(self, ctx:WhileParser.TrueContext):
        pass

    # Exit a parse tree produced by WhileParser#True.
    def exitTrue(self, ctx:WhileParser.TrueContext):
        pass


    # Enter a parse tree produced by WhileParser#False.
    def enterFalse(self, ctx:WhileParser.FalseContext):
        pass

    # Exit a parse tree produced by WhileParser#False.
    def exitFalse(self, ctx:WhileParser.FalseContext):
        pass


    # Enter a parse tree produced by WhileParser#BParen.
    def enterBParen(self, ctx:WhileParser.BParenContext):
        pass

    # Exit a parse tree produced by WhileParser#BParen.
    def exitBParen(self, ctx:WhileParser.BParenContext):
        pass


    # Enter a parse tree produced by WhileParser#AOp.
    def enterAOp(self, ctx:WhileParser.AOpContext):
        pass

    # Exit a parse tree produced by WhileParser#AOp.
    def exitAOp(self, ctx:WhileParser.AOpContext):
        pass


    # Enter a parse tree produced by WhileParser#Var.
    def enterVar(self, ctx:WhileParser.VarContext):
        pass

    # Exit a parse tree produced by WhileParser#Var.
    def exitVar(self, ctx:WhileParser.VarContext):
        pass


    # Enter a parse tree produced by WhileParser#Num.
    def enterNum(self, ctx:WhileParser.NumContext):
        pass

    # Exit a parse tree produced by WhileParser#Num.
    def exitNum(self, ctx:WhileParser.NumContext):
        pass


    # Enter a parse tree produced by WhileParser#AParen.
    def enterAParen(self, ctx:WhileParser.AParenContext):
        pass

    # Exit a parse tree produced by WhileParser#AParen.
    def exitAParen(self, ctx:WhileParser.AParenContext):
        pass



del WhileParser