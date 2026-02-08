"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


# ========== Simple Test Cases (10 types) ==========
def test_empty_program():
    """1. Empty program"""
    assert Parser("").parse() == "success"


def test_program_with_only_main():
    """2. Program with only main function"""
    assert Parser("void main() {}").parse() == "success"


def test_struct_simple():
    """3. Struct declaration"""
    source = "struct Point { int x; int y; };"
    assert Parser(source).parse() == "success"


def test_function_no_params():
    """4. Function with no parameters"""
    source = "void greet() { printString(\"Hello\"); }"
    assert Parser(source).parse() == "success"


def test_var_decl_auto_with_init():
    """5. Variable declaration"""
    source = "void main() { auto x = 5; }"
    assert Parser(source).parse() == "success"


def test_if_simple():
    """6. If statement"""
    source = "void main() { if (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_while_simple():
    """7. While statement"""
    source = "void main() { while (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_for_simple():
    """8. For statement"""
    source = "void main() { for (auto i = 0; i < 10; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_switch_simple():
    """9. Switch statement"""
    source = "void main() { switch (1) { case 1: printInt(1); break; } }"
    assert Parser(source).parse() == "success"


def test_assignment_simple():
    """10. Assignment statement"""
    source = "void main() { int x; x = 5; }"
    assert Parser(source).parse() == "success"

def test_11():
    source = """
    struct Point { int x; int y; };
    void main() {}
    struct Rect { Point p1; Point p2; };
    """
    assert Parser(source).parse() == "success"

def test_12():
    source = "struct Empty {}; void main() {}"
    assert Parser(source).parse() == "success"

def test_13():
    source = """
    struct Data {
        int id;
        float value;
        string name;
        Data next;
    };
    void main() {}
    """
    assert Parser(source).parse() == "success"

def test_14():
    source = """
    int getInt() { return 1; }
    float getFloat() { return 1.0; }
    string getString() { return ""; }
    void main() {}
    """
    assert Parser(source).parse() == "success"

def test_15():
    source = """
    struct Box { int id; };
    Box getBox() { Box b; return b; }
    void main() {}
    """
    assert Parser(source).parse() == "success"

def test_16():
    source = """
    void process(int a, float b, string c) {}
    void main() { process(1, 2.0, "s"); }
    """
    assert Parser(source).parse() == "success"

def test_17():
    source = """
    struct Point { int x; };
    void draw(Point p) {}
    void main() {}
    """
    assert Parser(source).parse() == "success"

def test_18():
    source = """
    void main() {
        int i = 0;
        float f = 1.5;
        string s = "hello";
    }
    """
    assert Parser(source).parse() == "success"

def test_19():
    source = """
    void main() {
        int i;
        float f;
        string s;
    }
    """
    assert Parser(source).parse() == "success"

def test_20():
    source = """
    struct Point { int x; int y; };
    void main() {
        Point p = {1, 2};
    }
    """
    assert Parser(source).parse() == "success"

def test_21():
    source = """
    struct P { int x; };
    struct L { P a; P b; };
    void main() {
        L line = {{1}, {2}};
    }
    """
    assert Parser(source).parse() == "success"

def test_22():
    source = "void main() { auto x = 1 + 2 * 3; }"
    assert Parser(source).parse() == "success"

def test_23():
    source = "void main() { auto x = 1 + 2 * 3 - 4 / 2; }"
    assert Parser(source).parse() == "success"

def test_24():
    source = "void main() { auto x = (1 + 2) * (3 - 4); }"
    assert Parser(source).parse() == "success"

def test_25():
    source = "void main() { auto x = 1 < 2 && 3 >= 4 || 5 == 6; }"
    assert Parser(source).parse() == "success"

def test_26():
    source = "void main() { auto x = -1; auto y = !x; auto z = +2; }"
    assert Parser(source).parse() == "success"

def test_27():
    source = "void main() { int x; ++x; --x; }"
    assert Parser(source).parse() == "success"

def test_28():
    source = "void main() { int x; x++; x--; }"
    assert Parser(source).parse() == "success"

def test_29():
    source = """
    struct P { int x; };
    void main() { P p; p.x = 1; auto y = p.x; }
    """
    assert Parser(source).parse() == "success"

