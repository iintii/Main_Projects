# Generated from While.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("Q\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\7\2\21\n\2\f\2\16\2\24\13\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2$\n\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\63\n\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\7\3;\n\3\f\3\16\3>\13\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\5\4G\n\4\3\4\3\4\3\4\7\4L\n\4\f")
        buf.write("\4\16\4O\13\4\3\4\2\4\4\6\5\2\4\6\2\2\2[\2#\3\2\2\2\4")
        buf.write("\62\3\2\2\2\6F\3\2\2\2\b\t\7\26\2\2\t\n\7\6\2\2\n$\5\6")
        buf.write("\4\2\13$\7\7\2\2\f\r\7\b\2\2\r\22\5\2\2\2\16\17\7\5\2")
        buf.write("\2\17\21\5\2\2\2\20\16\3\2\2\2\21\24\3\2\2\2\22\20\3\2")
        buf.write("\2\2\22\23\3\2\2\2\23\25\3\2\2\2\24\22\3\2\2\2\25\26\7")
        buf.write("\t\2\2\26$\3\2\2\2\27\30\7\n\2\2\30\31\5\4\3\2\31\32\7")
        buf.write("\13\2\2\32\33\5\2\2\2\33\34\7\f\2\2\34\35\5\2\2\2\35$")
        buf.write("\3\2\2\2\36\37\7\r\2\2\37 \5\4\3\2 !\7\16\2\2!\"\5\2\2")
        buf.write("\2\"$\3\2\2\2#\b\3\2\2\2#\13\3\2\2\2#\f\3\2\2\2#\27\3")
        buf.write("\2\2\2#\36\3\2\2\2$\3\3\2\2\2%&\b\3\1\2&\63\7\17\2\2\'")
        buf.write("\63\7\20\2\2()\7\21\2\2)\63\5\4\3\7*+\5\6\4\2+,\7\24\2")
        buf.write("\2,-\5\6\4\2-\63\3\2\2\2./\7\3\2\2/\60\5\4\3\2\60\61\7")
        buf.write("\4\2\2\61\63\3\2\2\2\62%\3\2\2\2\62\'\3\2\2\2\62(\3\2")
        buf.write("\2\2\62*\3\2\2\2\62.\3\2\2\2\63<\3\2\2\2\64\65\f\6\2\2")
        buf.write("\65\66\7\22\2\2\66;\5\4\3\7\678\f\5\2\289\7\23\2\29;\5")
        buf.write("\4\3\6:\64\3\2\2\2:\67\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3")
        buf.write("\2\2\2=\5\3\2\2\2><\3\2\2\2?@\b\4\1\2@G\7\26\2\2AG\7\27")
        buf.write("\2\2BC\7\3\2\2CD\5\6\4\2DE\7\4\2\2EG\3\2\2\2F?\3\2\2\2")
        buf.write("FA\3\2\2\2FB\3\2\2\2GM\3\2\2\2HI\f\4\2\2IJ\7\25\2\2JL")
        buf.write("\5\6\4\5KH\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2N\7\3")
        buf.write("\2\2\2OM\3\2\2\2\t\22#\62:<FM")
        return buf.getvalue()


class WhileParser ( Parser ):

    grammarFileName = "While.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "';'", "':='", "'skip'", 
                     "'begin'", "'end'", "'if'", "'then'", "'else'", "'while'", 
                     "'do'", "'true'", "'false'", "'not'", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "SEMICOLON", 
                      "ASSIGN", "SKIP_ln", "BEGIN", "END", "IF", "THEN", 
                      "ELSE", "WHILE", "DO", "TRUE", "FALSE", "NOT", "AND", 
                      "OR", "ROP", "AOP", "ID", "NUM", "WS", "SL_COMMENT" ]

    RULE_s = 0
    RULE_b = 1
    RULE_a = 2

    ruleNames =  [ "s", "b", "a" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    SEMICOLON=3
    ASSIGN=4
    SKIP_ln=5
    BEGIN=6
    END=7
    IF=8
    THEN=9
    ELSE=10
    WHILE=11
    DO=12
    TRUE=13
    FALSE=14
    NOT=15
    AND=16
    OR=17
    ROP=18
    AOP=19
    ID=20
    NUM=21
    WS=22
    SL_COMMENT=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
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
        def ASSIGN(self):
            return self.getToken(WhileParser.ASSIGN, 0)
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

        def SKIP_ln(self):
            return self.getToken(WhileParser.SKIP_ln, 0)

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

        def BEGIN(self):
            return self.getToken(WhileParser.BEGIN, 0)
        def s(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.SContext)
            else:
                return self.getTypedRuleContext(WhileParser.SContext,i)

        def END(self):
            return self.getToken(WhileParser.END, 0)
        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(WhileParser.SEMICOLON)
            else:
                return self.getToken(WhileParser.SEMICOLON, i)

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

        def WHILE(self):
            return self.getToken(WhileParser.WHILE, 0)
        def b(self):
            return self.getTypedRuleContext(WhileParser.BContext,0)

        def DO(self):
            return self.getToken(WhileParser.DO, 0)
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

        def IF(self):
            return self.getToken(WhileParser.IF, 0)
        def b(self):
            return self.getTypedRuleContext(WhileParser.BContext,0)

        def THEN(self):
            return self.getToken(WhileParser.THEN, 0)
        def s(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.SContext)
            else:
                return self.getTypedRuleContext(WhileParser.SContext,i)

        def ELSE(self):
            return self.getToken(WhileParser.ELSE, 0)

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
            if token in [WhileParser.ID]:
                localctx = WhileParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.match(WhileParser.ID)
                self.state = 7
                self.match(WhileParser.ASSIGN)
                self.state = 8
                self.a(0)
                pass
            elif token in [WhileParser.SKIP_ln]:
                localctx = WhileParser.SkipContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                self.match(WhileParser.SKIP_ln)
                pass
            elif token in [WhileParser.BEGIN]:
                localctx = WhileParser.CompoundContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 10
                self.match(WhileParser.BEGIN)
                self.state = 11
                self.s()
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==WhileParser.SEMICOLON:
                    self.state = 12
                    self.match(WhileParser.SEMICOLON)
                    self.state = 13
                    self.s()
                    self.state = 18
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 19
                self.match(WhileParser.END)
                pass
            elif token in [WhileParser.IF]:
                localctx = WhileParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 21
                self.match(WhileParser.IF)
                self.state = 22
                self.b(0)
                self.state = 23
                self.match(WhileParser.THEN)
                self.state = 24
                self.s()
                self.state = 25
                self.match(WhileParser.ELSE)
                self.state = 26
                self.s()
                pass
            elif token in [WhileParser.WHILE]:
                localctx = WhileParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 28
                self.match(WhileParser.WHILE)
                self.state = 29
                self.b(0)
                self.state = 30
                self.match(WhileParser.DO)
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
            self.copyFrom(ctx)

        def a(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.AContext)
            else:
                return self.getTypedRuleContext(WhileParser.AContext,i)

        def ROP(self):
            return self.getToken(WhileParser.ROP, 0)

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
                self.match(WhileParser.ROP)
                self.state = 42
                self.a(0)
                pass

            elif la_ == 5:
                localctx = WhileParser.BParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(WhileParser.T__0)
                self.state = 45
                self.b(0)
                self.state = 46
                self.match(WhileParser.T__1)
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
            self.copyFrom(ctx)

        def a(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.AContext)
            else:
                return self.getTypedRuleContext(WhileParser.AContext,i)

        def AOP(self):
            return self.getToken(WhileParser.AOP, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WhileParser.ID]:
                localctx = WhileParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 62
                self.match(WhileParser.ID)
                pass
            elif token in [WhileParser.NUM]:
                localctx = WhileParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.match(WhileParser.NUM)
                pass
            elif token in [WhileParser.T__0]:
                localctx = WhileParser.AParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.match(WhileParser.T__0)
                self.state = 65
                self.a(0)
                self.state = 66
                self.match(WhileParser.T__1)
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
                    self.match(WhileParser.AOP)
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
         




