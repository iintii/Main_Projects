# Generated from While.g4 by ANTLR 4.13.2
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
        4,1,30,79,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,5,0,15,8,0,10,0,12,0,18,9,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,3,0,34,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,49,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,57,8,
        1,10,1,12,1,60,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,69,8,2,1,2,1,
        2,1,2,5,2,74,8,2,10,2,12,2,77,9,2,1,2,0,2,2,4,3,0,2,4,0,2,1,0,20,
        24,1,0,25,28,89,0,33,1,0,0,0,2,48,1,0,0,0,4,68,1,0,0,0,6,7,5,18,
        0,0,7,8,5,1,0,0,8,34,3,4,2,0,9,34,5,2,0,0,10,11,5,3,0,0,11,16,3,
        0,0,0,12,13,5,4,0,0,13,15,3,0,0,0,14,12,1,0,0,0,15,18,1,0,0,0,16,
        14,1,0,0,0,16,17,1,0,0,0,17,19,1,0,0,0,18,16,1,0,0,0,19,20,5,5,0,
        0,20,34,1,0,0,0,21,22,5,6,0,0,22,23,3,2,1,0,23,24,5,7,0,0,24,25,
        3,0,0,0,25,26,5,8,0,0,26,27,3,0,0,0,27,34,1,0,0,0,28,29,5,9,0,0,
        29,30,3,2,1,0,30,31,5,10,0,0,31,32,3,0,0,0,32,34,1,0,0,0,33,6,1,
        0,0,0,33,9,1,0,0,0,33,10,1,0,0,0,33,21,1,0,0,0,33,28,1,0,0,0,34,
        1,1,0,0,0,35,36,6,1,-1,0,36,49,5,13,0,0,37,49,5,14,0,0,38,39,5,17,
        0,0,39,49,3,2,1,5,40,41,3,4,2,0,41,42,7,0,0,0,42,43,3,4,2,0,43,49,
        1,0,0,0,44,45,5,11,0,0,45,46,3,2,1,0,46,47,5,12,0,0,47,49,1,0,0,
        0,48,35,1,0,0,0,48,37,1,0,0,0,48,38,1,0,0,0,48,40,1,0,0,0,48,44,
        1,0,0,0,49,58,1,0,0,0,50,51,10,4,0,0,51,52,5,15,0,0,52,57,3,2,1,
        5,53,54,10,3,0,0,54,55,5,16,0,0,55,57,3,2,1,4,56,50,1,0,0,0,56,53,
        1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,3,1,0,0,0,60,
        58,1,0,0,0,61,62,6,2,-1,0,62,69,5,18,0,0,63,69,5,19,0,0,64,65,5,
        11,0,0,65,66,3,4,2,0,66,67,5,12,0,0,67,69,1,0,0,0,68,61,1,0,0,0,
        68,63,1,0,0,0,68,64,1,0,0,0,69,75,1,0,0,0,70,71,10,2,0,0,71,72,7,
        1,0,0,72,74,3,4,2,3,73,70,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,
        76,1,0,0,0,76,5,1,0,0,0,77,75,1,0,0,0,7,16,33,48,56,58,68,75
    ]

