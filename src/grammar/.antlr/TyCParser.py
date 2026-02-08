# Generated from d:\BTL_PPL_252\src\grammar\TyC.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u023f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\3\2\3\2\3\2\3\3\3\3\3\3\7\3\177\n\3\f\3\16\3\u0082")
        buf.write("\13\3\3\4\3\4\5\4\u0086\n\4\3\5\3\5\3\5\5\5\u008b\n\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\5\6\u0097\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\5\7\u009e\n\7\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\7\n\u00ad\n\n\f\n\16")
        buf.write("\n\u00b0\13\n\3\13\3\13\3\13\3\13\3\f\3\f\5\f\u00b8\n")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00c0\n\r\f\r\16\r\u00c3")
        buf.write("\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00ce\n\16\3\16\3\16\5\16\u00d2\n\16\3\17\3\17\3\17\3")
        buf.write("\17\7\17\u00d8\n\17\f\17\16\17\u00db\13\17\3\20\3\20\5")
        buf.write("\20\u00df\n\20\3\21\3\21\3\21\3\21\3\21\7\21\u00e6\n\21")
        buf.write("\f\21\16\21\u00e9\13\21\3\22\3\22\5\22\u00ed\n\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00f8\n")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\5\24\u0104\n\24\3\25\3\25\5\25\u0108\n\25\3\26\3\26\3")
        buf.write("\27\3\27\5\27\u010e\n\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\7\30\u0116\n\30\f\30\16\30\u0119\13\30\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\5\32\u0122\n\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\5\33\u0129\n\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\7\34\u0131\n\34\f\34\16\34\u0134\13\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\7\35\u013c\n\35\f\35\16\35\u013f\13\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u0147\n\36\f\36\16")
        buf.write("\36\u014a\13\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u0152")
        buf.write("\n\37\f\37\16\37\u0155\13\37\3 \3 \3 \3 \3 \3 \7 \u015d")
        buf.write("\n \f \16 \u0160\13 \3!\3!\3!\3!\3!\3!\7!\u0168\n!\f!")
        buf.write("\16!\u016b\13!\3\"\3\"\3\"\5\"\u0170\n\"\3#\3#\3#\5#\u0175")
        buf.write("\n#\3$\3$\3$\3$\3$\7$\u017c\n$\f$\16$\u017f\13$\3%\3%")
        buf.write("\3%\3%\3%\3%\7%\u0187\n%\f%\16%\u018a\13%\3&\3&\3&\3&")
        buf.write("\3&\3&\3&\5&\u0193\n&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3")
        buf.write(")\3)\3)\3)\3*\3*\3*\7*\u01a5\n*\f*\16*\u01a8\13*\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u01b4\n+\3,\3,\3-\3-\3-\5")
        buf.write("-\u01bb\n-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\5.\u01e0\n.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\5\61\u01f8\n\61\3\62\3\62\5\62\u01fc\n\62\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63")
        buf.write("\u0208\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u021a\n\65")
        buf.write("\3\66\3\66\5\66\u021e\n\66\3\67\3\67\3\67\3\67\3\67\7")
        buf.write("\67\u0225\n\67\f\67\16\67\u0228\13\67\38\38\38\38\38\3")
        buf.write("9\39\39\3:\3:\3:\3;\3;\3;\5;\u0238\n;\3;\3;\3<\3<\3<\3")
        buf.write("<\2\22\4\22\30\34 .\668:<>@FHRl=\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprtv\2\t\5\2\13\13\16\16\20\20\3\2\34\35")
        buf.write("\3\2\36!\3\2\27\30\3\2\31\33\4\2\27\30$$\3\2\25\26\2\u0244")
        buf.write("\2x\3\2\2\2\4{\3\2\2\2\6\u0085\3\2\2\2\b\u008a\3\2\2\2")
        buf.write("\n\u0096\3\2\2\2\f\u009d\3\2\2\2\16\u009f\3\2\2\2\20\u00a2")
        buf.write("\3\2\2\2\22\u00a9\3\2\2\2\24\u00b1\3\2\2\2\26\u00b7\3")
        buf.write("\2\2\2\30\u00b9\3\2\2\2\32\u00d1\3\2\2\2\34\u00d3\3\2")
        buf.write("\2\2\36\u00de\3\2\2\2 \u00e0\3\2\2\2\"\u00ec\3\2\2\2$")
        buf.write("\u00f7\3\2\2\2&\u0103\3\2\2\2(\u0107\3\2\2\2*\u0109\3")
        buf.write("\2\2\2,\u010d\3\2\2\2.\u010f\3\2\2\2\60\u011a\3\2\2\2")
        buf.write("\62\u0121\3\2\2\2\64\u0128\3\2\2\2\66\u012a\3\2\2\28\u0135")
        buf.write("\3\2\2\2:\u0140\3\2\2\2<\u014b\3\2\2\2>\u0156\3\2\2\2")
        buf.write("@\u0161\3\2\2\2B\u016f\3\2\2\2D\u0174\3\2\2\2F\u0176\3")
        buf.write("\2\2\2H\u0180\3\2\2\2J\u0192\3\2\2\2L\u0194\3\2\2\2N\u0198")
        buf.write("\3\2\2\2P\u019d\3\2\2\2R\u01a1\3\2\2\2T\u01b3\3\2\2\2")
        buf.write("V\u01b5\3\2\2\2X\u01b7\3\2\2\2Z\u01be\3\2\2\2\\\u01e1")
        buf.write("\3\2\2\2^\u01e7\3\2\2\2`\u01f7\3\2\2\2b\u01fb\3\2\2\2")
        buf.write("d\u0207\3\2\2\2f\u0209\3\2\2\2h\u0219\3\2\2\2j\u021d\3")
        buf.write("\2\2\2l\u021f\3\2\2\2n\u0229\3\2\2\2p\u022e\3\2\2\2r\u0231")
        buf.write("\3\2\2\2t\u0234\3\2\2\2v\u023b\3\2\2\2xy\5\4\3\2yz\7\2")
        buf.write("\2\3z\3\3\2\2\2{\u0080\b\3\1\2|}\f\4\2\2}\177\5\6\4\2")
        buf.write("~|\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080\u0081")
        buf.write("\3\2\2\2\u0081\5\3\2\2\2\u0082\u0080\3\2\2\2\u0083\u0086")
        buf.write("\5\b\5\2\u0084\u0086\5\20\t\2\u0085\u0083\3\2\2\2\u0085")
        buf.write("\u0084\3\2\2\2\u0086\7\3\2\2\2\u0087\u008b\5(\25\2\u0088")
        buf.write("\u008b\7\23\2\2\u0089\u008b\3\2\2\2\u008a\u0087\3\2\2")
        buf.write("\2\u008a\u0088\3\2\2\2\u008a\u0089\3\2\2\2\u008b\u008c")
        buf.write("\3\2\2\2\u008c\u008d\7.\2\2\u008d\u008e\7)\2\2\u008e\u008f")
        buf.write("\5\n\6\2\u008f\u0090\7*\2\2\u0090\u0091\7\'\2\2\u0091")
        buf.write("\u0092\5R*\2\u0092\u0093\7(\2\2\u0093\t\3\2\2\2\u0094")
        buf.write("\u0097\5\f\7\2\u0095\u0097\3\2\2\2\u0096\u0094\3\2\2\2")
        buf.write("\u0096\u0095\3\2\2\2\u0097\13\3\2\2\2\u0098\u0099\5\16")
        buf.write("\b\2\u0099\u009a\7,\2\2\u009a\u009b\5\f\7\2\u009b\u009e")
        buf.write("\3\2\2\2\u009c\u009e\5\16\b\2\u009d\u0098\3\2\2\2\u009d")
        buf.write("\u009c\3\2\2\2\u009e\r\3\2\2\2\u009f\u00a0\5(\25\2\u00a0")
        buf.write("\u00a1\7.\2\2\u00a1\17\3\2\2\2\u00a2\u00a3\7\21\2\2\u00a3")
        buf.write("\u00a4\7.\2\2\u00a4\u00a5\7\'\2\2\u00a5\u00a6\5\22\n\2")
        buf.write("\u00a6\u00a7\7(\2\2\u00a7\u00a8\7+\2\2\u00a8\21\3\2\2")
        buf.write("\2\u00a9\u00ae\b\n\1\2\u00aa\u00ab\f\4\2\2\u00ab\u00ad")
        buf.write("\5\24\13\2\u00ac\u00aa\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae")
        buf.write("\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\23\3\2\2\2\u00b0")
        buf.write("\u00ae\3\2\2\2\u00b1\u00b2\5(\25\2\u00b2\u00b3\7.\2\2")
        buf.write("\u00b3\u00b4\7+\2\2\u00b4\25\3\2\2\2\u00b5\u00b8\5\30")
        buf.write("\r\2\u00b6\u00b8\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b6")
        buf.write("\3\2\2\2\u00b8\27\3\2\2\2\u00b9\u00ba\b\r\1\2\u00ba\u00bb")
        buf.write("\5\32\16\2\u00bb\u00c1\3\2\2\2\u00bc\u00bd\f\4\2\2\u00bd")
        buf.write("\u00be\7,\2\2\u00be\u00c0\5\32\16\2\u00bf\u00bc\3\2\2")
        buf.write("\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\31\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c5")
        buf.write("\7.\2\2\u00c5\u00c6\7.\2\2\u00c6\u00d2\7+\2\2\u00c7\u00c8")
        buf.write("\7.\2\2\u00c8\u00c9\7.\2\2\u00c9\u00ca\7%\2\2\u00ca\u00cd")
        buf.write("\7\'\2\2\u00cb\u00ce\5\34\17\2\u00cc\u00ce\3\2\2\2\u00cd")
        buf.write("\u00cb\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\u00d0\7(\2\2\u00d0\u00d2\7+\2\2\u00d1\u00c4\3\2")
        buf.write("\2\2\u00d1\u00c7\3\2\2\2\u00d2\33\3\2\2\2\u00d3\u00d9")
        buf.write("\b\17\1\2\u00d4\u00d5\f\4\2\2\u00d5\u00d6\7,\2\2\u00d6")
        buf.write("\u00d8\5\36\20\2\u00d7\u00d4\3\2\2\2\u00d8\u00db\3\2\2")
        buf.write("\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\35\3")
        buf.write("\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00df\5J&\2\u00dd\u00df")
        buf.write("\5N(\2\u00de\u00dc\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\37")
        buf.write("\3\2\2\2\u00e0\u00e1\b\21\1\2\u00e1\u00e2\5\"\22\2\u00e2")
        buf.write("\u00e7\3\2\2\2\u00e3\u00e4\f\4\2\2\u00e4\u00e6\5\"\22")
        buf.write("\2\u00e5\u00e3\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5")
        buf.write("\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8!\3\2\2\2\u00e9\u00e7")
        buf.write("\3\2\2\2\u00ea\u00ed\5$\23\2\u00eb\u00ed\5&\24\2\u00ec")
        buf.write("\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed#\3\2\2\2\u00ee")
        buf.write("\u00ef\7\5\2\2\u00ef\u00f0\7.\2\2\u00f0\u00f8\7+\2\2\u00f1")
        buf.write("\u00f2\7\5\2\2\u00f2\u00f3\7.\2\2\u00f3\u00f4\7%\2\2\u00f4")
        buf.write("\u00f5\5\62\32\2\u00f5\u00f6\7+\2\2\u00f6\u00f8\3\2\2")
        buf.write("\2\u00f7\u00ee\3\2\2\2\u00f7\u00f1\3\2\2\2\u00f8%\3\2")
        buf.write("\2\2\u00f9\u00fa\5(\25\2\u00fa\u00fb\7.\2\2\u00fb\u00fc")
        buf.write("\7+\2\2\u00fc\u0104\3\2\2\2\u00fd\u00fe\5(\25\2\u00fe")
        buf.write("\u00ff\7.\2\2\u00ff\u0100\7%\2\2\u0100\u0101\5\62\32\2")
        buf.write("\u0101\u0102\7+\2\2\u0102\u0104\3\2\2\2\u0103\u00f9\3")
        buf.write("\2\2\2\u0103\u00fd\3\2\2\2\u0104\'\3\2\2\2\u0105\u0108")
        buf.write("\5*\26\2\u0106\u0108\7.\2\2\u0107\u0105\3\2\2\2\u0107")
        buf.write("\u0106\3\2\2\2\u0108)\3\2\2\2\u0109\u010a\t\2\2\2\u010a")
        buf.write("+\3\2\2\2\u010b\u010e\5.\30\2\u010c\u010e\3\2\2\2\u010d")
        buf.write("\u010b\3\2\2\2\u010d\u010c\3\2\2\2\u010e-\3\2\2\2\u010f")
        buf.write("\u0110\b\30\1\2\u0110\u0111\5\60\31\2\u0111\u0117\3\2")
        buf.write("\2\2\u0112\u0113\f\4\2\2\u0113\u0114\7,\2\2\u0114\u0116")
        buf.write("\5\60\31\2\u0115\u0112\3\2\2\2\u0116\u0119\3\2\2\2\u0117")
        buf.write("\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118/\3\2\2\2\u0119")
        buf.write("\u0117\3\2\2\2\u011a\u011b\5\62\32\2\u011b\61\3\2\2\2")
        buf.write("\u011c\u011d\5\64\33\2\u011d\u011e\7%\2\2\u011e\u011f")
        buf.write("\5\62\32\2\u011f\u0122\3\2\2\2\u0120\u0122\5\66\34\2\u0121")
        buf.write("\u011c\3\2\2\2\u0121\u0120\3\2\2\2\u0122\63\3\2\2\2\u0123")
        buf.write("\u0129\7.\2\2\u0124\u0125\5H%\2\u0125\u0126\7&\2\2\u0126")
        buf.write("\u0127\7.\2\2\u0127\u0129\3\2\2\2\u0128\u0123\3\2\2\2")
        buf.write("\u0128\u0124\3\2\2\2\u0129\65\3\2\2\2\u012a\u012b\b\34")
        buf.write("\1\2\u012b\u012c\58\35\2\u012c\u0132\3\2\2\2\u012d\u012e")
        buf.write("\f\4\2\2\u012e\u012f\7\"\2\2\u012f\u0131\58\35\2\u0130")
        buf.write("\u012d\3\2\2\2\u0131\u0134\3\2\2\2\u0132\u0130\3\2\2\2")
        buf.write("\u0132\u0133\3\2\2\2\u0133\67\3\2\2\2\u0134\u0132\3\2")
        buf.write("\2\2\u0135\u0136\b\35\1\2\u0136\u0137\5:\36\2\u0137\u013d")
        buf.write("\3\2\2\2\u0138\u0139\f\4\2\2\u0139\u013a\7#\2\2\u013a")
        buf.write("\u013c\5:\36\2\u013b\u0138\3\2\2\2\u013c\u013f\3\2\2\2")
        buf.write("\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e9\3\2\2")
        buf.write("\2\u013f\u013d\3\2\2\2\u0140\u0141\b\36\1\2\u0141\u0142")
        buf.write("\5<\37\2\u0142\u0148\3\2\2\2\u0143\u0144\f\4\2\2\u0144")
        buf.write("\u0145\t\3\2\2\u0145\u0147\5<\37\2\u0146\u0143\3\2\2\2")
        buf.write("\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3")
        buf.write("\2\2\2\u0149;\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014c")
        buf.write("\b\37\1\2\u014c\u014d\5> \2\u014d\u0153\3\2\2\2\u014e")
        buf.write("\u014f\f\4\2\2\u014f\u0150\t\4\2\2\u0150\u0152\5> \2\u0151")
        buf.write("\u014e\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2")
        buf.write("\u0153\u0154\3\2\2\2\u0154=\3\2\2\2\u0155\u0153\3\2\2")
        buf.write("\2\u0156\u0157\b \1\2\u0157\u0158\5@!\2\u0158\u015e\3")
        buf.write("\2\2\2\u0159\u015a\f\4\2\2\u015a\u015b\t\5\2\2\u015b\u015d")
        buf.write("\5@!\2\u015c\u0159\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c")
        buf.write("\3\2\2\2\u015e\u015f\3\2\2\2\u015f?\3\2\2\2\u0160\u015e")
        buf.write("\3\2\2\2\u0161\u0162\b!\1\2\u0162\u0163\5B\"\2\u0163\u0169")
        buf.write("\3\2\2\2\u0164\u0165\f\4\2\2\u0165\u0166\t\6\2\2\u0166")
        buf.write("\u0168\5B\"\2\u0167\u0164\3\2\2\2\u0168\u016b\3\2\2\2")
        buf.write("\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016aA\3\2\2")
        buf.write("\2\u016b\u0169\3\2\2\2\u016c\u016d\t\7\2\2\u016d\u0170")
        buf.write("\5B\"\2\u016e\u0170\5D#\2\u016f\u016c\3\2\2\2\u016f\u016e")
        buf.write("\3\2\2\2\u0170C\3\2\2\2\u0171\u0172\t\b\2\2\u0172\u0175")
        buf.write("\5D#\2\u0173\u0175\5F$\2\u0174\u0171\3\2\2\2\u0174\u0173")
        buf.write("\3\2\2\2\u0175E\3\2\2\2\u0176\u0177\b$\1\2\u0177\u0178")
        buf.write("\5H%\2\u0178\u017d\3\2\2\2\u0179\u017a\f\4\2\2\u017a\u017c")
        buf.write("\t\b\2\2\u017b\u0179\3\2\2\2\u017c\u017f\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017eG\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u0180\u0181\b%\1\2\u0181\u0182\5J&\2\u0182")
        buf.write("\u0188\3\2\2\2\u0183\u0184\f\4\2\2\u0184\u0185\7&\2\2")
        buf.write("\u0185\u0187\7.\2\2\u0186\u0183\3\2\2\2\u0187\u018a\3")
        buf.write("\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189I")
        buf.write("\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u0193\7/\2\2\u018c")
        buf.write("\u0193\7\60\2\2\u018d\u0193\7\61\2\2\u018e\u0193\5L\'")
        buf.write("\2\u018f\u0193\5N(\2\u0190\u0193\5P)\2\u0191\u0193\7.")
        buf.write("\2\2\u0192\u018b\3\2\2\2\u0192\u018c\3\2\2\2\u0192\u018d")
        buf.write("\3\2\2\2\u0192\u018e\3\2\2\2\u0192\u018f\3\2\2\2\u0192")
        buf.write("\u0190\3\2\2\2\u0192\u0191\3\2\2\2\u0193K\3\2\2\2\u0194")
        buf.write("\u0195\7\'\2\2\u0195\u0196\5,\27\2\u0196\u0197\7(\2\2")
        buf.write("\u0197M\3\2\2\2\u0198\u0199\7.\2\2\u0199\u019a\7)\2\2")
        buf.write("\u019a\u019b\5,\27\2\u019b\u019c\7*\2\2\u019cO\3\2\2\2")
        buf.write("\u019d\u019e\7)\2\2\u019e\u019f\5\60\31\2\u019f\u01a0")
        buf.write("\7*\2\2\u01a0Q\3\2\2\2\u01a1\u01a6\b*\1\2\u01a2\u01a3")
        buf.write("\f\4\2\2\u01a3\u01a5\5T+\2\u01a4\u01a2\3\2\2\2\u01a5\u01a8")
        buf.write("\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7")
        buf.write("S\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a9\u01b4\5V,\2\u01aa")
        buf.write("\u01b4\5X-\2\u01ab\u01b4\5Z.\2\u01ac\u01b4\5\\/\2\u01ad")
        buf.write("\u01b4\5^\60\2\u01ae\u01b4\5f\64\2\u01af\u01b4\5p9\2\u01b0")
        buf.write("\u01b4\5r:\2\u01b1\u01b4\5t;\2\u01b2\u01b4\5v<\2\u01b3")
        buf.write("\u01a9\3\2\2\2\u01b3\u01aa\3\2\2\2\u01b3\u01ab\3\2\2\2")
        buf.write("\u01b3\u01ac\3\2\2\2\u01b3\u01ad\3\2\2\2\u01b3\u01ae\3")
        buf.write("\2\2\2\u01b3\u01af\3\2\2\2\u01b3\u01b0\3\2\2\2\u01b3\u01b1")
        buf.write("\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4U\3\2\2\2\u01b5\u01b6")
        buf.write("\5\"\22\2\u01b6W\3\2\2\2\u01b7\u01ba\7\'\2\2\u01b8\u01bb")
        buf.write("\5 \21\2\u01b9\u01bb\5R*\2\u01ba\u01b8\3\2\2\2\u01ba\u01b9")
        buf.write("\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd\7(\2\2\u01bd")
        buf.write("Y\3\2\2\2\u01be\u01bf\7\r\2\2\u01bf\u01c0\7)\2\2\u01c0")
        buf.write("\u01c1\5\60\31\2\u01c1\u01df\7*\2\2\u01c2\u01c3\7\'\2")
        buf.write("\2\u01c3\u01c4\5T+\2\u01c4\u01c5\7(\2\2\u01c5\u01e0\3")
        buf.write("\2\2\2\u01c6\u01c7\7\'\2\2\u01c7\u01c8\5T+\2\u01c8\u01c9")
        buf.write("\7(\2\2\u01c9\u01ca\7\n\2\2\u01ca\u01cb\7\'\2\2\u01cb")
        buf.write("\u01cc\5T+\2\u01cc\u01cd\7(\2\2\u01cd\u01e0\3\2\2\2\u01ce")
        buf.write("\u01e0\5T+\2\u01cf\u01d0\5T+\2\u01d0\u01d1\7\n\2\2\u01d1")
        buf.write("\u01d2\5T+\2\u01d2\u01e0\3\2\2\2\u01d3\u01d4\7\'\2\2\u01d4")
        buf.write("\u01d5\5T+\2\u01d5\u01d6\7(\2\2\u01d6\u01d7\7\n\2\2\u01d7")
        buf.write("\u01d8\5T+\2\u01d8\u01e0\3\2\2\2\u01d9\u01da\5T+\2\u01da")
        buf.write("\u01db\7\n\2\2\u01db\u01dc\7\'\2\2\u01dc\u01dd\5T+\2\u01dd")
        buf.write("\u01de\7(\2\2\u01de\u01e0\3\2\2\2\u01df\u01c2\3\2\2\2")
        buf.write("\u01df\u01c6\3\2\2\2\u01df\u01ce\3\2\2\2\u01df\u01cf\3")
        buf.write("\2\2\2\u01df\u01d3\3\2\2\2\u01df\u01d9\3\2\2\2\u01e0[")
        buf.write("\3\2\2\2\u01e1\u01e2\7\24\2\2\u01e2\u01e3\7)\2\2\u01e3")
        buf.write("\u01e4\5\60\31\2\u01e4\u01e5\7*\2\2\u01e5\u01e6\5T+\2")
        buf.write("\u01e6]\3\2\2\2\u01e7\u01e8\7\f\2\2\u01e8\u01e9\7)\2\2")
        buf.write("\u01e9\u01ea\5`\61\2\u01ea\u01eb\5b\62\2\u01eb\u01ec\7")
        buf.write("+\2\2\u01ec\u01ed\5d\63\2\u01ed\u01ee\7*\2\2\u01ee\u01ef")
        buf.write("\5T+\2\u01ef_\3\2\2\2\u01f0\u01f8\5\"\22\2\u01f1\u01f2")
        buf.write("\5\64\33\2\u01f2\u01f3\7%\2\2\u01f3\u01f4\5\60\31\2\u01f4")
        buf.write("\u01f5\7+\2\2\u01f5\u01f8\3\2\2\2\u01f6\u01f8\7+\2\2\u01f7")
        buf.write("\u01f0\3\2\2\2\u01f7\u01f1\3\2\2\2\u01f7\u01f6\3\2\2\2")
        buf.write("\u01f8a\3\2\2\2\u01f9\u01fc\5\60\31\2\u01fa\u01fc\3\2")
        buf.write("\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fa\3\2\2\2\u01fcc\3")
        buf.write("\2\2\2\u01fd\u01fe\5\64\33\2\u01fe\u01ff\7%\2\2\u01ff")
        buf.write("\u0200\5\60\31\2\u0200\u0208\3\2\2\2\u0201\u0202\t\b\2")
        buf.write("\2\u0202\u0208\5D#\2\u0203\u0204\5F$\2\u0204\u0205\t\b")
        buf.write("\2\2\u0205\u0208\3\2\2\2\u0206\u0208\3\2\2\2\u0207\u01fd")
        buf.write("\3\2\2\2\u0207\u0201\3\2\2\2\u0207\u0203\3\2\2\2\u0207")
        buf.write("\u0206\3\2\2\2\u0208e\3\2\2\2\u0209\u020a\7\22\2\2\u020a")
        buf.write("\u020b\7)\2\2\u020b\u020c\5\60\31\2\u020c\u020d\7*\2\2")
        buf.write("\u020d\u020e\7\'\2\2\u020e\u020f\5h\65\2\u020f\u0210\7")
        buf.write("(\2\2\u0210g\3\2\2\2\u0211\u021a\5l\67\2\u0212\u0213\5")
        buf.write("j\66\2\u0213\u0214\7\t\2\2\u0214\u0215\7-\2\2\u0215\u0216")
        buf.write("\5R*\2\u0216\u0217\5j\66\2\u0217\u021a\3\2\2\2\u0218\u021a")
        buf.write("\3\2\2\2\u0219\u0211\3\2\2\2\u0219\u0212\3\2\2\2\u0219")
        buf.write("\u0218\3\2\2\2\u021ai\3\2\2\2\u021b\u021e\5l\67\2\u021c")
        buf.write("\u021e\3\2\2\2\u021d\u021b\3\2\2\2\u021d\u021c\3\2\2\2")
        buf.write("\u021ek\3\2\2\2\u021f\u0220\b\67\1\2\u0220\u0221\5n8\2")
        buf.write("\u0221\u0226\3\2\2\2\u0222\u0223\f\4\2\2\u0223\u0225\5")
        buf.write("n8\2\u0224\u0222\3\2\2\2\u0225\u0228\3\2\2\2\u0226\u0224")
        buf.write("\3\2\2\2\u0226\u0227\3\2\2\2\u0227m\3\2\2\2\u0228\u0226")
        buf.write("\3\2\2\2\u0229\u022a\7\7\2\2\u022a\u022b\5\60\31\2\u022b")
        buf.write("\u022c\7-\2\2\u022c\u022d\5R*\2\u022do\3\2\2\2\u022e\u022f")
        buf.write("\7\6\2\2\u022f\u0230\7+\2\2\u0230q\3\2\2\2\u0231\u0232")
        buf.write("\7\b\2\2\u0232\u0233\7+\2\2\u0233s\3\2\2\2\u0234\u0237")
        buf.write("\7\17\2\2\u0235\u0238\5\60\31\2\u0236\u0238\3\2\2\2\u0237")
        buf.write("\u0235\3\2\2\2\u0237\u0236\3\2\2\2\u0238\u0239\3\2\2\2")
        buf.write("\u0239\u023a\7+\2\2\u023au\3\2\2\2\u023b\u023c\5\60\31")
        buf.write("\2\u023c\u023d\7+\2\2\u023dw\3\2\2\2-\u0080\u0085\u008a")
        buf.write("\u0096\u009d\u00ae\u00b7\u00c1\u00cd\u00d1\u00d9\u00de")
        buf.write("\u00e7\u00ec\u00f7\u0103\u0107\u010d\u0117\u0121\u0128")
        buf.write("\u0132\u013d\u0148\u0153\u015e\u0169\u016f\u0174\u017d")
        buf.write("\u0188\u0192\u01a6\u01b3\u01ba\u01df\u01f7\u01fb\u0207")
        buf.write("\u0219\u021d\u0226\u0237")
        return buf.getvalue()


