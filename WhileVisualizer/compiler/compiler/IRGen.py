import os
import sys

sys.path.append('./')

from antlr4 import *
from grammar.WhileLexer import WhileLexer
from grammar.WhileParser import WhileParser
from grammar.WhileVisitor import WhileVisitor


import logging
from textwrap import indent, dedent




class IRGen(WhileVisitor):
    def __init__(self, outfile):
        self.outfile = outfile
        self.labelnum = 0
        self.varnum = 0

    def freshlabel(self):
        self.labelnum += 1
        return f"_l{self.labelnum}"

    def freshvar(self):
        self.varnum += 1
        return f"_t{self.varnum}"

    def visitAssignment(self, ctx:WhileParser.AssignmentContext):
        tempname = self.visit(ctx.a())
        varname = ctx.ID().getText()
        # Ensure each instruction is on its own line
        self.outfile.write(f"{varname} := {tempname}\n")
        return None

    def visitSkip(self, ctx:WhileParser.SkipContext):
        return None

    def visitCompound(self, ctx:WhileParser.CompoundContext):
        self.visitChildren(ctx)
        return None

    def visitIf(self, ctx:WhileParser.IfContext):
        elseLabel = self.freshlabel()
        endLabel = self.freshlabel()
        condTemp = self.visit(ctx.b())
        # Emit each instruction with a newline and proper spacing
        self.outfile.write(f"if {condTemp} = 0 goto {elseLabel}\n")
        self.visit(ctx.s(0))
        self.outfile.write(f"goto {endLabel}\n")
        self.outfile.write(f"{elseLabel}:\n")
        self.visit(ctx.s(1))
        self.outfile.write(f"{endLabel}:\n")
        return None

    def visitWhile(self, ctx:WhileParser.WhileContext):
        headLabel = self.freshlabel()
        endLabel = self.freshlabel()
        self.outfile.write(f"{headLabel}:\n")
        condTemp = self.visit(ctx.b())
        self.outfile.write(f"if {condTemp} = 0 goto {endLabel}\n")
        self.visit(ctx.s())
        self.outfile.write(f"goto {headLabel}\n")
        self.outfile.write(f"{endLabel}:\n")
        return None

    def visitTrue(self, ctx:WhileParser.TrueContext):
        temp = self.freshvar()
        self.outfile.write(f"{temp} := 1\n")
        return temp

    def visitFalse(self, ctx:WhileParser.FalseContext):
        temp = self.freshvar()
        self.outfile.write(f"{temp} := 0\n")
        return temp

    def visitNot(self, ctx:WhileParser.NotContext):
        inTemp = self.visit(ctx.b())
        resultTemp = self.freshvar()
        labelTrue = self.freshlabel()
        labelEnd = self.freshlabel()
        self.outfile.write(
            f"if {inTemp} = 0 goto {labelTrue}\n"
            f"{resultTemp} := 0\n"
            f"goto {labelEnd}\n"
            f"{labelTrue}:\n"
            f"{resultTemp} := 1\n"
            f"{labelEnd}:\n"
        )
        return resultTemp

    def visitAnd(self, ctx:WhileParser.AndContext):
        leftTemp = self.visit(ctx.b(0))
        rightTemp = self.visit(ctx.b(1))
        resultTemp = self.freshvar()
        labelFalse = self.freshlabel()
        labelEnd = self.freshlabel()
        self.outfile.write(
            f"if {leftTemp} = 0 goto {labelFalse}\n"
            f"if {rightTemp} = 0 goto {labelFalse}\n"
            f"{resultTemp} := 1\n"
            f"goto {labelEnd}\n"
            f"{labelFalse}:\n"
            f"{resultTemp} := 0\n"
            f"{labelEnd}:\n"
        )
        return resultTemp

    def visitOr(self, ctx:WhileParser.OrContext):
        leftTemp = self.visit(ctx.b(0))
        rightTemp = self.visit(ctx.b(1))
        resultTemp = self.freshvar()
        labelTrue = self.freshlabel()
        labelEnd = self.freshlabel()
        self.outfile.write(
            f"if {leftTemp} = 1 goto {labelTrue}\n"
            f"if {rightTemp} = 1 goto {labelTrue}\n"
            f"{resultTemp} := 0\n"
            f"goto {labelEnd}\n"
            f"{labelTrue}:\n"
            f"{resultTemp} := 1\n"
            f"{labelEnd}:\n"
        )
        return resultTemp

    def visitROp(self, ctx:WhileParser.ROpContext):
        leftTemp = self.visit(ctx.a(0))
        rightTemp = self.visit(ctx.a(1))
        resultTemp = self.freshvar()
        labelTrue = self.freshlabel()
        labelEnd = self.freshlabel()
        op = ctx.ROP().getText()  # Changed from ctx.op.text to ctx.ROP().getText()
        self.outfile.write(
            f"if {leftTemp} {op} {rightTemp} goto {labelTrue}\n"
            f"{resultTemp} := 0\n"
            f"goto {labelEnd}\n"
            f"{labelTrue}:\n"
            f"{resultTemp} := 1\n"
            f"{labelEnd}:\n"
        )
        return resultTemp

    def visitAOp(self, ctx:WhileParser.AOpContext):
        leftTemp = self.visit(ctx.a(0))
        rightTemp = self.visit(ctx.a(1))
        resultTemp = self.freshvar()
        op = ctx.AOP().getText()  # Changed from ctx.op.text to ctx.AOP().getText()
        self.outfile.write(
            f"{resultTemp} := {leftTemp} {op} {rightTemp}\n"
        )
        return resultTemp

    def visitVar(self, ctx:WhileParser.VarContext):
        resultTemp = self.freshvar()
        varname = ctx.ID().getText()
        self.outfile.write(
            f"{resultTemp} := {varname}\n"
        )
        return resultTemp

    def visitNum(self, ctx:WhileParser.NumContext):
        resultTemp = self.freshvar()
        num = ctx.NUM().getText()
        self.outfile.write(
            f"{resultTemp} := {num}\n"
        )
        return resultTemp

    def visitAParen(self, ctx:WhileParser.AParenContext):
        return self.visit(ctx.a())

    def visitBParen(self, ctx:WhileParser.BParenContext):
        return self.visit(ctx.b())

def irgen(input_stream, output_stream):
    lexer = WhileLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = WhileParser(stream)
    tree = parser.s()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
        exit(1)
    else:
        output_stream.write("function main\n")
        # TODO need to collect the local vars, e.g., in the type checker or just run through them first?
        translator = IRGen(output_stream)
        translator.visit(tree)
        output_stream.write("return 0\n")
        output_stream.write("end function\n")
      
def main():
    import sys
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = StdinStream()
    irgen(input_stream, sys.stdout)

if __name__ == '__main__':
    main()


