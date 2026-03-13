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
        return self.visit(ctx.getChild(0))

    # func_decl: (typ | VOID | ) ID LEFT_PAREN param_list RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACE;
    def visitFunc_decl(self, ctx: TyCParser.Func_declContext):
        if ctx.typ():
            is_typ = self.visit(ctx.typ())
        elif ctx.VOID():
            is_typ = VoidType()
        else:
            is_typ = None
        return FuncDecl(return_type=is_typ, name=ctx.ID().getText(), params=self.visit(ctx.param_list()), body=BlockStmt(statements=self.visit(ctx.stmt_list())))
    
    # param_list: param_list_exist | ;
    def visitParam_list(self, ctx:TyCParser.Param_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.param_list_exist())
    
    # param_list_exist: param_decl COMMA param_list_exist | param_decl;
    def visitParam_list_exist(self, ctx:TyCParser.Param_list_existContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param_decl())]
        return [self.visit(ctx.param_decl())] + self.visit(ctx.param_list_exist())

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
        return self.visit(ctx.struct_member_list()) + [self.visit(ctx.struct_member())]

    # struct_member: typ ID SEMICOLON;
    def visitStruct_member(self, ctx: TyCParser.Struct_memberContext):
        return MemberDecl(member_type=self.visit(ctx.typ()), name=ctx.ID().getText())
    
    # struct_var_decl_list: struct_var_decl_list_exist | ;
    def visitStruct_var_decl_list(self, ctx:TyCParser.Struct_var_decl_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.struct_var_decl_list_exist())

    # struct_var_decl_list_exist: struct_var_decl_list_exist COMMA struct_var_decl | struct_var_decl;
    def visitStruct_var_decl_list_exist(self, ctx:TyCParser.Struct_var_decl_list_existContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.struct_var_decl())]
        return self.visit(ctx.struct_var_decl_list_exist()) + [self.visit(ctx.struct_var_decl())]

    # struct_var_decl: ID ID SEMICOLON | ID ID ASSIGNMENT LEFT_BRACE (struct_var_member_list | )RIGHT_BRACE SEMICOLON;
    def visitStruct_var_decl(self, ctx:TyCParser.Struct_var_declContext):
        if ctx.getChildCount() == 3:
            return VarDecl(var_type=StructType(struct_name=ctx.getChild(0).getText()), name=ctx.getChild(1).getText())
        
        members_list = self.visit(ctx.struct_var_member_list()) if ctx.struct_var_member_list() else []
        struct_init_expr = StructLiteral(values=members_list)
        return VarDecl(var_type=StructType(struct_name=ctx.getChild(0).getText()), name=ctx.getChild(1).getText(), init_value=struct_init_expr)

    # struct_var_member_list: struct_var_member_list COMMA struct_var_member | ;
    def visitStruct_var_member_list(self, ctx:TyCParser.Struct_var_member_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.struct_var_member_list()) + [self.visit(ctx.struct_var_member())]

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
        if ctx.expr():
            return VarDecl(var_type=None,name=ctx.ID().getText(),init_value=self.visit(ctx.expr()))
        return VarDecl(var_type=None,name=ctx.ID().getText())

    # explicit_var_decl: typ ID SEMICOLON | typ ID ASSIGNMENT expr SEMICOLON;
    def visitExplicit_var_decl(self, ctx:TyCParser.Explicit_var_declContext):
        if ctx.getChildCount() == 3:
            return VarDecl(var_type=self.visit(ctx.typ()),name=ctx.ID().getText())
        return VarDecl(var_type=self.visit(ctx.typ()),name=ctx.ID().getText(),init_value=self.visit(ctx.expr()))
    
    # typ: primitive_typ | ID;
    def visitTyp(self, ctx:TyCParser.TypContext):
        if ctx.primitive_typ():
            return self.visit(ctx.primitive_typ())
        return StructType(ctx.ID().getText())

    # primitive_typ: INT | FLOAT | STRING;
    def visitPrimitive_typ(self, ctx:TyCParser.Primitive_typContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        
    # expr_list: expr_list COMMA expr | expr;
    def visitExpr_list(self, ctx:TyCParser.Expr_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return self.visit(ctx.expr_list()) + [self.visit(ctx.expr())]

    # expr: assign_lhs ASSIGNMENT expr | or_expr; //right
    def visitExpr(self, ctx:TyCParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.or_expr())
        return AssignExpr(lhs=self.visit(ctx.assign_lhs()), rhs=self.visit(ctx.expr()))

    # assign_lhs: ID | member_access_expr;
    def visitAssign_lhs(self, ctx: TyCParser.Assign_lhsContext):
        if ctx.ID():
            return Identifier(name=ctx.ID().getText())
        return self.visit(ctx.member_access_expr())

    # or_expr: or_expr LOGICAL_OR and_expr | and_expr;
    def visitOr_expr(self, ctx: TyCParser.Or_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.and_expr())
        return BinaryOp(left=self.visit(ctx.or_expr()), operator=ctx.LOGICAL_OR().getText(), right=self.visit(ctx.and_expr()))

    # and_expr: and_expr LOGICAL_AND eq_expr | eq_expr;
    def visitAnd_expr(self, ctx: TyCParser.And_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.eq_expr())
        return BinaryOp(left=self.visit(ctx.and_expr()), operator=ctx.LOGICAL_AND().getText(), right=self.visit(ctx.eq_expr()))

    # eq_expr: eq_expr (EQUAL | NOT_EQUAL) relational_expr | relational_expr;
    def visitEq_expr(self, ctx: TyCParser.Eq_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.relational_expr())
        op = ctx.getChild(1).getText()
        return BinaryOp(left=self.visit(ctx.eq_expr()), operator=op, right=self.visit(ctx.relational_expr()))

    # relational_expr: relational_expr (LESS_THAN | LESS_THAN_EQUAL | GREATER_THAN | GREATER_THAN_EQUAL) add_sub_expr | add_sub_expr;
    def visitRelational_expr(self, ctx: TyCParser.Relational_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.add_sub_expr())
        op = ctx.getChild(1).getText()
        return BinaryOp(left=self.visit(ctx.relational_expr()), operator=op, right=self.visit(ctx.add_sub_expr()))

    # add_sub_expr: add_sub_expr (ADDITION | SUBTRACTION) multi_div_mod_expr | multi_div_mod_expr;
    def visitAdd_sub_expr(self, ctx: TyCParser.Add_sub_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.multi_div_mod_expr())
        op = ctx.getChild(1).getText()
        return BinaryOp(left=self.visit(ctx.add_sub_expr()), operator=op, right=self.visit(ctx.multi_div_mod_expr()))

    # multi_div_mod_expr: multi_div_mod_expr (MULTI | DIVISION | MODULO) unary_expr | unary_expr;
    def visitMulti_div_mod_expr(self, ctx: TyCParser.Multi_div_mod_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unary_expr())
        op = ctx.getChild(1).getText()
        return BinaryOp(left=self.visit(ctx.multi_div_mod_expr()), operator=op, right=self.visit(ctx.unary_expr()))

    # unary_expr: (LOGICAL_NOT | SUBTRACTION | ADDITION) unary_expr | prefix_expr;
    def visitUnary_expr(self, ctx: TyCParser.Unary_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.prefix_expr())
        op = ctx.getChild(0).getText()
        return PrefixOp(operator=op, operand=self.visit(ctx.unary_expr()))

    # prefix_expr: (INCREMENT | DECREMENT) prefix_expr | postfix_expr;
    def visitPrefix_expr(self, ctx: TyCParser.Prefix_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.postfix_expr())
        op = ctx.getChild(0).getText()
        return PrefixOp(operator=op, operand=self.visit(ctx.prefix_expr()))

    # postfix_expr: postfix_expr (INCREMENT | DECREMENT) | member_access_expr;
    def visitPostfix_expr(self, ctx: TyCParser.Postfix_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.member_access_expr())
        op = ctx.getChild(1).getText()
        return PostfixOp(operator=op, operand=self.visit(ctx.postfix_expr()))

    # member_access_expr: member_access_expr MEMBER_ACCESS ID | operand;
    def visitMember_access_expr(self, ctx: TyCParser.Member_access_exprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operand())
        obj = self.visit(ctx.member_access_expr())
        member = ctx.ID().getText()
        return MemberAccess(obj=obj, member=member)

    # operand: INT_LIT | FLOAT_LIT | STRING_LIT | struct_lit | func_call_expr | paren_expr | ID;
    def visitOperand(self, ctx: TyCParser.OperandContext):
        if ctx.INT_LIT():
            return IntLiteral(value=int(ctx.INT_LIT().getText()))
        if ctx.FLOAT_LIT():
            return FloatLiteral(value=float(ctx.FLOAT_LIT().getText()))
        if ctx.STRING_LIT():
            return StringLiteral(value=str(ctx.STRING_LIT().getText()))
        if ctx.ID():
            return Identifier(name=ctx.ID().getText())
        return self.visit(ctx.getChild(0))

    # struct_lit: LEFT_BRACE (expr_list | ) RIGHT_BRACE;
    def visitStruct_lit(self, ctx: TyCParser.Struct_litContext):
        if ctx.expr_list():
            values = self.visit(ctx.expr_list())
            return StructLiteral(values=values)
        return StructLiteral(values=[])

    # func_call_expr: ID LEFT_PAREN expr_list RIGHT_PAREN;
    def visitFunc_call_expr(self, ctx:TyCParser.Func_call_exprContext):
        args = self.visit(ctx.expr_list()) if ctx.expr_list() else []
        return FuncCall(ctx.ID().getText(), args)

    # paren_expr: LEFT_PAREN expr RIGHT_PAREN;
    def visitParen_expr(self, ctx: TyCParser.Paren_exprContext):
        return self.visit(ctx.expr())

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
    def visitBlock_stmt(self, ctx: TyCParser.Block_stmtContext):
        if ctx.var_decl_list():
            return BlockStmt(statements=self.visit(ctx.var_decl_list()))
        if ctx.stmt_list():
            return BlockStmt(statements=self.visit(ctx.stmt_list()))
        return BlockStmt(statements=[])

    # if_stmt: IF LEFT_PAREN expr RIGHT_PAREN
    # (LEFT_BRACE stmt RIGHT_BRACE
    # | LEFT_BRACE stmt RIGHT_BRACE ELSE LEFT_BRACE stmt RIGHT_BRACE
    # | stmt
    # | stmt ELSE stmt
    # | LEFT_BRACE stmt RIGHT_BRACE ELSE stmt
    # | stmt ELSE LEFT_BRACE stmt RIGHT_BRACE);
    def visitIf_stmt(self, ctx: TyCParser.If_stmtContext):
        stmts = ctx.stmt()
        condition = self.visit(ctx.expr())
        then_stmt = self.visit(stmts[0])
        else_stmt = self.visit(stmts[1]) if len(stmts) > 1 else None
        
        return IfStmt(condition=condition, then_stmt=then_stmt, else_stmt=else_stmt)

    # while_stmt: WHILE LEFT_PAREN expr RIGHT_PAREN stmt;
    def visitWhile_stmt(self, ctx:TyCParser.While_stmtContext):
        return WhileStmt(condition=self.visit(ctx.expr()),body=self.visit(ctx.stmt()))

    # for_stmt: FOR LEFT_PAREN init condition SEMICOLON update RIGHT_PAREN stmt;
    def visitFor_stmt(self, ctx:TyCParser.For_stmtContext):
        return ForStmt(init=self.visit(ctx.init()),condition=self.visit(ctx.condition()),update=self.visit(ctx.update()),body=self.visit(ctx.stmt()))

    # assign_for: assign_lhs ASSIGNMENT expr;
    def visitAssign_for(self, ctx:TyCParser.Assign_forContext):
        return AssignExpr(lhs=self.visit(ctx.assign_lhs()),rhs=self.visit(ctx.expr()))
    
    # init: var_decl | assign_for SEMICOLON | SEMICOLON;
    def visitInit(self, ctx: TyCParser.InitContext):
        if ctx.getChildCount() == 1:
            if ctx.var_decl():
                return self.visit(ctx.var_decl())
            return None
        return ExprStmt(expr=self.visit(ctx.assign_for()))

    # condition: expr | ;
    def visitCondition(self, ctx:TyCParser.ConditionContext):
        if ctx.getChildCount() == 0:
            return None
        return self.visit(ctx.expr())

    # update: assign_for | (INCREMENT | DECREMENT) prefix_expr | postfix_expr (INCREMENT | DECREMENT) | ;
    def visitUpdate(self, ctx: TyCParser.UpdateContext):
        if ctx.getChildCount() == 0:
            return None
        if ctx.assign_for():
            return self.visit(ctx.assign_for())
        if ctx.prefix_expr():
            op = ctx.getChild(0).getText()
            return PrefixOp(operator=op, operand=self.visit(ctx.prefix_expr()))
        if ctx.postfix_expr():
            op = ctx.getChild(1).getText()
            return PostfixOp(operator=op, operand=self.visit(ctx.postfix_expr()))

    # switch_stmt: SWITCH LEFT_PAREN expr RIGHT_PAREN LEFT_BRACE switch_body RIGHT_BRACE;
    def visitSwitch_stmt(self, ctx: TyCParser.Switch_stmtContext):
        cases, default_stmts = self.visit(ctx.switch_body())
        default_case = DefaultStmt(statements=default_stmts) if default_stmts else None
        return SwitchStmt(expr=self.visit(ctx.expr()), cases=cases, default_case=default_case)

    # switch_body: case_list | case_list_branch DEFAULT COLON stmt_list case_list_branch | ;
    def visitSwitch_body(self, ctx: TyCParser.Switch_bodyContext):
        if ctx.DEFAULT():
            cases = []
            branches = ctx.case_list_branch()
            if branches[0].case_list(): cases.extend(self.visit(branches[0]))
            if branches[1].case_list(): cases.extend(self.visit(branches[1]))
            default_stmts = self.visit(ctx.stmt_list()) if ctx.stmt_list() else []
            return cases, default_stmts
        elif ctx.case_list():
            return self.visit(ctx.case_list()), []
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
        return self.visit(ctx.case_list()) + [self.visit(ctx.case_stmt())]

    # case_stmt: CASE expr COLON stmt_list;
    def visitCase_stmt(self, ctx: TyCParser.Case_stmtContext):
        expr = self.visit(ctx.expr())
        stmts = self.visit(ctx.stmt_list()) if ctx.stmt_list() else []
        return CaseStmt(expr, stmts)

    # break_stmt: BREAK SEMICOLON;
    def visitBreak_stmt(self, ctx:TyCParser.Break_stmtContext):
        return BreakStmt()

    # continue_stmt: CONTINUE SEMICOLON;
    def visitContinue_stmt(self, ctx:TyCParser.Continue_stmtContext):
        return ContinueStmt()

    # return_stmt: RETURN (expr | ) SEMICOLON;
    def visitReturn_stmt(self, ctx:TyCParser.Return_stmtContext):
        is_expr = self.visit(ctx.expr()) if ctx.expr() else None
        return ReturnStmt(expr=is_expr)

    # expr_stmt: expr SEMICOLON;
    def visitExpr_stmt(self, ctx:TyCParser.Expr_stmtContext):
        return ExprStmt(expr=self.visit(ctx.expr()))