"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer


# ========== Simple Test Cases (10 types) ==========
def test_keyword_auto():
    """1. Keyword"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"


def test_operator_assign():
    """2. Operator"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"


def test_separator_semi():
    """3. Separator"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"


def test_integer_single_digit():
    """4. Integer literal"""
    tokenizer = Tokenizer("5")
    assert tokenizer.get_tokens_as_string() == "5,<EOF>"


def test_float_decimal():
    """5. Float literal"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"


def test_string_simple():
    """6. String literal"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"


def test_identifier_simple():
    """7. Identifier"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"


def test_line_comment():
    """8. Line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_integer_in_expression():
    """9. Mixed: integers and operator"""
    tokenizer = Tokenizer("5+10")
    assert tokenizer.get_tokens_as_string() == "5,+,10,<EOF>"


def test_complex_expression():
    """10. Complex: variable declaration"""
    tokenizer = Tokenizer("auto x = 5 + 3 * 2;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,+,3,*,2,;,<EOF>"

def test_11():
    tokenizer = Tokenizer("break")
    assert tokenizer.get_tokens_as_string() == "break,<EOF>"

def test_12():
    tokenizer = Tokenizer("case")
    assert tokenizer.get_tokens_as_string() == "case,<EOF>"

def test_13():
    tokenizer = Tokenizer("continue")
    assert tokenizer.get_tokens_as_string() == "continue,<EOF>"

def test_14():
    tokenizer = Tokenizer("default")
    assert tokenizer.get_tokens_as_string() == "default,<EOF>"

def test_15():
    tokenizer = Tokenizer("else")
    assert tokenizer.get_tokens_as_string() == "else,<EOF>"

def test_16():
    tokenizer = Tokenizer("float")
    assert tokenizer.get_tokens_as_string() == "float,<EOF>"

def test_17():
    tokenizer = Tokenizer("for")
    assert tokenizer.get_tokens_as_string() == "for,<EOF>"

def test_18():
    tokenizer = Tokenizer("if")
    assert tokenizer.get_tokens_as_string() == "if,<EOF>"

def test_19():
    tokenizer = Tokenizer("int")
    assert tokenizer.get_tokens_as_string() == "int,<EOF>"

def test_20():
    tokenizer = Tokenizer("return")
    assert tokenizer.get_tokens_as_string() == "return,<EOF>"

def test_21():
    tokenizer = Tokenizer("string")
    assert tokenizer.get_tokens_as_string() == "string,<EOF>"

def test_22():
    tokenizer = Tokenizer("struct")
    assert tokenizer.get_tokens_as_string() == "struct,<EOF>"

def test_23():
    tokenizer = Tokenizer("switch")
    assert tokenizer.get_tokens_as_string() == "switch,<EOF>"

def test_24():
    tokenizer = Tokenizer("void")
    assert tokenizer.get_tokens_as_string() == "void,<EOF>"

def test_25():
    tokenizer = Tokenizer("while")
    assert tokenizer.get_tokens_as_string() == "while,<EOF>"

def test_26():
    tokenizer = Tokenizer("-")
    assert tokenizer.get_tokens_as_string() == "-,<EOF>"

def test_27():
    tokenizer = Tokenizer("*")
    assert tokenizer.get_tokens_as_string() == "*,<EOF>"

def test_28():
    tokenizer = Tokenizer("/")
    assert tokenizer.get_tokens_as_string() == "/,<EOF>"

def test_29():
    tokenizer = Tokenizer("%")
    assert tokenizer.get_tokens_as_string() == "%,<EOF>"

def test_30():
    tokenizer = Tokenizer("==")
    assert tokenizer.get_tokens_as_string() == "==,<EOF>"

def test_31():
    tokenizer = Tokenizer("!=")
    assert tokenizer.get_tokens_as_string() == "!=,<EOF>"

def test_32():
    tokenizer = Tokenizer("<")
    assert tokenizer.get_tokens_as_string() == "<,<EOF>"

def test_33():
    tokenizer = Tokenizer(">")
    assert tokenizer.get_tokens_as_string() == ">,<EOF>"

def test_34():
    tokenizer = Tokenizer("<=")
    assert tokenizer.get_tokens_as_string() == "<=,<EOF>"

def test_35():
    tokenizer = Tokenizer(">=")
    assert tokenizer.get_tokens_as_string() == ">=,<EOF>"

def test_36():
    tokenizer = Tokenizer("||")
    assert tokenizer.get_tokens_as_string() == "||,<EOF>"

def test_37():
    tokenizer = Tokenizer("&&")
    assert tokenizer.get_tokens_as_string() == "&&,<EOF>"

def test_38():
    tokenizer = Tokenizer("!")
    assert tokenizer.get_tokens_as_string() == "!,<EOF>"

def test_39():
    tokenizer = Tokenizer("++")
    assert tokenizer.get_tokens_as_string() == "++,<EOF>"

def test_40():
    tokenizer = Tokenizer("--")
    assert tokenizer.get_tokens_as_string() == "--,<EOF>"

def test_41():
    tokenizer = Tokenizer(".")
    assert tokenizer.get_tokens_as_string() == ".,<EOF>"

def test_42():
    tokenizer = Tokenizer("+")
    assert tokenizer.get_tokens_as_string() == "+,<EOF>"

def test_43():
    tokenizer = Tokenizer("{")
    assert tokenizer.get_tokens_as_string() == "{,<EOF>"

def test_44():
    tokenizer = Tokenizer("}")
    assert tokenizer.get_tokens_as_string() == "},<EOF>"

def test_45():
    tokenizer = Tokenizer("(")
    assert tokenizer.get_tokens_as_string() == "(,<EOF>"

def test_46():
    tokenizer = Tokenizer(")")
    assert tokenizer.get_tokens_as_string() == "),<EOF>"

def test_47():
    tokenizer = Tokenizer(",")
    assert tokenizer.get_tokens_as_string() == ",,<EOF>"

def test_48():
    tokenizer = Tokenizer(":")
    assert tokenizer.get_tokens_as_string() == ":,<EOF>"

def test_49():
    tokenizer = Tokenizer("{}(),:;")
    assert tokenizer.get_tokens_as_string() == "{,},(,),,,:,;,<EOF>"

def test_50():
    tokenizer = Tokenizer("_var")
    assert tokenizer.get_tokens_as_string() == "_var,<EOF>"

def test_51():
    tokenizer = Tokenizer("var_")
    assert tokenizer.get_tokens_as_string() == "var_,<EOF>"

def test_52():
    tokenizer = Tokenizer("MyVar")
    assert tokenizer.get_tokens_as_string() == "MyVar,<EOF>"

def test_53():
    tokenizer = Tokenizer("var123")
    assert tokenizer.get_tokens_as_string() == "var123,<EOF>"

def test_54():
    tokenizer = Tokenizer("MAX_VALUE")
    assert tokenizer.get_tokens_as_string() == "MAX_VALUE,<EOF>"

def test_55():
    tokenizer = Tokenizer("autoclass break_point")
    assert tokenizer.get_tokens_as_string() == "autoclass,break_point,<EOF>"

def test_56():
    tokenizer = Tokenizer("0")
    assert tokenizer.get_tokens_as_string() == "0,<EOF>"

def test_57():
    tokenizer = Tokenizer("2500")
    assert tokenizer.get_tokens_as_string() == "2500,<EOF>"

def test_58():
    tokenizer = Tokenizer("10 20 30")
    assert tokenizer.get_tokens_as_string() == "10,20,30,<EOF>"

def test_59():
    tokenizer = Tokenizer("255")
    assert tokenizer.get_tokens_as_string() == "255,<EOF>"

def test_60():
    tokenizer = Tokenizer("123456")
    assert tokenizer.get_tokens_as_string() == "123456,<EOF>"

def test_61():
    tokenizer = Tokenizer("0.0")
    assert tokenizer.get_tokens_as_string() == "0.0,<EOF>"

def test_62():
    tokenizer = Tokenizer("1.23e4")
    assert tokenizer.get_tokens_as_string() == "1.23e4,<EOF>"

def test_63():
    tokenizer = Tokenizer("5.67E-2")
    assert tokenizer.get_tokens_as_string() == "5.67E-2,<EOF>"

def test_64():
    tokenizer = Tokenizer("1.")
    assert tokenizer.get_tokens_as_string() == "1.,<EOF>"

def test_65():
    tokenizer = Tokenizer(".5")
    assert tokenizer.get_tokens_as_string() == ".5,<EOF>"

def test_66():
    tokenizer = Tokenizer("1e4")
    assert tokenizer.get_tokens_as_string() == "1e4,<EOF>"

def test_67():
    tokenizer = Tokenizer("2E-3")
    assert tokenizer.get_tokens_as_string() == "2E-3,<EOF>"

def test_68():
    tokenizer = Tokenizer("1.5e+2")
    assert tokenizer.get_tokens_as_string() == "1.5e+2,<EOF>"

def test_69():
    tokenizer = Tokenizer("0.")
    assert tokenizer.get_tokens_as_string() == "0.,<EOF>"

def test_70():
    tokenizer = Tokenizer(".5E10")
    assert tokenizer.get_tokens_as_string() == ".5E10,<EOF>"

def test_71():
    tokenizer = Tokenizer('""')
    assert tokenizer.get_tokens_as_string() == ",<EOF>"

def test_72():
    tokenizer = Tokenizer('" "')
    assert tokenizer.get_tokens_as_string() == " ,<EOF>"

def test_73():
    tokenizer = Tokenizer('"quote\\"here"')
    assert tokenizer.get_tokens_as_string() == 'quote\\"here,<EOF>'

def test_74():
    tokenizer = Tokenizer('"line\\n"')
    assert tokenizer.get_tokens_as_string() == "line\\n,<EOF>"

def test_75():
    tokenizer = Tokenizer('"tab\\t"')
    assert tokenizer.get_tokens_as_string() == "tab\\t,<EOF>"

def test_76():
    tokenizer = Tokenizer('"back\\b"')
    assert tokenizer.get_tokens_as_string() == "back\\b,<EOF>"

def test_77():
    tokenizer = Tokenizer('"path\\\\"')
    assert tokenizer.get_tokens_as_string() == "path\\\\,<EOF>"

def test_78():
    tokenizer = Tokenizer('"abc" "def"')
    assert tokenizer.get_tokens_as_string() == "abc,def,<EOF>"

def test_79():
    tokenizer = Tokenizer('"a-b_c 123"')
    assert tokenizer.get_tokens_as_string() == "a-b_c 123,<EOF>"

def test_80():
    tokenizer = Tokenizer('"page\\f"')
    assert tokenizer.get_tokens_as_string() == "page\\f,<EOF>"

def test_81():
    tokenizer = Tokenizer("/* comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_82():
    tokenizer = Tokenizer("/* line 1 \n line 2 */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_83():
    tokenizer = Tokenizer("/* // ignored */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_84():
    tokenizer = Tokenizer("// /* ignored")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_85():
    tokenizer = Tokenizer("a /* skip */ b // skip \n c")
    assert tokenizer.get_tokens_as_string() == "a,b,c,<EOF>"

def test_86():
    tokenizer = Tokenizer("a=b+c*d")
    assert tokenizer.get_tokens_as_string() == "a,=,b,+,c,*,d,<EOF>"

def test_87():
    tokenizer = Tokenizer("person.name")
    assert tokenizer.get_tokens_as_string() == "person,.,name,<EOF>"

def test_88():
    tokenizer = Tokenizer("p.x++")
    assert tokenizer.get_tokens_as_string() == "p,.,x,++,<EOF>"

def test_89():
    tokenizer = Tokenizer("add(1, 2)")
    assert tokenizer.get_tokens_as_string() == "add,(,1,,,2,),<EOF>"

def test_90():
    tokenizer = Tokenizer("1.x")
    assert tokenizer.get_tokens_as_string() == "1.,x,<EOF>"

def test_91():
    tokenizer = Tokenizer("i<10")
    assert tokenizer.get_tokens_as_string() == "i,<,10,<EOF>"

def test_92():
    tokenizer = Tokenizer("x==y")
    assert tokenizer.get_tokens_as_string() == "x,==,y,<EOF>"

def test_93():
    tokenizer = Tokenizer("-45")
    assert tokenizer.get_tokens_as_string() == "-,45,<EOF>"

def test_94():
    tokenizer = Tokenizer("-3.14")
    assert tokenizer.get_tokens_as_string() == "-,3.14,<EOF>"

def test_95():
    tokenizer = Tokenizer("struct Point { int x; };")
    assert tokenizer.get_tokens_as_string() == "struct,Point,{,int,x,;,},;,<EOF>"

def test_96():
    tokenizer = Tokenizer('"foo\\\\"')
    assert tokenizer.get_tokens_as_string() == "foo\\\\,<EOF>"

def test_97():
    tokenizer = Tokenizer("+ +")
    assert tokenizer.get_tokens_as_string() == "+,+,<EOF>"

def test_98():
    tokenizer = Tokenizer("i--")
    assert tokenizer.get_tokens_as_string() == "i,--,<EOF>"

def test_99():
    tokenizer = Tokenizer("integer")
    assert tokenizer.get_tokens_as_string() == "integer,<EOF>"

def test_100():
    tokenizer = Tokenizer("1.2e+5")
    assert tokenizer.get_tokens_as_string() == "1.2e+5,<EOF>"