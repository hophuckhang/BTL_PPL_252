"""
Test cases for TyC Static Semantic Checker

This module contains test cases for the static semantic checker.
100 test cases covering all error types and comprehensive scenarios.
"""

from tests.utils import Checker
from src.utils.nodes import (
    Program,
    FuncDecl,
    BlockStmt,
    VarDecl,
    AssignExpr,
    ExprStmt,
    IntType,
    FloatType,
    StringType,
    VoidType,
    StructType,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    Identifier,
    BinaryOp,
    MemberAccess,
    FuncCall,
    StructDecl,
    MemberDecl,
    Param,
    ReturnStmt,
)


# ============================================================================
# Valid Programs (test_001 - test_010)
# ============================================================================


def test_001():
    """Test a valid program that should pass all checks"""
    source = """
void main() {
    int x = 5;
    int y = x + 1;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_002():
    """Test valid program with auto type inference"""
    source = """
void main() {
    auto x = 10;
    auto y = 3.14;
    auto z = x + y;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_003():
    """Test valid program with functions"""
    source = """
int add(int x, int y) {
    return x + y;
}
void main() {
    int sum = add(5, 3);
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_004():
    """Test valid program with struct"""
    source = """
struct Point {
    int x;
    int y;
};
void main() {
    Point p;
    p.x = 10;
    p.y = 20;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_005():
    """Test valid program with nested blocks"""
    source = """
void main() {
    int x = 10;
    {
        int y = 20;
        int z = x + y;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_006():
    source = """
void main() {
    for (int i = 0; i < 10; ++i) {
        break;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_007():
    source = """
void main() {
    while (1) {
        continue;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_008():
    source = """
void main() {
    switch (1) {
        default: break;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_009():
    source = """
get_val() {
    return 10;
}
void main() {
    int x = get_val();
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_010():
    source = """
struct A { 
    int x; 
};
void main() {
    A a = {1};
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_011():
    source = """
void main() {
    int x;
    int x;
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_012():
    source = """
struct A {};
struct A {};
void main() {}
"""
    expected = "Redeclared(Struct, A)"
    assert Checker(source).check_from_source() == expected

def test_013():
    source = """
void f() {}
void f() {}
void main() {}
"""
    expected = "Redeclared(Function, f)"
    assert Checker(source).check_from_source() == expected

def test_014():
    source = """
void f(int x, int x) {}
void main() {}
"""
    expected = "Redeclared(Parameter, x)"
    assert Checker(source).check_from_source() == expected

def test_015():
    source = """
struct A {
    int x;
    float x;
};
void main() {}
"""
    expected = "Redeclared(Member, x)"
    assert Checker(source).check_from_source() == expected

def test_016():
    source = """
void f(int x) {
    int x;
}
void main() {}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_017():
    source = """
void f(int x) {
    {
        int x;
    }
}
void main() {}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_018():
    source = """
void f() {
    int x;
    int x;
}
void main() {}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_019():
    source = """
void f() {
    auto x = 1;
    auto x = 2;
}
void main() {}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_020():
    source = """
struct A {
    int x;
};
struct A {
    int y;
};
void main() {}
"""
    expected = "Redeclared(Struct, A)"
    assert Checker(source).check_from_source() == expected

def test_021():
    source = """
void main() {
    x = 1;
}
"""
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected

def test_022():
    source = """
void main() {
    int y = x;
}
"""
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected

def test_023():
    source = """
void main() {
    int x = 1;
    {
        int y = x;
    }
    z = y;
}
"""
    expected = "UndeclaredIdentifier(z)"
    assert Checker(source).check_from_source() == expected

def test_024():
    source = """
void main() {
    x++;
}
"""
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected

def test_025():
    source = """
void main() {
    if (x) {}
}
"""
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected

def test_026():
    source = """
void main() {
    while (x) {}
}
"""
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected

def test_027():
    source = """
void main() {
    for (x = 1; ;) {}
}
"""
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected

def test_028():
    source = """
void main() {
    switch (x) {}
}
"""
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected

def test_029():
    source = """
void main() {
    printInt(x);
}
"""
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected

def test_030():
    source = """
void main() {
    return x;
}
"""
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected

def test_031():
    source = """
void main() {
    g();
}
"""
    expected = "UndeclaredFunction(g)"
    assert Checker(source).check_from_source() == expected

def test_032():
    source = """
void main() {
    int x = g();
}
"""
    expected = "UndeclaredFunction(g)"
    assert Checker(source).check_from_source() == expected

def test_033():
    source = """
void main() {
    if (g()) {}
}
"""
    expected = "UndeclaredFunction(g)"
    assert Checker(source).check_from_source() == expected

def test_034():
    source = """
void main() {
    while (g()) {}
}
"""
    expected = "UndeclaredFunction(g)"
    assert Checker(source).check_from_source() == expected

def test_035():
    source = """
void main() {
    for (; g(); ) {}
}
"""
    expected = "UndeclaredFunction(g)"
    assert Checker(source).check_from_source() == expected

def test_036():
    source = """
void main() {
    switch (g()) {}
}
"""
    expected = "UndeclaredFunction(g)"
    assert Checker(source).check_from_source() == expected

def test_037():
    source = """
void main() {
    g(1);
}
"""
    expected = "UndeclaredFunction(g)"
    assert Checker(source).check_from_source() == expected

def test_038():
    source = """
void main() {
    return g();
}
"""
    expected = "UndeclaredFunction(g)"
    assert Checker(source).check_from_source() == expected

def test_039():
    source = """
void main() {
    printInt(g());
}
"""
    expected = "UndeclaredFunction(g)"
    assert Checker(source).check_from_source() == expected

def test_040():
    source = """
void main() {
    g() + 1;
}
"""
    expected = "UndeclaredFunction(g)"
    assert Checker(source).check_from_source() == expected

def test_041():
    source = """
void main() {
    A x;
}
"""
    expected = "UndeclaredStruct(A)"
    assert Checker(source).check_from_source() == expected

def test_042():
    source = """
void f(A x) {}
void main() {}
"""
    expected = "UndeclaredStruct(A)"
    assert Checker(source).check_from_source() == expected

def test_043():
    source = """
A f() {}
void main() {}
"""
    expected = "UndeclaredStruct(A)"
    assert Checker(source).check_from_source() == expected

def test_044():
    source = """
struct B {
    A x;
};
void main() {}
"""
    expected = "UndeclaredStruct(A)"
    assert Checker(source).check_from_source() == expected

def test_045():
    source = """
void main() {
    A x = {1};
}
"""
    expected = "UndeclaredStruct(A)"
    assert Checker(source).check_from_source() == expected

def test_046():
    source = """
struct B {
    int x;
};
void main() {
    C x;
}
"""
    expected = "UndeclaredStruct(C)"
    assert Checker(source).check_from_source() == expected

def test_047():
    source = """
void f(int x, B y) {}
void main() {}
"""
    expected = "UndeclaredStruct(B)"
    assert Checker(source).check_from_source() == expected

def test_048():
    source = """
struct B {
    int a;
    C b;
};
void main() {}
"""
    expected = "UndeclaredStruct(C)"
    assert Checker(source).check_from_source() == expected

def test_049():
    source = """
void main() {
    int x;
    A y;
}
"""
    expected = "UndeclaredStruct(A)"
    assert Checker(source).check_from_source() == expected

def test_050():
    source = """
A main() {}
"""
    expected = "UndeclaredStruct(A)"
    assert Checker(source).check_from_source() == expected

def test_051():
    source = """
void main() {
    auto x;
    auto y;
    x = y;
}
"""
    expected = "TypeCannotBeInferred(x)"
    assert Checker(source).check_from_source() == expected

def test_052():
    source = """
void main() {
    auto x;
    auto y;
    x + y;
}
"""
    expected = "TypeCannotBeInferred(x)"
    assert Checker(source).check_from_source() == expected

def test_053():
    source = """
void main() {
    auto x;
    return x;
}
"""
    expected = "TypeCannotBeInferred(x)"
    assert Checker(source).check_from_source() == expected

def test_054():
    source = """
void main() {
    auto x;
    x = {};
}
"""
    expected = "TypeCannotBeInferred(x)"
    assert Checker(source).check_from_source() == expected

def test_055():
    source = """
void main() {
    auto x;
    x.y;
}
"""
    expected = "TypeCannotBeInferred(x)"
    assert Checker(source).check_from_source() == expected

def test_056():
    source = """
void main() {
    auto x = {};
}
"""
    expected = "TypeCannotBeInferred(x)"
    assert Checker(source).check_from_source() == expected

def test_057():
    source = """
void main() {
    auto x;
    printInt(x + x);
}
"""
    expected = "TypeCannotBeInferred(x)"
    assert Checker(source).check_from_source() == expected

def test_058():
    source = """
void main() {
    auto x;
    x == x;
}
"""
    expected = "TypeCannotBeInferred(x)"
    assert Checker(source).check_from_source() == expected

def test_059():
    source = """
f() {
    auto x;
    return x;
}
void main() {}
"""
    expected = "TypeCannotBeInferred(x)"
    assert Checker(source).check_from_source() == expected

def test_060():
    source = """
void main() {
    auto x;
    auto y = x;
}
"""
    expected = "TypeCannotBeInferred(y)"
    assert Checker(source).check_from_source() == expected

def test_061():
    source = """
void main() {
    if ("a") {}
}
"""
    expected = "TypeMismatchInStatement(IfStmt(if StringLiteral('a') then BlockStmt([])))"
    assert Checker(source).check_from_source() == expected

def test_062():
    source = """
void main() {
    while (1.5) {}
}
"""
    expected = "TypeMismatchInStatement(WhileStmt(while FloatLiteral(1.5) do BlockStmt([])))"
    assert Checker(source).check_from_source() == expected

def test_063():
    source = """
void main() {
    for (; "a"; ) {}
}
"""
    expected = "TypeMismatchInStatement(ForStmt(for None; StringLiteral('a'); None do BlockStmt([])))"
    assert Checker(source).check_from_source() == expected

def test_064():
    source = """
void main() {
    switch (1.5) {}
}
"""
    expected = "TypeMismatchInStatement(SwitchStmt(switch FloatLiteral(1.5) cases []))"
    assert Checker(source).check_from_source() == expected

def test_065():
    source = """
void main() {
    switch (1) {
        case 1.5: {}
    }
}
"""
    expected = "TypeMismatchInStatement(CaseStmt(case FloatLiteral(1.5): [BlockStmt([])]))"
    assert Checker(source).check_from_source() == expected

def test_066():
    source = """
void main() {
    int x = "a";
}
"""
    expected = "TypeMismatchInStatement(VarDecl(IntType(), x = StringLiteral('a')))"
    assert Checker(source).check_from_source() == expected

def test_067():
    source = """
void main() {
    float x = "a";
}
"""
    expected = "TypeMismatchInStatement(VarDecl(FloatType(), x = StringLiteral('a')))"
    assert Checker(source).check_from_source() == expected

def test_068():
    source = """
void main() {
    string x = 1;
}
"""
    expected = "TypeMismatchInStatement(VarDecl(StringType(), x = IntLiteral(1)))"
    assert Checker(source).check_from_source() == expected

def test_069():
    source = """
void main() {
    int x;
    x = "a";
}
"""
    expected = "TypeMismatchInStatement(ExprStmt(AssignExpr(Identifier(x) = StringLiteral('a'))))"
    assert Checker(source).check_from_source() == expected

def test_070():
    source = """
int f() {
    return "a";
}
void main() {}
"""
    expected = "TypeMismatchInStatement(ReturnStmt(return StringLiteral('a')))"
    assert Checker(source).check_from_source() == expected

def test_071():
    source = """
void main() {
    return 1;
}
"""
    expected = "TypeMismatchInStatement(ReturnStmt(return IntLiteral(1)))"
    assert Checker(source).check_from_source() == expected

def test_072():
    source = """
int f() {
    return;
}
void main() {}
"""
    expected = "TypeMismatchInStatement(ReturnStmt(return))"
    assert Checker(source).check_from_source() == expected

def test_073():
    source = """
struct A {
    int x;
};
void main() {
    A a;
    a = 1;
}
"""
    expected = "TypeMismatchInStatement(ExprStmt(AssignExpr(Identifier(a) = IntLiteral(1))))"
    assert Checker(source).check_from_source() == expected

def test_074():
    source = """
struct A {
    int x;
};
void main() {
    int a;
    a = {1};
}
"""
    expected = "TypeMismatchInStatement(ExprStmt(AssignExpr(Identifier(a) = StructLiteral({IntLiteral(1)}))))"
    assert Checker(source).check_from_source() == expected

def test_075():
    source = """
void main() {
    int x;
    float y;
    x = y;
}
"""
    expected = "TypeMismatchInStatement(ExprStmt(AssignExpr(Identifier(x) = Identifier(y))))"
    assert Checker(source).check_from_source() == expected

def test_076():
    source = """
void main() {
    1 + "a";
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(IntLiteral(1), +, StringLiteral('a')))"
    assert Checker(source).check_from_source() == expected

def test_077():
    source = """
void main() {
    1 - "a";
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(IntLiteral(1), -, StringLiteral('a')))"
    assert Checker(source).check_from_source() == expected

def test_078():
    source = """
void main() {
    1 * "a";
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(IntLiteral(1), *, StringLiteral('a')))"
    assert Checker(source).check_from_source() == expected

def test_079():
    source = """
void main() {
    1 / "a";
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(IntLiteral(1), /, StringLiteral('a')))"
    assert Checker(source).check_from_source() == expected

def test_080():
    source = """
void main() {
    1.5 % 2;
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(FloatLiteral(1.5), %, IntLiteral(2)))"
    assert Checker(source).check_from_source() == expected

def test_081():
    source = """
void main() {
    1 < "a";
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(IntLiteral(1), <, StringLiteral('a')))"
    assert Checker(source).check_from_source() == expected

def test_082():
    source = """
void main() {
    1.5 && 1;
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(FloatLiteral(1.5), &&, IntLiteral(1)))"
    assert Checker(source).check_from_source() == expected

def test_083():
    source = """
void main() {
    !1.5;
}
"""
    expected = "TypeMismatchInExpression(PrefixOp(!FloatLiteral(1.5)))"
    assert Checker(source).check_from_source() == expected

def test_084():
    source = """
void main() {
    float x = 1.5;
    ++x;
}
"""
    expected = "TypeMismatchInExpression(PrefixOp(++Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_085():
    source = """
void main() {
    float x = 1.5;
    x++;
}
"""
    expected = "TypeMismatchInExpression(PostfixOp(Identifier(x)++))"
    assert Checker(source).check_from_source() == expected

def test_086():
    source = """
void main() {
    ++1;
}
"""
    expected = "TypeMismatchInExpression(PrefixOp(++IntLiteral(1)))"
    assert Checker(source).check_from_source() == expected

def test_087():
    source = """
void main() {
    printInt(1.5);
}
"""
    expected = "TypeMismatchInExpression(FuncCall(printInt, [FloatLiteral(1.5)]))"
    assert Checker(source).check_from_source() == expected

def test_088():
    source = """
void main() {
    printInt(1, 2);
}
"""
    expected = "TypeMismatchInExpression(FuncCall(printInt, [IntLiteral(1), IntLiteral(2)]))"
    assert Checker(source).check_from_source() == expected

def test_089():
    source = """
struct A {
    int x;
};
void main() {
    A a;
    a.y;
}
"""
    expected = "TypeMismatchInExpression(MemberAccess(Identifier(a).y))"
    assert Checker(source).check_from_source() == expected

def test_090():
    source = """
void main() {
    int x;
    x.y;
}
"""
    expected = "TypeMismatchInExpression(MemberAccess(Identifier(x).y))"
    assert Checker(source).check_from_source() == expected

def test_091():
    source = """
void main() {
    break;
}
"""
    expected = "MustInLoop(BreakStmt())"
    assert Checker(source).check_from_source() == expected

def test_092():
    source = """
void main() {
    continue;
}
"""
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected

def test_093():
    source = """
void main() {
    if (1) {
        break;
    }
}
"""
    expected = "MustInLoop(BreakStmt())"
    assert Checker(source).check_from_source() == expected

def test_094():
    source = """
void main() {
    if (1) {
        continue;
    }
}
"""
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected

def test_095():
    source = """
void main() {
    switch (1) {
        case 1:
            continue;
    }
}
"""
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected

def test_096():
    source = """
void main() {
    {
        break;
    }
}
"""
    expected = "MustInLoop(BreakStmt())"
    assert Checker(source).check_from_source() == expected

def test_097():
    source = """
void main() {
    {
        continue;
    }
}
"""
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected

def test_098():
    source = """
int f() {
    break;
    return 1;
}
void main() {}
"""
    expected = "MustInLoop(BreakStmt())"
    assert Checker(source).check_from_source() == expected

def test_099():
    source = """
int f() {
    continue;
    return 1;
}
void main() {}
"""
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected

def test_100():
    source = """
void main() {
    switch (1) {
        default:
            continue;
    }
}
"""
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected