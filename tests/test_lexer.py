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

    # ========== Keywords (Tests 11-25) ==========

def test_keyword_break():
    """11. Keyword: break"""
    tokenizer = Tokenizer("break")
    assert tokenizer.get_tokens_as_string() == "break,<EOF>"

def test_keyword_case():
    """12. Keyword: case"""
    tokenizer = Tokenizer("case")
    assert tokenizer.get_tokens_as_string() == "case,<EOF>"

def test_keyword_continue():
    """13. Keyword: continue"""
    tokenizer = Tokenizer("continue")
    assert tokenizer.get_tokens_as_string() == "continue,<EOF>"

def test_keyword_default():
    """14. Keyword: default"""
    tokenizer = Tokenizer("default")
    assert tokenizer.get_tokens_as_string() == "default,<EOF>"

def test_keyword_else():
    """15. Keyword: else"""
    tokenizer = Tokenizer("else")
    assert tokenizer.get_tokens_as_string() == "else,<EOF>"

def test_keyword_float():
    """16. Keyword: float"""
    tokenizer = Tokenizer("float")
    assert tokenizer.get_tokens_as_string() == "float,<EOF>"

def test_keyword_for():
    """17. Keyword: for"""
    tokenizer = Tokenizer("for")
    assert tokenizer.get_tokens_as_string() == "for,<EOF>"

def test_keyword_if():
    """18. Keyword: if"""
    tokenizer = Tokenizer("if")
    assert tokenizer.get_tokens_as_string() == "if,<EOF>"

def test_keyword_int():
    """19. Keyword: int"""
    tokenizer = Tokenizer("int")
    assert tokenizer.get_tokens_as_string() == "int,<EOF>"

def test_keyword_return():
    """20. Keyword: return"""
    tokenizer = Tokenizer("return")
    assert tokenizer.get_tokens_as_string() == "return,<EOF>"

def test_keyword_string():
    """21. Keyword: string"""
    tokenizer = Tokenizer("string")
    assert tokenizer.get_tokens_as_string() == "string,<EOF>"

def test_keyword_struct():
    """22. Keyword: struct"""
    tokenizer = Tokenizer("struct")
    assert tokenizer.get_tokens_as_string() == "struct,<EOF>"

def test_keyword_switch():
    """23. Keyword: switch"""
    tokenizer = Tokenizer("switch")
    assert tokenizer.get_tokens_as_string() == "switch,<EOF>"

def test_keyword_void():
    """24. Keyword: void"""
    tokenizer = Tokenizer("void")
    assert tokenizer.get_tokens_as_string() == "void,<EOF>"

def test_keyword_while():
    """25. Keyword: while"""
    tokenizer = Tokenizer("while")
    assert tokenizer.get_tokens_as_string() == "while,<EOF>"


# ========== Operators (Tests 26-42) ==========

def test_operator_minus():
    """26. Operator: -"""
    tokenizer = Tokenizer("-")
    assert tokenizer.get_tokens_as_string() == "-,<EOF>"

def test_operator_multiply():
    """27. Operator: *"""
    tokenizer = Tokenizer("*")
    assert tokenizer.get_tokens_as_string() == "*,<EOF>"

def test_operator_divide():
    """28. Operator: /"""
    tokenizer = Tokenizer("/")
    assert tokenizer.get_tokens_as_string() == "/,<EOF>"

def test_operator_modulus():
    """29. Operator: %"""
    tokenizer = Tokenizer("%")
    assert tokenizer.get_tokens_as_string() == "%,<EOF>"

def test_operator_equal_check():
    """30. Operator: =="""
    tokenizer = Tokenizer("==")
    assert tokenizer.get_tokens_as_string() == "==,<EOF>"

def test_operator_not_equal():
    """31. Operator: !="""
    tokenizer = Tokenizer("!=")
    assert tokenizer.get_tokens_as_string() == "!=,<EOF>"

def test_operator_less_than():
    """32. Operator: <"""
    tokenizer = Tokenizer("<")
    assert tokenizer.get_tokens_as_string() == "<,<EOF>"

def test_operator_greater_than():
    """33. Operator: >"""
    tokenizer = Tokenizer(">")
    assert tokenizer.get_tokens_as_string() == ">,<EOF>"

def test_operator_less_equal():
    """34. Operator: <="""
    tokenizer = Tokenizer("<=")
    assert tokenizer.get_tokens_as_string() == "<=,<EOF>"

