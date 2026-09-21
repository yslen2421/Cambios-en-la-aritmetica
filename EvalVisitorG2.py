from G2Parser import G2Parser
from G2Visitor import G2Visitor


class EvalVisitorG2(G2Visitor):

    # prog : e EOF
    def visitProg(self, ctx):
        return self.visit(ctx.e())

    # e : t '+' e
    def visitG2Suma(self, ctx):
        return self.visit(ctx.t()) + self.visit(ctx.e())

    # e : t '-' e
    def visitG2Resta(self, ctx):
        return self.visit(ctx.t()) - self.visit(ctx.e())

    # e : t
    def visitG2TermE(self, ctx):
        return self.visit(ctx.t())

    # t : f '*' t
    def visitG2Mult(self, ctx):
        return self.visit(ctx.f()) * self.visit(ctx.t())

    # t : f '/' t
    def visitG2Div(self, ctx):
        divisor = self.visit(ctx.t())
        if divisor == 0:
            raise ZeroDivisionError("Error: división por cero")
        return self.visit(ctx.f()) / divisor

    # t : f
    def visitG2TermT(self, ctx):
        return self.visit(ctx.f())

    # f : '(' e ')'
    def visitG2Paren(self, ctx):
        return self.visit(ctx.e())

    # f : NUM
    def visitG2Num(self, ctx):
        return float(ctx.NUM().getText())
