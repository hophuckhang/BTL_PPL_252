"""
AST Generation test cases for TyC compiler.
TODO: Implement 100 test cases for AST generation
"""

import pytest
from tests.utils import ASTGenerator

# def test_ast_gen_placeholder():
#     """Placeholder test - replace with actual test cases"""
#     source = """void main() {}"""
#     expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])"
#     assert str(ASTGenerator(source).generate()) == expected

def test_1():
    source = "void main() { }"
    expected = "Program([FuncDecl(VoidType(), main, [], [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_2():
    source = "void main() { a = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = IntLiteral(1)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_3():
    source = "void main() { a = b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_4():
    source = "void main() { a = b + 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), +, IntLiteral(1))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_5():
    source = "void main() { a = b * 2; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), *, IntLiteral(2))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_6():
    source = "void main() { if (a) b = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then ExprStmt(AssignExpr(Identifier(b) = IntLiteral(1))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_7():
    source = "void main() { while (a) b = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do ExprStmt(AssignExpr(Identifier(b) = IntLiteral(1))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_8():
    source = "void main() { a++; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PostfixOp(Identifier(a)++))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_9():
    source = "void main() { ++a; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(++Identifier(a)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_10():
    source = "void main() { a = (b); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_11():
    source = "void main() { for (i = 0; i < 5; i++) x = x + 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(5)); PostfixOp(Identifier(i)++) do ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_12():
    source = "void main() { for (i = 0; i < 3; i++) { x = x + i; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(3)); PostfixOp(Identifier(i)++) do BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, Identifier(i))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_13():
    source = "void main() { if (a) for (i = 0; i < 2; i++) x = i; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(2)); PostfixOp(Identifier(i)++) do ExprStmt(AssignExpr(Identifier(x) = Identifier(i)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_14():
    source = "void main() { while (a) for (i = 0; i < 2; i++) x = x + 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(2)); PostfixOp(Identifier(i)++) do ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1))))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_15():
    source = "void main() { a.b = 5; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(Identifier(a).b) = IntLiteral(5)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_16():
    source = "void main() { a.b.c = 5; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(MemberAccess(Identifier(a).b).c) = IntLiteral(5)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_17():
    source = "void main() { if (a) if (b) c = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then IfStmt(if Identifier(b) then ExprStmt(AssignExpr(Identifier(c) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_18():
    source = "void main() { while (a) while (b) c = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do WhileStmt(while Identifier(b) do ExprStmt(AssignExpr(Identifier(c) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_19():
    source = "void main() { for (i = 0; i < 2; i++) for (j = 0; j < 2; j++) x = x + 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(2)); PostfixOp(Identifier(i)++) do ForStmt(for ExprStmt(AssignExpr(Identifier(j) = IntLiteral(0))); BinaryOp(Identifier(j), <, IntLiteral(2)); PostfixOp(Identifier(j)++) do ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1))))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_20():
    source = "void main() { for (i = 0; i < 3; i++) while (a) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(3)); PostfixOp(Identifier(i)++) do WhileStmt(while Identifier(a) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_21():
    source = "void main() { ++a; a++; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(++Identifier(a))), ExprStmt(PostfixOp(Identifier(a)++))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_22():
    source = "void main() { a = b = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = IntLiteral(1))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_23():
    source = "void main() { a = b + c * d; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), +, BinaryOp(Identifier(c), *, Identifier(d)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_24():
    source = "void main() { a = (b + c) * d; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(b), +, Identifier(c)), *, Identifier(d))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_25():
    source = "void main() { a.b.c.d = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(MemberAccess(MemberAccess(Identifier(a).b).c).d) = IntLiteral(1)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_26():
    source = "void main() { if (a) { b = 1; c = 2; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then BlockStmt([ExprStmt(AssignExpr(Identifier(b) = IntLiteral(1))), ExprStmt(AssignExpr(Identifier(c) = IntLiteral(2)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_27():
    source = "void main() { while (a) { b = 1; c = 2; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do BlockStmt([ExprStmt(AssignExpr(Identifier(b) = IntLiteral(1))), ExprStmt(AssignExpr(Identifier(c) = IntLiteral(2)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_28():
    source = "void main() { for (i = 0; i < 2; i++) { a++; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(2)); PostfixOp(Identifier(i)++) do BlockStmt([ExprStmt(PostfixOp(Identifier(a)++))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_29():
    source = "void main() { if (a) while (b) c++; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then WhileStmt(while Identifier(b) do ExprStmt(PostfixOp(Identifier(c)++))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_30():
    source = "void main() { while (a) if (b) c = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do IfStmt(if Identifier(b) then ExprStmt(AssignExpr(Identifier(c) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_31():
    source = "void main() { a = b + c + d; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(b), +, Identifier(c)), +, Identifier(d))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_32():
    source = "void main() { for (i = 0; i < 1; i++) {} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(1)); PostfixOp(Identifier(i)++) do BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_33():
    source = "void main() { if (a) if (b) if (c) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then IfStmt(if Identifier(b) then IfStmt(if Identifier(c) then ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_34():
    source = "void main() { while (a) while (b) while (c) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do WhileStmt(while Identifier(b) do WhileStmt(while Identifier(c) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_35():
    source = "void main() { for (i = 0; i < 2; i++) for (j = 0; j < 2; j++) for (k = 0; k < 2; k++) x = x + 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(2)); PostfixOp(Identifier(i)++) do ForStmt(for ExprStmt(AssignExpr(Identifier(j) = IntLiteral(0))); BinaryOp(Identifier(j), <, IntLiteral(2)); PostfixOp(Identifier(j)++) do ForStmt(for ExprStmt(AssignExpr(Identifier(k) = IntLiteral(0))); BinaryOp(Identifier(k), <, IntLiteral(2)); PostfixOp(Identifier(k)++) do ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1)))))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_36():
    source = "void main() { a = b + c * d + e; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(b), +, BinaryOp(Identifier(c), *, Identifier(d))), +, Identifier(e))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_37():
    source = "void main() { a = b * c + d * e; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(b), *, Identifier(c)), +, BinaryOp(Identifier(d), *, Identifier(e)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_38():
    source = "void main() { a = (b + c) * (d + e); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(b), +, Identifier(c)), *, BinaryOp(Identifier(d), +, Identifier(e)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_39():
    source = "void main() { a.b.c.d.e = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(MemberAccess(MemberAccess(MemberAccess(Identifier(a).b).c).d).e) = IntLiteral(1)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_40():
    source = "void main() { if (a) { if (b) { if (c) x = 1; } } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then IfStmt(if Identifier(b) then IfStmt(if Identifier(c) then ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_41():
    source = "void main() { while (a) { while (b) { while (c) x = 1; } } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do BlockStmt([WhileStmt(while Identifier(b) do BlockStmt([WhileStmt(while Identifier(c) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_42():
    source = "void main() { for (i = 0; i < 2; i++) { for (j = 0; j < 2; j++) { x = x + 1; } } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(2)); PostfixOp(Identifier(i)++) do BlockStmt([ForStmt(for ExprStmt(AssignExpr(Identifier(j) = IntLiteral(0))); BinaryOp(Identifier(j), <, IntLiteral(2)); PostfixOp(Identifier(j)++) do BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1))))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_43():
    source = "void main() { ++a; ++b; ++c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(++Identifier(a))), ExprStmt(PrefixOp(++Identifier(b))), ExprStmt(PrefixOp(++Identifier(c)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_44():
    source = "void main() { a++; b++; c++; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PostfixOp(Identifier(a)++)), ExprStmt(PostfixOp(Identifier(b)++)), ExprStmt(PostfixOp(Identifier(c)++))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_45():
    source = "void main() { a = b = c = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = AssignExpr(Identifier(c) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_46():
    source = "void main() { if (a) while (b) for (i = 0; i < 2; i++) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then WhileStmt(while Identifier(b) do ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(2)); PostfixOp(Identifier(i)++) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_47():
    source = "void main() { while (a) if (b) while (c) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do IfStmt(if Identifier(b) then WhileStmt(while Identifier(c) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_48():
    source = "void main() { a = b + c + d + e; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(BinaryOp(Identifier(b), +, Identifier(c)), +, Identifier(d)), +, Identifier(e))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_49():
    source = "void main() { a = b * c * d * e; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(BinaryOp(Identifier(b), *, Identifier(c)), *, Identifier(d)), *, Identifier(e))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_50():
    source = "void main() { a = (b + c + d) * e; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(BinaryOp(Identifier(b), +, Identifier(c)), +, Identifier(d)), *, Identifier(e))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_51():
    source = "void main() { a.b.c.d.e.f = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(MemberAccess(MemberAccess(MemberAccess(MemberAccess(Identifier(a).b).c).d).e).f) = IntLiteral(1)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_52():
    source = "void main() { for (i = 0; i < 2; i++) { if (a) while (b) x = x + 1; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(2)); PostfixOp(Identifier(i)++) do BlockStmt([IfStmt(if Identifier(a) then WhileStmt(while Identifier(b) do ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1))))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_53():
    source = "void main() { a = b + c * d * e + f; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(b), +, BinaryOp(BinaryOp(Identifier(c), *, Identifier(d)), *, Identifier(e))), +, Identifier(f))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_54():
    source = "void main() { a = (b + c) * (d + e) * f; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(BinaryOp(Identifier(b), +, Identifier(c)), *, BinaryOp(Identifier(d), +, Identifier(e))), *, Identifier(f))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_55():
    source = "void main() { a = b = c = d = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = AssignExpr(Identifier(c) = AssignExpr(Identifier(d) = IntLiteral(1))))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_56():
    source = "void main() { while (a) x = x + 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_57():
    source = "void main() { while (a) while (b) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do WhileStmt(while Identifier(b) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_58():
    source = "void main() { if (a) while (b) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then WhileStmt(while Identifier(b) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_59():
    source = "void main() { while (a) if (b) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do IfStmt(if Identifier(b) then ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_60():
    source = "void main() { for (i = 0; i < 3; i++) x = i; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(3)); PostfixOp(Identifier(i)++) do ExprStmt(AssignExpr(Identifier(x) = Identifier(i))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_61():
    source = "void main() { for (i = 0; i < 3; i++) while (a) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(3)); PostfixOp(Identifier(i)++) do WhileStmt(while Identifier(a) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_62():
    source = "void main() { for (i = 0; i < 3; i++) if (a) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(3)); PostfixOp(Identifier(i)++) do IfStmt(if Identifier(a) then ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_63():
    source = "void main() { ++a; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(++Identifier(a)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_64():
    source = "void main() { a++; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PostfixOp(Identifier(a)++))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_65():
    source = "void main() { ++a; ++b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(++Identifier(a))), ExprStmt(PrefixOp(++Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_66():
    source = "void main() { a++; b++; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PostfixOp(Identifier(a)++)), ExprStmt(PostfixOp(Identifier(b)++))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_67():
    source = "void main() { a = b + c + d + e + f; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(BinaryOp(BinaryOp(Identifier(b), +, Identifier(c)), +, Identifier(d)), +, Identifier(e)), +, Identifier(f))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_68():
    source = "void main() { a = b * c * d * e * f; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(BinaryOp(BinaryOp(Identifier(b), *, Identifier(c)), *, Identifier(d)), *, Identifier(e)), *, Identifier(f))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_69():
    source = "void main() { if (a) if (b) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then IfStmt(if Identifier(b) then ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_70():
    source = "void main() { while (a) while (b) while (c) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do WhileStmt(while Identifier(b) do WhileStmt(while Identifier(c) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_71():
    source = "void main() { for (i = 0; i < 2; i++) for (j = 0; j < 2; j++) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(2)); PostfixOp(Identifier(i)++) do ForStmt(for ExprStmt(AssignExpr(Identifier(j) = IntLiteral(0))); BinaryOp(Identifier(j), <, IntLiteral(2)); PostfixOp(Identifier(j)++) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_72():
    source = "void main() { a.b.c = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(MemberAccess(Identifier(a).b).c) = IntLiteral(1)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_73():
    source = "void main() { a.b.c.d = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(MemberAccess(MemberAccess(Identifier(a).b).c).d) = IntLiteral(1)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_74():
    source = "void main() { a = (b + c) * d + e; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(BinaryOp(Identifier(b), +, Identifier(c)), *, Identifier(d)), +, Identifier(e))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_75():
    source = "void main() { a = b + (c * d + e); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), +, BinaryOp(BinaryOp(Identifier(c), *, Identifier(d)), +, Identifier(e)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_76():
    source = "void main() { while (a) { x = 1; y = 2; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do BlockStmt([ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))), ExprStmt(AssignExpr(Identifier(y) = IntLiteral(2)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_77():
    source = "void main() { if (a) { x = 1; y = 2; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then BlockStmt([ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))), ExprStmt(AssignExpr(Identifier(y) = IntLiteral(2)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_78():
    source = "void main() { for (i = 0; i < 2; i++) { x = 1; y = 2; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(2)); PostfixOp(Identifier(i)++) do BlockStmt([ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))), ExprStmt(AssignExpr(Identifier(y) = IntLiteral(2)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_79():
    source = "void main() { a = (b + c + d) * (e + f); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(BinaryOp(Identifier(b), +, Identifier(c)), +, Identifier(d)), *, BinaryOp(Identifier(e), +, Identifier(f)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_80():
    source = "void main() { a = b * (c + d * e); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), *, BinaryOp(Identifier(c), +, BinaryOp(Identifier(d), *, Identifier(e))))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_81():
    source = "void main() { a = ((b)); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_82():
    source = "void main() { (((a)))++; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PostfixOp(Identifier(a)++))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_83():
    source = "void main() { a = b + c * d; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), +, BinaryOp(Identifier(c), *, Identifier(d)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_84():
    source = "void main() { a = (b + c) * d; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(b), +, Identifier(c)), *, Identifier(d))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_85():
    source = "void main() { a = b * c + d * e; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(b), *, Identifier(c)), +, BinaryOp(Identifier(d), *, Identifier(e)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_86():
    source = "void main() { a = b = c = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = AssignExpr(Identifier(c) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_87():
    source = "void main() { while (a) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_88():
    source = "void main() { if (a) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_89():
    source = "void main() { if (a) while (b) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then WhileStmt(while Identifier(b) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_90():
    source = "void main() { while (a) if (b) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(a) do IfStmt(if Identifier(b) then ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_91():
    source = "void main() { for (i = 0; i < 3; i++) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(3)); PostfixOp(Identifier(i)++) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_92():
    source = "void main() { for (i = 0; i < 3; i++) while (a) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(3)); PostfixOp(Identifier(i)++) do WhileStmt(while Identifier(a) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_93():
    source = "void main() { for (i = 0; i < 3; i++) if (a) x = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(3)); PostfixOp(Identifier(i)++) do IfStmt(if Identifier(a) then ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_94():
    source = "void main() { ++a; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(++Identifier(a)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_95():
    source = "void main() { a++; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PostfixOp(Identifier(a)++))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_96():
    source = "void main() { ++a; ++b; ++c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PrefixOp(++Identifier(a))), ExprStmt(PrefixOp(++Identifier(b))), ExprStmt(PrefixOp(++Identifier(c)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_97():
    source = "void main() { a++; b++; c++; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(PostfixOp(Identifier(a)++)), ExprStmt(PostfixOp(Identifier(b)++)), ExprStmt(PostfixOp(Identifier(c)++))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_98():
    source = "void main() { a.b = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(Identifier(a).b) = IntLiteral(1)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_99():
    source = "void main() { a.b.c = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(MemberAccess(Identifier(a).b).c) = IntLiteral(1)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_100():
    source = "void main() { a.b.c.d = 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(MemberAccess(MemberAccess(Identifier(a).b).c).d) = IntLiteral(1)))])])"
    assert str(ASTGenerator(source).generate()) == expected