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
        buf.write("\u0239\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\3\2\3\2\3\2\3\3\3\3\3\3\7\3}\n\3\f\3\16\3\u0080\13\3")
        buf.write("\3\4\3\4\5\4\u0084\n\4\3\5\3\5\3\5\5\5\u0089\n\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\5\6\u0095\n\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\5\7\u009c\n\7\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\7\n\u00ab\n\n\f\n\16\n\u00ae")
        buf.write("\13\n\3\13\3\13\3\13\3\13\3\f\3\f\5\f\u00b6\n\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\7\r\u00be\n\r\f\r\16\r\u00c1\13\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00cc")
        buf.write("\n\16\3\16\3\16\5\16\u00d0\n\16\3\17\3\17\3\17\3\17\7")
        buf.write("\17\u00d6\n\17\f\17\16\17\u00d9\13\17\3\20\3\20\5\20\u00dd")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\7\21\u00e4\n\21\f\21\16")
        buf.write("\21\u00e7\13\21\3\22\3\22\5\22\u00eb\n\22\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00f6\n\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0102")
        buf.write("\n\24\3\25\3\25\5\25\u0106\n\25\3\26\3\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\7\27\u0110\n\27\f\27\16\27\u0113\13")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\5\30\u011a\n\30\3\31\3\31")
        buf.write("\5\31\u011e\n\31\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u0126")
        buf.write("\n\32\f\32\16\32\u0129\13\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\7\33\u0131\n\33\f\33\16\33\u0134\13\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\7\34\u013c\n\34\f\34\16\34\u013f")
        buf.write("\13\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0147\n\35\f")
        buf.write("\35\16\35\u014a\13\35\3\36\3\36\3\36\3\36\3\36\3\36\7")
        buf.write("\36\u0152\n\36\f\36\16\36\u0155\13\36\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\7\37\u015d\n\37\f\37\16\37\u0160\13\37\3")
        buf.write(" \3 \3 \5 \u0165\n \3!\3!\3!\5!\u016a\n!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\7\"\u0171\n\"\f\"\16\"\u0174\13\"\3#\3#\3#\3#\3")
        buf.write("#\3#\7#\u017c\n#\f#\16#\u017f\13#\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\5$\u0188\n$\3%\3%\3%\5%\u018d\n%\3%\3%\3&\3&\3&\3&\5")
        buf.write("&\u0195\n&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\7(\u01a0\n(")
        buf.write("\f(\16(\u01a3\13(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u01af")
        buf.write("\n)\3*\3*\3+\3+\3+\5+\u01b6\n+\3+\3+\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u01db\n,\3-\3-\3-\3-\3")
        buf.write("-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\5\60\u01f5\n\60\3\61\3\61\5\61\u01f9\n")
        buf.write("\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u0202\n\62")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\5\64\u0214\n\64\3\65\3\65\5")
        buf.write("\65\u0218\n\65\3\66\3\66\3\66\3\66\3\66\7\66\u021f\n\66")
        buf.write("\f\66\16\66\u0222\13\66\3\67\3\67\3\67\3\67\3\67\38\3")
        buf.write("8\38\39\39\39\3:\3:\3:\5:\u0232\n:\3:\3:\3;\3;\3;\3;\2")
        buf.write("\22\4\22\30\34 ,\62\64\668:<BDNj<\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprt\2\t\5\2\13\13\16\16\20\20\3\2\34\35")
        buf.write("\3\2\36!\3\2\27\30\3\2\31\33\4\2\27\30$$\3\2\25\26\2\u0240")
        buf.write("\2v\3\2\2\2\4y\3\2\2\2\6\u0083\3\2\2\2\b\u0088\3\2\2\2")
        buf.write("\n\u0094\3\2\2\2\f\u009b\3\2\2\2\16\u009d\3\2\2\2\20\u00a0")
        buf.write("\3\2\2\2\22\u00a7\3\2\2\2\24\u00af\3\2\2\2\26\u00b5\3")
        buf.write("\2\2\2\30\u00b7\3\2\2\2\32\u00cf\3\2\2\2\34\u00d1\3\2")
        buf.write("\2\2\36\u00dc\3\2\2\2 \u00de\3\2\2\2\"\u00ea\3\2\2\2$")
        buf.write("\u00f5\3\2\2\2&\u0101\3\2\2\2(\u0105\3\2\2\2*\u0107\3")
        buf.write("\2\2\2,\u0109\3\2\2\2.\u0119\3\2\2\2\60\u011d\3\2\2\2")
        buf.write("\62\u011f\3\2\2\2\64\u012a\3\2\2\2\66\u0135\3\2\2\28\u0140")
        buf.write("\3\2\2\2:\u014b\3\2\2\2<\u0156\3\2\2\2>\u0164\3\2\2\2")
        buf.write("@\u0169\3\2\2\2B\u016b\3\2\2\2D\u0175\3\2\2\2F\u0187\3")
        buf.write("\2\2\2H\u0189\3\2\2\2J\u0190\3\2\2\2L\u0198\3\2\2\2N\u019c")
        buf.write("\3\2\2\2P\u01ae\3\2\2\2R\u01b0\3\2\2\2T\u01b2\3\2\2\2")
        buf.write("V\u01b9\3\2\2\2X\u01dc\3\2\2\2Z\u01e2\3\2\2\2\\\u01eb")
        buf.write("\3\2\2\2^\u01f4\3\2\2\2`\u01f8\3\2\2\2b\u0201\3\2\2\2")
        buf.write("d\u0203\3\2\2\2f\u0213\3\2\2\2h\u0217\3\2\2\2j\u0219\3")
        buf.write("\2\2\2l\u0223\3\2\2\2n\u0228\3\2\2\2p\u022b\3\2\2\2r\u022e")
        buf.write("\3\2\2\2t\u0235\3\2\2\2vw\5\4\3\2wx\7\2\2\3x\3\3\2\2\2")
        buf.write("y~\b\3\1\2z{\f\4\2\2{}\5\6\4\2|z\3\2\2\2}\u0080\3\2\2")
        buf.write("\2~|\3\2\2\2~\177\3\2\2\2\177\5\3\2\2\2\u0080~\3\2\2\2")
        buf.write("\u0081\u0084\5\b\5\2\u0082\u0084\5\20\t\2\u0083\u0081")
        buf.write("\3\2\2\2\u0083\u0082\3\2\2\2\u0084\7\3\2\2\2\u0085\u0089")
        buf.write("\5(\25\2\u0086\u0089\7\23\2\2\u0087\u0089\3\2\2\2\u0088")
        buf.write("\u0085\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0087\3\2\2\2")
        buf.write("\u0089\u008a\3\2\2\2\u008a\u008b\7.\2\2\u008b\u008c\7")
        buf.write(")\2\2\u008c\u008d\5\n\6\2\u008d\u008e\7*\2\2\u008e\u008f")
        buf.write("\7\'\2\2\u008f\u0090\5N(\2\u0090\u0091\7(\2\2\u0091\t")
        buf.write("\3\2\2\2\u0092\u0095\5\f\7\2\u0093\u0095\3\2\2\2\u0094")
        buf.write("\u0092\3\2\2\2\u0094\u0093\3\2\2\2\u0095\13\3\2\2\2\u0096")
        buf.write("\u0097\5\16\b\2\u0097\u0098\7,\2\2\u0098\u0099\5\f\7\2")
        buf.write("\u0099\u009c\3\2\2\2\u009a\u009c\5\16\b\2\u009b\u0096")
        buf.write("\3\2\2\2\u009b\u009a\3\2\2\2\u009c\r\3\2\2\2\u009d\u009e")
        buf.write("\5(\25\2\u009e\u009f\7.\2\2\u009f\17\3\2\2\2\u00a0\u00a1")
        buf.write("\7\21\2\2\u00a1\u00a2\7.\2\2\u00a2\u00a3\7\'\2\2\u00a3")
        buf.write("\u00a4\5\22\n\2\u00a4\u00a5\7(\2\2\u00a5\u00a6\7+\2\2")
        buf.write("\u00a6\21\3\2\2\2\u00a7\u00ac\b\n\1\2\u00a8\u00a9\f\4")
        buf.write("\2\2\u00a9\u00ab\5\24\13\2\u00aa\u00a8\3\2\2\2\u00ab\u00ae")
        buf.write("\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\23\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b0\5(\25\2\u00b0")
        buf.write("\u00b1\7.\2\2\u00b1\u00b2\7+\2\2\u00b2\25\3\2\2\2\u00b3")
        buf.write("\u00b6\5\30\r\2\u00b4\u00b6\3\2\2\2\u00b5\u00b3\3\2\2")
        buf.write("\2\u00b5\u00b4\3\2\2\2\u00b6\27\3\2\2\2\u00b7\u00b8\b")
        buf.write("\r\1\2\u00b8\u00b9\5\32\16\2\u00b9\u00bf\3\2\2\2\u00ba")
        buf.write("\u00bb\f\4\2\2\u00bb\u00bc\7,\2\2\u00bc\u00be\5\32\16")
        buf.write("\2\u00bd\u00ba\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00bd")
        buf.write("\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\31\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c2\u00c3\7.\2\2\u00c3\u00c4\7.\2\2\u00c4\u00d0")
        buf.write("\7+\2\2\u00c5\u00c6\7.\2\2\u00c6\u00c7\7.\2\2\u00c7\u00c8")
        buf.write("\7%\2\2\u00c8\u00cb\7\'\2\2\u00c9\u00cc\5\34\17\2\u00ca")
        buf.write("\u00cc\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca\3\2\2\2")
        buf.write("\u00cc\u00cd\3\2\2\2\u00cd\u00ce\7(\2\2\u00ce\u00d0\7")
        buf.write("+\2\2\u00cf\u00c2\3\2\2\2\u00cf\u00c5\3\2\2\2\u00d0\33")
        buf.write("\3\2\2\2\u00d1\u00d7\b\17\1\2\u00d2\u00d3\f\4\2\2\u00d3")
        buf.write("\u00d4\7,\2\2\u00d4\u00d6\5\36\20\2\u00d5\u00d2\3\2\2")
        buf.write("\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8")
        buf.write("\3\2\2\2\u00d8\35\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00dd")
        buf.write("\5F$\2\u00db\u00dd\5J&\2\u00dc\u00da\3\2\2\2\u00dc\u00db")
        buf.write("\3\2\2\2\u00dd\37\3\2\2\2\u00de\u00df\b\21\1\2\u00df\u00e0")
        buf.write("\5\"\22\2\u00e0\u00e5\3\2\2\2\u00e1\u00e2\f\4\2\2\u00e2")
        buf.write("\u00e4\5\"\22\2\u00e3\u00e1\3\2\2\2\u00e4\u00e7\3\2\2")
        buf.write("\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6!\3\2")
        buf.write("\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00eb\5$\23\2\u00e9\u00eb")
        buf.write("\5&\24\2\u00ea\u00e8\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb")
        buf.write("#\3\2\2\2\u00ec\u00ed\7\5\2\2\u00ed\u00ee\7.\2\2\u00ee")
        buf.write("\u00f6\7+\2\2\u00ef\u00f0\7\5\2\2\u00f0\u00f1\7.\2\2\u00f1")
        buf.write("\u00f2\7%\2\2\u00f2\u00f3\5.\30\2\u00f3\u00f4\7+\2\2\u00f4")
        buf.write("\u00f6\3\2\2\2\u00f5\u00ec\3\2\2\2\u00f5\u00ef\3\2\2\2")
        buf.write("\u00f6%\3\2\2\2\u00f7\u00f8\5(\25\2\u00f8\u00f9\7.\2\2")
        buf.write("\u00f9\u00fa\7+\2\2\u00fa\u0102\3\2\2\2\u00fb\u00fc\5")
        buf.write("(\25\2\u00fc\u00fd\7.\2\2\u00fd\u00fe\7%\2\2\u00fe\u00ff")
        buf.write("\5.\30\2\u00ff\u0100\7+\2\2\u0100\u0102\3\2\2\2\u0101")
        buf.write("\u00f7\3\2\2\2\u0101\u00fb\3\2\2\2\u0102\'\3\2\2\2\u0103")
        buf.write("\u0106\5*\26\2\u0104\u0106\7.\2\2\u0105\u0103\3\2\2\2")
        buf.write("\u0105\u0104\3\2\2\2\u0106)\3\2\2\2\u0107\u0108\t\2\2")
        buf.write("\2\u0108+\3\2\2\2\u0109\u010a\b\27\1\2\u010a\u010b\5.")
        buf.write("\30\2\u010b\u0111\3\2\2\2\u010c\u010d\f\4\2\2\u010d\u010e")
        buf.write("\7,\2\2\u010e\u0110\5.\30\2\u010f\u010c\3\2\2\2\u0110")
        buf.write("\u0113\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2")
        buf.write("\u0112-\3\2\2\2\u0113\u0111\3\2\2\2\u0114\u0115\5\60\31")
        buf.write("\2\u0115\u0116\7%\2\2\u0116\u0117\5.\30\2\u0117\u011a")
        buf.write("\3\2\2\2\u0118\u011a\5\62\32\2\u0119\u0114\3\2\2\2\u0119")
        buf.write("\u0118\3\2\2\2\u011a/\3\2\2\2\u011b\u011e\7.\2\2\u011c")
        buf.write("\u011e\5D#\2\u011d\u011b\3\2\2\2\u011d\u011c\3\2\2\2\u011e")
        buf.write("\61\3\2\2\2\u011f\u0120\b\32\1\2\u0120\u0121\5\64\33\2")
        buf.write("\u0121\u0127\3\2\2\2\u0122\u0123\f\4\2\2\u0123\u0124\7")
        buf.write("\"\2\2\u0124\u0126\5\64\33\2\u0125\u0122\3\2\2\2\u0126")
        buf.write("\u0129\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2")
        buf.write("\u0128\63\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012b\b\33")
        buf.write("\1\2\u012b\u012c\5\66\34\2\u012c\u0132\3\2\2\2\u012d\u012e")
        buf.write("\f\4\2\2\u012e\u012f\7#\2\2\u012f\u0131\5\66\34\2\u0130")
        buf.write("\u012d\3\2\2\2\u0131\u0134\3\2\2\2\u0132\u0130\3\2\2\2")
        buf.write("\u0132\u0133\3\2\2\2\u0133\65\3\2\2\2\u0134\u0132\3\2")
        buf.write("\2\2\u0135\u0136\b\34\1\2\u0136\u0137\58\35\2\u0137\u013d")
        buf.write("\3\2\2\2\u0138\u0139\f\4\2\2\u0139\u013a\t\3\2\2\u013a")
        buf.write("\u013c\58\35\2\u013b\u0138\3\2\2\2\u013c\u013f\3\2\2\2")
        buf.write("\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e\67\3\2")
        buf.write("\2\2\u013f\u013d\3\2\2\2\u0140\u0141\b\35\1\2\u0141\u0142")
        buf.write("\5:\36\2\u0142\u0148\3\2\2\2\u0143\u0144\f\4\2\2\u0144")
        buf.write("\u0145\t\4\2\2\u0145\u0147\5:\36\2\u0146\u0143\3\2\2\2")
        buf.write("\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3")
        buf.write("\2\2\2\u01499\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014c")
        buf.write("\b\36\1\2\u014c\u014d\5<\37\2\u014d\u0153\3\2\2\2\u014e")
        buf.write("\u014f\f\4\2\2\u014f\u0150\t\5\2\2\u0150\u0152\5<\37\2")
        buf.write("\u0151\u014e\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3")
        buf.write("\2\2\2\u0153\u0154\3\2\2\2\u0154;\3\2\2\2\u0155\u0153")
        buf.write("\3\2\2\2\u0156\u0157\b\37\1\2\u0157\u0158\5> \2\u0158")
        buf.write("\u015e\3\2\2\2\u0159\u015a\f\4\2\2\u015a\u015b\t\6\2\2")
        buf.write("\u015b\u015d\5> \2\u015c\u0159\3\2\2\2\u015d\u0160\3\2")
        buf.write("\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f=\3")
        buf.write("\2\2\2\u0160\u015e\3\2\2\2\u0161\u0162\t\7\2\2\u0162\u0165")
        buf.write("\5> \2\u0163\u0165\5@!\2\u0164\u0161\3\2\2\2\u0164\u0163")
        buf.write("\3\2\2\2\u0165?\3\2\2\2\u0166\u0167\t\b\2\2\u0167\u016a")
        buf.write("\5@!\2\u0168\u016a\5B\"\2\u0169\u0166\3\2\2\2\u0169\u0168")
        buf.write("\3\2\2\2\u016aA\3\2\2\2\u016b\u016c\b\"\1\2\u016c\u016d")
        buf.write("\5D#\2\u016d\u0172\3\2\2\2\u016e\u016f\f\4\2\2\u016f\u0171")
        buf.write("\t\b\2\2\u0170\u016e\3\2\2\2\u0171\u0174\3\2\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173C\3\2\2\2\u0174")
        buf.write("\u0172\3\2\2\2\u0175\u0176\b#\1\2\u0176\u0177\5F$\2\u0177")
        buf.write("\u017d\3\2\2\2\u0178\u0179\f\4\2\2\u0179\u017a\7&\2\2")
        buf.write("\u017a\u017c\7.\2\2\u017b\u0178\3\2\2\2\u017c\u017f\3")
        buf.write("\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017eE")
        buf.write("\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0188\7/\2\2\u0181")
        buf.write("\u0188\7\60\2\2\u0182\u0188\7\61\2\2\u0183\u0188\5H%\2")
        buf.write("\u0184\u0188\5J&\2\u0185\u0188\5L\'\2\u0186\u0188\7.\2")
        buf.write("\2\u0187\u0180\3\2\2\2\u0187\u0181\3\2\2\2\u0187\u0182")
        buf.write("\3\2\2\2\u0187\u0183\3\2\2\2\u0187\u0184\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0187\u0186\3\2\2\2\u0188G\3\2\2\2\u0189")
        buf.write("\u018c\7\'\2\2\u018a\u018d\5,\27\2\u018b\u018d\3\2\2\2")
        buf.write("\u018c\u018a\3\2\2\2\u018c\u018b\3\2\2\2\u018d\u018e\3")
        buf.write("\2\2\2\u018e\u018f\7(\2\2\u018fI\3\2\2\2\u0190\u0191\7")
        buf.write(".\2\2\u0191\u0194\7)\2\2\u0192\u0195\5,\27\2\u0193\u0195")
        buf.write("\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0193\3\2\2\2\u0195")
        buf.write("\u0196\3\2\2\2\u0196\u0197\7*\2\2\u0197K\3\2\2\2\u0198")
        buf.write("\u0199\7)\2\2\u0199\u019a\5.\30\2\u019a\u019b\7*\2\2\u019b")
        buf.write("M\3\2\2\2\u019c\u01a1\b(\1\2\u019d\u019e\f\4\2\2\u019e")
        buf.write("\u01a0\5P)\2\u019f\u019d\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2O\3\2\2\2\u01a3")
        buf.write("\u01a1\3\2\2\2\u01a4\u01af\5R*\2\u01a5\u01af\5T+\2\u01a6")
        buf.write("\u01af\5V,\2\u01a7\u01af\5X-\2\u01a8\u01af\5Z.\2\u01a9")
        buf.write("\u01af\5d\63\2\u01aa\u01af\5n8\2\u01ab\u01af\5p9\2\u01ac")
        buf.write("\u01af\5r:\2\u01ad\u01af\5t;\2\u01ae\u01a4\3\2\2\2\u01ae")
        buf.write("\u01a5\3\2\2\2\u01ae\u01a6\3\2\2\2\u01ae\u01a7\3\2\2\2")
        buf.write("\u01ae\u01a8\3\2\2\2\u01ae\u01a9\3\2\2\2\u01ae\u01aa\3")
        buf.write("\2\2\2\u01ae\u01ab\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01ad")
        buf.write("\3\2\2\2\u01afQ\3\2\2\2\u01b0\u01b1\5\"\22\2\u01b1S\3")
        buf.write("\2\2\2\u01b2\u01b5\7\'\2\2\u01b3\u01b6\5 \21\2\u01b4\u01b6")
        buf.write("\5N(\2\u01b5\u01b3\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6\u01b7")
        buf.write("\3\2\2\2\u01b7\u01b8\7(\2\2\u01b8U\3\2\2\2\u01b9\u01ba")
        buf.write("\7\r\2\2\u01ba\u01bb\7)\2\2\u01bb\u01bc\5.\30\2\u01bc")
        buf.write("\u01da\7*\2\2\u01bd\u01be\7\'\2\2\u01be\u01bf\5P)\2\u01bf")
        buf.write("\u01c0\7(\2\2\u01c0\u01db\3\2\2\2\u01c1\u01c2\7\'\2\2")
        buf.write("\u01c2\u01c3\5P)\2\u01c3\u01c4\7(\2\2\u01c4\u01c5\7\n")
        buf.write("\2\2\u01c5\u01c6\7\'\2\2\u01c6\u01c7\5P)\2\u01c7\u01c8")
        buf.write("\7(\2\2\u01c8\u01db\3\2\2\2\u01c9\u01db\5P)\2\u01ca\u01cb")
        buf.write("\5P)\2\u01cb\u01cc\7\n\2\2\u01cc\u01cd\5P)\2\u01cd\u01db")
        buf.write("\3\2\2\2\u01ce\u01cf\7\'\2\2\u01cf\u01d0\5P)\2\u01d0\u01d1")
        buf.write("\7(\2\2\u01d1\u01d2\7\n\2\2\u01d2\u01d3\5P)\2\u01d3\u01db")
        buf.write("\3\2\2\2\u01d4\u01d5\5P)\2\u01d5\u01d6\7\n\2\2\u01d6\u01d7")
        buf.write("\7\'\2\2\u01d7\u01d8\5P)\2\u01d8\u01d9\7(\2\2\u01d9\u01db")
        buf.write("\3\2\2\2\u01da\u01bd\3\2\2\2\u01da\u01c1\3\2\2\2\u01da")
        buf.write("\u01c9\3\2\2\2\u01da\u01ca\3\2\2\2\u01da\u01ce\3\2\2\2")
        buf.write("\u01da\u01d4\3\2\2\2\u01dbW\3\2\2\2\u01dc\u01dd\7\24\2")
        buf.write("\2\u01dd\u01de\7)\2\2\u01de\u01df\5.\30\2\u01df\u01e0")
        buf.write("\7*\2\2\u01e0\u01e1\5P)\2\u01e1Y\3\2\2\2\u01e2\u01e3\7")
        buf.write("\f\2\2\u01e3\u01e4\7)\2\2\u01e4\u01e5\5^\60\2\u01e5\u01e6")
        buf.write("\5`\61\2\u01e6\u01e7\7+\2\2\u01e7\u01e8\5b\62\2\u01e8")
        buf.write("\u01e9\7*\2\2\u01e9\u01ea\5P)\2\u01ea[\3\2\2\2\u01eb\u01ec")
        buf.write("\5\60\31\2\u01ec\u01ed\7%\2\2\u01ed\u01ee\5.\30\2\u01ee")
        buf.write("]\3\2\2\2\u01ef\u01f5\5\"\22\2\u01f0\u01f1\5\\/\2\u01f1")
        buf.write("\u01f2\7+\2\2\u01f2\u01f5\3\2\2\2\u01f3\u01f5\7+\2\2\u01f4")
        buf.write("\u01ef\3\2\2\2\u01f4\u01f0\3\2\2\2\u01f4\u01f3\3\2\2\2")
        buf.write("\u01f5_\3\2\2\2\u01f6\u01f9\5.\30\2\u01f7\u01f9\3\2\2")
        buf.write("\2\u01f8\u01f6\3\2\2\2\u01f8\u01f7\3\2\2\2\u01f9a\3\2")
        buf.write("\2\2\u01fa\u0202\5\\/\2\u01fb\u01fc\t\b\2\2\u01fc\u0202")
        buf.write("\5@!\2\u01fd\u01fe\5B\"\2\u01fe\u01ff\t\b\2\2\u01ff\u0202")
        buf.write("\3\2\2\2\u0200\u0202\3\2\2\2\u0201\u01fa\3\2\2\2\u0201")
        buf.write("\u01fb\3\2\2\2\u0201\u01fd\3\2\2\2\u0201\u0200\3\2\2\2")
        buf.write("\u0202c\3\2\2\2\u0203\u0204\7\22\2\2\u0204\u0205\7)\2")
        buf.write("\2\u0205\u0206\5.\30\2\u0206\u0207\7*\2\2\u0207\u0208")
        buf.write("\7\'\2\2\u0208\u0209\5f\64\2\u0209\u020a\7(\2\2\u020a")
        buf.write("e\3\2\2\2\u020b\u0214\5j\66\2\u020c\u020d\5h\65\2\u020d")
        buf.write("\u020e\7\t\2\2\u020e\u020f\7-\2\2\u020f\u0210\5N(\2\u0210")
        buf.write("\u0211\5h\65\2\u0211\u0214\3\2\2\2\u0212\u0214\3\2\2\2")
        buf.write("\u0213\u020b\3\2\2\2\u0213\u020c\3\2\2\2\u0213\u0212\3")
        buf.write("\2\2\2\u0214g\3\2\2\2\u0215\u0218\5j\66\2\u0216\u0218")
        buf.write("\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0216\3\2\2\2\u0218")
        buf.write("i\3\2\2\2\u0219\u021a\b\66\1\2\u021a\u021b\5l\67\2\u021b")
        buf.write("\u0220\3\2\2\2\u021c\u021d\f\4\2\2\u021d\u021f\5l\67\2")
        buf.write("\u021e\u021c\3\2\2\2\u021f\u0222\3\2\2\2\u0220\u021e\3")
        buf.write("\2\2\2\u0220\u0221\3\2\2\2\u0221k\3\2\2\2\u0222\u0220")
        buf.write("\3\2\2\2\u0223\u0224\7\7\2\2\u0224\u0225\5.\30\2\u0225")
        buf.write("\u0226\7-\2\2\u0226\u0227\5N(\2\u0227m\3\2\2\2\u0228\u0229")
        buf.write("\7\6\2\2\u0229\u022a\7+\2\2\u022ao\3\2\2\2\u022b\u022c")
        buf.write("\7\b\2\2\u022c\u022d\7+\2\2\u022dq\3\2\2\2\u022e\u0231")
        buf.write("\7\17\2\2\u022f\u0232\5.\30\2\u0230\u0232\3\2\2\2\u0231")
        buf.write("\u022f\3\2\2\2\u0231\u0230\3\2\2\2\u0232\u0233\3\2\2\2")
        buf.write("\u0233\u0234\7+\2\2\u0234s\3\2\2\2\u0235\u0236\5.\30\2")
        buf.write("\u0236\u0237\7+\2\2\u0237u\3\2\2\2.~\u0083\u0088\u0094")
        buf.write("\u009b\u00ac\u00b5\u00bf\u00cb\u00cf\u00d7\u00dc\u00e5")
        buf.write("\u00ea\u00f5\u0101\u0105\u0111\u0119\u011d\u0127\u0132")
        buf.write("\u013d\u0148\u0153\u015e\u0164\u0169\u0172\u017d\u0187")
        buf.write("\u018c\u0194\u01a1\u01ae\u01b5\u01da\u01f4\u01f8\u0201")
        buf.write("\u0213\u0217\u0220\u0231")
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
    RULE_expr = 22
    RULE_assign_lhs = 23
    RULE_or_expr = 24
    RULE_and_expr = 25
    RULE_eq_expr = 26
    RULE_relational_expr = 27
    RULE_add_sub_expr = 28
    RULE_multi_div_mod_expr = 29
    RULE_unary_expr = 30
    RULE_prefix_expr = 31
    RULE_postfix_expr = 32
    RULE_member_access_expr = 33
    RULE_operand = 34
    RULE_struct_lit = 35
    RULE_func_call_expr = 36
    RULE_paren_expr = 37
    RULE_stmt_list = 38
    RULE_stmt = 39
    RULE_var_decl_stmt = 40
    RULE_block_stmt = 41
    RULE_if_stmt = 42
    RULE_while_stmt = 43
    RULE_for_stmt = 44
    RULE_assign_for = 45
    RULE_init = 46
    RULE_condition = 47
    RULE_update = 48
    RULE_switch_stmt = 49
    RULE_switch_body = 50
    RULE_case_list_branch = 51
    RULE_case_list = 52
    RULE_case_stmt = 53
    RULE_break_stmt = 54
    RULE_continue_stmt = 55
    RULE_return_stmt = 56
    RULE_expr_stmt = 57

    ruleNames =  [ "program", "decl_list", "decl", "func_decl", "param_list", 
                   "param_list_exist", "param_decl", "struct_decl", "struct_member_list", 
                   "struct_member", "struct_var_decl_list", "struct_var_decl_list_exist", 
                   "struct_var_decl", "struct_var_member_list", "struct_var_member", 
                   "var_decl_list", "var_decl", "auto_var_decl", "explicit_var_decl", 
                   "typ", "primitive_typ", "expr_list", "expr", "assign_lhs", 
                   "or_expr", "and_expr", "eq_expr", "relational_expr", 
                   "add_sub_expr", "multi_div_mod_expr", "unary_expr", "prefix_expr", 
                   "postfix_expr", "member_access_expr", "operand", "struct_lit", 
                   "func_call_expr", "paren_expr", "stmt_list", "stmt", 
                   "var_decl_stmt", "block_stmt", "if_stmt", "while_stmt", 
                   "for_stmt", "assign_for", "init", "condition", "update", 
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
            self.state = 116
            self.decl_list(0)
            self.state = 117
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
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Decl_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_decl_list)
                    self.state = 120
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 121
                    self.decl() 
                self.state = 126
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
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.VOID, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.func_decl()
                pass
            elif token in [TyCParser.STRUCT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
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
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 131
                self.typ()
                pass

            elif la_ == 2:
                self.state = 132
                self.match(TyCParser.VOID)
                pass

            elif la_ == 3:
                pass


            self.state = 136
            self.match(TyCParser.ID)
            self.state = 137
            self.match(TyCParser.LEFT_PAREN)
            self.state = 138
            self.param_list()
            self.state = 139
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 140
            self.match(TyCParser.LEFT_BRACE)
            self.state = 141
            self.stmt_list(0)
            self.state = 142
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
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
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
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.param_decl()
                self.state = 149
                self.match(TyCParser.COMMA)
                self.state = 150
                self.param_list_exist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
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
            self.state = 155
            self.typ()
            self.state = 156
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
            self.state = 158
            self.match(TyCParser.STRUCT)
            self.state = 159
            self.match(TyCParser.ID)
            self.state = 160
            self.match(TyCParser.LEFT_BRACE)
            self.state = 161
            self.struct_member_list(0)
            self.state = 162
            self.match(TyCParser.RIGHT_BRACE)
            self.state = 163
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
            self.state = 170
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Struct_member_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_member_list)
                    self.state = 166
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 167
                    self.struct_member() 
                self.state = 172
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
            self.state = 173
            self.typ()
            self.state = 174
            self.match(TyCParser.ID)
            self.state = 175
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
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
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
            self.state = 182
            self.struct_var_decl()
            self._ctx.stop = self._input.LT(-1)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Struct_var_decl_list_existContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_var_decl_list_exist)
                    self.state = 184
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 185
                    self.match(TyCParser.COMMA)
                    self.state = 186
                    self.struct_var_decl() 
                self.state = 191
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
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(TyCParser.ID)
                self.state = 193
                self.match(TyCParser.ID)
                self.state = 194
                self.match(TyCParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.match(TyCParser.ID)
                self.state = 196
                self.match(TyCParser.ID)
                self.state = 197
                self.match(TyCParser.ASSIGNMENT)
                self.state = 198
                self.match(TyCParser.LEFT_BRACE)
                self.state = 201
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 199
                    self.struct_var_member_list(0)
                    pass

                elif la_ == 2:
                    pass


                self.state = 203
                self.match(TyCParser.RIGHT_BRACE)
                self.state = 204
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
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Struct_var_member_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_var_member_list)
                    self.state = 208
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 209
                    self.match(TyCParser.COMMA)
                    self.state = 210
                    self.struct_var_member() 
                self.state = 215
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
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.operand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
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
            self.state = 221
            self.var_decl()
            self._ctx.stop = self._input.LT(-1)
            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Var_decl_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_var_decl_list)
                    self.state = 223
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 224
                    self.var_decl() 
                self.state = 229
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
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.AUTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.auto_var_decl()
                pass
            elif token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING, TyCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
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

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_auto_var_decl




    def auto_var_decl(self):

        localctx = TyCParser.Auto_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_auto_var_decl)
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(TyCParser.AUTO)
                self.state = 235
                self.match(TyCParser.ID)
                self.state = 236
                self.match(TyCParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.match(TyCParser.AUTO)
                self.state = 238
                self.match(TyCParser.ID)
                self.state = 239
                self.match(TyCParser.ASSIGNMENT)
                self.state = 240
                self.expr()
                self.state = 241
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

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_explicit_var_decl




    def explicit_var_decl(self):

        localctx = TyCParser.Explicit_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_explicit_var_decl)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.typ()
                self.state = 246
                self.match(TyCParser.ID)
                self.state = 247
                self.match(TyCParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.typ()
                self.state = 250
                self.match(TyCParser.ID)
                self.state = 251
                self.match(TyCParser.ASSIGNMENT)
                self.state = 252
                self.expr()
                self.state = 253
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
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.FLOAT, TyCParser.INT, TyCParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.primitive_typ()
                pass
            elif token in [TyCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
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
            self.state = 261
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

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def expr_list(self):
            return self.getTypedRuleContext(TyCParser.Expr_listContext,0)


        def COMMA(self):
            return self.getToken(TyCParser.COMMA, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_expr_list



    def expr_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.Expr_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 271
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Expr_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_list)
                    self.state = 266
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 267
                    self.match(TyCParser.COMMA)
                    self.state = 268
                    self.expr() 
                self.state = 273
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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

        def assign_lhs(self):
            return self.getTypedRuleContext(TyCParser.Assign_lhsContext,0)


        def ASSIGNMENT(self):
            return self.getToken(TyCParser.ASSIGNMENT, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def or_expr(self):
            return self.getTypedRuleContext(TyCParser.Or_exprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_expr




    def expr(self):

        localctx = TyCParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.assign_lhs()
                self.state = 275
                self.match(TyCParser.ASSIGNMENT)
                self.state = 276
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
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


        def getRuleIndex(self):
            return TyCParser.RULE_assign_lhs




    def assign_lhs(self):

        localctx = TyCParser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assign_lhs)
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.match(TyCParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.member_access_expr(0)
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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_or_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.and_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_or_expr)
                    self.state = 288
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 289
                    self.match(TyCParser.LOGICAL_OR)
                    self.state = 290
                    self.and_expr(0) 
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_and_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.eq_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.And_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_expr)
                    self.state = 299
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 300
                    self.match(TyCParser.LOGICAL_AND)
                    self.state = 301
                    self.eq_expr(0) 
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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_eq_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.relational_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Eq_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_eq_expr)
                    self.state = 310
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 311
                    _la = self._input.LA(1)
                    if not(_la==TyCParser.EQUAL or _la==TyCParser.NOT_EQUAL):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 312
                    self.relational_expr(0) 
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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_relational_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.add_sub_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Relational_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expr)
                    self.state = 321
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 322
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.LESS_THAN) | (1 << TyCParser.GREATER_THAN) | (1 << TyCParser.LESS_THAN_EQUAL) | (1 << TyCParser.GREATER_THAN_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 323
                    self.add_sub_expr(0) 
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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_add_sub_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.multi_div_mod_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 337
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Add_sub_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub_expr)
                    self.state = 332
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 333
                    _la = self._input.LA(1)
                    if not(_la==TyCParser.ADDITION or _la==TyCParser.SUBTRACTION):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 334
                    self.multi_div_mod_expr(0) 
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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_multi_div_mod_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.unary_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 348
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Multi_div_mod_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multi_div_mod_expr)
                    self.state = 343
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 344
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.MULTI) | (1 << TyCParser.DIVISION) | (1 << TyCParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 345
                    self.unary_expr() 
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
        self.enterRule(localctx, 60, self.RULE_unary_expr)
        self._la = 0 # Token type
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.ADDITION, TyCParser.SUBTRACTION, TyCParser.LOGICAL_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TyCParser.ADDITION) | (1 << TyCParser.SUBTRACTION) | (1 << TyCParser.LOGICAL_NOT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 352
                self.unary_expr()
                pass
            elif token in [TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.LEFT_BRACE, TyCParser.LEFT_PAREN, TyCParser.ID, TyCParser.INT_LIT, TyCParser.FLOAT_LIT, TyCParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
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
        self.enterRule(localctx, 62, self.RULE_prefix_expr)
        self._la = 0 # Token type
        try:
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INCREMENT, TyCParser.DECREMENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                _la = self._input.LA(1)
                if not(_la==TyCParser.INCREMENT or _la==TyCParser.DECREMENT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 357
                self.prefix_expr()
                pass
            elif token in [TyCParser.LEFT_BRACE, TyCParser.LEFT_PAREN, TyCParser.ID, TyCParser.INT_LIT, TyCParser.FLOAT_LIT, TyCParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_postfix_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.member_access_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Postfix_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix_expr)
                    self.state = 364
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 365
                    _la = self._input.LA(1)
                    if not(_la==TyCParser.INCREMENT or _la==TyCParser.DECREMENT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 370
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_member_access_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Member_access_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_member_access_expr)
                    self.state = 374
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 375
                    self.match(TyCParser.MEMBER_ACCESS)
                    self.state = 376
                    self.match(TyCParser.ID) 
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
        self.enterRule(localctx, 68, self.RULE_operand)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.match(TyCParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.match(TyCParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 384
                self.match(TyCParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 385
                self.struct_lit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 386
                self.func_call_expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 387
                self.paren_expr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 388
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

        def RIGHT_BRACE(self):
            return self.getToken(TyCParser.RIGHT_BRACE, 0)

        def expr_list(self):
            return self.getTypedRuleContext(TyCParser.Expr_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_struct_lit




    def struct_lit(self):

        localctx = TyCParser.Struct_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_struct_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(TyCParser.LEFT_BRACE)
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.ADDITION, TyCParser.SUBTRACTION, TyCParser.LOGICAL_NOT, TyCParser.LEFT_BRACE, TyCParser.LEFT_PAREN, TyCParser.ID, TyCParser.INT_LIT, TyCParser.FLOAT_LIT, TyCParser.STRING_LIT]:
                self.state = 392
                self.expr_list(0)
                pass
            elif token in [TyCParser.RIGHT_BRACE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 396
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

        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def expr_list(self):
            return self.getTypedRuleContext(TyCParser.Expr_listContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_func_call_expr




    def func_call_expr(self):

        localctx = TyCParser.Func_call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_func_call_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(TyCParser.ID)
            self.state = 399
            self.match(TyCParser.LEFT_PAREN)
            self.state = 402
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.ADDITION, TyCParser.SUBTRACTION, TyCParser.LOGICAL_NOT, TyCParser.LEFT_BRACE, TyCParser.LEFT_PAREN, TyCParser.ID, TyCParser.INT_LIT, TyCParser.FLOAT_LIT, TyCParser.STRING_LIT]:
                self.state = 400
                self.expr_list(0)
                pass
            elif token in [TyCParser.RIGHT_PAREN]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 404
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
        self.enterRule(localctx, 74, self.RULE_paren_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(TyCParser.LEFT_PAREN)
            self.state = 407
            self.expr()
            self.state = 408
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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_stmt_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self._ctx.stop = self._input.LT(-1)
            self.state = 415
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Stmt_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_stmt_list)
                    self.state = 411
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 412
                    self.stmt() 
                self.state = 417
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        self.enterRule(localctx, 78, self.RULE_stmt)
        try:
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.var_decl_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.block_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 420
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 421
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 422
                self.for_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 423
                self.switch_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 424
                self.break_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 425
                self.continue_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 426
                self.return_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 427
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
        self.enterRule(localctx, 80, self.RULE_var_decl_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
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
        self.enterRule(localctx, 82, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(TyCParser.LEFT_BRACE)
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 433
                self.var_decl_list(0)
                pass

            elif la_ == 2:
                self.state = 434
                self.stmt_list(0)
                pass


            self.state = 437
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
        self.enterRule(localctx, 84, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(TyCParser.IF)
            self.state = 440
            self.match(TyCParser.LEFT_PAREN)
            self.state = 441
            self.expr()
            self.state = 442
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 472
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 443
                self.match(TyCParser.LEFT_BRACE)
                self.state = 444
                self.stmt()
                self.state = 445
                self.match(TyCParser.RIGHT_BRACE)
                pass

            elif la_ == 2:
                self.state = 447
                self.match(TyCParser.LEFT_BRACE)
                self.state = 448
                self.stmt()
                self.state = 449
                self.match(TyCParser.RIGHT_BRACE)
                self.state = 450
                self.match(TyCParser.ELSE)
                self.state = 451
                self.match(TyCParser.LEFT_BRACE)
                self.state = 452
                self.stmt()
                self.state = 453
                self.match(TyCParser.RIGHT_BRACE)
                pass

            elif la_ == 3:
                self.state = 455
                self.stmt()
                pass

            elif la_ == 4:
                self.state = 456
                self.stmt()
                self.state = 457
                self.match(TyCParser.ELSE)
                self.state = 458
                self.stmt()
                pass

            elif la_ == 5:
                self.state = 460
                self.match(TyCParser.LEFT_BRACE)
                self.state = 461
                self.stmt()
                self.state = 462
                self.match(TyCParser.RIGHT_BRACE)
                self.state = 463
                self.match(TyCParser.ELSE)
                self.state = 464
                self.stmt()
                pass

            elif la_ == 6:
                self.state = 466
                self.stmt()
                self.state = 467
                self.match(TyCParser.ELSE)
                self.state = 468
                self.match(TyCParser.LEFT_BRACE)
                self.state = 469
                self.stmt()
                self.state = 470
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
        self.enterRule(localctx, 86, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(TyCParser.WHILE)
            self.state = 475
            self.match(TyCParser.LEFT_PAREN)
            self.state = 476
            self.expr()
            self.state = 477
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 478
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
        self.enterRule(localctx, 88, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(TyCParser.FOR)
            self.state = 481
            self.match(TyCParser.LEFT_PAREN)
            self.state = 482
            self.init()
            self.state = 483
            self.condition()
            self.state = 484
            self.match(TyCParser.SEMICOLON)
            self.state = 485
            self.update()
            self.state = 486
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 487
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_forContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return TyCParser.RULE_assign_for




    def assign_for(self):

        localctx = TyCParser.Assign_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_assign_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.assign_lhs()
            self.state = 490
            self.match(TyCParser.ASSIGNMENT)
            self.state = 491
            self.expr()
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


        def assign_for(self):
            return self.getTypedRuleContext(TyCParser.Assign_forContext,0)


        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_init




    def init(self):

        localctx = TyCParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_init)
        try:
            self.state = 498
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 494
                self.assign_for()
                self.state = 495
                self.match(TyCParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 497
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
        self.enterRule(localctx, 94, self.RULE_condition)
        try:
            self.state = 502
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.ADDITION, TyCParser.SUBTRACTION, TyCParser.LOGICAL_NOT, TyCParser.LEFT_BRACE, TyCParser.LEFT_PAREN, TyCParser.ID, TyCParser.INT_LIT, TyCParser.FLOAT_LIT, TyCParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
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

        def assign_for(self):
            return self.getTypedRuleContext(TyCParser.Assign_forContext,0)


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
        self.enterRule(localctx, 96, self.RULE_update)
        self._la = 0 # Token type
        try:
            self.state = 511
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 504
                self.assign_for()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 505
                _la = self._input.LA(1)
                if not(_la==TyCParser.INCREMENT or _la==TyCParser.DECREMENT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 506
                self.prefix_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 507
                self.postfix_expr(0)
                self.state = 508
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
        self.enterRule(localctx, 98, self.RULE_switch_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(TyCParser.SWITCH)
            self.state = 514
            self.match(TyCParser.LEFT_PAREN)
            self.state = 515
            self.expr()
            self.state = 516
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 517
            self.match(TyCParser.LEFT_BRACE)
            self.state = 518
            self.switch_body()
            self.state = 519
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
        self.enterRule(localctx, 100, self.RULE_switch_body)
        try:
            self.state = 529
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.case_list(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.case_list_branch()
                self.state = 523
                self.match(TyCParser.DEFAULT)
                self.state = 524
                self.match(TyCParser.COLON)
                self.state = 525
                self.stmt_list(0)
                self.state = 526
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
        self.enterRule(localctx, 102, self.RULE_case_list_branch)
        try:
            self.state = 533
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.CASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
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
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_case_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.case_stmt()
            self._ctx.stop = self._input.LT(-1)
            self.state = 542
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TyCParser.Case_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_case_list)
                    self.state = 538
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 539
                    self.case_stmt() 
                self.state = 544
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
        self.enterRule(localctx, 106, self.RULE_case_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.match(TyCParser.CASE)
            self.state = 546
            self.expr()
            self.state = 547
            self.match(TyCParser.COLON)
            self.state = 548
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
        self.enterRule(localctx, 108, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.match(TyCParser.BREAK)
            self.state = 551
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
        self.enterRule(localctx, 110, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.match(TyCParser.CONTINUE)
            self.state = 554
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
        self.enterRule(localctx, 112, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.match(TyCParser.RETURN)
            self.state = 559
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TyCParser.INCREMENT, TyCParser.DECREMENT, TyCParser.ADDITION, TyCParser.SUBTRACTION, TyCParser.LOGICAL_NOT, TyCParser.LEFT_BRACE, TyCParser.LEFT_PAREN, TyCParser.ID, TyCParser.INT_LIT, TyCParser.FLOAT_LIT, TyCParser.STRING_LIT]:
                self.state = 557
                self.expr()
                pass
            elif token in [TyCParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 561
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
        self.enterRule(localctx, 114, self.RULE_expr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self.expr()
            self.state = 564
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
        self._predicates[21] = self.expr_list_sempred
        self._predicates[24] = self.or_expr_sempred
        self._predicates[25] = self.and_expr_sempred
        self._predicates[26] = self.eq_expr_sempred
        self._predicates[27] = self.relational_expr_sempred
        self._predicates[28] = self.add_sub_expr_sempred
        self._predicates[29] = self.multi_div_mod_expr_sempred
        self._predicates[32] = self.postfix_expr_sempred
        self._predicates[33] = self.member_access_expr_sempred
        self._predicates[38] = self.stmt_list_sempred
        self._predicates[52] = self.case_list_sempred
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
         

    def expr_list_sempred(self, localctx:Expr_listContext, predIndex:int):
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
         