def test_operator_greater_equal():
    """35. Operator: >="""
    tokenizer = Tokenizer(">=")
    assert tokenizer.get_tokens_as_string() == ">=,<EOF>"

def test_operator_logical_or():
    """36. Operator: ||"""
    tokenizer = Tokenizer("||")
    assert tokenizer.get_tokens_as_string() == "||,<EOF>"

def test_operator_logical_and():
    """37. Operator: &&"""
    tokenizer = Tokenizer("&&")
    assert tokenizer.get_tokens_as_string() == "&&,<EOF>"

def test_operator_logical_not():
    """38. Operator: !"""
    tokenizer = Tokenizer("!")
    assert tokenizer.get_tokens_as_string() == "!,<EOF>"

def test_operator_increment():
    """39. Operator: ++"""
    tokenizer = Tokenizer("++")
    assert tokenizer.get_tokens_as_string() == "++,<EOF>"

def test_operator_decrement():
    """40. Operator: --"""
    tokenizer = Tokenizer("--")
    assert tokenizer.get_tokens_as_string() == "--,<EOF>"

def test_operator_member_access():
    """41. Operator: ."""
    tokenizer = Tokenizer(".")
    assert tokenizer.get_tokens_as_string() == ".,<EOF>"

def test_operator_plus():
    """42. Operator: +"""
    tokenizer = Tokenizer("+")
    assert tokenizer.get_tokens_as_string() == "+,<EOF>"


# ========== Separators (Tests 43-49) ==========

def test_separator_lbrace():
    """43. Separator: {"""
    tokenizer = Tokenizer("{")
    assert tokenizer.get_tokens_as_string() == "{,<EOF>"

def test_separator_rbrace():
    """44. Separator: }"""
    tokenizer = Tokenizer("}")
    assert tokenizer.get_tokens_as_string() == "},<EOF>"

def test_separator_lparen():
    """45. Separator: ("""
    tokenizer = Tokenizer("(")
    assert tokenizer.get_tokens_as_string() == "(,<EOF>"

def test_separator_rparen():
    """46. Separator: )"""
    tokenizer = Tokenizer(")")
    assert tokenizer.get_tokens_as_string() == "),<EOF>"

def test_separator_comma():
    """47. Separator: ,"""
    tokenizer = Tokenizer(",")
    assert tokenizer.get_tokens_as_string() == ",,<EOF>"

def test_separator_colon():
    """48. Separator: :"""
    tokenizer = Tokenizer(":")
    assert tokenizer.get_tokens_as_string() == ":,<EOF>"

def test_all_separators():
    """49. All separators sequence"""
    tokenizer = Tokenizer("{}(),:;")
    assert tokenizer.get_tokens_as_string() == "{,},(,),,,:,;,<EOF>"


# ========== Identifiers (Tests 50-55) ==========

def test_identifier_underscore_start():
    """50. Identifier starting with underscore"""
    tokenizer = Tokenizer("_var")
    assert tokenizer.get_tokens_as_string() == "_var,<EOF>"

def test_identifier_underscore_end():
    """51. Identifier ending with underscore"""
    tokenizer = Tokenizer("var_")
    assert tokenizer.get_tokens_as_string() == "var_,<EOF>"

def test_identifier_mixed_case():
    """52. Identifier mixed case"""
    tokenizer = Tokenizer("MyVar")
    assert tokenizer.get_tokens_as_string() == "MyVar,<EOF>"

def test_identifier_with_digits():
    """53. Identifier with digits"""
    tokenizer = Tokenizer("var123")
    assert tokenizer.get_tokens_as_string() == "var123,<EOF>"

def test_identifier_all_caps():
    """54. Identifier all caps"""
    tokenizer = Tokenizer("MAX_VALUE")
    assert tokenizer.get_tokens_as_string() == "MAX_VALUE,<EOF>"

def test_identifier_keywords_prefix():
    """55. Identifiers that look like keywords but aren't"""
    tokenizer = Tokenizer("autoclass break_point")
    assert tokenizer.get_tokens_as_string() == "autoclass,break_point,<EOF>"


# ========== Integer Literals (Tests 56-60) ==========

def test_integer_zero():
    """56. Integer: 0"""
    tokenizer = Tokenizer("0")
    assert tokenizer.get_tokens_as_string() == "0,<EOF>"

def test_integer_large():
    """57. Integer: large number"""
    tokenizer = Tokenizer("2500")
    assert tokenizer.get_tokens_as_string() == "2500,<EOF>"

