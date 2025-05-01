from grammar.WhileParser import WhileParser
from grammar.WhileVisitor import WhileVisitor

class CGen(WhileVisitor):
    def __init__(self):
        self.indent = 0
        self.lines = []

    def ind(self):
        return "    " * self.indent

    def emit(self, tree):
        # Preamble
        self.lines.append("#include <stdio.h>")
        self.lines.append("int main() {")
        self.indent += 1
        # Visit the “begin … end” (your top‐level) node
        self.visit(tree)
        # return
        self.lines.append(self.ind() + "return 0;")
        self.indent -= 1
        self.lines.append("}")
        return "\n".join(self.lines)

    # Compound (begin … end)
    def visitCompound(self, ctx:WhileParser.CompoundContext):
        # children are a sequence of statements
        # ctx.s(0), ctx.s(1), ... represent the statements inside begin/end
        for stmt in ctx.s():
            self.visit(stmt)

    # Assignment: ID := a ;
    def visitAssignment(self, ctx:WhileParser.AssignmentContext):
        var = ctx.ID().getText()
        expr = self.visit(ctx.a())
        self.lines.append(self.ind() + f"{var} = {expr};")

    # Arithmetic expression
    def visitAOp(self, ctx:WhileParser.AOpContext):
        left = self.visit(ctx.a(0))
        right = self.visit(ctx.a(1))
        op = ctx.AOP().getText()
        return f"({left} {op} {right})"

    def visitNum(self, ctx:WhileParser.NumContext):
        return ctx.NUM().getText()

    def visitVar(self, ctx:WhileParser.VarContext):
        return ctx.ID().getText()

    # If‐then‐else
    def visitIf(self, ctx:WhileParser.IfContext):
        cond = self.visit(ctx.b())
        self.lines.append(self.ind() + f"if ({cond}) {{")
        self.indent += 1
        self.visit(ctx.s(0))
        self.indent -= 1
        self.lines.append(self.ind() + "} else {")
        self.indent += 1
        self.visit(ctx.s(1))
        self.indent -= 1
        self.lines.append(self.ind() + "}")

    # Boolean ROp
    def visitROp(self, ctx:WhileParser.ROpContext):
        l = self.visit(ctx.a(0))
        r = self.visit(ctx.a(1))
        op = ctx.ROP().getText()
        return f"{l} {op} {r}"

    # while b do s
    def visitWhile(self, ctx:WhileParser.WhileContext):
        cond = self.visit(ctx.b())
        self.lines.append(self.ind() + f"while ({cond}) {{")
        self.indent += 1
        self.visit(ctx.s())
        self.indent -= 1
        self.lines.append(self.ind() + "}")

# In gui.py, replace emit_c to use CGen:
from CEmitter.CGen import CGen

def emit_c():
    input_text = code_input.get("1.0", tk.END)
    # Parse to AST
    in_stream = InputStream(input_text)
    lexer = WhileLexer(in_stream)
    stream = CommonTokenStream(lexer)
    parser = WhileParser(stream)
    tree = parser.s()   # or the correct start rule
    # Generate C
    cgen = CGen()
    c_code = cgen.emit(tree)
    output_text.configure(state='normal')
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, c_code)
    output_text.configure(state='disabled')