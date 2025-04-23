# Generated from TypeWhile.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\"")
        buf.write(";\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2")
        buf.write("\17\n\2\f\2\16\2\22\13\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2$\n\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\61\n\3\3\3\3\3")
        buf.write("\3\3\7\3\66\n\3\f\3\16\39\13\3\3\3\2\3\4\4\2\4\2\4\3\2")
        buf.write("\17\20\4\2\23\24\30 \2D\2#\3\2\2\2\4\60\3\2\2\2\6\7\7")
        buf.write("\26\2\2\7\b\7\3\2\2\b$\5\4\3\2\t$\7\4\2\2\n\13\7\5\2\2")
        buf.write("\13\20\5\2\2\2\f\r\7\6\2\2\r\17\5\2\2\2\16\f\3\2\2\2\17")
        buf.write("\22\3\2\2\2\20\16\3\2\2\2\20\21\3\2\2\2\21\23\3\2\2\2")
        buf.write("\22\20\3\2\2\2\23\24\7\7\2\2\24$\3\2\2\2\25\26\7\b\2\2")
        buf.write("\26\27\5\4\3\2\27\30\7\t\2\2\30\31\5\2\2\2\31\32\7\n\2")
        buf.write("\2\32\33\5\2\2\2\33$\3\2\2\2\34\35\7\13\2\2\35\36\5\4")
        buf.write("\3\2\36\37\7\f\2\2\37 \5\2\2\2 $\3\2\2\2!\"\t\2\2\2\"")
        buf.write("$\7\26\2\2#\6\3\2\2\2#\t\3\2\2\2#\n\3\2\2\2#\25\3\2\2")
        buf.write("\2#\34\3\2\2\2#!\3\2\2\2$\3\3\2\2\2%&\b\3\1\2&\61\7\21")
        buf.write("\2\2\'\61\7\22\2\2(\61\7\26\2\2)\61\7\27\2\2*+\7\25\2")
        buf.write("\2+\61\5\4\3\4,-\7\r\2\2-.\5\4\3\2./\7\16\2\2/\61\3\2")
        buf.write("\2\2\60%\3\2\2\2\60\'\3\2\2\2\60(\3\2\2\2\60)\3\2\2\2")
        buf.write("\60*\3\2\2\2\60,\3\2\2\2\61\67\3\2\2\2\62\63\f\5\2\2\63")
        buf.write("\64\t\3\2\2\64\66\5\4\3\6\65\62\3\2\2\2\669\3\2\2\2\67")
        buf.write("\65\3\2\2\2\678\3\2\2\28\5\3\2\2\29\67\3\2\2\2\6\20#\60")
        buf.write("\67")
        return buf.getvalue()


