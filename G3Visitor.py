# Generated from G3.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .G3Parser import G3Parser
else:
    from G3Parser import G3Parser

# This class defines a complete generic visitor for a parse tree produced by G3Parser.

class G3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by G3Parser#prog.
    def visitProg(self, ctx:G3Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G3Parser#G3Div.
    def visitG3Div(self, ctx:G3Parser.G3DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G3Parser#G3Mult.
    def visitG3Mult(self, ctx:G3Parser.G3MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G3Parser#G3TermE.
    def visitG3TermE(self, ctx:G3Parser.G3TermEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G3Parser#G3Resta.
    def visitG3Resta(self, ctx:G3Parser.G3RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G3Parser#G3TermT.
    def visitG3TermT(self, ctx:G3Parser.G3TermTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G3Parser#G3Suma.
    def visitG3Suma(self, ctx:G3Parser.G3SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G3Parser#G3Paren.
    def visitG3Paren(self, ctx:G3Parser.G3ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by G3Parser#G3Num.
    def visitG3Num(self, ctx:G3Parser.G3NumContext):
        return self.visitChildren(ctx)



del G3Parser