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
        return self.visit(ctx.decl_list()) + [self.visit(ctx.decl())]
 
    # decl: func_decl | struct_decl;
    def visitDecl(self, ctx:TyCParser.DeclContext):
        if ctx.func_decl():
            return Decl(self.visit(ctx.func_decl()))
        return Decl(self.visit(ctx.struct_decl()))

    # func_decl: (typ | VOID | ) ID LEFT_PAREN param_list RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACE;
    def visitFunc_decl(self, ctx:TyCParser.Func_declContext):
        is_typ = self.visit(ctx.typ() if ctx.typ() else ctx.VOID().getText() if ctx.VOID() else None)
        return FuncDecl(return_type=is_typ,name=ctx.ID().getText(),param=self.visit(ctx.param_list()),body=self.visit(ctx.stmt_list()))
    
    # param_list: param_list_exist | ;
    def visitParam_list(self, ctx:TyCParser.Param_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.param_list_exist())
    
    # param_list_exist: param_decl COMMA param_list_exist | param_decl;
    def visitParam_list_exist(self, ctx:TyCParser.Param_list_existContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param_decl())]
        return self.visit(ctx.param_list_exist()) + [self.visit(ctx.param_decl())]

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
        return self.visit(ctx.struct_var_decl_list_exist()) + [self.visit(ctx.struct_var_decl)]

    # struct_var_decl: ID ID SEMICOLON | ID ID ASSIGNMENT LEFT_BRACE (struct_var_member_list | )RIGHT_BRACE SEMICOLON;
    def visitStruct_var_decl(self, ctx:TyCParser.Struct_var_declContext):
        if ctx.getChildCount() == 3:
            return VarDecl(var_type=StructType(ctx.getChild(0).getText()),name=ctx.getChild(1).getText())
        return VarDecl(var_type=StructType(ctx.getChild(0).getText()),name=ctx.getChild(1).getText(),init_value=self.visit(ctx.struct_var_member_list() if ctx.struct_var_member_list() else None))

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
        return self.visit(ctx.var_decl_list()) + [self.visit(ctx.var_decl())]

    # var_decl: auto_var_decl | explicit_var_decl;
    def visitVar_decl(self, ctx:TyCParser.Var_declContext):
        return self.visit(ctx.getChild(0))

    # auto_var_decl: AUTO ID SEMICOLON | AUTO ID ASSIGNMENT expr SEMICOLON;
    def visitAuto_var_decl(self, ctx:TyCParser.Auto_var_declContext):
        if ctx.getChildCount() == 3:
            return VarDecl(var_type=None,name=ctx.ID().getText())
        return VarDecl(var_type=None,name=ctx.ID().getText(),init_value=self.visit(ctx.expr()))

    # explicit_var_decl: typ ID SEMICOLON | typ ID ASSIGNMENT expr SEMICOLON;
    def visitExplicit_var_decl(self, ctx:TyCParser.Explicit_var_declContext):
        if ctx.getChildCount() == 3:
            return VarDecl(var_type=self.visit(ctx.typ()),name=ctx.ID().getText())
        return VarDecl(var_type=self.visit(ctx.typ()),name=ctx.ID().getText(),init_value=self.visit(ctx.expr()))
    
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
        
    # expr_list: expr_list COMMA expr | expr;
    def visitExpr_list(self, ctx:TyCParser.Expr_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return self.visit(ctx.expr_list_exist()) + [self.visit(ctx.expr())]

    # expr: assign_lhs ASSIGNMENT expr | or_expr; //right
    def visitExpr(self, ctx:TyCParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.or_expr())
        return AssignExpr(lhs=self.visit(ctx.assign_lhs()))
    
    # stmt_list: stmt_list stmt | ;
    def visitStmt_list(self, ctx:TyCParser.Stmt_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.stmt_list()) + [self.visit(ctx.stmt())]

    # stmt: var_decl_stmt | block_stmt | if_stmt | while_stmt | for_stmt | switch_stmt | break_stmt | continue_stmt | return_stmt | expr_stmt;
    def visitStmt(self, ctx:TyCParser.StmtContext):
        return self.visit(ctx.getChild(0))

    # var_decl_stmt: var_decl;
    def visitVar_decl_stmt(self, ctx:TyCParser.Var_decl_stmtContext):
        return self.visit(ctx.getChild(0))

    # block_stmt: LEFT_BRACE (var_decl_list | stmt_list) RIGHT_BRACE;
    def visitBlock_stmt(self, ctx:TyCParser.Block_stmtContext):
        return BlockStmt(statements=self.visit(ctx.var_decl_list() if ctx.var_decl_list() else ctx.stmt_list()))

    # while_stmt: WHILE LEFT_PAREN expr RIGHT_PAREN stmt;
    def visitWhile_stmt(self, ctx:TyCParser.While_stmtContext):
        return WhileStmt(condition=self.visit(ctx.expr()),body=elf.visit(ctx.stmt()))

    # for_stmt: FOR LEFT_PAREN init condition SEMICOLON update RIGHT_PAREN stmt;
    def visitFor_stmt(self, ctx:TyCParser.For_stmtContext):
        return ForStmt(init=self.visit(ctx.init()),condition=self.visit(ctx.condition()),update=self.visit(ctx.update()),body=self.visit(ctx.body()))

    # assign_for: assign_lhs ASSIGNMENT expr;
    def visitAssign_for(self, ctx:TyCParser.Assign_forContext):
        return AssignExpr(lhs=self.visit(ctx.assign_lhs()),rhs=self.visit(ctx.expr()))
    
    # init: var_decl | assign_for SEMICOLON | SEMICOLON;
    def visitInit(self, ctx:TyCParser.InitContext):
        if ctx.getChildCount() == 1:
            if ctx.var_decl():
                return self.visit(ctx.var_decl())
            return None
        return self.visit(ctx.assign_for())

    # condition: expr | ;
    def visitCondition(self, ctx:TyCParser.ConditionContext):
        if ctx.getChildCount() == 0:
            return None
        return self.visit(ctx.expr())

    # update: assign_for | (INCREMENT | DECREMENT) prefix_expr | postfix_expr (INCREMENT | DECREMENT) | ;
    def visitUpdate(self, ctx:TyCParser.UpdateContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.assign_for())

    # switch_stmt: SWITCH LEFT_PAREN expr RIGHT_PAREN LEFT_BRACE switch_body RIGHT_BRACE;
    def visitSwitch_stmt(self, ctx:TyCParser.Switch_stmtContext):
        return SwitchStmt(expr=self.visit(ctx.expr()),cases=self.visit(ctx.switch_body()))

    # break_stmt: BREAK SEMICOLON;
    def visitBreak_stmt(self, ctx:TyCParser.Break_stmtContext):
        return ctx.BREAK().getText()

    # continue_stmt: CONTINUE SEMICOLON;
    def visitContinue_stmt(self, ctx:TyCParser.ContinueStmt):
        return ctx.CONTINUE().getText()

    

    
    