class TypeWhileParser ( Parser ):

    grammarFileName = "TypeWhile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'skip'", "'begin'", "';'", "'end'", 
                     "'if'", "'then'", "'else'", "'while'", "'do'", "'('", 
                     "')'", "'int'", "'bool'", "'true'", "'false'", "'and'", 
                     "'or'", "'not'", "<INVALID>", "<INVALID>", "'='", "'<'", 
                     "'<='", "'>'", "'>='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "BOOL", "TRUE", "FALSE", "AND", 
                      "OR", "NOT", "ID", "NUM", "EQ", "LT", "LE", "GT", 
                      "GE", "PLUS", "MINUS", "MULT", "DIV", "WS", "SL_COMMENT" ]

    RULE_s = 0
    RULE_e = 1

    ruleNames =  [ "s", "e" ]

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
    INT=13
    BOOL=14
    TRUE=15
    FALSE=16
    AND=17
    OR=18
    NOT=19
    ID=20
    NUM=21
    EQ=22
    LT=23
    LE=24
    GT=25
    GE=26
    PLUS=27
    MINUS=28
    MULT=29
    DIV=30
    WS=31
    SL_COMMENT=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TypeWhileParser.RULE_s

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignmentContext(SContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeWhileParser.SContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(TypeWhileParser.ID, 0)
        def e(self):
            return self.getTypedRuleContext(TypeWhileParser.EContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeWhileParser.SContext
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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeWhileParser.SContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def s(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeWhileParser.SContext)
            else:
                return self.getTypedRuleContext(TypeWhileParser.SContext,i)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeWhileParser.SContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self):
            return self.getTypedRuleContext(TypeWhileParser.EContext,0)

        def s(self):
            return self.getTypedRuleContext(TypeWhileParser.SContext,0)


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


    class DeclarationContext(SContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeWhileParser.SContext
            super().__init__(parser)
            self.typeName = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(TypeWhileParser.ID, 0)
        def INT(self):
            return self.getToken(TypeWhileParser.INT, 0)
        def BOOL(self):
            return self.getToken(TypeWhileParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(SContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeWhileParser.SContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self):
            return self.getTypedRuleContext(TypeWhileParser.EContext,0)

        def s(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeWhileParser.SContext)
            else:
                return self.getTypedRuleContext(TypeWhileParser.SContext,i)


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

        localctx = TypeWhileParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        self._la = 0 # Token type
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TypeWhileParser.ID]:
                localctx = TypeWhileParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.match(TypeWhileParser.ID)
                self.state = 5
                self.match(TypeWhileParser.T__0)
                self.state = 6
                self.e(0)
                pass
            elif token in [TypeWhileParser.T__1]:
                localctx = TypeWhileParser.SkipContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.match(TypeWhileParser.T__1)
                pass
            elif token in [TypeWhileParser.T__2]:
                localctx = TypeWhileParser.CompoundContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 8
                self.match(TypeWhileParser.T__2)
                self.state = 9
                self.s()
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TypeWhileParser.T__3:
                    self.state = 10
                    self.match(TypeWhileParser.T__3)
                    self.state = 11
                    self.s()
                    self.state = 16
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 17
                self.match(TypeWhileParser.T__4)
                pass
            elif token in [TypeWhileParser.T__5]:
                localctx = TypeWhileParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 19
                self.match(TypeWhileParser.T__5)
                self.state = 20
                self.e(0)
                self.state = 21
                self.match(TypeWhileParser.T__6)
                self.state = 22
                self.s()
                self.state = 23
                self.match(TypeWhileParser.T__7)
                self.state = 24
                self.s()
                pass
            elif token in [TypeWhileParser.T__8]:
                localctx = TypeWhileParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 26
                self.match(TypeWhileParser.T__8)
                self.state = 27
                self.e(0)
                self.state = 28
                self.match(TypeWhileParser.T__9)
                self.state = 29
                self.s()
                pass
            elif token in [TypeWhileParser.INT, TypeWhileParser.BOOL]:
                localctx = TypeWhileParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 31
                localctx.typeName = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==TypeWhileParser.INT or _la==TypeWhileParser.BOOL):
                    localctx.typeName = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 32
                self.match(TypeWhileParser.ID)
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

    class EContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TypeWhileParser.RULE_e

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NotContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeWhileParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(TypeWhileParser.NOT, 0)
        def e(self):
            return self.getTypedRuleContext(TypeWhileParser.EContext,0)


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


    class VarContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeWhileParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(TypeWhileParser.ID, 0)

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


    class NumContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeWhileParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(TypeWhileParser.NUM, 0)

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


    class TrueContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeWhileParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(TypeWhileParser.TRUE, 0)

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


    class FalseContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeWhileParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(TypeWhileParser.FALSE, 0)

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


    class BinOpContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeWhileParser.EContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeWhileParser.EContext)
            else:
                return self.getTypedRuleContext(TypeWhileParser.EContext,i)

        def PLUS(self):
            return self.getToken(TypeWhileParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(TypeWhileParser.MINUS, 0)
        def MULT(self):
            return self.getToken(TypeWhileParser.MULT, 0)
        def DIV(self):
            return self.getToken(TypeWhileParser.DIV, 0)
        def LT(self):
            return self.getToken(TypeWhileParser.LT, 0)
        def LE(self):
            return self.getToken(TypeWhileParser.LE, 0)
        def EQ(self):
            return self.getToken(TypeWhileParser.EQ, 0)
        def GT(self):
            return self.getToken(TypeWhileParser.GT, 0)
        def GE(self):
            return self.getToken(TypeWhileParser.GE, 0)
        def AND(self):
            return self.getToken(TypeWhileParser.AND, 0)
        def OR(self):
            return self.getToken(TypeWhileParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinOp" ):
                listener.enterBinOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinOp" ):
                listener.exitBinOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinOp" ):
                return visitor.visitBinOp(self)
            else:
                return visitor.visitChildren(self)


    class ParenContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeWhileParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self):
            return self.getTypedRuleContext(TypeWhileParser.EContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParen" ):
                listener.enterParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParen" ):
                listener.exitParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)



    def e(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TypeWhileParser.EContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_e, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TypeWhileParser.TRUE]:
                localctx = TypeWhileParser.TrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 36
                self.match(TypeWhileParser.TRUE)
                pass
            elif token in [TypeWhileParser.FALSE]:
                localctx = TypeWhileParser.FalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                self.match(TypeWhileParser.FALSE)
                pass
            elif token in [TypeWhileParser.ID]:
                localctx = TypeWhileParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.match(TypeWhileParser.ID)
                pass
            elif token in [TypeWhileParser.NUM]:
                localctx = TypeWhileParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.match(TypeWhileParser.NUM)
                pass
            elif token in [TypeWhileParser.NOT]:
                localctx = TypeWhileParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.match(TypeWhileParser.NOT)
                self.state = 41
                self.e(2)
                pass
            elif token in [TypeWhileParser.T__10]:
                localctx = TypeWhileParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.match(TypeWhileParser.T__10)
                self.state = 43
                self.e(0)
                self.state = 44
                self.match(TypeWhileParser.T__11)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TypeWhileParser.BinOpContext(self, TypeWhileParser.EContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                    self.state = 48
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 49
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TypeWhileParser.AND) | (1 << TypeWhileParser.OR) | (1 << TypeWhileParser.EQ) | (1 << TypeWhileParser.LT) | (1 << TypeWhileParser.LE) | (1 << TypeWhileParser.GT) | (1 << TypeWhileParser.GE) | (1 << TypeWhileParser.PLUS) | (1 << TypeWhileParser.MINUS) | (1 << TypeWhileParser.MULT) | (1 << TypeWhileParser.DIV))) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 50
                    self.e(4) 
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        self._predicates[1] = self.e_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def e_sempred(self, localctx:EContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




