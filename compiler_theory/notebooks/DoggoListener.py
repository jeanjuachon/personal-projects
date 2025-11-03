# Generated from Doggo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DoggoParser import DoggoParser
else:
    from DoggoParser import DoggoParser

# This class defines a complete listener for a parse tree produced by DoggoParser.
class DoggoListener(ParseTreeListener):

    # Enter a parse tree produced by DoggoParser#start.
    def enterStart(self, ctx:DoggoParser.StartContext):
        pass

    # Exit a parse tree produced by DoggoParser#start.
    def exitStart(self, ctx:DoggoParser.StartContext):
        pass


    # Enter a parse tree produced by DoggoParser#MulDiv.
    def enterMulDiv(self, ctx:DoggoParser.MulDivContext):
        pass

    # Exit a parse tree produced by DoggoParser#MulDiv.
    def exitMulDiv(self, ctx:DoggoParser.MulDivContext):
        pass


    # Enter a parse tree produced by DoggoParser#AddSub.
    def enterAddSub(self, ctx:DoggoParser.AddSubContext):
        pass

    # Exit a parse tree produced by DoggoParser#AddSub.
    def exitAddSub(self, ctx:DoggoParser.AddSubContext):
        pass


    # Enter a parse tree produced by DoggoParser#AtomicExpression.
    def enterAtomicExpression(self, ctx:DoggoParser.AtomicExpressionContext):
        pass

    # Exit a parse tree produced by DoggoParser#AtomicExpression.
    def exitAtomicExpression(self, ctx:DoggoParser.AtomicExpressionContext):
        pass


    # Enter a parse tree produced by DoggoParser#Number.
    def enterNumber(self, ctx:DoggoParser.NumberContext):
        pass

    # Exit a parse tree produced by DoggoParser#Number.
    def exitNumber(self, ctx:DoggoParser.NumberContext):
        pass


    # Enter a parse tree produced by DoggoParser#Parentheses.
    def enterParentheses(self, ctx:DoggoParser.ParenthesesContext):
        pass

    # Exit a parse tree produced by DoggoParser#Parentheses.
    def exitParentheses(self, ctx:DoggoParser.ParenthesesContext):
        pass



del DoggoParser