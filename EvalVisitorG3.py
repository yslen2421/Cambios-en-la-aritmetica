from G3Parser import G3Parser
from G3Visitor import G3Visitor


class EvalVisitorG3(G3Visitor):

    # prog : e EOF
    def visitProg(self, ctx):
        return self.visit(ctx.e())

    # e : e '*' t
    def visitG3Mult(self, ctx):
        return self.visit(ctx.e()) * self.visit(ctx.t())

    # e : e '/' t
    def visitG3Div(self, ctx):
        divisor = self.visit(ctx.t())
        if divisor == 0:
            raise ZeroDivisionError("Error: división por cero")
        return self.visit(ctx.e()) / divisor

    # e : t
    def visitG3TermE(self, ctx):
        return self.visit(ctx.t())

    # t : t '+' f
    def visitG3Suma(self, ctx):
        return self.visit(ctx.t()) + self.visit(ctx.f())

    # t : t '-' f
    def visitG3Resta(self, ctx):
        return self.visit(ctx.t()) - self.visit(ctx.f())

    # t : f
    def visitG3TermT(self, ctx):
        return self.visit(ctx.f())

    # f : '(' e ')'
    def visitG3Paren(self, ctx):
        return self.visit(ctx.e())

    # f : NUM
    def visitG3Num(self, ctx):
        return float(ctx.NUM().getText())

