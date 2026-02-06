# def test_082():
#         source = '.e-2 -. .010e-0.5'
#         expected = '.e-2,-.,.010e-0,.5,EOF'
#         assert Tokenizer(source).get_tokens_as_string() == expected
def test_009():
        source = """
    void main () {
        return 1;
        return 1.0;
        return "votien";
        return {1, 2, 1.0}; // struct lit
        return {};
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_009():
        source = """
    void main () {
        return 1;
        return 1.0;
        return "votien";
        return {1, 2, 1.0}; // struct lit
        return {};
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_009():
        source = """
    void main () {
        return 1;
        return 1.0;
        return "votien";
        return {1, 2, 1.0}; // struct lit
        return {};
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_010():
        source = """
    void main () {
        return 1 = 2 = 3;
        return (a = b) + 7;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_020():
        source = """
    void main () {
        return ++!a;
    }
    """
        expected = "Error on line 3 col 13: !"
        assert Parser(source).parse() == expected
def test_019():
        source = """
    void main () {
        return ++--++a;
        return !++a;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_028():
        source = """
    void main () {
        a.foo();
    }
    """
        expected = "Error on line 3 col 9: ("
        assert Parser(source).parse() == expected
def test_028():
        source = """
    void main () {
        a.foo();
    }
    """
        expected = "Error on line 3 col 9: ("
        assert Parser(source).parse() == expected
def test_020():
        source = """
    void main () {
        return ++!a;
    }
    """
        expected = "Error on line 3 col 13: !"
        assert Parser(source).parse() == expected
def test_022():
        source = """
    void main () {
        return a++--++--;
        return ++--++--a++--++--;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_028():
        source = """
    void main () {
        a.foo();
    }
    """
        expected = "Error on line 3 col 9: ("
        assert Parser(source).parse() == expected
def test_020():
        source = """
    void main () {
        return ++!a;
    }
    """
        expected = "Error on line 3 col 13: !"
        assert Parser(source).parse() == expected
def test_020():
        source = """
    void main () {
        return ++!a;
    }
    """
        expected = "Error on line 3 col 13: !"
        assert Parser(source).parse() == expected
def test_019():
        source = """
    void main () {
        return ++--++a;
        return !++a;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_020():
        source = """
    void main () {
        return ++!a;
    }
    """
        expected = "Error on line 3 col 13: !"
        assert Parser(source).parse() == expected
def test_028():
        source = """
    void main () {
        a.foo();
    }
    """
        expected = "Error on line 3 col 9: ("
        assert Parser(source).parse() == expected
def test_028():
        source = """
    void main () {
        a.foo();
    }
    """
        expected = "Error on line 3 col 9: ("
        assert Parser(source).parse() == expected
def test_028():
        source = """
    void main () {
        a.foo();
    }
    """
        expected = "Error on line 3 col 9: ("
        assert Parser(source).parse() == expected
def test_010():
        source = """
    void main () {
        return 1 = 2 = 3;
        return (a = b) + 7;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_010():
        source = """
    void main () {
        return 1 = 2 = 3;
        return (a = b) + 7;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_001():
        source = """
    void main() {
        printString("Hello, World!");
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_010():
        source = """
    void main () {
        return 1 = 2 = 3;
        return (a = b) + 7;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_019():
        source = """
    void main () {
        return ++--++a;
        return !++a;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_022():
        source = """
    void main () {
        return a++--++--;
        return ++--++--a++--++--;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_023():
        source = """
    void main () {
        return ++(+a) * (a / (c));
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_024():
        source = """
    void main () {
        return {1+3, "s"++};
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_029():
        source = """
    void main () {
        foo().a.b;
        ++a.b;
        a.b++;
    }
    """
        expected = "Error on line 5 col 7: ++"
        assert Parser(source).parse() == expected
def test_047():
        source = """
    void main () {
        return ;
        return 1 +2 *++3;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_057():
        source = """
    void main () {
       for(; ; -a) continue;
    }
    """
        expected = "Error on line 3 col 13: )"
        assert Parser(source).parse() == expected
def test_066():
        source = """
    void main () {
        switch (1) {
            case 1 + 2 * "s":
                printInt(0);
                return ;
                break;
            default:
                printInt(0);
                {if(1){}}
        }
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_067():
        source = """
    void main () {
        switch (1 *3 / 4) {
            default:
                1;
            case 2:
                 2;
        }
    }
    """
        expected = "Error on line 6 col 8: case"
        assert Parser(source).parse() == expected
def test_068():
        source = """
    auto main (int a, int b) {return;}
    void main3 () {}
    ID main2 (int a) {return;}
    """
        expected = "success"
        assert Parser(source).parse() == expected
# def test_006(): # True
#         source = "0   100   255   2500   -45"
#         expected = "0,100,255,2500,-,45,<EOF>"
#         assert Tokenizer(source).get_tokens_as_string() == expected
# def test_086(): # True
#         source = "["
#         try:
#             Tokenizer(source).get_tokens_as_string()
#             assert False, "Expected ErrorToken but no exception was raised"
# def test_082(): # False
#         source = '.e-2'
#         expected = '.,e,-,2,<EOF>'
#         assert Tokenizer(source).get_tokens_as_string() == expected
# def test_077():  # True
#         """Test invalid float: missing integer part before dot"""
#         source = '.5 -.055'
#         expected = '.5,-,.055,<EOF>'
#         assert Tokenizer(source).get_tokens_as_string() == expected
# def test_007():  # True
#         source = "0.0   3.14   -2.5   1.23e4   5.67E-2   1.   .5"
#         expected = "0.0,3.14,-,2.5,1.23e4,5.67E-2,1.,.5,<EOF>"
#         assert Tokenizer(source).get_tokens_as_string() == expected
def test_108():
        source = """
    void main () {
        auto x = readInt();
        switch (x) {
            default:
                printInt(0);
            default:
                printInt(0);
        }
    }
    """
        expected = "Error on line 7 col 8: default"
        assert Parser(source).parse() == expected
def test_102():
        source = """
    auto main(){}
    """
        expected = "Error on line 2 col 0: auto"
        assert Parser(source).parse() == expected
def test_067():
        source = """
    void main () {
        switch (1 *3 / 4) {
            default:
                1;
            case 2:
                 2;
        }

        switch (1 *3 / 4) {
            case 3:1;
            default:1;
            case 2: 2;
        }
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_057():
        source = """
    void main () {
       for(; ; -a) continue;
    }
    """
        expected = "Error on line 3 col 11: -"
        assert Parser(source).parse() == expected
def test_038():
        source = """
    void main () {
        ++a = 1;
    }
    """
        expected = "Error on line 3 col 8: ="
        assert Parser(source).parse() == expected
def test_024():
        source = """
    void main () {
        return {1+3, "s"++};
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_037():
        source = """
    void main () {
        foo().b = 2;
    }
    """
        expected = "Error on line 3 col 9: ."
        assert Parser(source).parse() == expected
def test_029():
        source = """
    void main () {
        foo.a.b;
        ++a.b;
        a.b++;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected

######################### NEW #############################
def test_123():     
        source = """
    void main () {
        a = foo().a = (a).b = "string".c.d.e = 1;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_039():
        source = """
    void main () {
        foo() = 1;
    }
    """
        expected = "Error on line 3 col 10: ="
        assert Parser(source).parse() == expected
def test_122():
        source = """
    void main () {
        foo().b = 2;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_121():
        source = """
    void main () {
        ++a.b;
        a.b = 1;
        ++(a.b) = 1;
    }
    """
        expected = "Error on line 5 col 12: ="
        assert Parser(source).parse() == expected
def test_029():
        source = """
    void main () {
        foo.a.b;
        ++a.b;
        a.b++;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_047():
        source = """
    void main () {
        return ;
        return 1 +2 *++3;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_022():
        source = """
    void main () {
        return a++--++--;
        return ++--++--a++--++--;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_021():
        source = """
    void main () {
        return +++a;
    }
    """
        expected = "Error on line 3 col 13: +"
        assert Parser(source).parse() == expected
def test_020():
        source = """
    void main () {
        return ++!a;
    }
    """
        expected = "Error on line 3 col 13: !"
        assert Parser(source).parse() == expected
def test_023():
        source = """
    void main () {
        return ++(+a) * (a / (c));
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_001():
        source = """
    void main() {
        printString("Hello, World!");
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_051():
        source = """
    void main () {
       for(int a = 1 + 2; i > 2; a++) continue;
       for(a = a.b = 1; ; --a) a++;
       for(auto a = 1; i * 2; a = 2) {return ;}
       for(; ; ) {}
       for({1,2}.a = 1; ; (a+2).b = 2) a++;
    }
    """
        expected = "success"
        assert Parser(source).parse() == expected
def test_098():
        source = """
    main(){for({1,2}; i * 2; a++ = 2 = 3) {return ;}}
    """
        expected = "Error on line 2 col 16: ;"
        assert Parser(source).parse() == expected