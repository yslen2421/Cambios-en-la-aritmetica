from G4Parser import G4Parser
from G4Visitor import G4Visitor


class EvalVisitorG4(G4Visitor):

    # prog : suma EOF
    def visitProg(self, ctx):
        return self.visit(ctx.suma())

    # suma : suma '+' resta
    def visitG4Suma(self, ctx):
        return self.visit(ctx.suma()) + self.visit(ctx.resta())

    # suma : resta
    def visitG4PasaResta(self, ctx):
        return self.visit(ctx.resta())

    # resta : resta '-' mult
    def visitG4Resta(self, ctx):
        return self.visit(ctx.resta()) - self.visit(ctx.mult())

    # resta : mult
    def visitG4PasaMult(self, ctx):
        return self.visit(ctx.mult())

    # mult : mult '*' div
    def visitG4Mult(self, ctx):
        return self.visit(ctx.mult()) * self.visit(ctx.div())

    # mult : div
    def visitG4PasaDiv(self, ctx):
        return self.visit(ctx.div())

    # div : div '/' factor
    def visitG4Div(self, ctx):
        divisor = self.visit(ctx.factor())
        if divisor == 0:
            raise ZeroDivisionError("Error: división por cero")
        return self.visit(ctx.div()) / divisor

    # div : factor
    def visitG4PasaFactor(self, ctx):
        return self.visit(ctx.factor())

    # factor : '(' suma ')'
    def visitG4Paren(self, ctx):
        return self.visit(ctx.suma())

    # factor : NUM
    def visitG4Num(self, ctx):
        return float(ctx.NUM().getText())