def test_integer_multiple():
    """58. Multiple integers separated by space"""
    tokenizer = Tokenizer("10 20 30")
    assert tokenizer.get_tokens_as_string() == "10,20,30,<EOF>"

def test_integer_max_byte():
    """59. Integer: 255"""
    tokenizer = Tokenizer("255")
    assert tokenizer.get_tokens_as_string() == "255,<EOF>"

def test_integer_sequence():
    """60. Integers without space (logic check)"""
    # Note: 123456 is one token
    tokenizer = Tokenizer("123456")
    assert tokenizer.get_tokens_as_string() == "123456,<EOF>"


# ========== Float Literals (Tests 61-70) ==========

def test_float_zero_dot_zero():
    """61. Float: 0.0"""
    tokenizer = Tokenizer("0.0")
    assert tokenizer.get_tokens_as_string() == "0.0,<EOF>"

def test_float_scientific():
    """62. Float: 1.23e4"""
    tokenizer = Tokenizer("1.23e4")
    assert tokenizer.get_tokens_as_string() == "1.23e4,<EOF>"

def test_float_scientific_negative_exponent():
    """63. Float: 5.67E-2"""
    tokenizer = Tokenizer("5.67E-2")
    assert tokenizer.get_tokens_as_string() == "5.67E-2,<EOF>"

def test_float_dot_at_end():
    """64. Float: 1."""
    tokenizer = Tokenizer("1.")
    assert tokenizer.get_tokens_as_string() == "1.,<EOF>"

def test_float_dot_at_start():
    """65. Float: .5"""
    tokenizer = Tokenizer(".5")
    assert tokenizer.get_tokens_as_string() == ".5,<EOF>"

def test_float_scientific_no_dot():
    """66. Float: 1e4"""
    tokenizer = Tokenizer("1e4")
    assert tokenizer.get_tokens_as_string() == "1e4,<EOF>"

def test_float_scientific_uppercase():
    """67. Float: 2E-3"""
    tokenizer = Tokenizer("2E-3")
    assert tokenizer.get_tokens_as_string() == "2E-3,<EOF>"

def test_float_scientific_plus_sign():
    """68. Float: 1.5e+2"""
    tokenizer = Tokenizer("1.5e+2")
    assert tokenizer.get_tokens_as_string() == "1.5e+2,<EOF>"

def test_float_zero_dot():
    """69. Float: 0."""
    tokenizer = Tokenizer("0.")
    assert tokenizer.get_tokens_as_string() == "0.,<EOF>"

def test_float_complex_scientific():
    """70. Float: .5E10"""
    tokenizer = Tokenizer(".5E10")
    assert tokenizer.get_tokens_as_string() == ".5E10,<EOF>"


# ========== String Literals (Tests 71-80) ==========
# Note: Spec says lexer strips double quotes from recognized string literals.

def test_string_empty():
    """71. String: empty"""
    tokenizer = Tokenizer('""')
    assert tokenizer.get_tokens_as_string() == ",<EOF>"

def test_string_space():
    """72. String: single space"""
    tokenizer = Tokenizer('" "')
    assert tokenizer.get_tokens_as_string() == " ,<EOF>"

def test_string_with_escaped_quote():
    """73. String: escaped quote"""
    # Input: "quote\"here" -> Content: quote\"here
    tokenizer = Tokenizer('"quote\\"here"')
    assert tokenizer.get_tokens_as_string() == 'quote\\"here,<EOF>'

def test_string_with_newline_escape():
    """74. String: escaped newline"""
    # Input: "line\n" (literal \n)
    tokenizer = Tokenizer('"line\\n"')
    assert tokenizer.get_tokens_as_string() == "line\\n,<EOF>"

def test_string_with_tab_escape():
    """75. String: escaped tab"""
    tokenizer = Tokenizer('"tab\\t"')
    assert tokenizer.get_tokens_as_string() == "tab\\t,<EOF>"

def test_string_with_backspace_escape():
    """76. String: escaped backspace"""
    tokenizer = Tokenizer('"back\\b"')
    assert tokenizer.get_tokens_as_string() == "back\\b,<EOF>"

def test_string_with_backslash_escape():
    """77. String: escaped backslash"""
    tokenizer = Tokenizer('"path\\\\"')
    assert tokenizer.get_tokens_as_string() == "path\\\\,<EOF>"

def test_string_multiple():
    """78. Multiple strings"""
    tokenizer = Tokenizer('"abc" "def"')
    assert tokenizer.get_tokens_as_string() == "abc,def,<EOF>"