def test_30():
    source = """
    struct A { int x; };
    struct B { A a; };
    void main() { B b; auto val = b.a.x; }
    """
    assert Parser(source).parse() == "success"

def test_31():
    source = "void f() {} void main() { f(); }"
    assert Parser(source).parse() == "success"

def test_32():
    source = "void f(int a, int b) {} void main() { f(1, 2); }"
    assert Parser(source).parse() == "success"

def test_33():
    source = "int f(int x) { return x; } void main() { f(f(1)); }"
    assert Parser(source).parse() == "success"

def test_34():
    source = """
    struct P { int x; };
    void f(P p) {}
    void main() { f({1}); }
    """
    assert Parser(source).parse() == "success"

def test_35():
    source = "void main() { float f = 1.2e-3; float g = .5E2; }"
    assert Parser(source).parse() == "success"

def test_36():
    source = "void main() { int a; int b; a = b = 5; }"
    assert Parser(source).parse() == "success"

def test_37():
    source = "void main() { { int x; { int y; } } }"
    assert Parser(source).parse() == "success"

def test_38():
    source = "void main() { if (1) {} else {} }"
    assert Parser(source).parse() == "success"

def test_39():
    source = "void main() { if (1) if (2) {} else {} else {} }"
    assert Parser(source).parse() == "success"

def test_40():
    source = "void main() { while (1 && (2 || 3)) {} }"
    assert Parser(source).parse() == "success"

def test_41():
    source = "void main() { int i; for (; i < 10; i++) {} }"
    assert Parser(source).parse() == "success"

def test_42():
    source = "void main() { for (int i=0; ; i++) break; }"
    assert Parser(source).parse() == "success"

def test_43():
    source = "void main() { for (int i=0; i < 10; ) {} }"
    assert Parser(source).parse() == "success"

def test_44():
    source = "void main() { for (;;) {} }"
    assert Parser(source).parse() == "success"

def test_45():
    source = "void main() { int i; for (i = 0; i < 10; i++) {} }"
    assert Parser(source).parse() == "success"

def test_46():
    source = "void main() { int i; for (i = 0; i < 10; i = i + 1) {} }"
    assert Parser(source).parse() == "success"

