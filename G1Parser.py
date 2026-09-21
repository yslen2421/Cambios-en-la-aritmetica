# Generated from G1.g4 by ANTLR 4.13.2
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
        4,1,8,47,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,5,2,35,8,2,10,2,12,2,38,9,2,1,3,1,3,1,3,
        1,3,1,3,3,3,45,8,3,1,3,0,2,2,4,4,0,2,4,6,0,0,47,0,8,1,0,0,0,2,11,
        1,0,0,0,4,25,1,0,0,0,6,44,1,0,0,0,8,9,3,2,1,0,9,10,5,0,0,1,10,1,
        1,0,0,0,11,12,6,1,-1,0,12,13,3,4,2,0,13,22,1,0,0,0,14,15,10,3,0,
        0,15,16,5,1,0,0,16,21,3,4,2,0,17,18,10,2,0,0,18,19,5,2,0,0,19,21,
        3,4,2,0,20,14,1,0,0,0,20,17,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,
        22,23,1,0,0,0,23,3,1,0,0,0,24,22,1,0,0,0,25,26,6,2,-1,0,26,27,3,
        6,3,0,27,36,1,0,0,0,28,29,10,3,0,0,29,30,5,3,0,0,30,35,3,6,3,0,31,
        32,10,2,0,0,32,33,5,4,0,0,33,35,3,6,3,0,34,28,1,0,0,0,34,31,1,0,
        0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,5,1,0,0,0,38,36,
        1,0,0,0,39,40,5,5,0,0,40,41,3,2,1,0,41,42,5,6,0,0,42,45,1,0,0,0,
        43,45,5,7,0,0,44,39,1,0,0,0,44,43,1,0,0,0,45,7,1,0,0,0,5,20,22,34,
        36,44
    ]

class G1Parser ( Parser ):

    grammarFileName = "G1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUM", "WS" ]

    RULE_prog = 0
    RULE_e = 1
    RULE_t = 2
    RULE_f = 3

    ruleNames =  [ "prog", "e", "t", "f" ]

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

        def e(self):
            return self.getTypedRuleContext(G1Parser.EContext,0)


        def EOF(self):
            return self.getToken(G1Parser.EOF, 0)

        def getRuleIndex(self):
            return G1Parser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = G1Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.e(0)
            self.state = 9
            self.match(G1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return G1Parser.RULE_e

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class G1SumaContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G1Parser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self):
            return self.getTypedRuleContext(G1Parser.EContext,0)

        def t(self):
            return self.getTypedRuleContext(G1Parser.TContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG1Suma" ):
                return visitor.visitG1Suma(self)
            else:
                return visitor.visitChildren(self)


    class G1TermEContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G1Parser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def t(self):
            return self.getTypedRuleContext(G1Parser.TContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG1TermE" ):
                return visitor.visitG1TermE(self)
            else:
                return visitor.visitChildren(self)


    class G1RestaContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G1Parser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self):
            return self.getTypedRuleContext(G1Parser.EContext,0)

        def t(self):
            return self.getTypedRuleContext(G1Parser.TContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG1Resta" ):
                return visitor.visitG1Resta(self)
            else:
                return visitor.visitChildren(self)



    def e(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = G1Parser.EContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_e, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = G1Parser.G1TermEContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 12
            self.t(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 22
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 20
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = G1Parser.G1SumaContext(self, G1Parser.EContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 14
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 15
                        self.match(G1Parser.T__0)
                        self.state = 16
                        self.t(0)
                        pass

                    elif la_ == 2:
                        localctx = G1Parser.G1RestaContext(self, G1Parser.EContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 17
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 18
                        self.match(G1Parser.T__1)
                        self.state = 19
                        self.t(0)
                        pass

             
                self.state = 24
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return G1Parser.RULE_t

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class G1MultContext(TContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G1Parser.TContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def t(self):
            return self.getTypedRuleContext(G1Parser.TContext,0)

        def f(self):
            return self.getTypedRuleContext(G1Parser.FContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG1Mult" ):
                return visitor.visitG1Mult(self)
            else:
                return visitor.visitChildren(self)


    class G1DivContext(TContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G1Parser.TContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def t(self):
            return self.getTypedRuleContext(G1Parser.TContext,0)

        def f(self):
            return self.getTypedRuleContext(G1Parser.FContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG1Div" ):
                return visitor.visitG1Div(self)
            else:
                return visitor.visitChildren(self)


    class G1TermTContext(TContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G1Parser.TContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def f(self):
            return self.getTypedRuleContext(G1Parser.FContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG1TermT" ):
                return visitor.visitG1TermT(self)
            else:
                return visitor.visitChildren(self)



    def t(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = G1Parser.TContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_t, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = G1Parser.G1TermTContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 26
            self.f()
            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 34
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = G1Parser.G1MultContext(self, G1Parser.TContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_t)
                        self.state = 28
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 29
                        self.match(G1Parser.T__2)
                        self.state = 30
                        self.f()
                        pass

                    elif la_ == 2:
                        localctx = G1Parser.G1DivContext(self, G1Parser.TContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_t)
                        self.state = 31
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 32
                        self.match(G1Parser.T__3)
                        self.state = 33
                        self.f()
                        pass

             
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return G1Parser.RULE_f

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class G1NumContext(FContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G1Parser.FContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(G1Parser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG1Num" ):
                return visitor.visitG1Num(self)
            else:
                return visitor.visitChildren(self)


    class G1ParenContext(FContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a G1Parser.FContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self):
            return self.getTypedRuleContext(G1Parser.EContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG1Paren" ):
                return visitor.visitG1Paren(self)
            else:
                return visitor.visitChildren(self)



    def f(self):

        localctx = G1Parser.FContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_f)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = G1Parser.G1ParenContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(G1Parser.T__4)
                self.state = 40
                self.e(0)
                self.state = 41
                self.match(G1Parser.T__5)
                pass
            elif token in [7]:
                localctx = G1Parser.G1NumContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(G1Parser.NUM)
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
        self._predicates[1] = self.e_sempred
        self._predicates[2] = self.t_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def e_sempred(self, localctx:EContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def t_sempred(self, localctx:TContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




