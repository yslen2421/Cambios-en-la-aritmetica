# Generated from G2.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .G2Parser import G2Parser
else:
    from G2Parser import G2Parser

# This class defines a complete generic visitor for a parse tree produced by G2Parser.

class G2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by G2Parser#prog.
    def visitProg(self, ctx:G2Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G2Parser#G2Suma.
    def visitG2Suma(self, ctx:G2Parser.G2SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G2Parser#G2Resta.
    def visitG2Resta(self, ctx:G2Parser.G2RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G2Parser#G2TermE.
    def visitG2TermE(self, ctx:G2Parser.G2TermEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G2Parser#G2Mult.
    def visitG2Mult(self, ctx:G2Parser.G2MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G2Parser#G2Div.
    def visitG2Div(self, ctx:G2Parser.G2DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G2Parser#G2TermT.
    def visitG2TermT(self, ctx:G2Parser.G2TermTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G2Parser#G2Paren.
    def visitG2Paren(self, ctx:G2Parser.G2ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G2Parser#G2Num.
    def visitG2Num(self, ctx:G2Parser.G2NumContext):
        return self.visitChildren(ctx)



del G2Parser