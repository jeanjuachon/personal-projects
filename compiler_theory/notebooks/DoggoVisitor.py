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


    # Visit a parse tree produced by DoggoParser#DeclarationStatement.
    def visitDeclarationStatement(self, ctx:DoggoParser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#StringMethods.
    def visitStringMethods(self, ctx:DoggoParser.StringMethodsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#AssignmentStatement.
    def visitAssignmentStatement(self, ctx:DoggoParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#ExpressionStatement.
    def visitExpressionStatement(self, ctx:DoggoParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#KennelDefinition.
    def visitKennelDefinition(self, ctx:DoggoParser.KennelDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#ImportStatement.
    def visitImportStatement(self, ctx:DoggoParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#IfStatement.
    def visitIfStatement(self, ctx:DoggoParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#WhileStatement.
    def visitWhileStatement(self, ctx:DoggoParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#ForStatement.
    def visitForStatement(self, ctx:DoggoParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#TryCatchFinallyStatement.
    def visitTryCatchFinallyStatement(self, ctx:DoggoParser.TryCatchFinallyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#GrowlStatement.
    def visitGrowlStatement(self, ctx:DoggoParser.GrowlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#MethodCallStatement.
    def visitMethodCallStatement(self, ctx:DoggoParser.MethodCallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#ListMethodStatement.
    def visitListMethodStatement(self, ctx:DoggoParser.ListMethodStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#LeaveScentStatement.
    def visitLeaveScentStatement(self, ctx:DoggoParser.LeaveScentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#BuryBoneStatement.
    def visitBuryBoneStatement(self, ctx:DoggoParser.BuryBoneStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#BegStatement.
    def visitBegStatement(self, ctx:DoggoParser.BegStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#WoofStatement.
    def visitWoofStatement(self, ctx:DoggoParser.WoofStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#declaration.
    def visitDeclaration(self, ctx:DoggoParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#assignment_statement.
    def visitAssignment_statement(self, ctx:DoggoParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#kennel_definition.
    def visitKennel_definition(self, ctx:DoggoParser.Kennel_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#import_statement.
    def visitImport_statement(self, ctx:DoggoParser.Import_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#if_statement.
    def visitIf_statement(self, ctx:DoggoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#while_statement.
    def visitWhile_statement(self, ctx:DoggoParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#for_statement.
    def visitFor_statement(self, ctx:DoggoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#try_statement.
    def visitTry_statement(self, ctx:DoggoParser.Try_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#sniff_catch_clause.
    def visitSniff_catch_clause(self, ctx:DoggoParser.Sniff_catch_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#sniff_finally_clause.
    def visitSniff_finally_clause(self, ctx:DoggoParser.Sniff_finally_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#raise_statement.
    def visitRaise_statement(self, ctx:DoggoParser.Raise_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#method_call_statement.
    def visitMethod_call_statement(self, ctx:DoggoParser.Method_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#list_method_statement.
    def visitList_method_statement(self, ctx:DoggoParser.List_method_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#SlicingMethod.
    def visitSlicingMethod(self, ctx:DoggoParser.SlicingMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#UppercaseMethod.
    def visitUppercaseMethod(self, ctx:DoggoParser.UppercaseMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#LowercaseMethod.
    def visitLowercaseMethod(self, ctx:DoggoParser.LowercaseMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#RemoveWhitespaceMethod.
    def visitRemoveWhitespaceMethod(self, ctx:DoggoParser.RemoveWhitespaceMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#ReplaceMethod.
    def visitReplaceMethod(self, ctx:DoggoParser.ReplaceMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#SplitMethod.
    def visitSplitMethod(self, ctx:DoggoParser.SplitMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#FormatMethod.
    def visitFormatMethod(self, ctx:DoggoParser.FormatMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#slicing_args.
    def visitSlicing_args(self, ctx:DoggoParser.Slicing_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#string_format_args.
    def visitString_format_args(self, ctx:DoggoParser.String_format_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#block.
    def visitBlock(self, ctx:DoggoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#type_.
    def visitType_(self, ctx:DoggoParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#FillbowlExpression.
    def visitFillbowlExpression(self, ctx:DoggoParser.FillbowlExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#Or.
    def visitOr(self, ctx:DoggoParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#MulDiv.
    def visitMulDiv(self, ctx:DoggoParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#In.
    def visitIn(self, ctx:DoggoParser.InContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#AtomicExpression.
    def visitAtomicExpression(self, ctx:DoggoParser.AtomicExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#GreaterThanEqual.
    def visitGreaterThanEqual(self, ctx:DoggoParser.GreaterThanEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#NotIn.
    def visitNotIn(self, ctx:DoggoParser.NotInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#LessThanEqual.
    def visitLessThanEqual(self, ctx:DoggoParser.LessThanEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#SniffapartExpression.
    def visitSniffapartExpression(self, ctx:DoggoParser.SniffapartExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#LessThan.
    def visitLessThan(self, ctx:DoggoParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#Equal.
    def visitEqual(self, ctx:DoggoParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#GreaterThan.
    def visitGreaterThan(self, ctx:DoggoParser.GreaterThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#ChewExpression.
    def visitChewExpression(self, ctx:DoggoParser.ChewExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#WhimperExpression.
    def visitWhimperExpression(self, ctx:DoggoParser.WhimperExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#NotEqual.
    def visitNotEqual(self, ctx:DoggoParser.NotEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#AddSub.
    def visitAddSub(self, ctx:DoggoParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#Modulo.
    def visitModulo(self, ctx:DoggoParser.ModuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#SniffswapStrExpression.
    def visitSniffswapStrExpression(self, ctx:DoggoParser.SniffswapStrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#FloorDiv.
    def visitFloorDiv(self, ctx:DoggoParser.FloorDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#Not.
    def visitNot(self, ctx:DoggoParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#ListLiteral.
    def visitListLiteral(self, ctx:DoggoParser.ListLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#And.
    def visitAnd(self, ctx:DoggoParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#GroomExpression.
    def visitGroomExpression(self, ctx:DoggoParser.GroomExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#HowlExpression.
    def visitHowlExpression(self, ctx:DoggoParser.HowlExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#Exp.
    def visitExp(self, ctx:DoggoParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#list_literal.
    def visitList_literal(self, ctx:DoggoParser.List_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#element.
    def visitElement(self, ctx:DoggoParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#Number.
    def visitNumber(self, ctx:DoggoParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#VariableReference.
    def visitVariableReference(self, ctx:DoggoParser.VariableReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#StringLiteral.
    def visitStringLiteral(self, ctx:DoggoParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#NullLiteral.
    def visitNullLiteral(self, ctx:DoggoParser.NullLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#Parentheses.
    def visitParentheses(self, ctx:DoggoParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#CallExpression.
    def visitCallExpression(self, ctx:DoggoParser.CallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#SqrtCall.
    def visitSqrtCall(self, ctx:DoggoParser.SqrtCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#PawsizeCall.
    def visitPawsizeCall(self, ctx:DoggoParser.PawsizeCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#SmallestPupCall.
    def visitSmallestPupCall(self, ctx:DoggoParser.SmallestPupCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#BiggestPupCall.
    def visitBiggestPupCall(self, ctx:DoggoParser.BiggestPupCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#AlphaPowerCall.
    def visitAlphaPowerCall(self, ctx:DoggoParser.AlphaPowerCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DoggoParser#identifier.
    def visitIdentifier(self, ctx:DoggoParser.IdentifierContext):
        return self.visitChildren(ctx)



del DoggoParser