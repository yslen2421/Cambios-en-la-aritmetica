# Generated from G4.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .G4Parser import G4Parser
else:
    from G4Parser import G4Parser

# This class defines a complete generic visitor for a parse tree produced by G4Parser.

class G4Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by G4Parser#prog.
    def visitProg(self, ctx:G4Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4Parser#G4PasaResta.
    def visitG4PasaResta(self, ctx:G4Parser.G4PasaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4Parser#G4Suma.
    def visitG4Suma(self, ctx:G4Parser.G4SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4Parser#G4PasaMult.
    def visitG4PasaMult(self, ctx:G4Parser.G4PasaMultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4Parser#G4Resta.
    def visitG4Resta(self, ctx:G4Parser.G4RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4Parser#G4Mult.
    def visitG4Mult(self, ctx:G4Parser.G4MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4Parser#G4PasaDiv.
    def visitG4PasaDiv(self, ctx:G4Parser.G4PasaDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4Parser#G4Div.
    def visitG4Div(self, ctx:G4Parser.G4DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4Parser#G4PasaFactor.
    def visitG4PasaFactor(self, ctx:G4Parser.G4PasaFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4Parser#G4Paren.
    def visitG4Paren(self, ctx:G4Parser.G4ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G4Parser#G4Num.
    def visitG4Num(self, ctx:G4Parser.G4NumContext):
        return self.visitChildren(ctx)



del G4Parser