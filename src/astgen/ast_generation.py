"""
AST Generation module for TyC programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from functools import reduce
from build.TyCVisitor import TyCVisitor
from build.TyCParser import TyCParser
from src.utils.nodes import *


class ASTGeneration(TyCVisitor):
    """AST Generation visitor for TyC language."""
    # program: decl_list EOF;
    def visitProgram(self, ctx:TyCParser.ProgramContext):
        return Program(self.visit(ctx.decl_list()))

    # decl_list: decl_list decl | ;
    def visitDecl_list(self, ctx:TyCParser.Decl_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.decl_list()) + self.visit(ctx.decl())]
 
    # decl: func_decl | struct_decl;
    def visitDecl(self, ctx:TyCParser.DeclContext):
        if ctx.func_decl():
            return Decl(self.visit(ctx.func_decl()))
        return Decl(self.visit(ctx.struct_decl()))

    # func_decl: (typ | VOID | ) ID LEFT_PAREN param_list RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACE;
    def visitFunc_decl(self, ctx:TyCParser.Func_declContext):
        pass
    
    # param_list: param_list_exist | ;
    def visitParam_list(self, ctx:TyCParser.Param_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.param_list_exist())
    
    # param_list_exist: param_decl COMMA param_list_exist | param_decl;
    def visitParam_list_exist(self, ctx:TyCParser.Param_list_existContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param_decl())]
        return [self.visit(ctx.param_list_exist()) + self.visit(ctx.param_decl())]

    # param_decl: typ ID;
    def visitParam_decl(self, ctx:TyCParser.Param_declContext):
        return Param(param_type=self.visit(ctx.typ()), name=ctx.ID().getText())
    
    # struct_decl: STRUCT ID LEFT_BRACE struct_member_list RIGHT_BRACE SEMICOLON;
    def visitStruct_decl(self, ctx:TyCParser.Struct_declContext):
        return StructDecl(name=ctx.ID().getText(), members=self.visit(ctx.struct_member_list()))

    # struct_member_list: struct_member_list struct_member | ;
    def visitStruct_member_list(self, ctx:TyCParser.Struct_member_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.struct_member_list()) + [self.visit(ctx.struct_member)]

    # struct_member: typ ID SEMICOLON;
    def visitStruct_member(self, ctx:TyCParser.Struct_memberContext):
        return self.visit(ctx.typ()) + ctx.ID().getText()
    
    # struct_var_decl_list: struct_var_decl_list_exist | ;
    def visitStruct_var_decl_list(self, ctx:TyCParser.Struct_var_decl_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.struct_var_decl_list_exist())

    # struct_var_decl_list_exist: struct_var_decl_list_exist COMMA struct_var_decl | struct_var_decl;
    def visitStruct_var_decl_list_exist(self, ctx:TyCParser.Struct_var_decl_list_existContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.struct_var_decl)]
        return [self.visit(ctx.struct_var_decl_list_exist()) + self.visit(ctx.struct_var_decl)]

    # struct_var_decl: ID ID SEMICOLON | ID ID ASSIGNMENT LEFT_BRACE (struct_var_member_list | )RIGHT_BRACE SEMICOLON;
    def visitStruct_var_decl(self, ctx:TyCParser.Struct_var_declContext):
        pass

    # struct_var_member_list: struct_var_member_list COMMA struct_var_member | ;
    def visitStruct_var_member_list(self, ctx:TyCParser.Struct_var_member_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.struct_var_member_list()) + self.visit(ctx.struct_var_member())]

    # struct_var_member: operand | func_call_expr;
    def visitStruct_var_member(self, ctx:TyCParser.Struct_var_memberContext):
        return self.visit(ctx.getChild(0))

    # var_decl_list: var_decl_list var_decl | var_decl;
    def visitVar_decl_list(self, ctx:TyCParser.Var_decl_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.var_decl())]
        return [self.visit(ctx.var_decl_list()) + self.visit(ctx.var_decl())]

    # var_decl: auto_var_decl | explicit_var_decl;
    def visitVar_decl(self, ctx:TyCParser.Var_declContext):
        return self.visit(ctx.getChild(0))

    # auto_var_decl: AUTO ID SEMICOLON | AUTO ID ASSIGNMENT assign_expr SEMICOLON;
    def visitAuto_var_decl(self, ctx:TyCParser.Auto_var_declContext):
        if ctx.getChildCount() == 0:
            return VarDecl(var_type=None,name=ctx.ID().getText())
        return VarDecl(var_type=None,name=ctx.ID().getText(),init_value=AssignExpr())

    # explicit_var_decl: typ ID SEMICOLON | typ ID ASSIGNMENT assign_expr SEMICOLON;
    def visitExplicit_var_decl(self, ctx:TyCParser.Explicit_var_declContext):
        pass
    
    # typ: primitive_typ | ID;
    def visitTyp(self, ctx:TyCParser.TypContext):
        if ctx.primitive_typ():
            return self.visit(ctx.primitive_typ())
        return ctx.ID().getText()

    # primitive_typ: INT | FLOAT | STRING;
    def visitPrimitive_typ(self, ctx:TyCParser.Primitive_typContext):
        if ctx.INT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        if ctx.FLOAT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        if ctx.STRING():
            return StringLiteral(str(ctx.STRING_LIT().getText()))
    
    # expr_list: expr_list_exist | ;
    def visitExpr_list(self, ctx:TyCParser.Expr_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.expr_list_exist())
    
    # expr_list_exist: expr_list_exist COMMA expr | expr;
    def visitExpr_list_exist(self, ctx:TyCParser.Expr_list_existContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr())
        return [self.visit(ctx.expr_list_exist()) + self.visit(ctx.expr())]

    # expr: assign_expr;
    def visitExpr(self, ctx:TyCParser.ExprContext):
        return self.visit(ctx.getChild(0))
    
    # assign_expr: assign_lhs ASSIGNMENT assign_expr | or_expr; //right
    def visitAssign_expr(self, ctx:TyCParser.Assign_exprContext):
        if ctx.getChildCount() == 1:
            return self.getChild(0)
        return ctx.getChild(0) + ctx.getChild(1)
    
    # assign_lhs: ID | member_access_expr MEMBER_ACCESS ID;
    def visitAssign_lhs(self, ctx:TyCParser.Assign_lhsContext):
        if ctx.getChildCount() == 0:
            return
        return ctx.getChild(0) + ctx.ID().getText()
