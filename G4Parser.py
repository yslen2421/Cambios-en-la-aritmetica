# Generated from G4.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,22,8,1,10,1,12,1,25,9,1,1,2,1,2,
        1,2,1,2,1,2,1,2,5,2,33,8,2,10,2,12,2,36,9,2,1,3,1,3,1,3,1,3,1,3,
        1,3,5,3,44,8,3,10,3,12,3,47,9,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,55,8,
        4,10,4,12,4,58,9,4,1,5,1,5,1,5,1,5,1,5,3,5,65,8,5,1,5,0,4,2,4,6,
        8,6,0,2,4,6,8,10,0,0,65,0,12,1,0,0,0,2,15,1,0,0,0,4,26,1,0,0,0,6,
        37,1,0,0,0,8,48,1,0,0,0,10,64,1,0,0,0,12,13,3,2,1,0,13,14,5,0,0,
        1,14,1,1,0,0,0,15,16,6,1,-1,0,16,17,3,4,2,0,17,23,1,0,0,0,18,19,
        10,2,0,0,19,20,5,1,0,0,20,22,3,4,2,0,21,18,1,0,0,0,22,25,1,0,0,0,
        23,21,1,0,0,0,23,24,1,0,0,0,24,3,1,0,0,0,25,23,1,0,0,0,26,27,6,2,
        -1,0,27,28,3,6,3,0,28,34,1,0,0,0,29,30,10,2,0,0,30,31,5,2,0,0,31,
        33,3,6,3,0,32,29,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,
        0,35,5,1,0,0,0,36,34,1,0,0,0,37,38,6,3,-1,0,38,39,3,8,4,0,39,45,
        1,0,0,0,40,41,10,2,0,0,41,42,5,3,0,0,42,44,3,8,4,0,43,40,1,0,0,0,
        44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,7,1,0,0,0,47,45,1,0,
        0,0,48,49,6,4,-1,0,49,50,3,10,5,0,50,56,1,0,0,0,51,52,10,2,0,0,52,
        53,5,4,0,0,53,55,3,10,5,0,54,51,1,0,0,0,55,58,1,0,0,0,56,54,1,0,
        0,0,56,57,1,0,0,0,57,9,1,0,0,0,58,56,1,0,0,0,59,60,5,5,0,0,60,61,
        3,2,1,0,61,62,5,6,0,0,62,65,1,0,0,0,63,65,5,7,0,0,64,59,1,0,0,0,
        64,63,1,0,0,0,65,11,1,0,0,0,5,23,34,45,56,64
    ]

