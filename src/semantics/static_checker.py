"""
Static Semantic Checker for TyC Programming Language

This module implements a comprehensive static semantic checker using visitor pattern
for the TyC procedural programming language. It performs type checking,
scope management, type inference, and detects all semantic errors as
specified in the TyC language specification.
"""

from functools import reduce
from typing import (
    Dict,
    List,
    Set,
    Optional,
    Any,
    Tuple,
    NamedTuple,
    Union,
    TYPE_CHECKING,
)
from ..utils.visitor import ASTVisitor
from ..utils.nodes import (
    ASTNode,
    Program,
    StructDecl,
    MemberDecl,
    FuncDecl,
    Param,
    VarDecl,
    IfStmt,
    WhileStmt,
    ForStmt,
    BreakStmt,
    ContinueStmt,
    ReturnStmt,
    BlockStmt,
    SwitchStmt,
    CaseStmt,
    DefaultStmt,
    Type,
    IntType,
    FloatType,
    StringType,
    VoidType,
    StructType,
    BinaryOp,
    PrefixOp,
    PostfixOp,
    AssignExpr,
    MemberAccess,
    FuncCall,
    Identifier,
    StructLiteral,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    ExprStmt,
    Expr,
    Stmt,
    Decl,
)

# Type aliases for better type hints
TyCType = Union[IntType, FloatType, StringType, VoidType, StructType]
from .static_error import (
    StaticError,
    Redeclared,
    UndeclaredIdentifier,
    UndeclaredFunction,
    UndeclaredStruct,
    TypeCannotBeInferred,
    TypeMismatchInStatement,
    TypeMismatchInExpression,
    MustInLoop,
)


