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

    # # decl_list: decl_list decl | ;
    # def visitDecl_list(self, ctx:TyCParser.Decl_listContext):
    #     if ctx.getChildCount() == 0:
    #         return []
    #     return [self.visit(ctx.decl_list()) + self.visit(ctx.decl())]
 
    # # decl: func_decl | struct_decl;
    # def visitDecl(self, ctx:TyCParser.DeclContext):
    #     if ctx.func_decl():
    #         return Decl(self.visit(ctx.func_decl()))
    #     return Decl(self.visit(ctx.struct_decl()))

    # # func_decl: (typ | VOID | ) ID LEFT_PAREN param_list RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACE;
    # def visitFunc_decl(self, ctx:TyCParser.Func_declContext):
    #     pass
    
    # # param_list: param_list_exist | ;
    # def visitParam_list(self, ctx:TyCParser.Param_listContext):
    #     if ctx.getChildCount() == 0:
    #         return []
    #     return self.visit(ctx.param_list_exist())
    
    # # param_list_exist: param_decl COMMA param_list_exist | param_decl;
    # def visitParam_list_exist(self, ctx:TyCParser.Param_list_existContext):
    #     if ctx.getChildCount() == 1:
    #         return [self.visit(ctx.param_decl())]
    #     return [self.visit(ctx.param_list_exist()) + self.visit(ctx.param_decl())]

    # # param_decl: typ ID;
    # def visitParam_decl(self, ctx:TyCParser.Param_declContext):
    #     return Param(param_type=self.visit(ctx.typ()), name=ctx.ID().getText())
    
    # # struct_decl: STRUCT ID LEFT_BRACE struct_member_list RIGHT_BRACE SEMICOLON;
    # def visitStruct_decl(self, ctx:TyCParser.Struct_declContext):
    #     return StructDecl(name=ctx.ID().getText(), members=self.visit(ctx.struct_member_list()))

    # # struct_member_list: struct_member_list struct_member | ;
    # def visitStruct_member_list(self, ctx:TyCParser.Struct_member_listContext):
    #     if ctx.getChildCount() == 0:
    #         return []
    #     return self.visit(ctx.struct_member_list()) + [self.visit(ctx.struct_member)]

    # # struct_member: typ ID SEMICOLON;
    # def visitStruct_member(self, ctx:TyCParser.Struct_memberContext):
    #     return self.visit(ctx.typ()) + ctx.ID().getText()
    
    # # struct_var_decl_list: struct_var_decl_list_exist | ;
    # def visitStruct_var_decl_list(self, ctx:TyCParser.Struct_var_decl_listContext):
    #     if ctx.getChildCount() == 0:
    #         return []
    #     return self.visit(ctx.struct_var_decl_list_exist())

    # # struct_var_decl_list_exist: struct_var_decl_list_exist COMMA struct_var_decl | struct_var_decl;
    # def visitStruct_var_decl_list_exist(self, ctx:TyCParser.Struct_var_decl_list_existContext):
    #     if ctx.getChildCount() == 1:
    #         return [self.visit(ctx.struct_var_decl)]
    #     return [self.visit(ctx.struct_var_decl_list_exist()) + self.visit(ctx.struct_var_decl)]

    # # struct_var_decl: ID ID SEMICOLON | ID ID ASSIGNMENT LEFT_BRACE (struct_var_member_list | )RIGHT_BRACE SEMICOLON;
    # def visitStruct_var_decl(self, ctx:TyCParser.Struct_var_declContext):
    #     pass

    # # struct_var_member_list: struct_var_member_list COMMA struct_var_member | ;
    # def visitStruct_var_member_list(self, ctx:TyCParser.Struct_var_member_listContext):
    #     if ctx.getChildCount() == 0:
    #         return []
    #     return [self.visit(ctx.struct_var_member_list()) + self.visit(ctx.struct_var_member())]

    # # struct_var_member: operand | func_call_expr;
    # def visitStruct_var_member(self, ctx:TyCParser.Struct_var_memberContext):
    #     return self.visit(ctx.getChild(0))

    # # var_decl_list: var_decl_list var_decl | var_decl;
    # def visitVar_decl_list(self, ctx:TyCParser.Var_decl_listContext):
    #     if ctx.getChildCount() == 1:
    #         return [self.visit(ctx.var_decl())]
    #     return [self.visit(ctx.var_decl_list()) + self.visit(ctx.var_decl())]

    # # var_decl: auto_var_decl | explicit_var_decl;
    # def visitVar_decl(self, ctx:TyCParser.Var_declContext):
    #     return self.visit(ctx.getChild(0))

    # # auto_var_decl: AUTO ID SEMICOLON | AUTO ID ASSIGNMENT assign_expr SEMICOLON;
    # def visitAuto_var_decl(self, ctx:TyCParser.Auto_var_declContext):
    #     if ctx.getChildCount() == 0:
    #         return VarDecl(var_type=None,name=ctx.ID().getText())
    #     return VarDecl(var_type=None,name=ctx.ID().getText(),init_value=AssignExpr())

    # # explicit_var_decl: typ ID SEMICOLON | typ ID ASSIGNMENT assign_expr SEMICOLON;
    # def visitExplicit_var_decl(self, ctx:TyCParser.Explicit_var_declContext):
    #     pass
    
    # # typ: primitive_typ | ID;
    # def visitTyp(self, ctx:TyCParser.TypContext):
    #     if ctx.primitive_typ():
    #         return self.visit(ctx.primitive_typ())
    #     return ctx.ID().getText()

    # # primitive_typ: INT | FLOAT | STRING;
    # def visitPrimitive_typ(self, ctx:TyCParser.Primitive_typContext):
    #     if ctx.INT():
    #         return IntLiteral(int(ctx.INT_LIT().getText()))
    #     if ctx.FLOAT():
    #         return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
    #     if ctx.STRING():
    #         return StringLiteral(str(ctx.STRING_LIT().getText()))
    
    # # expr_list: expr_list_exist | ;
    # def visitExpr_list(self, ctx:TyCParser.Expr_listContext):
    #     if ctx.getChildCount() == 0:
    #         return []
    #     return self.visit(ctx.expr_list_exist())
    
    # # expr_list_exist: expr_list_exist COMMA expr | expr;
    # def visitExpr_list_exist(self, ctx:TyCParser.Expr_list_existContext):
    #     if ctx.getChildCount() == 1:
    #         return self.visit(ctx.expr())
    #     return [self.visit(ctx.expr_list_exist()) + self.visit(ctx.expr())]

    # # expr: assign_expr;
    # def visitExpr(self, ctx:TyCParser.ExprContext):
    #     return self.visit(ctx.getChild(0))
    
    # # assign_expr: assign_lhs ASSIGNMENT assign_expr | or_expr; //right
    # def visitAssign_expr(self, ctx:TyCParser.Assign_exprContext):
    #     pass

    # while_stmt: WHILE LEFT_PAREN expr RIGHT_PAREN stmt;
    def visitWhile_stmt(self, ctx: TyCParser.While_stmtContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.stmt()))

    # for_stmt: FOR LEFT_PAREN init condition SEMICOLON update RIGHT_PAREN stmt;
    def visitFor_stmt(self, ctx: TyCParser.For_stmtContext):
        init_node = self.visit(ctx.init())
        condition_node = self.visit(ctx.condition())
        update_node = self.visit(ctx.update())
        stmt_node = self.visit(ctx.stmt())
        return ForStmt(init_node, condition_node, update_node, stmt_node)

    # init: var_decl | assign_lhs ASSIGNMENT expr SEMICOLON | SEMICOLON;
    def visitInit(self, ctx: TyCParser.InitContext):
        # Rule 1: var_decl
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
            
        # Rule 2: assign_lhs ASSIGNMENT expr SEMICOLON
        elif ctx.ASSIGNMENT():
            lhs = self.visit(ctx.assign_lhs())
            expr = self.visit(ctx.expr())
            return AssignExpr(lhs, expr)
            
        # Rule 3: SEMICOLON (Khởi tạo rỗng)
        return None

    # condition: expr | ;
    def visitCondition(self, ctx: TyCParser.ConditionContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        return None

    # update: assign_lhs ASSIGNMENT expr | (INCREMENT | DECREMENT) prefix_expr | postfix_expr (INCREMENT | DECREMENT) | ;
    def visitUpdate(self, ctx: TyCParser.UpdateContext):
        # Rule 1: assign_lhs ASSIGNMENT expr
        if ctx.ASSIGNMENT():
            lhs = self.visit(ctx.assign_lhs())
            expr = self.visit(ctx.expr())
            return AssignExpr(lhs, expr)
            
        # Rule 2: (INCREMENT | DECREMENT) prefix_expr
        elif ctx.prefix_expr():
            # Lấy toán tử ++ hoặc -- (nằm ở vị trí con đầu tiên - index 0)
            op = ctx.getChild(0).getText() 
            expr = self.visit(ctx.prefix_expr())
            # Trả về node Unary, có thể thiết lập cờ để nhận biết là tiền tố (prefix)
            return UnaryExpr(op, expr)
            
        # Rule 3: postfix_expr (INCREMENT | DECREMENT)
        elif ctx.postfix_expr():
            # Lấy toán tử ++ hoặc -- (nằm ở vị trí con thứ hai - index 1)
            op = ctx.getChild(1).getText()
            expr = self.visit(ctx.postfix_expr())
            # Trả về node Unary, có thể thiết lập cờ để nhận biết là hậu tố (postfix)
            return UnaryExpr(op, expr)
            
        # Rule 4: epsilon (Cập nhật rỗng)
        return None


    # switch_stmt: SWITCH LEFT_PAREN expr RIGHT_PAREN LEFT_BRACE switch_body RIGHT_BRACE;
    def visitSwitch_stmt(self, ctx: TyCParser.Switch_stmtContext):
        # Lấy biểu thức của switch
        expr = self.visit(ctx.expr())
        
        # Lấy danh sách cases và danh sách lệnh của default từ switch_body
        cases, default_stmts = self.visit(ctx.switch_body()) if ctx.switch_body() else ([], [])
        
        return SwitchStmt(expr, cases, default_stmts)

    # switch_body: case_list | case_list_branch DEFAULT COLON stmt_list case_list_branch | ;
    def visitSwitch_body(self, ctx: TyCParser.Switch_bodyContext):
        # Rule: case_list_branch DEFAULT COLON stmt_list case_list_branch
        if ctx.DEFAULT():
            cases = []
            branches = ctx.case_list_branch()
            
            # Lấy các case nằm trước DEFAULT
            cases.extend(self.visit(branches[0]))
            # Lấy các case nằm sau DEFAULT
            cases.extend(self.visit(branches[1]))
            
            # Lấy các statements của khối DEFAULT
            default_stmts = self.visit(ctx.stmt_list()) if ctx.stmt_list() else []
            return cases, default_stmts
        
        # Rule: case_list
        elif ctx.case_list():
            cases = self.visit(ctx.case_list())
            return cases, []
            
        # Rule: epsilon (switch_body rỗng)
        return [], []

    # case_list_branch: case_list | ;
    def visitCase_list_branch(self, ctx: TyCParser.Case_list_branchContext):
        if ctx.case_list():
            return self.visit(ctx.case_list())
        return []

    # case_list: case_list case_stmt | case_stmt;
    def visitCase_list(self, ctx: TyCParser.Case_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.case_stmt())]
        else:
            return self.visit(ctx.case_list()) + [self.visit(ctx.case_stmt())]

    # case_stmt: CASE expr COLON stmt_list;
    def visitCase_stmt(self, ctx: TyCParser.Case_stmtContext):
        expr = self.visit(ctx.expr())
        stmts = self.visit(ctx.stmt_list()) if ctx.stmt_list() else []
        return (expr, stmts)
        
    # stmt_list: stmt_list stmt | ;
    def visitStmt_list(self, ctx: TyCParser.Stmt_listContext):
        # Rule: stmt_list stmt | epsilon
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.stmt_list()) + [self.visit(ctx.stmt())]

    # break_stmt: BREAK SEMICOLON;
    def visitBreak_stmt(self, ctx: TyCParser.Break_stmtContext):
        return BreakStmt()

    # continue_stmt: CONTINUE SEMICOLON;
    def visitContinue_stmt(self, ctx: TyCParser.Continue_stmtContext):
        return ContinueStmt()

    # return_stmt: RETURN (expr | ) SEMICOLON;
    def visitReturn_stmt(self, ctx: TyCParser.Return_stmtContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt()

    # expr_stmt: expr SEMICOLON;
    def visitExpr_stmt(self, ctx: TyCParser.Expr_stmtContext):
        return ExprStmt(self.visit(ctx.expr()))