class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'auto'", "'break'", 
                     "'case'", "'continue'", "'default'", "'else'", "'float'", 
                     "'for'", "'if'", "'int'", "'return'", "'string'", "'struct'", 
                     "'switch'", "'void'", "'while'", "'++'", "'--'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'='", 
                     "'.'", "'{'", "'}'", "'('", "')'", "';'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "LINE_COMMENT", "BLOCK_COMMENT", "AUTO", 
                      "BREAK", "CASE", "CONTINUE", "DEFAULT", "ELSE", "FLOAT", 
                      "FOR", "IF", "INT", "RETURN", "STRING", "STRUCT", 
                      "SWITCH", "VOID", "WHILE", "INCREMENT", "DECREMENT", 
                      "ADDITION", "SUBTRACTION", "MULTI", "DIVISION", "MODULO", 
                      "EQUAL", "NOT_EQUAL", "LESS_THAN", "GREATER_THAN", 
                      "LESS_THAN_EQUAL", "GREATER_THAN_EQUAL", "LOGICAL_OR", 
                      "LOGICAL_AND", "LOGICAL_NOT", "ASSIGNMENT", "MEMBER_ACCESS", 
                      "LEFT_BRACE", "RIGHT_BRACE", "LEFT_PAREN", "RIGHT_PAREN", 
                      "SEMICOLON", "COMMA", "COLON", "ID", "INT_LIT", "FLOAT_LIT", 
                      "STRING_LIT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl_list = 1
    RULE_decl = 2
    RULE_func_decl = 3
    RULE_param_list = 4
    RULE_param_list_exist = 5
    RULE_param_decl = 6
    RULE_struct_decl = 7
    RULE_struct_member_list = 8
    RULE_struct_member = 9
    RULE_struct_var_decl_list = 10
    RULE_struct_var_decl_list_exist = 11
    RULE_struct_var_decl = 12
    RULE_struct_var_member_list = 13
    RULE_struct_var_member = 14
    RULE_var_decl_list = 15
    RULE_var_decl = 16
    RULE_auto_var_decl = 17
    RULE_explicit_var_decl = 18
    RULE_typ = 19
    RULE_primitive_typ = 20
    RULE_expr_list = 21
    RULE_expr_list_exist = 22
    RULE_expr = 23
    RULE_assign_expr = 24
    RULE_assign_lhs = 25
    RULE_or_expr = 26
    RULE_and_expr = 27
    RULE_eq_expr = 28
    RULE_relational_expr = 29
    RULE_add_sub_expr = 30
    RULE_multi_div_mod_expr = 31
    RULE_unary_expr = 32
    RULE_prefix_expr = 33
    RULE_postfix_expr = 34
    RULE_member_access_expr = 35
    RULE_operand = 36
    RULE_struct_lit = 37
    RULE_func_call_expr = 38
    RULE_paren_expr = 39
    RULE_stmt_list = 40
    RULE_stmt = 41
    RULE_var_decl_stmt = 42
    RULE_block_stmt = 43
    RULE_if_stmt = 44
    RULE_while_stmt = 45
    RULE_for_stmt = 46
    RULE_init = 47
    RULE_condition = 48
    RULE_update = 49
    RULE_switch_stmt = 50
    RULE_switch_body = 51
    RULE_case_list_branch = 52
    RULE_case_list = 53
    RULE_case_stmt = 54
    RULE_break_stmt = 55
    RULE_continue_stmt = 56
    RULE_return_stmt = 57
    RULE_expr_stmt = 58

    ruleNames =  [ "program", "decl_list", "decl", "func_decl", "param_list", 
                   "param_list_exist", "param_decl", "struct_decl", "struct_member_list", 
                   "struct_member", "struct_var_decl_list", "struct_var_decl_list_exist", 
                   "struct_var_decl", "struct_var_member_list", "struct_var_member", 
                   "var_decl_list", "var_decl", "auto_var_decl", "explicit_var_decl", 
                   "typ", "primitive_typ", "expr_list", "expr_list_exist", 
                   "expr", "assign_expr", "assign_lhs", "or_expr", "and_expr", 
                   "eq_expr", "relational_expr", "add_sub_expr", "multi_div_mod_expr", 
                   "unary_expr", "prefix_expr", "postfix_expr", "member_access_expr", 
                   "operand", "struct_lit", "func_call_expr", "paren_expr", 
                   "stmt_list", "stmt", "var_decl_stmt", "block_stmt", "if_stmt", 
                   "while_stmt", "for_stmt", "init", "condition", "update", 
                   "switch_stmt", "switch_body", "case_list_branch", "case_list", 
                   "case_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "expr_stmt" ]

    EOF = Token.EOF
    LINE_COMMENT=1
    BLOCK_COMMENT=2
    AUTO=3
    BREAK=4
    CASE=5
    CONTINUE=6
    DEFAULT=7
    ELSE=8
    FLOAT=9
    FOR=10
    IF=11
    INT=12
    RETURN=13
    STRING=14
    STRUCT=15
    SWITCH=16
    VOID=17
    WHILE=18
    INCREMENT=19
    DECREMENT=20
    ADDITION=21
    SUBTRACTION=22
    MULTI=23
    DIVISION=24
    MODULO=25
    EQUAL=26
    NOT_EQUAL=27
    LESS_THAN=28
    GREATER_THAN=29
    LESS_THAN_EQUAL=30
    GREATER_THAN_EQUAL=31
    LOGICAL_OR=32
    LOGICAL_AND=33
    LOGICAL_NOT=34
    ASSIGNMENT=35
    MEMBER_ACCESS=36
    LEFT_BRACE=37
    RIGHT_BRACE=38
    LEFT_PAREN=39
    RIGHT_PAREN=40
    SEMICOLON=41
    COMMA=42
    COLON=43
    ID=44
    INT_LIT=45
    FLOAT_LIT=46
    STRING_LIT=47
    WS=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50
    ERROR_CHAR=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_list(self):
            return self.getTypedRuleContext(TyCParser.Decl_listContext,0)


        def EOF(self):
            return self.getToken(TyCParser.EOF, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.decl_list(0)
            self.state = 119
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_list(self):
            return self.getTypedRuleContext(TyCParser.Decl_listContext,0)


        def decl(self):
            return self.getTypedRuleContext(TyCParser.DeclContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_decl_list



    def decl_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Decl_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_decl_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self._ctx.stop = self._input.LT(-1)
            self.state = 126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Decl_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_decl_list)
                    self.state = 122
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 123
                    self.decl() 
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self):
            return self.getTypedRuleContext(TyCParser.Func_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(TyCParser.Struct_declContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_decl




    def decl(self):

        localctx = TyCParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.VOID, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.func_decl()
                pass
            elif token in [TyCParser.STRUCT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.struct_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def param_list(self):
            return self.getTypedRuleContext(TyCParser.Param_listContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def LEFT_BRACE(self):
            return self.getToken(TyCParser.LEFT_BRACE, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(TyCParser.Stmt_listContext,0)


        def RIGHT_BRACE(self):
            return self.getToken(TyCParser.RIGHT_BRACE, 0)

        def typ(self):
            return self.getTypedRuleContext(TyCParser.TypContext,0)


        def VOID(self):
            return self.getToken(TyCParser.VOID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_func_decl




    def func_decl(self):

        localctx = TyCParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 133
                self.typ()
                pass

            elif la_ == 2:
                self.state = 134
                self.match(TyCParser.VOID)
                pass

            elif la_ == 3:
                pass


            self.state = 138
            self.match(TyCParser.ID)
            self.state = 139
            self.match(TyCParser.LEFT_PAREN)
            self.state = 140
            self.param_list()
            self.state = 141
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 142
            self.match(TyCParser.LEFT_BRACE)
            self.state = 143
            self.stmt_list(0)
            self.state = 144
            self.match(TyCParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_list_exist(self):
            return self.getTypedRuleContext(TyCParser.Param_list_existContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_param_list




    def param_list(self):

        localctx = TyCParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_param_list)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.param_list_exist()
                pass
            elif token in [TyCParser.RIGHT_PAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_list_existContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_decl(self):
            return self.getTypedRuleContext(TyCParser.Param_declContext,0)


        def COMMA(self):
            return self.getToken(TyCParser.COMMA, 0)

        def param_list_exist(self):
            return self.getTypedRuleContext(TyCParser.Param_list_existContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_param_list_exist




    def param_list_exist(self):

        localctx = TyCParser.Param_list_existContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param_list_exist)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.param_decl()
                self.state = 151
                self.match(TyCParser.COMMA)
                self.state = 152
                self.param_list_exist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.param_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(TyCParser.TypContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_param_decl




    def param_decl(self):

        localctx = TyCParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.typ()
            self.state = 158
            self.match(TyCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(TyCParser.STRUCT, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LEFT_BRACE(self):
            return self.getToken(TyCParser.LEFT_BRACE, 0)

        def struct_member_list(self):
            return self.getTypedRuleContext(TyCParser.Struct_member_listContext,0)


        def RIGHT_BRACE(self):
            return self.getToken(TyCParser.RIGHT_BRACE, 0)

        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_struct_decl




    def struct_decl(self):

        localctx = TyCParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(TyCParser.STRUCT)
            self.state = 161
            self.match(TyCParser.ID)
            self.state = 162
            self.match(TyCParser.LEFT_BRACE)
            self.state = 163
            self.struct_member_list(0)
            self.state = 164
            self.match(TyCParser.RIGHT_BRACE)
            self.state = 165
            self.match(TyCParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_member_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_member_list(self):
            return self.getTypedRuleContext(TyCParser.Struct_member_listContext,0)


        def struct_member(self):
            return self.getTypedRuleContext(TyCParser.Struct_memberContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_struct_member_list



    def struct_member_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Struct_member_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_struct_member_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self._ctx.stop = self._input.LT(-1)
            self.state = 172
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Struct_member_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_member_list)
                    self.state = 168
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 169
                    self.struct_member() 
                self.state = 174
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Struct_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(TyCParser.TypContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_struct_member




    def struct_member(self):

        localctx = TyCParser.Struct_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_struct_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.typ()
            self.state = 176
            self.match(TyCParser.ID)
            self.state = 177
            self.match(TyCParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_var_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_var_decl_list_exist(self):
            return self.getTypedRuleContext(TyCParser.Struct_var_decl_list_existContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_struct_var_decl_list




    def struct_var_decl_list(self):

        localctx = TyCParser.Struct_var_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_struct_var_decl_list)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.struct_var_decl_list_exist(0)
                pass
            elif token in [TyCParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_var_decl_list_existContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_var_decl(self):
            return self.getTypedRuleContext(TyCParser.Struct_var_declContext,0)


        def struct_var_decl_list_exist(self):
            return self.getTypedRuleContext(TyCParser.Struct_var_decl_list_existContext,0)


        def COMMA(self):
            return self.getToken(TyCParser.COMMA, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_struct_var_decl_list_exist



    def struct_var_decl_list_exist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Struct_var_decl_list_existContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_struct_var_decl_list_exist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.struct_var_decl()
            self._ctx.stop = self._input.LT(-1)
            self.state = 191
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Struct_var_decl_list_existContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_var_decl_list_exist)
                    self.state = 186
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 187
                    self.match(TyCParser.COMMA)
                    self.state = 188
                    self.struct_var_decl() 
                self.state = 193
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Struct_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def ASSIGNMENT(self):
            return self.getToken(TyCParser.ASSIGNMENT, 0)

        def LEFT_BRACE(self):
            return self.getToken(TyCParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(TyCParser.RIGHT_BRACE, 0)

        def struct_var_member_list(self):
            return self.getTypedRuleContext(TyCParser.Struct_var_member_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_struct_var_decl




    def struct_var_decl(self):

        localctx = TyCParser.Struct_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_struct_var_decl)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(TyCParser.ID)
                self.state = 195
                self.match(TyCParser.ID)
                self.state = 196
                self.match(TyCParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.match(TyCParser.ID)
                self.state = 198
                self.match(TyCParser.ID)
                self.state = 199
                self.match(TyCParser.ASSIGNMENT)
                self.state = 200
                self.match(TyCParser.LEFT_BRACE)
                self.state = 203
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 201
                    self.struct_var_member_list(0)
                    pass

                elif la_ == 2:
                    pass


                self.state = 205
                self.match(TyCParser.RIGHT_BRACE)
                self.state = 206
                self.match(TyCParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_var_member_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_var_member_list(self):
            return self.getTypedRuleContext(TyCParser.Struct_var_member_listContext,0)


        def COMMA(self):
            return self.getToken(TyCParser.COMMA, 0)

        def struct_var_member(self):
            return self.getTypedRuleContext(TyCParser.Struct_var_memberContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_struct_var_member_list



    def struct_var_member_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Struct_var_member_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_struct_var_member_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self._ctx.stop = self._input.LT(-1)
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Struct_var_member_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_var_member_list)
                    self.state = 210
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 211
                    self.match(TyCParser.COMMA)
                    self.state = 212
                    self.struct_var_member() 
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Struct_var_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(TyCParser.OperandContext,0)


        def func_call_expr(self):
            return self.getTypedRuleContext(TyCParser.Func_call_exprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_struct_var_member




    def struct_var_member(self):

        localctx = TyCParser.Struct_var_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_struct_var_member)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.operand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.func_call_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(TyCParser.Var_declContext,0)


        def var_decl_list(self):
            return self.getTypedRuleContext(TyCParser.Var_decl_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_var_decl_list



    def var_decl_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Var_decl_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_var_decl_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.var_decl()
            self._ctx.stop = self._input.LT(-1)
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Var_decl_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_var_decl_list)
                    self.state = 225
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 226
                    self.var_decl() 
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def auto_var_decl(self):
            return self.getTypedRuleContext(TyCParser.Auto_var_declContext,0)


        def explicit_var_decl(self):
            return self.getTypedRuleContext(TyCParser.Explicit_var_declContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_var_decl




    def var_decl(self):

        localctx = TyCParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_var_decl)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.AUTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.auto_var_decl()
                pass
            elif token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.explicit_var_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Auto_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTO(self):
            return self.getToken(TyCParser.AUTO, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def ASSIGNMENT(self):
            return self.getToken(TyCParser.ASSIGNMENT, 0)

        def assign_expr(self):
            return self.getTypedRuleContext(TyCParser.Assign_exprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_auto_var_decl




    def auto_var_decl(self):

        localctx = TyCParser.Auto_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_auto_var_decl)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(TyCParser.AUTO)
                self.state = 237
                self.match(TyCParser.ID)
                self.state = 238
                self.match(TyCParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(TyCParser.AUTO)
                self.state = 240
                self.match(TyCParser.ID)
                self.state = 241
                self.match(TyCParser.ASSIGNMENT)
                self.state = 242
                self.assign_expr()
                self.state = 243
                self.match(TyCParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explicit_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(TyCParser.TypContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def ASSIGNMENT(self):
            return self.getToken(TyCParser.ASSIGNMENT, 0)

        def assign_expr(self):
            return self.getTypedRuleContext(TyCParser.Assign_exprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_explicit_var_decl




    def explicit_var_decl(self):

        localctx = TyCParser.Explicit_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_explicit_var_decl)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.typ()
                self.state = 248
                self.match(TyCParser.ID)
                self.state = 249
                self.match(TyCParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.typ()
                self.state = 252
                self.match(TyCParser.ID)
                self.state = 253
                self.match(TyCParser.ASSIGNMENT)
                self.state = 254
                self.assign_expr()
                self.state = 255
                self.match(TyCParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_typ(self):
            return self.getTypedRuleContext(TyCParser.Primitive_typContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_typ




    def typ(self):

        localctx = TyCParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_typ)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.primitive_typ()
                pass
            elif token in [TyCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.match(TyCParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_primitive_typ




    def primitive_typ(self):

        localctx = TyCParser.Primitive_typContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_primitive_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.FLOAT) | (1 << TyCParser.INT) | (1 << TyCParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_list_exist(self):
            return self.getTypedRuleContext(TyCParser.Expr_list_existContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_expr_list




    def expr_list(self):

        localctx = TyCParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr_list)
        try:
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.ADDITION, TyCParser.SUBTRACTION, TyCParser.LOGICAL_NOT, TyCParser.LEFT_BRACE, TyCParser.LEFT_PAREN, TyCParser.ID, TyCParser.INT_LIT, TyCParser.FLOAT_LIT, TyCParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.expr_list_exist(0)
                pass
            elif token in [TyCParser.RIGHT_BRACE, TyCParser.RIGHT_PAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_list_existContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def expr_list_exist(self):
            return self.getTypedRuleContext(TyCParser.Expr_list_existContext,0)


        def COMMA(self):
            return self.getToken(TyCParser.COMMA, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_expr_list_exist



    def expr_list_exist(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Expr_list_existContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr_list_exist, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Expr_list_existContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_list_exist)
                    self.state = 272
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 273
                    self.match(TyCParser.COMMA)
                    self.state = 274
                    self.expr() 
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_expr(self):
            return self.getTypedRuleContext(TyCParser.Assign_exprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_expr




    def expr(self):

        localctx = TyCParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.assign_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(TyCParser.Assign_lhsContext,0)


        def ASSIGNMENT(self):
            return self.getToken(TyCParser.ASSIGNMENT, 0)

        def assign_expr(self):
            return self.getTypedRuleContext(TyCParser.Assign_exprContext,0)


        def or_expr(self):
            return self.getTypedRuleContext(TyCParser.Or_exprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_assign_expr




    def assign_expr(self):

        localctx = TyCParser.Assign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assign_expr)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.assign_lhs()
                self.state = 283
                self.match(TyCParser.ASSIGNMENT)
                self.state = 284
                self.assign_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.or_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def member_access_expr(self):
            return self.getTypedRuleContext(TyCParser.Member_access_exprContext,0)


        def MEMBER_ACCESS(self):
            return self.getToken(TyCParser.MEMBER_ACCESS, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_assign_lhs




    def assign_lhs(self):

        localctx = TyCParser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assign_lhs)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.match(TyCParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.member_access_expr(0)
                self.state = 291
                self.match(TyCParser.MEMBER_ACCESS)
                self.state = 292
                self.match(TyCParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expr(self):
            return self.getTypedRuleContext(TyCParser.And_exprContext,0)


        def or_expr(self):
            return self.getTypedRuleContext(TyCParser.Or_exprContext,0)


        def LOGICAL_OR(self):
            return self.getToken(TyCParser.LOGICAL_OR, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_or_expr



    def or_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Or_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_or_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.and_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_or_expr)
                    self.state = 299
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 300
                    self.match(TyCParser.LOGICAL_OR)
                    self.state = 301
                    self.and_expr(0) 
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class And_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eq_expr(self):
            return self.getTypedRuleContext(TyCParser.Eq_exprContext,0)


        def and_expr(self):
            return self.getTypedRuleContext(TyCParser.And_exprContext,0)


        def LOGICAL_AND(self):
            return self.getToken(TyCParser.LOGICAL_AND, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_and_expr



    def and_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.And_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_and_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.eq_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.And_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_expr)
                    self.state = 310
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 311
                    self.match(TyCParser.LOGICAL_AND)
                    self.state = 312
                    self.eq_expr(0) 
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Eq_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expr(self):
            return self.getTypedRuleContext(TyCParser.Relational_exprContext,0)


        def eq_expr(self):
            return self.getTypedRuleContext(TyCParser.Eq_exprContext,0)


        def EQUAL(self):
            return self.getToken(TyCParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(TyCParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_eq_expr



    def eq_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Eq_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_eq_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.relational_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Eq_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_eq_expr)
                    self.state = 321
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 322
                    _la = self._input.LA(1)
                    if not(_la==TyCParser.EQUAL or _la==TyCParser.NOT_EQUAL):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 323
                    self.relational_expr(0) 
                self.state = 328
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_sub_expr(self):
            return self.getTypedRuleContext(TyCParser.Add_sub_exprContext,0)


        def relational_expr(self):
            return self.getTypedRuleContext(TyCParser.Relational_exprContext,0)


        def LESS_THAN(self):
            return self.getToken(TyCParser.LESS_THAN, 0)

        def LESS_THAN_EQUAL(self):
            return self.getToken(TyCParser.LESS_THAN_EQUAL, 0)

        def GREATER_THAN(self):
            return self.getToken(TyCParser.GREATER_THAN, 0)

        def GREATER_THAN_EQUAL(self):
            return self.getToken(TyCParser.GREATER_THAN_EQUAL, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_relational_expr



    def relational_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Relational_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_relational_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.add_sub_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 337
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Relational_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expr)
                    self.state = 332
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 333
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.LESS_THAN) | (1 << TyCParser.GREATER_THAN) | (1 << TyCParser.LESS_THAN_EQUAL) | (1 << TyCParser.GREATER_THAN_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 334
                    self.add_sub_expr(0) 
                self.state = 339
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Add_sub_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multi_div_mod_expr(self):
            return self.getTypedRuleContext(TyCParser.Multi_div_mod_exprContext,0)


        def add_sub_expr(self):
            return self.getTypedRuleContext(TyCParser.Add_sub_exprContext,0)


        def ADDITION(self):
            return self.getToken(TyCParser.ADDITION, 0)

        def SUBTRACTION(self):
            return self.getToken(TyCParser.SUBTRACTION, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_add_sub_expr



    def add_sub_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Add_sub_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_add_sub_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.multi_div_mod_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 348
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Add_sub_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub_expr)
                    self.state = 343
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 344
                    _la = self._input.LA(1)
                    if not(_la==TyCParser.ADDITION or _la==TyCParser.SUBTRACTION):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 345
                    self.multi_div_mod_expr(0) 
                self.state = 350
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multi_div_mod_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expr(self):
            return self.getTypedRuleContext(TyCParser.Unary_exprContext,0)


        def multi_div_mod_expr(self):
            return self.getTypedRuleContext(TyCParser.Multi_div_mod_exprContext,0)


        def MULTI(self):
            return self.getToken(TyCParser.MULTI, 0)

        def DIVISION(self):
            return self.getToken(TyCParser.DIVISION, 0)

        def MODULO(self):
            return self.getToken(TyCParser.MODULO, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_multi_div_mod_expr



    def multi_div_mod_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Multi_div_mod_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_multi_div_mod_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.unary_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 359
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Multi_div_mod_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multi_div_mod_expr)
                    self.state = 354
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 355
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.MULTI) | (1 << TyCParser.DIVISION) | (1 << TyCParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 356
                    self.unary_expr() 
                self.state = 361
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Unary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expr(self):
            return self.getTypedRuleContext(TyCParser.Unary_exprContext,0)


        def LOGICAL_NOT(self):
            return self.getToken(TyCParser.LOGICAL_NOT, 0)

        def SUBTRACTION(self):
            return self.getToken(TyCParser.SUBTRACTION, 0)

        def ADDITION(self):
            return self.getToken(TyCParser.ADDITION, 0)

        def prefix_expr(self):
            return self.getTypedRuleContext(TyCParser.Prefix_exprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_unary_expr




    def unary_expr(self):

        localctx = TyCParser.Unary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_unary_expr)
        self._la = 0 # Token type
        try:
            self.state = 365
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ADDITION, TyCParser.SUBTRACTION, TyCParser.LOGICAL_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.ADDITION) | (1 << TyCParser.SUBTRACTION) | (1 << TyCParser.LOGICAL_NOT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 363
                self.unary_expr()
                pass
            elif token in [TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LEFT_BRACE, TyCParser.LEFT_PAREN, TyCParser.ID, TyCParser.INT_LIT, TyCParser.FLOAT_LIT, TyCParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.prefix_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prefix_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prefix_expr(self):
            return self.getTypedRuleContext(TyCParser.Prefix_exprContext,0)


        def INCREMENT(self):
            return self.getToken(TyCParser.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(TyCParser.DECREMENT, 0)

        def postfix_expr(self):
            return self.getTypedRuleContext(TyCParser.Postfix_exprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_prefix_expr




    def prefix_expr(self):

        localctx = TyCParser.Prefix_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_prefix_expr)
        self._la = 0 # Token type
        try:
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INCREMENT, TyCParser.DECREMENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                _la = self._input.LA(1)
                if not(_la==TyCParser.INCREMENT or _la==TyCParser.DECREMENT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 368
                self.prefix_expr()
                pass
            elif token in [TyCParser.LEFT_BRACE, TyCParser.LEFT_PAREN, TyCParser.ID, TyCParser.INT_LIT, TyCParser.FLOAT_LIT, TyCParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.postfix_expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Postfix_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member_access_expr(self):
            return self.getTypedRuleContext(TyCParser.Member_access_exprContext,0)


        def postfix_expr(self):
            return self.getTypedRuleContext(TyCParser.Postfix_exprContext,0)


        def INCREMENT(self):
            return self.getToken(TyCParser.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(TyCParser.DECREMENT, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_postfix_expr



    def postfix_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Postfix_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_postfix_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.member_access_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Postfix_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix_expr)
                    self.state = 375
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 376
                    _la = self._input.LA(1)
                    if not(_la==TyCParser.INCREMENT or _la==TyCParser.DECREMENT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Member_access_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(TyCParser.OperandContext,0)


        def member_access_expr(self):
            return self.getTypedRuleContext(TyCParser.Member_access_exprContext,0)


        def MEMBER_ACCESS(self):
            return self.getToken(TyCParser.MEMBER_ACCESS, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_member_access_expr



    def member_access_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Member_access_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_member_access_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 390
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Member_access_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access_expr)
                    self.state = 385
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 386
                    self.match(TyCParser.MEMBER_ACCESS)
                    self.state = 387
                    self.match(TyCParser.ID) 
                self.state = 392
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(TyCParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(TyCParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(TyCParser.STRING_LIT, 0)

        def struct_lit(self):
            return self.getTypedRuleContext(TyCParser.Struct_litContext,0)


        def func_call_expr(self):
            return self.getTypedRuleContext(TyCParser.Func_call_exprContext,0)


        def paren_expr(self):
            return self.getTypedRuleContext(TyCParser.Paren_exprContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_operand




    def operand(self):

        localctx = TyCParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_operand)
        try:
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.match(TyCParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.match(TyCParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 395
                self.match(TyCParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 396
                self.struct_lit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 397
                self.func_call_expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 398
                self.paren_expr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 399
                self.match(TyCParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(TyCParser.LEFT_BRACE, 0)

        def expr_list(self):
            return self.getTypedRuleContext(TyCParser.Expr_listContext,0)


        def RIGHT_BRACE(self):
            return self.getToken(TyCParser.RIGHT_BRACE, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_struct_lit




    def struct_lit(self):

        localctx = TyCParser.Struct_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_struct_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(TyCParser.LEFT_BRACE)
            self.state = 403
            self.expr_list()
            self.state = 404
            self.match(TyCParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def expr_list(self):
            return self.getTypedRuleContext(TyCParser.Expr_listContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_func_call_expr




    def func_call_expr(self):

        localctx = TyCParser.Func_call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_func_call_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(TyCParser.ID)
            self.state = 407
            self.match(TyCParser.LEFT_PAREN)
            self.state = 408
            self.expr_list()
            self.state = 409
            self.match(TyCParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paren_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_paren_expr




    def paren_expr(self):

        localctx = TyCParser.Paren_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_paren_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(TyCParser.LEFT_PAREN)
            self.state = 412
            self.expr()
            self.state = 413
            self.match(TyCParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_list(self):
            return self.getTypedRuleContext(TyCParser.Stmt_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(TyCParser.StmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_stmt_list



    def stmt_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Stmt_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_stmt_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self._ctx.stop = self._input.LT(-1)
            self.state = 420
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Stmt_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_stmt_list)
                    self.state = 416
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 417
                    self.stmt() 
                self.state = 422
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_stmt(self):
            return self.getTypedRuleContext(TyCParser.Var_decl_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(TyCParser.Block_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(TyCParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(TyCParser.While_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(TyCParser.For_stmtContext,0)


        def switch_stmt(self):
            return self.getTypedRuleContext(TyCParser.Switch_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(TyCParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(TyCParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(TyCParser.Return_stmtContext,0)


        def expr_stmt(self):
            return self.getTypedRuleContext(TyCParser.Expr_stmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_stmt




    def stmt(self):

        localctx = TyCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_stmt)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.var_decl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.block_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 425
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 426
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 427
                self.for_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 428
                self.switch_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 429
                self.break_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 430
                self.continue_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 431
                self.return_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 432
                self.expr_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(TyCParser.Var_declContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_var_decl_stmt




    def var_decl_stmt(self):

        localctx = TyCParser.Var_decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_var_decl_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.var_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(TyCParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(TyCParser.RIGHT_BRACE, 0)

        def var_decl_list(self):
            return self.getTypedRuleContext(TyCParser.Var_decl_listContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(TyCParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_block_stmt




    def block_stmt(self):

        localctx = TyCParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(TyCParser.LEFT_BRACE)
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 438
                self.var_decl_list(0)
                pass

            elif la_ == 2:
                self.state = 439
                self.stmt_list(0)
                pass


            self.state = 442
            self.match(TyCParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(TyCParser.IF, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def LEFT_BRACE(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.LEFT_BRACE)
            else:
                return self.getToken(TyCParser.LEFT_BRACE, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def RIGHT_BRACE(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.RIGHT_BRACE)
            else:
                return self.getToken(TyCParser.RIGHT_BRACE, i)

        def ELSE(self):
            return self.getToken(TyCParser.ELSE, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_if_stmt




    def if_stmt(self):

        localctx = TyCParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(TyCParser.IF)
            self.state = 445
            self.match(TyCParser.LEFT_PAREN)
            self.state = 446
            self.expr()
            self.state = 447
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 477
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 448
                self.match(TyCParser.LEFT_BRACE)
                self.state = 449
                self.stmt()
                self.state = 450
                self.match(TyCParser.RIGHT_BRACE)
                pass

            elif la_ == 2:
                self.state = 452
                self.match(TyCParser.LEFT_BRACE)
                self.state = 453
                self.stmt()
                self.state = 454
                self.match(TyCParser.RIGHT_BRACE)
                self.state = 455
                self.match(TyCParser.ELSE)
                self.state = 456
                self.match(TyCParser.LEFT_BRACE)
                self.state = 457
                self.stmt()
                self.state = 458
                self.match(TyCParser.RIGHT_BRACE)
                pass

            elif la_ == 3:
                self.state = 460
                self.stmt()
                pass

            elif la_ == 4:
                self.state = 461
                self.stmt()
                self.state = 462
                self.match(TyCParser.ELSE)
                self.state = 463
                self.stmt()
                pass

            elif la_ == 5:
                self.state = 465
                self.match(TyCParser.LEFT_BRACE)
                self.state = 466
                self.stmt()
                self.state = 467
                self.match(TyCParser.RIGHT_BRACE)
                self.state = 468
                self.match(TyCParser.ELSE)
                self.state = 469
                self.stmt()
                pass

            elif la_ == 6:
                self.state = 471
                self.stmt()
                self.state = 472
                self.match(TyCParser.ELSE)
                self.state = 473
                self.match(TyCParser.LEFT_BRACE)
                self.state = 474
                self.stmt()
                self.state = 475
                self.match(TyCParser.RIGHT_BRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(TyCParser.WHILE, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def stmt(self):
            return self.getTypedRuleContext(TyCParser.StmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_while_stmt




    def while_stmt(self):

        localctx = TyCParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(TyCParser.WHILE)
            self.state = 480
            self.match(TyCParser.LEFT_PAREN)
            self.state = 481
            self.expr()
            self.state = 482
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 483
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(TyCParser.FOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def init(self):
            return self.getTypedRuleContext(TyCParser.InitContext,0)


        def condition(self):
            return self.getTypedRuleContext(TyCParser.ConditionContext,0)


        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def update(self):
            return self.getTypedRuleContext(TyCParser.UpdateContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def stmt(self):
            return self.getTypedRuleContext(TyCParser.StmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_for_stmt




    def for_stmt(self):

        localctx = TyCParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(TyCParser.FOR)
            self.state = 486
            self.match(TyCParser.LEFT_PAREN)
            self.state = 487
            self.init()
            self.state = 488
            self.condition()
            self.state = 489
            self.match(TyCParser.SEMICOLON)
            self.state = 490
            self.update()
            self.state = 491
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 492
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(TyCParser.Var_declContext,0)


        def assign_lhs(self):
            return self.getTypedRuleContext(TyCParser.Assign_lhsContext,0)


        def ASSIGNMENT(self):
            return self.getToken(TyCParser.ASSIGNMENT, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_init




    def init(self):

        localctx = TyCParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_init)
        try:
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
                self.assign_lhs()
                self.state = 496
                self.match(TyCParser.ASSIGNMENT)
                self.state = 497
                self.expr()
                self.state = 498
                self.match(TyCParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 500
                self.match(TyCParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_condition




    def condition(self):

        localctx = TyCParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_condition)
        try:
            self.state = 505
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.ADDITION, TyCParser.SUBTRACTION, TyCParser.LOGICAL_NOT, TyCParser.LEFT_BRACE, TyCParser.LEFT_PAREN, TyCParser.ID, TyCParser.INT_LIT, TyCParser.FLOAT_LIT, TyCParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.expr()
                pass
            elif token in [TyCParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(TyCParser.Assign_lhsContext,0)


        def ASSIGNMENT(self):
            return self.getToken(TyCParser.ASSIGNMENT, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def prefix_expr(self):
            return self.getTypedRuleContext(TyCParser.Prefix_exprContext,0)


        def INCREMENT(self):
            return self.getToken(TyCParser.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(TyCParser.DECREMENT, 0)

        def postfix_expr(self):
            return self.getTypedRuleContext(TyCParser.Postfix_exprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_update




    def update(self):

        localctx = TyCParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_update)
        self._la = 0 # Token type
        try:
            self.state = 517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.assign_lhs()
                self.state = 508
                self.match(TyCParser.ASSIGNMENT)
                self.state = 509
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 511
                _la = self._input.LA(1)
                if not(_la==TyCParser.INCREMENT or _la==TyCParser.DECREMENT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 512
                self.prefix_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 513
                self.postfix_expr(0)
                self.state = 514
                _la = self._input.LA(1)
                if not(_la==TyCParser.INCREMENT or _la==TyCParser.DECREMENT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(TyCParser.SWITCH, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def LEFT_BRACE(self):
            return self.getToken(TyCParser.LEFT_BRACE, 0)

        def switch_body(self):
            return self.getTypedRuleContext(TyCParser.Switch_bodyContext,0)


        def RIGHT_BRACE(self):
            return self.getToken(TyCParser.RIGHT_BRACE, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_switch_stmt




    def switch_stmt(self):

        localctx = TyCParser.Switch_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_switch_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(TyCParser.SWITCH)
            self.state = 520
            self.match(TyCParser.LEFT_PAREN)
            self.state = 521
            self.expr()
            self.state = 522
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 523
            self.match(TyCParser.LEFT_BRACE)
            self.state = 524
            self.switch_body()
            self.state = 525
            self.match(TyCParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def case_list(self):
            return self.getTypedRuleContext(TyCParser.Case_listContext,0)


        def case_list_branch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.Case_list_branchContext)
            else:
                return self.getTypedRuleContext(TyCParser.Case_list_branchContext,i)


        def DEFAULT(self):
            return self.getToken(TyCParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(TyCParser.COLON, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(TyCParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_switch_body




    def switch_body(self):

        localctx = TyCParser.Switch_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_switch_body)
        try:
            self.state = 535
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.case_list(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 528
                self.case_list_branch()
                self.state = 529
                self.match(TyCParser.DEFAULT)
                self.state = 530
                self.match(TyCParser.COLON)
                self.state = 531
                self.stmt_list(0)
                self.state = 532
                self.case_list_branch()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_list_branchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def case_list(self):
            return self.getTypedRuleContext(TyCParser.Case_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_case_list_branch




    def case_list_branch(self):

        localctx = TyCParser.Case_list_branchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_case_list_branch)
        try:
            self.state = 539
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 537
                self.case_list(0)
                pass
            elif token in [TyCParser.DEFAULT, TyCParser.RIGHT_BRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def case_stmt(self):
            return self.getTypedRuleContext(TyCParser.Case_stmtContext,0)


        def case_list(self):
            return self.getTypedRuleContext(TyCParser.Case_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_case_list



    def case_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Case_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_case_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.case_stmt()
            self._ctx.stop = self._input.LT(-1)
            self.state = 548
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Case_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_case_list)
                    self.state = 544
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 545
                    self.case_stmt() 
                self.state = 550
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Case_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(TyCParser.CASE, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def COLON(self):
            return self.getToken(TyCParser.COLON, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(TyCParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_case_stmt




    def case_stmt(self):

        localctx = TyCParser.Case_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_case_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.match(TyCParser.CASE)
            self.state = 552
            self.expr()
            self.state = 553
            self.match(TyCParser.COLON)
            self.state = 554
            self.stmt_list(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(TyCParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_break_stmt




    def break_stmt(self):

        localctx = TyCParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.match(TyCParser.BREAK)
            self.state = 557
            self.match(TyCParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(TyCParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = TyCParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(TyCParser.CONTINUE)
            self.state = 560
            self.match(TyCParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(TyCParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_return_stmt




    def return_stmt(self):

        localctx = TyCParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.match(TyCParser.RETURN)
            self.state = 565
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.ADDITION, TyCParser.SUBTRACTION, TyCParser.LOGICAL_NOT, TyCParser.LEFT_BRACE, TyCParser.LEFT_PAREN, TyCParser.ID, TyCParser.INT_LIT, TyCParser.FLOAT_LIT, TyCParser.STRING_LIT]:
                self.state = 563
                self.expr()
                pass
            elif token in [TyCParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 567
            self.match(TyCParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_expr_stmt




    def expr_stmt(self):

        localctx = TyCParser.Expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_expr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.expr()
            self.state = 570
            self.match(TyCParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.decl_list_sempred
        self._predicates[8] = self.struct_member_list_sempred
        self._predicates[11] = self.struct_var_decl_list_exist_sempred
        self._predicates[13] = self.struct_var_member_list_sempred
        self._predicates[15] = self.var_decl_list_sempred
        self._predicates[22] = self.expr_list_exist_sempred
        self._predicates[26] = self.or_expr_sempred
        self._predicates[27] = self.and_expr_sempred
        self._predicates[28] = self.eq_expr_sempred
        self._predicates[29] = self.relational_expr_sempred
        self._predicates[30] = self.add_sub_expr_sempred
        self._predicates[31] = self.multi_div_mod_expr_sempred
        self._predicates[34] = self.postfix_expr_sempred
        self._predicates[35] = self.member_access_expr_sempred
        self._predicates[40] = self.stmt_list_sempred
        self._predicates[53] = self.case_list_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def decl_list_sempred(self, localctx:Decl_listContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def struct_member_list_sempred(self, localctx:Struct_member_listContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def struct_var_decl_list_exist_sempred(self, localctx:Struct_var_decl_list_existContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def struct_var_member_list_sempred(self, localctx:Struct_var_member_listContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def var_decl_list_sempred(self, localctx:Var_decl_listContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr_list_exist_sempred(self, localctx:Expr_list_existContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def or_expr_sempred(self, localctx:Or_exprContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def and_expr_sempred(self, localctx:And_exprContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def eq_expr_sempred(self, localctx:Eq_exprContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def relational_expr_sempred(self, localctx:Relational_exprContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def add_sub_expr_sempred(self, localctx:Add_sub_exprContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         

    def multi_div_mod_expr_sempred(self, localctx:Multi_div_mod_exprContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

    def postfix_expr_sempred(self, localctx:Postfix_exprContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         

    def member_access_expr_sempred(self, localctx:Member_access_exprContext, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         

    def stmt_list_sempred(self, localctx:Stmt_listContext, predIndex:int):
            if predIndex == 14:
                return self.precpred(self._ctx, 2)
         

    def case_list_sempred(self, localctx:Case_listContext, predIndex:int):
            if predIndex == 15:
                return self.precpred(self._ctx, 2)
         