def test_string_mixed_content():
    """79. String with alphanumeric and symbols"""
    tokenizer = Tokenizer('"a-b_c 123"')
    assert tokenizer.get_tokens_as_string() == "a-b_c 123,<EOF>"

def test_string_with_formfeed():
    """80. String with formfeed escape"""
    tokenizer = Tokenizer('"page\\f"')
    assert tokenizer.get_tokens_as_string() == "page\\f,<EOF>"


# ========== Comments (Tests 81-85) ==========

def test_block_comment_simple():
    """81. Block comment on one line"""
    tokenizer = Tokenizer("/* comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_block_comment_multiline():
    """82. Block comment spanning lines"""
    tokenizer = Tokenizer("/* line 1 \n line 2 */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_comment_mixed_block_ignores_line():
    """83. Block comment ignores line comment syntax"""
    tokenizer = Tokenizer("/* // ignored */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_comment_line_ignores_block():
    """84. Line comment ignores block start"""
    tokenizer = Tokenizer("// /* ignored")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_comment_between_code():
    """85. Comments between tokens"""
    tokenizer = Tokenizer("a /* skip */ b // skip \n c")
    assert tokenizer.get_tokens_as_string() == "a,b,c,<EOF>"


# ========== Complex Lexing & Edge Cases (Tests 86-100) ==========

def test_complex_tight_arithmetic():
    """86. Arithmetic without spaces"""
    tokenizer = Tokenizer("a=b+c*d")
    assert tokenizer.get_tokens_as_string() == "a,=,b,+,c,*,d,<EOF>"

def test_complex_struct_access():
    """87. Struct member access"""
    tokenizer = Tokenizer("person.name")
    assert tokenizer.get_tokens_as_string() == "person,.,name,<EOF>"

def test_complex_struct_access_increment():
    """88. Struct member increment"""
    tokenizer = Tokenizer("p.x++")
    assert tokenizer.get_tokens_as_string() == "p,.,x,++,<EOF>"

def test_complex_function_call():
    """89. Function call"""
    tokenizer = Tokenizer("add(1, 2)")
    assert tokenizer.get_tokens_as_string() == "add,(,1,,,2,),<EOF>"

def test_complex_float_vs_member():
    """90. Float vs Member Access Distinguisher"""
    tokenizer = Tokenizer("1.x")
    assert tokenizer.get_tokens_as_string() == "1.,x,<EOF>"

def test_complex_comparison_no_space():
    """91. Comparison without space"""
    tokenizer = Tokenizer("i<10")
    assert tokenizer.get_tokens_as_string() == "i,<,10,<EOF>"

def test_complex_comparison_equal_no_space():
    """92. Equality without space"""
    tokenizer = Tokenizer("x==y")
    assert tokenizer.get_tokens_as_string() == "x,==,y,<EOF>"

def test_complex_negative_number_logic():
    """93. Negative number tokenization"""
    tokenizer = Tokenizer("-45")
    assert tokenizer.get_tokens_as_string() == "-,45,<EOF>"

def test_complex_negative_float():
    """94. Negative float tokenization"""
    tokenizer = Tokenizer("-3.14")
    assert tokenizer.get_tokens_as_string() == "-,3.14,<EOF>"

def test_complex_struct_declaration():
    """95. Struct declaration tokens"""
    tokenizer = Tokenizer("struct Point { int x; };")
    assert tokenizer.get_tokens_as_string() == "struct,Point,{,int,x,;,},;,<EOF>"

def test_complex_escaped_string_logic():
    """96. String with escaped backslash at end"""
    tokenizer = Tokenizer('"foo\\\\"')
    assert tokenizer.get_tokens_as_string() == "foo\\\\,<EOF>"

def test_complex_increment_space():
    """97. Increment with space (invalid as single token)"""
    tokenizer = Tokenizer("+ +")
    assert tokenizer.get_tokens_as_string() == "+,+,<EOF>"

def test_complex_decrement_nospace():
    """98. Decrement no space"""
    tokenizer = Tokenizer("i--")
    assert tokenizer.get_tokens_as_string() == "i,--,<EOF>"

def test_complex_keyword_prefix():
    """99. Keyword as prefix of identifier"""
    tokenizer = Tokenizer("integer")
    assert tokenizer.get_tokens_as_string() == "integer,<EOF>"

def test_complex_float_exponent_case():
    """100. Float with lowercase e and signed exponent"""
    tokenizer = Tokenizer("1.2e+5")
    assert tokenizer.get_tokens_as_string() == "1.2e+5,<EOF>"
