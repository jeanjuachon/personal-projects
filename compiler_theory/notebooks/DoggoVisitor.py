# Generated from Doggo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DoggoParser import DoggoParser
else:
    from DoggoParser import DoggoParser

# This class defines a complete generic visitor for a parse tree produced by DoggoParser.

class DoggoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DoggoParser#start.
    def visitStart(self, ctx:DoggoParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#MulDiv.
    def visitMulDiv(self, ctx:DoggoParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#AddSub.
    def visitAddSub(self, ctx:DoggoParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#AtomicExpression.
    def visitAtomicExpression(self, ctx:DoggoParser.AtomicExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#Number.
    def visitNumber(self, ctx:DoggoParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#Parentheses.
    def visitParentheses(self, ctx:DoggoParser.ParenthesesContext):
        return self.visitChildren(ctx)



del DoggoParser