class WhileParser ( Parser ):

    grammarFileName = "While.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'skip'", "'begin'", "';'", "'end'", 
                     "'if'", "'then'", "'else'", "'while'", "'do'", "'('", 
                     "')'", "'true'", "'false'", "'and'", "'or'", "'not'", 
                     "<INVALID>", "<INVALID>", "'='", "'<'", "'<='", "'>'", 
                     "'>='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TRUE", "FALSE", "AND", "OR", "NOT", 
                      "ID", "NUM", "EQ", "LT", "LE", "GT", "GE", "PLUS", 
                      "MINUS", "MULT", "DIV", "WS", "SL_COMMENT" ]

    RULE_s = 0
    RULE_b = 1
    RULE_a = 2

    ruleNames =  [ "s", "b", "a" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    TRUE=13
    FALSE=14
    AND=15
    OR=16
    NOT=17
    ID=18
    NUM=19
    EQ=20
    LT=21
    LE=22
    GT=23
    GE=24
    PLUS=25
    MINUS=26
    MULT=27
    DIV=28
    WS=29
    SL_COMMENT=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileParser.RULE_s

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignmentContext(SContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.SContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(WhileParser.ID, 0)
        def a(self):
            return self.getTypedRuleContext(WhileParser.AContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class SkipContext(SContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.SContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSkip" ):
                listener.enterSkip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSkip" ):
                listener.exitSkip(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkip" ):
                return visitor.visitSkip(self)
            else:
                return visitor.visitChildren(self)


    class CompoundContext(SContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.SContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def s(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.SContext)
            else:
                return self.getTypedRuleContext(WhileParser.SContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound" ):
                listener.enterCompound(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound" ):
                listener.exitCompound(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound" ):
                return visitor.visitCompound(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(SContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.SContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def b(self):
            return self.getTypedRuleContext(WhileParser.BContext,0)

        def s(self):
            return self.getTypedRuleContext(WhileParser.SContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(SContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.SContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def b(self):
            return self.getTypedRuleContext(WhileParser.BContext,0)

        def s(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.SContext)
            else:
                return self.getTypedRuleContext(WhileParser.SContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)



    def s(self):

        localctx = WhileParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        self._la = 0 # Token type
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                localctx = WhileParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.match(WhileParser.ID)
                self.state = 7
                self.match(WhileParser.T__0)
                self.state = 8
                self.a(0)
                pass
            elif token in [2]:
                localctx = WhileParser.SkipContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                self.match(WhileParser.T__1)
                pass
            elif token in [3]:
                localctx = WhileParser.CompoundContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 10
                self.match(WhileParser.T__2)
                self.state = 11
                self.s()
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 12
                    self.match(WhileParser.T__3)
                    self.state = 13
                    self.s()
                    self.state = 18
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 19
                self.match(WhileParser.T__4)
                pass
            elif token in [6]:
                localctx = WhileParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 21
                self.match(WhileParser.T__5)
                self.state = 22
                self.b(0)
                self.state = 23
                self.match(WhileParser.T__6)
                self.state = 24
                self.s()
                self.state = 25
                self.match(WhileParser.T__7)
                self.state = 26
                self.s()
                pass
            elif token in [9]:
                localctx = WhileParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 28
                self.match(WhileParser.T__8)
                self.state = 29
                self.b(0)
                self.state = 30
                self.match(WhileParser.T__9)
                self.state = 31
                self.s()
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


    class BContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileParser.RULE_b

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NotContext(BContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.BContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(WhileParser.NOT, 0)
        def b(self):
            return self.getTypedRuleContext(WhileParser.BContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class ROpContext(BContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.BContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def a(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.AContext)
            else:
                return self.getTypedRuleContext(WhileParser.AContext,i)

        def LT(self):
            return self.getToken(WhileParser.LT, 0)
        def LE(self):
            return self.getToken(WhileParser.LE, 0)
        def EQ(self):
            return self.getToken(WhileParser.EQ, 0)
        def GT(self):
            return self.getToken(WhileParser.GT, 0)
        def GE(self):
            return self.getToken(WhileParser.GE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterROp" ):
                listener.enterROp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitROp" ):
                listener.exitROp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitROp" ):
                return visitor.visitROp(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(BContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.BContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def b(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.BContext)
            else:
                return self.getTypedRuleContext(WhileParser.BContext,i)

        def OR(self):
            return self.getToken(WhileParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(BContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.BContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def b(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.BContext)
            else:
                return self.getTypedRuleContext(WhileParser.BContext,i)

        def AND(self):
            return self.getToken(WhileParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class TrueContext(BContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.BContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(WhileParser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrue" ):
                listener.enterTrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrue" ):
                listener.exitTrue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrue" ):
                return visitor.visitTrue(self)
            else:
                return visitor.visitChildren(self)


    class FalseContext(BContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.BContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(WhileParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalse" ):
                listener.enterFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalse" ):
                listener.exitFalse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalse" ):
                return visitor.visitFalse(self)
            else:
                return visitor.visitChildren(self)


    class BParenContext(BContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.BContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def b(self):
            return self.getTypedRuleContext(WhileParser.BContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBParen" ):
                listener.enterBParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBParen" ):
                listener.exitBParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBParen" ):
                return visitor.visitBParen(self)
            else:
                return visitor.visitChildren(self)



    def b(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = WhileParser.BContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_b, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = WhileParser.TrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 36
                self.match(WhileParser.TRUE)
                pass

            elif la_ == 2:
                localctx = WhileParser.FalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                self.match(WhileParser.FALSE)
                pass

            elif la_ == 3:
                localctx = WhileParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.match(WhileParser.NOT)
                self.state = 39
                self.b(5)
                pass

            elif la_ == 4:
                localctx = WhileParser.ROpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.a(0)
                self.state = 41
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32505856) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 42
                self.a(0)
                pass

            elif la_ == 5:
                localctx = WhileParser.BParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(WhileParser.T__10)
                self.state = 45
                self.b(0)
                self.state = 46
                self.match(WhileParser.T__11)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 56
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = WhileParser.AndContext(self, WhileParser.BContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_b)
                        self.state = 50
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 51
                        self.match(WhileParser.AND)
                        self.state = 52
                        self.b(5)
                        pass

                    elif la_ == 2:
                        localctx = WhileParser.OrContext(self, WhileParser.BContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_b)
                        self.state = 53
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 54
                        self.match(WhileParser.OR)
                        self.state = 55
                        self.b(4)
                        pass

             
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileParser.RULE_a

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AOpContext(AContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.AContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def a(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.AContext)
            else:
                return self.getTypedRuleContext(WhileParser.AContext,i)

        def PLUS(self):
            return self.getToken(WhileParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(WhileParser.MINUS, 0)
        def MULT(self):
            return self.getToken(WhileParser.MULT, 0)
        def DIV(self):
            return self.getToken(WhileParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAOp" ):
                listener.enterAOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAOp" ):
                listener.exitAOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAOp" ):
                return visitor.visitAOp(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(AContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.AContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(WhileParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(AContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.AContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(WhileParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class AParenContext(AContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.AContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def a(self):
            return self.getTypedRuleContext(WhileParser.AContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAParen" ):
                listener.enterAParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAParen" ):
                listener.exitAParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAParen" ):
                return visitor.visitAParen(self)
            else:
                return visitor.visitChildren(self)



    def a(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = WhileParser.AContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_a, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                localctx = WhileParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 62
                self.match(WhileParser.ID)
                pass
            elif token in [19]:
                localctx = WhileParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.match(WhileParser.NUM)
                pass
            elif token in [11]:
                localctx = WhileParser.AParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.match(WhileParser.T__10)
                self.state = 65
                self.a(0)
                self.state = 66
                self.match(WhileParser.T__11)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = WhileParser.AOpContext(self, WhileParser.AContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_a)
                    self.state = 70
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 71
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 72
                    self.a(3) 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.b_sempred
        self._predicates[2] = self.a_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def b_sempred(self, localctx:BContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

    def a_sempred(self, localctx:AContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