def test_47():
    source = """
    void main() {
        switch(1) {
            case 1: break;
            case 2: return;
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_48():
    source = "void main() { switch(1) { default: break; } }"
    assert Parser(source).parse() == "success"

def test_49():
    source = """
    void main() {
        switch(1) {
            case 1: break;
            default: break;
            case 2: break;
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_50():
    source = "void main() { switch(1) {} }"
    assert Parser(source).parse() == "success"

def test_51():
    source = "void main() { switch(1+2) { case 3*4: break; } }"
    assert Parser(source).parse() == "success"

def test_52():
    source = "void main() { while(1) { if(1) break; else continue; } }"
    assert Parser(source).parse() == "success"

def test_53():
    source = "void main() { return; }"
    assert Parser(source).parse() == "success"

def test_54():
    source = "int main() { return 1 + 2; }"
    assert Parser(source).parse() == "success"

def test_55():
    source = """
    struct S { int x; };
    S getS() { S s; return s; }
    void main() { getS().x; }
    """
    assert Parser(source).parse() == "success"

def test_56():
    source = "void main() { auto x = a.b++ + c; }"
    assert Parser(source).parse() == "success"

def test_57():
    source = "void main() { auto x = -a * b + c; }"
    assert Parser(source).parse() == "success"

def test_58():
    source = "void main() { auto x = a < b == c > d; }"
    assert Parser(source).parse() == "success"

def test_59():
    source = """
    struct S { int x; };
    void main() { S s; s.x = 10; }
    """
    assert Parser(source).parse() == "success"

def test_60():
    source = "void main() { int a; int b = (a = 5) + 2; }"
    assert Parser(source).parse() == "success"

def test_61():
    source = """
    // This is a comment
    void main() {} // Another comment
    """
    assert Parser(source).parse() == "success"

def test_62():
    source = """
    /* Comment */
    void main() { /* Inline */ }
    """
    assert Parser(source).parse() == "success"

def test_63():
    source = "int global = 1; void main() {}"
    assert "Error" in Parser(source).parse()

def test_64():
    source = "void main() { void x; }"
    assert "Error" in Parser(source).parse()

def test_65():
    source = "void f(){} void main() { f() = 1; }"
    assert "Error" in Parser(source).parse()

def test_66():
    source = "void main() { int a; ++a = 1; }"
    assert "Error" in Parser(source).parse()

def test_67():
    source = "struct A { struct B {}; }; void main() {}"
    assert "Error" in Parser(source).parse()

def test_68():
    source = "void main() { switch(1) { default: break; default: break; } }"
    assert "Error" in Parser(source).parse()

def test_69():
    source = "void main() { for(;;1+1) {} }"
    assert "Error" in Parser(source).parse()

def test_70():
    source = """
    struct A { int x; };
    void main() { A a = { 1 + 2 }; }
    """
    assert Parser(source).parse() == "success"

def test_71():
    source = "void f() { f(); } void main() {}"
    assert Parser(source).parse() == "success"

def test_72():
    source = "struct Node { int val; Node next; }; void main() {}"
    assert Parser(source).parse() == "success"

def test_73():
    source = "void main() { ; }"
    assert "Error" in Parser(source).parse()

def test_74():
    source = "void main() { int x; { float x; } }"
    assert Parser(source).parse() == "success"

def test_75():
    source = "void main() { float f = 1E10; }"
    assert Parser(source).parse() == "success"

def test_76():
    source = r'void main() { string s = "Line\nTab\tQuote\""; }'
    assert Parser(source).parse() == "success"

def test_77():
    source = "void f(int) {} void main() {}"
    assert "Error" in Parser(source).parse()

def test_78():
    source = "void main() { int x }"
    assert "Error" in Parser(source).parse()

def test_79():
    source = "struct A { int x }"
    assert "Error" in Parser(source).parse()

def test_80():
    source = "void main() { "
    assert "Error" in Parser(source).parse()

def test_81():
    source = "void main() { for(;;) { while(1) break; } }"
    assert Parser(source).parse() == "success"

def test_82():
    source = "void main() { switch(1) { case 1: switch(2) { default: break; } } }"
    assert Parser(source).parse() == "success"

def test_83():
    source = "void main() {} struct A {};"
    assert Parser(source).parse() == "success"

def test_84():
    source = """
    struct A { int x; };
    void main() { A a; auto b = a; }
    """
    assert Parser(source).parse() == "success"

def test_85():
    source = "void main() { int x = 1 ? 2 : 3; }"
    assert "Error" in Parser(source).parse()

def test_86():
    source = "void main() { int a[10]; }"
    assert "Error" in Parser(source).parse()

def test_87():
    source = "void main() { int* p; }"
    assert "Error" in Parser(source).parse()

def test_88():
    source = "void main() { switch(1) { case -1: break; } }"
    assert Parser(source).parse() == "success"

def test_89():
    source = "void main() { switch(1) { case (1): break; } }"
    assert Parser(source).parse() == "success"

def test_90():
    source = "void main ( ) { }"
    assert Parser(source).parse() == "success"

def test_91():
    source = "void main() { for(;;i--) {} }"
    assert Parser(source).parse() == "success"

def test_92():
    source = "void main() { for(;;++i) {} }"
    assert Parser(source).parse() == "success"

def test_93():
    source = """
    struct A { int x; };
    void main() { A a; a . x = 1; }
    """
    assert Parser(source).parse() == "success"

def test_94():
    source = """
    struct P { int x; };
    struct R { P p; };
    R getR() { R r; return r; }
    void main() { getR().p.x = 1; }
    """
    assert Parser(source).parse() == "success"

def test_95():
    source = "int f() { int x; return x = 1; }"
    assert Parser(source).parse() == "success"

def test_96():
    source = "void main() { while(1) {} }"
    assert Parser(source).parse() == "success"

def test_97():
    source = "void main() { if(1) return; }"
    assert Parser(source).parse() == "success"

def test_98():
    source = "void main() { if(1) return; else return; }"
    assert Parser(source).parse() == "success"

def test_99():
    source = """
    struct Node { int val; Node next; };
    Node create() { Node n; return n; }
    void main() {
        auto head = create();
        for (auto curr = head; curr.next != head; curr = curr.next) {
            if (curr.val > 10) break;
            else continue;
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_100():
    source = "void main() {} junk"
    assert "Error" in Parser(source).parse()