class G4Parser ( Parser ):

    grammarFileName = "G4.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUM", "WS" ]

    RULE_prog = 0
    RULE_suma = 1
    RULE_resta = 2
    RULE_mult = 3
    RULE_div = 4
    RULE_factor = 5

    ruleNames =  [ "prog", "suma", "resta", "mult", "div", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NUM=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def suma(self):
            return self.getTypedRuleContext(G4Parser.SumaContext,0)


        def EOF(self):
            return self.getToken(G4Parser.EOF, 0)

        def getRuleIndex(self):
            return G4Parser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = G4Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.suma(0)
            self.state = 13
            self.match(G4Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return G4Parser.RULE_suma

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class G4PasaRestaContext(SumaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G4Parser.SumaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def resta(self):
            return self.getTypedRuleContext(G4Parser.RestaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG4PasaResta" ):
                return visitor.visitG4PasaResta(self)
            else:
                return visitor.visitChildren(self)


    class G4SumaContext(SumaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G4Parser.SumaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def suma(self):
            return self.getTypedRuleContext(G4Parser.SumaContext,0)

        def resta(self):
            return self.getTypedRuleContext(G4Parser.RestaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG4Suma" ):
                return visitor.visitG4Suma(self)
            else:
                return visitor.visitChildren(self)



    def suma(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = G4Parser.SumaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_suma, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = G4Parser.G4PasaRestaContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 16
            self.resta(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = G4Parser.G4SumaContext(self, G4Parser.SumaContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_suma)
                    self.state = 18
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 19
                    self.match(G4Parser.T__0)
                    self.state = 20
                    self.resta(0) 
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RestaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return G4Parser.RULE_resta

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class G4PasaMultContext(RestaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G4Parser.RestaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mult(self):
            return self.getTypedRuleContext(G4Parser.MultContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG4PasaMult" ):
                return visitor.visitG4PasaMult(self)
            else:
                return visitor.visitChildren(self)


    class G4RestaContext(RestaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G4Parser.RestaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def resta(self):
            return self.getTypedRuleContext(G4Parser.RestaContext,0)

        def mult(self):
            return self.getTypedRuleContext(G4Parser.MultContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG4Resta" ):
                return visitor.visitG4Resta(self)
            else:
                return visitor.visitChildren(self)



    def resta(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = G4Parser.RestaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_resta, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = G4Parser.G4PasaMultContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 27
            self.mult(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 34
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = G4Parser.G4RestaContext(self, G4Parser.RestaContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_resta)
                    self.state = 29
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 30
                    self.match(G4Parser.T__1)
                    self.state = 31
                    self.mult(0) 
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return G4Parser.RULE_mult

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class G4MultContext(MultContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G4Parser.MultContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mult(self):
            return self.getTypedRuleContext(G4Parser.MultContext,0)

        def div(self):
            return self.getTypedRuleContext(G4Parser.DivContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG4Mult" ):
                return visitor.visitG4Mult(self)
            else:
                return visitor.visitChildren(self)


    class G4PasaDivContext(MultContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G4Parser.MultContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def div(self):
            return self.getTypedRuleContext(G4Parser.DivContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG4PasaDiv" ):
                return visitor.visitG4PasaDiv(self)
            else:
                return visitor.visitChildren(self)



    def mult(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = G4Parser.MultContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_mult, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = G4Parser.G4PasaDivContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 38
            self.div(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = G4Parser.G4MultContext(self, G4Parser.MultContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mult)
                    self.state = 40
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 41
                    self.match(G4Parser.T__2)
                    self.state = 42
                    self.div(0) 
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DivContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return G4Parser.RULE_div

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class G4DivContext(DivContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G4Parser.DivContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def div(self):
            return self.getTypedRuleContext(G4Parser.DivContext,0)

        def factor(self):
            return self.getTypedRuleContext(G4Parser.FactorContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG4Div" ):
                return visitor.visitG4Div(self)
            else:
                return visitor.visitChildren(self)


    class G4PasaFactorContext(DivContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G4Parser.DivContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(G4Parser.FactorContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG4PasaFactor" ):
                return visitor.visitG4PasaFactor(self)
            else:
                return visitor.visitChildren(self)



    def div(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = G4Parser.DivContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_div, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = G4Parser.G4PasaFactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 49
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = G4Parser.G4DivContext(self, G4Parser.DivContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_div)
                    self.state = 51
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 52
                    self.match(G4Parser.T__3)
                    self.state = 53
                    self.factor() 
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return G4Parser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class G4ParenContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G4Parser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def suma(self):
            return self.getTypedRuleContext(G4Parser.SumaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG4Paren" ):
                return visitor.visitG4Paren(self)
            else:
                return visitor.visitChildren(self)


    class G4NumContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G4Parser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(G4Parser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG4Num" ):
                return visitor.visitG4Num(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = G4Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_factor)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = G4Parser.G4ParenContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(G4Parser.T__4)
                self.state = 60
                self.suma(0)
                self.state = 61
                self.match(G4Parser.T__5)
                pass
            elif token in [7]:
                localctx = G4Parser.G4NumContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.match(G4Parser.NUM)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.suma_sempred
        self._predicates[2] = self.resta_sempred
        self._predicates[3] = self.mult_sempred
        self._predicates[4] = self.div_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def suma_sempred(self, localctx:SumaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def resta_sempred(self, localctx:RestaContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def mult_sempred(self, localctx:MultContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def div_sempred(self, localctx:DivContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




