from grammar.WhileParser import WhileParser
from grammar.WhileVisitor import WhileVisitor

class PythonGen(WhileVisitor):
    def __init__(self):
        self.indent = 0
        self.lines = []

    def ind(self):
        return '    ' * self.indent

    def emit(self, tree):
        # Generate Python function
        self.lines.append('def main():')
        self.indent += 1
        # Visit the top-level statement (begin...end)
        self.visit(tree)
        # Add return 0 at end
        self.lines.append(self.ind() + 'return 0')
        return '\n'.join(self.lines)

    def visitCompound(self, ctx:WhileParser.CompoundContext):
        # Compound block: begin s; ... end
        for stmt in ctx.s():
            self.visit(stmt)

    def visitAssignment(self, ctx:WhileParser.AssignmentContext):
        var = ctx.ID().getText()
        expr = self.visit(ctx.a())
        self.lines.append(self.ind() + f"{var} = {expr}")

    def visitSkip(self, ctx:WhileParser.SkipContext):
        self.lines.append(self.ind() + 'pass')

    def visitAOp(self, ctx:WhileParser.AOpContext):
        left = self.visit(ctx.a(0))
        right = self.visit(ctx.a(1))
        op = ctx.AOP().getText()
        return f"({left} {op} {right})"

    def visitVar(self, ctx:WhileParser.VarContext):
        return ctx.ID().getText()

    def visitNum(self, ctx:WhileParser.NumContext):
        return ctx.NUM().getText()

    def visitIf(self, ctx:WhileParser.IfContext):
        cond = self.visit(ctx.b())
        self.lines.append(self.ind() + f"if {cond}:")
        self.indent += 1
        self.visit(ctx.s(0))
        self.indent -= 1
        self.lines.append(self.ind() + 'else:')
        self.indent += 1
        self.visit(ctx.s(1))
        self.indent -= 1

    def visitROp(self, ctx:WhileParser.ROpContext):
        left = self.visit(ctx.a(0))
        right = self.visit(ctx.a(1))
        op = ctx.ROP().getText()
        return f"{left} {op} {right}"

    def visitWhile(self, ctx:WhileParser.WhileContext):
        cond = self.visit(ctx.b())
        self.lines.append(self.ind() + f"while {cond}:")
        self.indent += 1
        self.visit(ctx.s())
        self.indent -= 1

    # Boolean literal true
    def visitTrue(self, ctx:WhileParser.TrueContext):
        return 'True'

    # Boolean literal false
    def visitFalse(self, ctx:WhileParser.FalseContext):
        return 'False'

    # Parenthesized arithmetic expression
    def visitAParen(self, ctx:WhileParser.AParenContext):
        return f"({self.visit(ctx.a())})"

    # Parenthesized boolean expression
    def visitBParen(self, ctx:WhileParser.BParenContext):
        return f"({self.visit(ctx.b())})"

    # Negation
    def visitNot(self, ctx:WhileParser.NotContext):
        expr = self.visit(ctx.b())
        return f"not {expr}"

    # Conjunction
    def visitAnd(self, ctx:WhileParser.AndContext):
        left = self.visit(ctx.b(0))
        right = self.visit(ctx.b(1))
        return f"{left} and {right}"

    # Disjunction
    def visitOr(self, ctx:WhileParser.OrContext):
        left = self.visit(ctx.b(0))
        right = self.visit(ctx.b(1))
        return f"{left} or {right}"
