from G1Parser import G1Parser
from G1Visitor import G1Visitor


class EvalVisitor(G1Visitor):

    # prog : e EOF
    def visitProg(self, ctx):
        return self.visit(ctx.e())

    # e : e '+' t
    def visitG1Suma(self, ctx):
        return self.visit(ctx.e()) + self.visit(ctx.t())

    # e : e '-' t
    def visitG1Resta(self, ctx):
        return self.visit(ctx.e()) - self.visit(ctx.t())

    # e : t
    def visitG1TermE(self, ctx):
        return self.visit(ctx.t())

    # t : t '*' f
    def visitG1Mult(self, ctx):
        return self.visit(ctx.t()) * self.visit(ctx.f())

    # t : t '/' f
    def visitG1Div(self, ctx):
        divisor = self.visit(ctx.f())
        if divisor == 0:
            raise ZeroDivisionError("Error: división por cero")
        return self.visit(ctx.t()) / divisor

    # t : f
    def visitG1TermT(self, ctx):
        return self.visit(ctx.f())

    # f : '(' e ')'
    def visitG1Paren(self, ctx):
        return self.visit(ctx.e())

    # f : NUM
    def visitG1Num(self, ctx):
        return float(ctx.NUM().getText())