class StaticChecker(ASTVisitor):
    def check_program(self, ast):
        self.global_functions = {
            "readInt": {"param_types": [], "return_type": "int"},
            "readFloat": {"param_types": [], "return_type": "float"},
            "readString": {"param_types": [], "return_type": "string"},
            "printInt": {"param_types": ["int"], "return_type": "void"},
            "printFloat": {"param_types": ["float"], "return_type": "void"},
            "printString": {"param_types": ["string"], "return_type": "void"},
        }
        self.global_structs = {}
        
        self.global_env = [{
            "functions": self.global_functions,
            "structs": self.global_structs,
            "vars": {} 
        }]
        
        self.visit_program(ast, self.global_env)

    def visit_program(self, node: "Program", o: Any = None):
        env = o
        for decl in node.decls:
            if isinstance(decl, StructDecl):
                if decl.name in env[0]["structs"]:
                    raise Redeclared("Struct", decl.name)
                members = {}
                for m in decl.members:
                    if m.name in members:
                        raise Redeclared("Member", m.name)
                    m_type = self.getTypeName(m.member_type)
                    if m_type == decl.name:
                        raise UndeclaredStruct(m_type)
                    if not self.isPrimitive(m_type) and m_type not in env[0]["structs"]:
                        raise UndeclaredStruct(m_type)
                    members[m.name] = m_type
                env[0]["structs"][decl.name] = members
                
            elif isinstance(decl, FuncDecl):
                if decl.name in env[0]["functions"]:
                    raise Redeclared("Function", decl.name)
                param_names = set()
                param_types = []
                for p in decl.params:
                    if p.name in param_names:
                        raise Redeclared("Parameter", p.name)
                    param_names.add(p.name)
                    p_type = self.getTypeName(p.param_type)
                    if not self.isPrimitive(p_type) and p_type not in env[0]["structs"]:
                        raise UndeclaredStruct(p_type)
                    param_types.append(p_type)
                return_type = self.getTypeName(decl.return_type) if decl.return_type else None
                if return_type and not self.isPrimitive(return_type) and return_type not in env[0]["structs"]:
                    raise UndeclaredStruct(return_type)
                env[0]["functions"][decl.name] = {
                    "param_types": param_types,
                    "return_type": return_type
                }
                self.visit(decl, env)

    def visit_func_decl(self, node: "FuncDecl", o: Any = None):
        func_info = self.findFunction(node.name, o)
        method_scope = {
            "func_name": node.name,
            "return_type": func_info["return_type"],
            "in_loop": False,
            "in_switch": False,
            "vars": {},
            "params": set()
        }
        for p in node.params:
            method_scope["vars"][p.name] = {
                "name": p.name,
                "type": self.getTypeName(p.param_type),
                "node": p
            }
            method_scope["params"].add(p.name)
        new_env = [method_scope] + o
        self.visit(node.body, new_env)
        inferred_rt = new_env[0].get("return_type")
        if func_info["return_type"] is None:
            func_info["return_type"] = inferred_rt if inferred_rt else "void"

    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        parent_scope = o[0]
        new_scope = {
            "func_name": parent_scope.get("func_name"),
            "return_type": parent_scope.get("return_type"),
            "in_loop": parent_scope.get("in_loop"),
            "in_switch": parent_scope.get("in_switch"),
            "vars": {}
        }
        env = [new_scope] + o
        for stmt in node.statements:
            self.visit(stmt, env)
        for v_name, v_info in new_scope["vars"].items():
            if v_info["type"] is None:
                raise TypeCannotBeInferred(node)
        if parent_scope.get("return_type") is None and new_scope.get("return_type") is not None:
            for scope in o:
                if "return_type" in scope and scope["return_type"] is None:
                    scope["return_type"] = new_scope["return_type"]

    def visit_var_decl(self, node: "VarDecl", o: Any = None):
        name = node.name
        current_scope = o[0]["vars"]
        if name in current_scope:
            raise Redeclared("Variable", name)
        for scope in o:
            if "params" in scope and name in scope["params"]:
                raise Redeclared("Variable", name)
        decl_type = self.getTypeName(node.var_type)
        if decl_type and not self.isPrimitive(decl_type):
            if self.findStruct(decl_type, o) is None:
                raise UndeclaredStruct(decl_type)
        if node.init_value:
            original_expected = o[0].get("expected_type")
            if decl_type is not None:
                o[0]["expected_type"] = decl_type
            init_val = self.visit(node.init_value, o)
            if decl_type is not None:
                if original_expected is None:
                    o[0].pop("expected_type", None)
                else:
                    o[0]["expected_type"] = original_expected
            if isinstance(init_val, dict) and init_val.get("kind") == "struct_literal":
                if decl_type is None:
                    raise TypeCannotBeInferred(node)
                if self.isPrimitive(decl_type):
                    raise TypeMismatchInStatement(node)
                self.validateStructLiteral(decl_type, init_val, o, stmt_context=True)
                init_type = decl_type
            else:
                init_type = init_val["type"] if isinstance(init_val, dict) and "type" in init_val else init_val
            if init_type is None:
                if decl_type is not None:
                    init_type = decl_type
                    if isinstance(init_val, dict):
                        init_val["type"] = decl_type
                else:
                    raise TypeCannotBeInferred(node)
            if decl_type is None:
                decl_type = init_type
            elif decl_type != init_type:
                raise TypeMismatchInStatement(node)
        var_info = {"name": name, "type": decl_type, "node": node}
        current_scope[name] = var_info

    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        cond_val = self.visit(node.condition, o)
        cond_type = cond_val["type"] if isinstance(cond_val, dict) and "type" in cond_val else cond_val
        if cond_type is None:
            cond_type = "int"
            if isinstance(cond_val, dict):
                cond_val["type"] = "int"
        if cond_type != "int":
            raise TypeMismatchInStatement(node)
        parent_scope = o[0]
        for stmt in [node.then_stmt, node.else_stmt]:
            if stmt:
                if isinstance(stmt, BlockStmt):
                    self.visit(stmt, o)
                else:
                    new_scope = {k: parent_scope.get(k) for k in ["func_name", "return_type", "in_loop", "in_switch"]}
                    new_scope["vars"] = {}
                    env = [new_scope] + o
                    self.visit(stmt, env)
                    for v_name, v_info in new_scope["vars"].items():
                        if v_info["type"] is None:
                            raise TypeCannotBeInferred(stmt)
                    if parent_scope.get("return_type") is None and new_scope.get("return_type") is not None:
                        for scope in o:
                            if "return_type" in scope and scope["return_type"] is None:
                                scope["return_type"] = new_scope["return_type"]

    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        cond_val = self.visit(node.condition, o)
        cond_type = cond_val["type"] if isinstance(cond_val, dict) and "type" in cond_val else cond_val
        if cond_type is None:
            cond_type = "int"
            if isinstance(cond_val, dict):
                cond_val["type"] = "int"
        if cond_type != "int":
            raise TypeMismatchInStatement(node)
        parent_scope = o[0]
        new_scope = {k: parent_scope.get(k) for k in ["func_name", "return_type", "in_switch"]}
        new_scope.update({"in_loop": True, "vars": {}})
        env = [new_scope] + o
        self.visit(node.body, env)
        for v_name, v_info in new_scope["vars"].items():
            if v_info["type"] is None:
                raise TypeCannotBeInferred(node.body)

    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        if node.init:
            self.visit(node.init, o)
        if node.condition:
            cond_val = self.visit(node.condition, o)
            cond_type = cond_val["type"] if isinstance(cond_val, dict) and "type" in cond_val else cond_val
            if cond_type is None:
                cond_type = "int"
                if isinstance(cond_val, dict):
                    cond_val["type"] = "int"
            if cond_type != "int":
                raise TypeMismatchInStatement(node)
        if node.update:
            self.visit(node.update, o)
        parent_scope = o[0]
        new_scope = {k: parent_scope.get(k) for k in ["func_name", "return_type", "in_switch"]}
        new_scope.update({"in_loop": True, "vars": {}})
        env = [new_scope] + o
        self.visit(node.body, env)
        for v_name, v_info in new_scope["vars"].items():
            if v_info["type"] is None:
                raise TypeCannotBeInferred(node.body)

    def visit_switch_stmt(self, node: "SwitchStmt", o: Any = None):
        expr_val = self.visit(node.expr, o)
        expr_type = expr_val["type"] if isinstance(expr_val, dict) and "type" in expr_val else expr_val
        if expr_type is None:
            expr_type = "int"
            if isinstance(expr_val, dict):
                expr_val["type"] = "int"
        if expr_type != "int":
            raise TypeMismatchInStatement(node)
        
        parent_scope = o[0]
        switch_scope = {k: parent_scope.get(k) for k in ["func_name", "return_type", "in_loop"]}
        switch_scope.update({"in_switch": True, "vars": {}})
        env = [switch_scope] + o
        
        def is_constant_expr(e):
            if isinstance(e, (IntLiteral, FloatLiteral, StringLiteral)):
                return True
            if isinstance(e, PrefixOp):
                return is_constant_expr(e.operand)
            if isinstance(e, BinaryOp):
                return is_constant_expr(e.left) and is_constant_expr(e.right)
            return False
        
        for case_stmt in node.cases:
            val = self.visit(case_stmt.expr, env)
            typ = val["type"] if isinstance(val, dict) and "type" in val else val
            if typ != "int" or not is_constant_expr(case_stmt.expr):
                raise TypeMismatchInStatement(node)
            self.visit(case_stmt, env)
            
        if node.default_case:
            self.visit(node.default_case, env)
        for v_name, v_info in switch_scope["vars"].items():
            if v_info["type"] is None:
                raise TypeCannotBeInferred(node)

    def visit_case_stmt(self, node: "CaseStmt", o: Any = None):
        for stmt in node.statements:
            self.visit(stmt, o)

    def visit_default_stmt(self, node: "DefaultStmt", o: Any = None):
        for stmt in node.statements:
            self.visit(stmt, o)

    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        if not any(scope.get("in_loop") or scope.get("in_switch") for scope in o):
            raise MustInLoop(node)

    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        if not any(scope.get("in_loop") for scope in o):
            raise MustInLoop(node)

    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        expected_type = next((s["return_type"] for s in o if "return_type" in s), None)
        if node.expr:
            original_expected = o[0].get("expected_type")
            if expected_type and expected_type != "void":
                o[0]["expected_type"] = expected_type
            ret_val = self.visit(node.expr, o)
            if expected_type and expected_type != "void":
                if original_expected is None:
                    o[0].pop("expected_type", None)
                else:
                    o[0]["expected_type"] = original_expected
            if isinstance(ret_val, dict) and ret_val.get("kind") == "struct_literal":
                if expected_type is None or expected_type == "void":
                    raise TypeCannotBeInferred(node)
                if self.isPrimitive(expected_type):
                    raise TypeMismatchInStatement(node)
                self.validateStructLiteral(expected_type, ret_val, o, stmt_context=True)
                ret_type = expected_type
            else:
                ret_type = ret_val["type"] if isinstance(ret_val, dict) and "type" in ret_val else ret_val
        else:
            ret_type = "void"
            
        if ret_type is None:
            if expected_type and expected_type != "void":
                ret_type = expected_type
                if isinstance(ret_val, dict):
                    ret_val["type"] = expected_type
            else:
                raise TypeCannotBeInferred(node)
                
        if expected_type is None:
            for s in o:
                if "return_type" in s:
                    s["return_type"] = ret_type
                    
                    # Cập nhật ngay vào func_info toàn cục để hàm đệ quy sau lệnh return này có thể suy luận được
                    f_name = s.get("func_name")
                    if f_name:
                        f_info = self.findFunction(f_name, o)
                        if f_info and f_info["return_type"] is None:
                            f_info["return_type"] = ret_type
                            
        elif expected_type != ret_type:
            raise TypeMismatchInStatement(node)

    def visit_expr_stmt(self, node: "ExprStmt", o: Any = None):
        try:
            self.visit(node.expr, o)
        except TypeMismatchInExpression as e:
            err_node = getattr(e, "node", getattr(e, "expr", getattr(e, "exp", (e.args[0] if e.args else None))))
            if err_node is node.expr and isinstance(node.expr, AssignExpr):
                raise TypeMismatchInStatement(node)
            raise e

    def visit_assign_expr(self, node: "AssignExpr", o: Any = None):
        if not isinstance(node.lhs, (Identifier, MemberAccess)):
            raise TypeMismatchInExpression(node)
            
        lhs_val = self.visit(node.lhs, o)
        lhs_type = lhs_val["type"] if isinstance(lhs_val, dict) and "type" in lhs_val else lhs_val
        original_expected = o[0].get("expected_type")
        
        if lhs_type:
            o[0]["expected_type"] = lhs_type
            
        rhs_val = self.visit(node.rhs, o)
        
        if lhs_type:
            if original_expected is None:
                o[0].pop("expected_type", None)
            else:
                o[0]["expected_type"] = original_expected
                
        rhs_type = rhs_val["type"] if isinstance(rhs_val, dict) and "type" in rhs_val else rhs_val
        
        if isinstance(rhs_val, dict) and rhs_val.get("kind") == "struct_literal":
            if not lhs_type:
                raise TypeCannotBeInferred(node)
            if self.isPrimitive(lhs_type):
                raise TypeMismatchInExpression(node)
            self.validateStructLiteral(lhs_type, rhs_val, o)
            rhs_type = lhs_type
            
        if not lhs_type and not rhs_type:
            raise TypeCannotBeInferred(node)
            
        if not lhs_type:
            lhs_type = rhs_type
            if isinstance(lhs_val, dict):
                lhs_val["type"] = rhs_type
                
        if not rhs_type:
            rhs_type = lhs_type
            if isinstance(rhs_val, dict):
                rhs_val["type"] = lhs_type
                
        if lhs_type != rhs_type:
            raise TypeMismatchInExpression(node)
            
        return lhs_type

    def visit_binary_op(self, node: "BinaryOp", o: Any = None):
        expected = o[0].get("expected_type")
        original_expected = expected
        if "expected_type" in o[0]:
            o[0].pop("expected_type", None)
            
        l_val = self.visit(node.left, o)
        r_val = self.visit(node.right, o)
        
        if original_expected:
            o[0]["expected_type"] = original_expected
            
        lt = l_val["type"] if isinstance(l_val, dict) and "type" in l_val else l_val
        rt = r_val["type"] if isinstance(r_val, dict) and "type" in r_val else r_val
        op = node.operator
        
        if op in ['+', '-', '*', '/']:
            if lt is None and rt is None:
                raise TypeCannotBeInferred(node)
                
            if expected == 'int':
                if lt is None and rt == 'int':
                    lt = 'int'
                    if isinstance(l_val, dict):
                        l_val["type"] = 'int'
                elif rt is None and lt == 'int':
                    rt = 'int'
                    if isinstance(r_val, dict):
                        r_val["type"] = 'int'
            elif expected is None:
                if lt is None and rt == 'int' and isinstance(node.right, IntLiteral):
                    lt = 'int'
                    if isinstance(l_val, dict):
                        l_val["type"] = 'int'
                elif rt is None and lt == 'int' and isinstance(node.left, IntLiteral):
                    rt = 'int'
                    if isinstance(r_val, dict):
                        r_val["type"] = 'int'
                        
            if lt is None or rt is None:
                raise TypeCannotBeInferred(node)
            if lt not in ['int', 'float'] or rt not in ['int', 'float']:
                raise TypeMismatchInExpression(node)
            return 'float' if 'float' in [lt, rt] else 'int'
            
        elif op == '%':
            for val, t in [(l_val, lt), (r_val, rt)]:
                if t is None:
                    if isinstance(val, dict):
                        val["type"] = 'int'
            lt = 'int' if lt is None else lt
            rt = 'int' if rt is None else rt
            if lt != 'int' or rt != 'int':
                raise TypeMismatchInExpression(node)
            return 'int'
            
        elif op in ['<', '<=', '>', '>=', '==', '!=']:
            if lt is None or rt is None:
                raise TypeCannotBeInferred(node)
            if lt not in ['int', 'float'] or rt not in ['int', 'float']:
                raise TypeMismatchInExpression(node)
            return 'int'
            
        elif op in ['&&', '||']:
            for val, t in [(l_val, lt), (r_val, rt)]:
                if t is None:
                    if isinstance(val, dict):
                        val["type"] = 'int'
            lt = 'int' if lt is None else lt
            rt = 'int' if rt is None else rt
            if lt != 'int' or rt != 'int':
                raise TypeMismatchInExpression(node)
            return 'int'

    def visit_prefix_op(self, node: "PrefixOp", o: Any = None):
        expected = o[0].get("expected_type")
        original_expected = expected
        if "expected_type" in o[0]:
            o[0].pop("expected_type", None)
            
        val = self.visit(node.operand, o)
        
        if original_expected:
            o[0]["expected_type"] = original_expected
            
        t = val["type"] if isinstance(val, dict) and "type" in val else val
        op = node.operator
        
        if op in ['++', '--']:
            if not isinstance(node.operand, (Identifier, MemberAccess)):
                raise TypeMismatchInExpression(node)
            if t is None:
                t = 'int'
                if isinstance(val, dict):
                    val["type"] = 'int'
            if t != 'int':
                raise TypeMismatchInExpression(node)
            return 'int'
            
        elif op in ['+', '-']:
            if expected == 'int' and t is None:
                t = 'int'
                if isinstance(val, dict):
                    val["type"] = 'int'
            if t is None:
                raise TypeCannotBeInferred(node)
            if t not in ['int', 'float']:
                raise TypeMismatchInExpression(node)
            return t
            
        elif op == '!':
            if t is None:
                t = 'int'
                if isinstance(val, dict):
                    val["type"] = 'int'
            if t != 'int':
                raise TypeMismatchInExpression(node)
            return 'int'

    def visit_postfix_op(self, node: "PostfixOp", o: Any = None):
        if not isinstance(node.operand, (Identifier, MemberAccess)):
            raise TypeMismatchInExpression(node)
        val = self.visit(node.operand, o)
        t = val["type"] if isinstance(val, dict) and "type" in val else val
        if t is None:
            t = 'int'
            if isinstance(val, dict):
                val["type"] = 'int'
        if t != 'int':
            raise TypeMismatchInExpression(node)
        return 'int'

    def visit_member_access(self, node: "MemberAccess", o: Any = None):
        obj_val = self.visit(node.obj, o)
        obj_t = obj_val["type"] if isinstance(obj_val, dict) and "type" in obj_val else obj_val
        if not obj_t:
            raise TypeCannotBeInferred(node)
        struct_info = self.findStruct(obj_t, o)
        if not struct_info or node.member not in struct_info:
            raise TypeMismatchInExpression(node)
        return struct_info[node.member]

    def visit_func_call(self, node: "FuncCall", o: Any = None):
        f = self.findFunction(node.name, o)
        if not f:
            raise UndeclaredFunction(node.name)
        if len(node.args) != len(f["param_types"]):
            raise TypeMismatchInExpression(node)
            
        for arg, pt in zip(node.args, f["param_types"]):
            orig = o[0].get("expected_type")
            o[0]["expected_type"] = pt
            val = self.visit(arg, o)
            if orig is None:
                o[0].pop("expected_type", None)
            else:
                o[0]["expected_type"] = orig
                
            if isinstance(val, dict) and val.get("kind") == "struct_literal":
                if self.isPrimitive(pt):
                    raise TypeMismatchInExpression(node)
                self.validateStructLiteral(pt, val, o)
            else:
                at = val["type"] if isinstance(val, dict) and "type" in val else val
                if at is None:
                    at = pt
                    if isinstance(val, dict):
                        val["type"] = pt
                if at != pt:
                    raise TypeMismatchInExpression(node)
                    
        # Bắt lỗi TypeCannotBeInferred ngay lập tức nếu hàm được gọi trước khi xác định kiểu trả về
        if f["return_type"] is None:
            raise TypeCannotBeInferred(node)
            
        return f["return_type"]

    def visit_identifier(self, node: "Identifier", o: Any = None):
        v = self.findIdentifier(node.name, o)
        if not v:
            raise UndeclaredIdentifier(node.name)
        return v

    def visit_struct_literal(self, node: "StructLiteral", o: Any = None):
        return {
            "kind": "struct_literal", 
            "values": [self.visit(v, o) for v in node.values], 
            "node": node
        }

    def visit_int_literal(self, node: "IntLiteral", o: Any = None):
        return "int"

    def visit_float_literal(self, node: "FloatLiteral", o: Any = None):
        return "float"

    def visit_string_literal(self, node: "StringLiteral", o: Any = None):
        return "string"

    def visit_struct_decl(self, node: "StructDecl", o: Any = None):
        pass

    def visit_member_decl(self, node: "MemberDecl", o: Any = None):
        pass

    def visit_param(self, node: "Param", o: Any = None):
        pass

    def visit_int_type(self, node: "IntType", o: Any = None):
        pass

    def visit_float_type(self, node: "FloatType", o: Any = None):
        pass

    def visit_string_type(self, node: "StringType", o: Any = None):
        pass

    def visit_void_type(self, node: "VoidType", o: Any = None):
        pass

    def visit_struct_type(self, node: "StructType", o: Any = None):
        pass

    def getTypeName(self, t: Any):
        if not t:
            return None
        if isinstance(t, IntType):
            return "int"
        if isinstance(t, FloatType):
            return "float"
        if isinstance(t, StringType):
            return "string"
        if isinstance(t, VoidType):
            return "void"
        if isinstance(t, StructType):
            return t.struct_name
        return str(t)

    def isPrimitive(self, t: str):
        return t in ["int", "float", "string", "void"]

    def findFunction(self, name: str, env: Any):
        return env[-1]["functions"].get(name)

    def findStruct(self, name: str, env: Any):
        return env[-1]["structs"].get(name)

    def findIdentifier(self, name: str, env: Any):
        for s in env:
            if "vars" in s and name in s["vars"]:
                return s["vars"][name]
        return None

    def validateStructLiteral(self, target, lit, env, stmt_context=False):
        info = self.findStruct(target, env)
        node = lit["node"]
        
        if not info:
            if stmt_context:
                raise TypeMismatchInStatement(node)
            else:
                raise TypeMismatchInExpression(node)
                
        m_types = list(info.values())
        if len(m_types) != len(lit["values"]):
            raise TypeMismatchInExpression(node)
            
        for mt, val in zip(m_types, lit["values"]):
            if isinstance(val, dict) and val.get("kind") == "struct_literal":
                if self.isPrimitive(mt):
                    raise TypeMismatchInExpression(val["node"])
                self.validateStructLiteral(mt, val, env)
            else:
                vt = val["type"] if isinstance(val, dict) and "type" in val else val
                if vt is None:
                    vt = mt
                    if isinstance(val, dict):
                        val["type"] = mt
                if vt != mt:
                    raise TypeMismatchInExpression(node)