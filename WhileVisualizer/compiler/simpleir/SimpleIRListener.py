# Generated from SimpleIR.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleIRParser import SimpleIRParser
else:
    from SimpleIRParser import SimpleIRParser

# This class defines a complete listener for a parse tree produced by SimpleIRParser.
class SimpleIRListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleIRParser#unit.
    def enterUnit(self, ctx:SimpleIRParser.UnitContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#unit.
    def exitUnit(self, ctx:SimpleIRParser.UnitContext):
        pass


    # Enter a parse tree produced by SimpleIRParser#function.
    def enterFunction(self, ctx:SimpleIRParser.FunctionContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#function.
    def exitFunction(self, ctx:SimpleIRParser.FunctionContext):
        pass


    # Enter a parse tree produced by SimpleIRParser#statementList.
    def enterStatementList(self, ctx:SimpleIRParser.StatementListContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#statementList.
    def exitStatementList(self, ctx:SimpleIRParser.StatementListContext):
        pass


    # Enter a parse tree produced by SimpleIRParser#localVariables.
    def enterLocalVariables(self, ctx:SimpleIRParser.LocalVariablesContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#localVariables.
    def exitLocalVariables(self, ctx:SimpleIRParser.LocalVariablesContext):
        pass


    # Enter a parse tree produced by SimpleIRParser#parameters.
    def enterParameters(self, ctx:SimpleIRParser.ParametersContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#parameters.
    def exitParameters(self, ctx:SimpleIRParser.ParametersContext):
        pass


    # Enter a parse tree produced by SimpleIRParser#returnStatement.
    def enterReturnStatement(self, ctx:SimpleIRParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#returnStatement.
    def exitReturnStatement(self, ctx:SimpleIRParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by SimpleIRParser#end.
    def enterEnd(self, ctx:SimpleIRParser.EndContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#end.
    def exitEnd(self, ctx:SimpleIRParser.EndContext):
        pass


    # Enter a parse tree produced by SimpleIRParser#statement.
    def enterStatement(self, ctx:SimpleIRParser.StatementContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#statement.
    def exitStatement(self, ctx:SimpleIRParser.StatementContext):
        pass


    # Enter a parse tree produced by SimpleIRParser#operation.
    def enterOperation(self, ctx:SimpleIRParser.OperationContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#operation.
    def exitOperation(self, ctx:SimpleIRParser.OperationContext):
        pass


    # Enter a parse tree produced by SimpleIRParser#assign.
    def enterAssign(self, ctx:SimpleIRParser.AssignContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#assign.
    def exitAssign(self, ctx:SimpleIRParser.AssignContext):
        pass


    # Enter a parse tree produced by SimpleIRParser#dereference.
    def enterDereference(self, ctx:SimpleIRParser.DereferenceContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#dereference.
    def exitDereference(self, ctx:SimpleIRParser.DereferenceContext):
        pass


    # Enter a parse tree produced by SimpleIRParser#reference.
    def enterReference(self, ctx:SimpleIRParser.ReferenceContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#reference.
    def exitReference(self, ctx:SimpleIRParser.ReferenceContext):
        pass


    # Enter a parse tree produced by SimpleIRParser#assignDereference.
    def enterAssignDereference(self, ctx:SimpleIRParser.AssignDereferenceContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#assignDereference.
    def exitAssignDereference(self, ctx:SimpleIRParser.AssignDereferenceContext):
        pass


    # Enter a parse tree produced by SimpleIRParser#call.
    def enterCall(self, ctx:SimpleIRParser.CallContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#call.
    def exitCall(self, ctx:SimpleIRParser.CallContext):
        pass


    # Enter a parse tree produced by SimpleIRParser#label.
    def enterLabel(self, ctx:SimpleIRParser.LabelContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#label.
    def exitLabel(self, ctx:SimpleIRParser.LabelContext):
        pass


    # Enter a parse tree produced by SimpleIRParser#gotoStatement.
    def enterGotoStatement(self, ctx:SimpleIRParser.GotoStatementContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#gotoStatement.
    def exitGotoStatement(self, ctx:SimpleIRParser.GotoStatementContext):
        pass


    # Enter a parse tree produced by SimpleIRParser#ifGoto.
    def enterIfGoto(self, ctx:SimpleIRParser.IfGotoContext):
        pass

    # Exit a parse tree produced by SimpleIRParser#ifGoto.
    def exitIfGoto(self, ctx:SimpleIRParser.IfGotoContext):
        pass



del SimpleIRParser