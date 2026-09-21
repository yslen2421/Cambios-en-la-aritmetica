# Generated from G1.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .G1Parser import G1Parser
else:
    from G1Parser import G1Parser

# This class defines a complete generic visitor for a parse tree produced by G1Parser.

class G1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by G1Parser#prog.
    def visitProg(self, ctx:G1Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G1Parser#G1Suma.
    def visitG1Suma(self, ctx:G1Parser.G1SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G1Parser#G1TermE.
    def visitG1TermE(self, ctx:G1Parser.G1TermEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G1Parser#G1Resta.
    def visitG1Resta(self, ctx:G1Parser.G1RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G1Parser#G1Mult.
    def visitG1Mult(self, ctx:G1Parser.G1MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G1Parser#G1Div.
    def visitG1Div(self, ctx:G1Parser.G1DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G1Parser#G1TermT.
    def visitG1TermT(self, ctx:G1Parser.G1TermTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G1Parser#G1Paren.
    def visitG1Paren(self, ctx:G1Parser.G1ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G1Parser#G1Num.
    def visitG1Num(self, ctx:G1Parser.G1NumContext):
        return self.visitChildren(ctx)



del G1Parser