"""
AST Generation test cases for TyC compiler.
TODO: Implement 100 test cases for AST generation
"""

import pytest
from tests.utils import ASTGenerator


def test_ast_gen_placeholder():
    """Placeholder test - replace with actual test cases"""
    source = """void main() {}"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_01():
    source = """void main() { int x; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_02():
    source = """void main() { auto y = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, y = IntLiteral(5))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_03():
    source = """void main() { x = 1 + 2; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(IntLiteral(1), +, IntLiteral(2))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_04():
    source = """void main() { if (x > 0) return 1; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(0)) then ReturnStmt(return IntLiteral(1)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_05():
    source = """void main() { while (1) { break; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while IntLiteral(1) do BlockStmt([BreakStmt()]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_06():
    source = """struct Point { int x; float y; };"""
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(FloatType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_07():
    source = """int add(int a, int b) { return a + b; }"""
    expected = "Program([FuncDecl(IntType(), add, [Param(IntType(), a), Param(IntType(), b)], BlockStmt([ReturnStmt(return BinaryOp(Identifier(a), +, Identifier(b)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_08():
    source = """void main() { printInt(10); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(printInt, [IntLiteral(10)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_09():
    source = """void main() { ++x; y--; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(PrefixOp(++Identifier(x))), ExprStmt(PostfixOp(Identifier(y)--))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_10():
    source = """void main() { switch(x) { case 1: break; default: continue; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])], default DefaultStmt(default: [ContinueStmt()]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_11():
    source = """void main() { int a = 10; float b = 2.5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), a = IntLiteral(10)), VarDecl(FloatType(), b = FloatLiteral(2.5))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_12():
    source = """void main() { x = (1 + 2) * 3; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(IntLiteral(1), +, IntLiteral(2)), *, IntLiteral(3))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_13():
    source = """void main() { if (a) b = 1; else b = 2; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(a) then ExprStmt(AssignExpr(Identifier(b) = IntLiteral(1))), else ExprStmt(AssignExpr(Identifier(b) = IntLiteral(2))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_14():
    source = """void main() { while (x < 10) x++; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while BinaryOp(Identifier(x), <, IntLiteral(10)) do ExprStmt(PostfixOp(Identifier(x)++)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_15():
    source = """void main() { for (i = 0; i < 10; i++) x = x + i; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, Identifier(i)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_16():
    source = """void main() { auto s = {1,2,3}; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, s = StructLiteral({IntLiteral(1), IntLiteral(2), IntLiteral(3)}))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_17():
    source = """void main() { a.b = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(a).b) = IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_18():
    source = """void main() { return; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_19():
    source = """void main() { switch(x){ case 1: x=2; case 2: break; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ExprStmt(AssignExpr(Identifier(x) = IntLiteral(2)))]), CaseStmt(case IntLiteral(2): [BreakStmt()])])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_20():
    source = """void main() { foo(1,2,3); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, [IntLiteral(1), IntLiteral(2), IntLiteral(3)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_21():
    source = """void main() { int a; a = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), a), ExprStmt(AssignExpr(Identifier(a) = IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_22():
    source = """void main() { int a = 1 + 2 * 3; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), a = BinaryOp(IntLiteral(1), +, BinaryOp(IntLiteral(2), *, IntLiteral(3))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_23():
    source = """void main() { if (x) { y = 1; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(x) then ExprStmt(AssignExpr(Identifier(y) = IntLiteral(1))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_24():
    source = """void main() { while (x) y = y + 1; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while Identifier(x) do ExprStmt(AssignExpr(Identifier(y) = BinaryOp(Identifier(y), +, IntLiteral(1)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_25():
    source = """void main() { ++a; --b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(PrefixOp(++Identifier(a))), ExprStmt(PrefixOp(--Identifier(b)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_26():
    source = """void main() { a++; b--; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(PostfixOp(Identifier(a)++)), ExprStmt(PostfixOp(Identifier(b)--))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_27():
    source = """void main() { foo(); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, []))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_28():
    source = """void main() { foo(1); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, [IntLiteral(1)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_29():
    source = """void main() { a.b.c = 10; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(MemberAccess(Identifier(a).b).c) = IntLiteral(10)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_30():
    source = """void main() { { int x; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([BlockStmt([VarDecl(IntType(), x)])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_31():
    source = """void main() { int a = 5; int b = a; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), a = IntLiteral(5)), VarDecl(IntType(), b = Identifier(a))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_32():
    source = """void main() { x = a + b + c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), +, Identifier(c))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_33():
    source = """void main() { x = a * b + c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), *, Identifier(b)), +, Identifier(c))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_34():
    source = """void main() { x = a + b * c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), +, BinaryOp(Identifier(b), *, Identifier(c)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_35():
    source = """void main() { if (a) b = 1; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(a) then ExprStmt(AssignExpr(Identifier(b) = IntLiteral(1))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_36():
    source = """void main() { while (a < b) a = a + 1; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while BinaryOp(Identifier(a), <, Identifier(b)) do ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(a), +, IntLiteral(1)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_37():
    source = """void main() { a = foo(1) + 2; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(FuncCall(foo, [IntLiteral(1)]), +, IntLiteral(2))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_38():
    source = """void main() { a = (b + c) * d; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(b), +, Identifier(c)), *, Identifier(d))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_39():
    source = """void main() { a = b == c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), ==, Identifier(c))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_40():
    source = """void main() { a = b != c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), !=, Identifier(c))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_41():
    source = """void main() { x = (a); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = Identifier(a)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_42():
    source = """void main() { x = (a + b); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), +, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_43():
    source = """void main() { x = a * (b + c); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), *, BinaryOp(Identifier(b), +, Identifier(c)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_44():
    source = """void main() { x = a && b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), &&, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_45():
    source = """void main() { x = a || b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), ||, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_46():
    source = """void main() { x = a >= b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), >=, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_47():
    source = """void main() { x = a <= b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), <=, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_48():
    source = """void main() { x = a - b - c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), -, Identifier(b)), -, Identifier(c))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_49():
    source = """void main() { x = a / b / c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), /, Identifier(b)), /, Identifier(c))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_50():
    source = """void main() { x = a + b + c + d; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), +, Identifier(c)), +, Identifier(d))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_51():
    source = """void main() { x = 1; y = 2; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))), ExprStmt(AssignExpr(Identifier(y) = IntLiteral(2)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_52():
    source = """void main() { x = a * b * c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), *, Identifier(b)), *, Identifier(c))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_53():
    source = """void main() { x = a / (b + c); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), /, BinaryOp(Identifier(b), +, Identifier(c)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_54():
    source = """void main() { x = (a + b) * (c + d); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), *, BinaryOp(Identifier(c), +, Identifier(d)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_55():
    source = """void main() { x = a > b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), >, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_56():
    source = """void main() { x = a < b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), <, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_57():
    source = """void main() { x = a % b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), %, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_58():
    source = """void main() { x = (a); y = (b); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = Identifier(a))), ExprStmt(AssignExpr(Identifier(y) = Identifier(b)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_59():
    source = """void main() { x = foo(1) * bar(2); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(FuncCall(foo, [IntLiteral(1)]), *, FuncCall(bar, [IntLiteral(2)]))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_60():
    source = """void main() { x = (a + b) + (c + d); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), +, BinaryOp(Identifier(c), +, Identifier(d)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_61():
    source = """void main() { a = 1 + 2 + 3; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(IntLiteral(1), +, IntLiteral(2)), +, IntLiteral(3))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_62():
    source = """void main() { a = 1 * 2 * 3; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(IntLiteral(1), *, IntLiteral(2)), *, IntLiteral(3))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_63():
    source = """void main() { a = (1 + 2) * 3; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(IntLiteral(1), +, IntLiteral(2)), *, IntLiteral(3))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_64():
    source = """void main() { a = 1 + (2 * 3); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(IntLiteral(1), +, BinaryOp(IntLiteral(2), *, IntLiteral(3)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_65():
    source = """void main() { a = (1 + 2) + (3 + 4); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(IntLiteral(1), +, IntLiteral(2)), +, BinaryOp(IntLiteral(3), +, IntLiteral(4)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_66():
    source = """void main() { a = 1 + 2 * 3 + 4; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(IntLiteral(1), +, BinaryOp(IntLiteral(2), *, IntLiteral(3))), +, IntLiteral(4))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_67():
    source = """void main() { a = (1 + 2) * (3 + 4); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(IntLiteral(1), +, IntLiteral(2)), *, BinaryOp(IntLiteral(3), +, IntLiteral(4)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_68():
    source = """void main() { a = foo(1) + foo(2); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(FuncCall(foo, [IntLiteral(1)]), +, FuncCall(foo, [IntLiteral(2)]))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_69():
    source = """void main() { a = foo(1 + 2); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = FuncCall(foo, [BinaryOp(IntLiteral(1), +, IntLiteral(2))])))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_70():
    source = """void main() { a = foo(1) * (2 + 3); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(FuncCall(foo, [IntLiteral(1)]), *, BinaryOp(IntLiteral(2), +, IntLiteral(3)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_71():
    source = """void main() { a = (1); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = IntLiteral(1)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_72():
    source = """void main() { a = ((1)); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = IntLiteral(1)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_73():
    source = """void main() { a = 1 + (2 + (3 + 4)); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(IntLiteral(1), +, BinaryOp(IntLiteral(2), +, BinaryOp(IntLiteral(3), +, IntLiteral(4))))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_74():
    source = """void main() { a = (1 + 2) + 3 + 4; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(BinaryOp(IntLiteral(1), +, IntLiteral(2)), +, IntLiteral(3)), +, IntLiteral(4))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_75():
    source = """void main() { a = foo(1) + bar(2); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(FuncCall(foo, [IntLiteral(1)]), +, FuncCall(bar, [IntLiteral(2)]))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_76():
    source = """void main() { a = foo(1 + 2) * 3; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(FuncCall(foo, [BinaryOp(IntLiteral(1), +, IntLiteral(2))]), *, IntLiteral(3))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_77():
    source = """void main() { a = foo(1) * foo(2); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(FuncCall(foo, [IntLiteral(1)]), *, FuncCall(foo, [IntLiteral(2)]))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_78():
    source = """void main() { a = (foo(1) + foo(2)) * 3; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(FuncCall(foo, [IntLiteral(1)]), +, FuncCall(foo, [IntLiteral(2)])), *, IntLiteral(3))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_79():
    source = """void main() { a = foo(foo(1)); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = FuncCall(foo, [FuncCall(foo, [IntLiteral(1)])])))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_80():
    source = """void main() { a = foo(1) + foo(2) + foo(3); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(FuncCall(foo, [IntLiteral(1)]), +, FuncCall(foo, [IntLiteral(2)])), +, FuncCall(foo, [IntLiteral(3)]))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_81():
    source = """void main() { if (a) b = 1; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(a) then ExprStmt(AssignExpr(Identifier(b) = IntLiteral(1))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_82():
    source = """void main() { if (a) b = 1; else c = 2; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(a) then ExprStmt(AssignExpr(Identifier(b) = IntLiteral(1))), else ExprStmt(AssignExpr(Identifier(c) = IntLiteral(2))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_83():
    source = """void main() { if (a) { b = 1; } else { c = 2; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(a) then ExprStmt(AssignExpr(Identifier(b) = IntLiteral(1))), else ExprStmt(AssignExpr(Identifier(c) = IntLiteral(2))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_84():
    source = """void main() { while (a) b = b + 1; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while Identifier(a) do ExprStmt(AssignExpr(Identifier(b) = BinaryOp(Identifier(b), +, IntLiteral(1)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_85():
    source = """void main() { while (a) { b = b + 1; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while Identifier(a) do BlockStmt([ExprStmt(AssignExpr(Identifier(b) = BinaryOp(Identifier(b), +, IntLiteral(1))))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_86():
    source = """void main() { for (i = 0; i < 5; i++) x = x + 1; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(5)); PostfixOp(Identifier(i)++) do ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_87():
    source = """void main() { return 1; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ReturnStmt(return IntLiteral(1))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_88():
    source = """void main() { foo(1); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, [IntLiteral(1)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_89():
    source = """void main() { a.b = 10; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(a).b) = IntLiteral(10)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_90():
    source = """void main() { a = foo(1) + bar(2) * baz(3); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(FuncCall(foo, [IntLiteral(1)]), +, BinaryOp(FuncCall(bar, [IntLiteral(2)]), *, FuncCall(baz, [IntLiteral(3)])))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_91():
    source = """void main() { for (i = 0; i < 3; i++) { x = x + i; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(3)); PostfixOp(Identifier(i)++) do BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, Identifier(i))))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_92():
    source = """void main() { if (a) for (i = 0; i < 2; i++) x = i; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(a) then ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(2)); PostfixOp(Identifier(i)++) do ExprStmt(AssignExpr(Identifier(x) = Identifier(i)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_93():
    source = """void main() { while (a) for (i = 0; i < 2; i++) x = x + 1; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while Identifier(a) do ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(2)); PostfixOp(Identifier(i)++) do ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1))))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_94():
    source = """void main() { a.b.c = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(MemberAccess(Identifier(a).b).c) = IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_95():
    source = """void main() { x = foo(bar(1)); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = FuncCall(foo, [FuncCall(bar, [IntLiteral(1)])])))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_96():
    source = """void main() { x = foo(bar(baz(1))); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = FuncCall(foo, [FuncCall(bar, [FuncCall(baz, [IntLiteral(1)])])])))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_97():
    source = """void main() { x = a + b * c + d; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), +, BinaryOp(Identifier(b), *, Identifier(c))), +, Identifier(d))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_98():
    source = """void main() { x = (a + b) * (c + d); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), *, BinaryOp(Identifier(c), +, Identifier(d)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_99():
    source = """void main() { return x + 1; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ReturnStmt(return BinaryOp(Identifier(x), +, IntLiteral(1)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_100():
    source = """void main() { foo(bar(1), baz(2)); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, [FuncCall(bar, [IntLiteral(1)]), FuncCall(baz, [IntLiteral(2)])]))]))])"
    assert str(ASTGenerator(source).generate()) == expected