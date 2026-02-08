# Generated from d:\BTL_PPL_252\src\grammar\TyC.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u01c1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\3\2\7\2~\n\2\f\2\16\2\u0081\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u0089\n\3\f\3\16\3\u008c")
        buf.write("\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'")
        buf.write("\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\7-\u012d\n-\f-\16")
        buf.write("-\u0130\13-\3.\3.\3/\3/\3\60\3\60\5\60\u0138\n\60\3\60")
        buf.write("\6\60\u013b\n\60\r\60\16\60\u013c\3\61\6\61\u0140\n\61")
        buf.write("\r\61\16\61\u0141\3\62\6\62\u0145\n\62\r\62\16\62\u0146")
        buf.write("\3\62\3\62\7\62\u014b\n\62\f\62\16\62\u014e\13\62\3\62")
        buf.write("\5\62\u0151\n\62\3\62\3\62\6\62\u0155\n\62\r\62\16\62")
        buf.write("\u0156\3\62\5\62\u015a\n\62\3\62\6\62\u015d\n\62\r\62")
        buf.write("\16\62\u015e\3\62\3\62\5\62\u0163\n\62\3\63\3\63\7\63")
        buf.write("\u0167\n\63\f\63\16\63\u016a\13\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\64\5\64\u0173\n\64\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65")
        buf.write("\u0183\n\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\5\66\u0193\n\66\3\67\3\67")
        buf.write("\38\38\38\39\69\u019b\n9\r9\169\u019c\39\39\3:\3:\7:\u01a3")
        buf.write("\n:\f:\16:\u01a6\13:\3:\5:\u01a9\n:\3:\3:\3:\3:\5:\u01af")
        buf.write("\n:\3:\3:\3;\3;\3;\7;\u01b6\n;\f;\16;\u01b9\13;\3;\3;")
        buf.write("\3;\3;\3<\3<\3<\3\u008a\2=\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[\2]\2_\2a/c\60e\61")
        buf.write("g\2i\2k\2m\2o\2q\62s\63u\64w\65\3\2\r\4\2\f\f\17\17\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\4\2C\\c|\3\2\62;\4\2GGgg\4\2")
        buf.write("--//\6\2\f\f\17\17$$^^\t\2))^^ddhhppttvv\5\2\13\f\16\17")
        buf.write("\"\"\13\2\f\f\17\17$$^^ddhhppttvv\2\u01dc\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2")
        buf.write("\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3y\3")
        buf.write("\2\2\2\5\u0084\3\2\2\2\7\u0092\3\2\2\2\t\u0097\3\2\2\2")
        buf.write("\13\u009d\3\2\2\2\r\u00a2\3\2\2\2\17\u00ab\3\2\2\2\21")
        buf.write("\u00b3\3\2\2\2\23\u00b8\3\2\2\2\25\u00be\3\2\2\2\27\u00c2")
        buf.write("\3\2\2\2\31\u00c5\3\2\2\2\33\u00c9\3\2\2\2\35\u00d0\3")
        buf.write("\2\2\2\37\u00d7\3\2\2\2!\u00de\3\2\2\2#\u00e5\3\2\2\2")
        buf.write("%\u00ea\3\2\2\2\'\u00f0\3\2\2\2)\u00f3\3\2\2\2+\u00f6")
        buf.write("\3\2\2\2-\u00f8\3\2\2\2/\u00fa\3\2\2\2\61\u00fc\3\2\2")
        buf.write("\2\63\u00fe\3\2\2\2\65\u0100\3\2\2\2\67\u0103\3\2\2\2")
        buf.write("9\u0106\3\2\2\2;\u0108\3\2\2\2=\u010a\3\2\2\2?\u010d\3")
        buf.write("\2\2\2A\u0110\3\2\2\2C\u0113\3\2\2\2E\u0116\3\2\2\2G\u0118")
        buf.write("\3\2\2\2I\u011a\3\2\2\2K\u011c\3\2\2\2M\u011e\3\2\2\2")
        buf.write("O\u0120\3\2\2\2Q\u0122\3\2\2\2S\u0124\3\2\2\2U\u0126\3")
        buf.write("\2\2\2W\u0128\3\2\2\2Y\u012a\3\2\2\2[\u0131\3\2\2\2]\u0133")
        buf.write("\3\2\2\2_\u0135\3\2\2\2a\u013f\3\2\2\2c\u0162\3\2\2\2")
        buf.write("e\u0164\3\2\2\2g\u0172\3\2\2\2i\u0182\3\2\2\2k\u0192\3")
        buf.write("\2\2\2m\u0194\3\2\2\2o\u0196\3\2\2\2q\u019a\3\2\2\2s\u01a0")
        buf.write("\3\2\2\2u\u01b2\3\2\2\2w\u01be\3\2\2\2yz\7\61\2\2z{\7")
        buf.write("\61\2\2{\177\3\2\2\2|~\n\2\2\2}|\3\2\2\2~\u0081\3\2\2")
        buf.write("\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0082\3\2\2\2")
        buf.write("\u0081\177\3\2\2\2\u0082\u0083\b\2\2\2\u0083\4\3\2\2\2")
        buf.write("\u0084\u0085\7\61\2\2\u0085\u0086\7,\2\2\u0086\u008a\3")
        buf.write("\2\2\2\u0087\u0089\13\2\2\2\u0088\u0087\3\2\2\2\u0089")
        buf.write("\u008c\3\2\2\2\u008a\u008b\3\2\2\2\u008a\u0088\3\2\2\2")
        buf.write("\u008b\u008d\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u008e\7")
        buf.write(",\2\2\u008e\u008f\7\61\2\2\u008f\u0090\3\2\2\2\u0090\u0091")
        buf.write("\b\3\2\2\u0091\6\3\2\2\2\u0092\u0093\7c\2\2\u0093\u0094")
        buf.write("\7w\2\2\u0094\u0095\7v\2\2\u0095\u0096\7q\2\2\u0096\b")
        buf.write("\3\2\2\2\u0097\u0098\7d\2\2\u0098\u0099\7t\2\2\u0099\u009a")
        buf.write("\7g\2\2\u009a\u009b\7c\2\2\u009b\u009c\7m\2\2\u009c\n")
        buf.write("\3\2\2\2\u009d\u009e\7e\2\2\u009e\u009f\7c\2\2\u009f\u00a0")
        buf.write("\7u\2\2\u00a0\u00a1\7g\2\2\u00a1\f\3\2\2\2\u00a2\u00a3")
        buf.write("\7e\2\2\u00a3\u00a4\7q\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6")
        buf.write("\7v\2\2\u00a6\u00a7\7k\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9")
        buf.write("\7w\2\2\u00a9\u00aa\7g\2\2\u00aa\16\3\2\2\2\u00ab\u00ac")
        buf.write("\7f\2\2\u00ac\u00ad\7g\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af")
        buf.write("\7c\2\2\u00af\u00b0\7w\2\2\u00b0\u00b1\7n\2\2\u00b1\u00b2")
        buf.write("\7v\2\2\u00b2\20\3\2\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5")
        buf.write("\7n\2\2\u00b5\u00b6\7u\2\2\u00b6\u00b7\7g\2\2\u00b7\22")
        buf.write("\3\2\2\2\u00b8\u00b9\7h\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb")
        buf.write("\7q\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7v\2\2\u00bd\24")
        buf.write("\3\2\2\2\u00be\u00bf\7h\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1")
        buf.write("\7t\2\2\u00c1\26\3\2\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4")
        buf.write("\7h\2\2\u00c4\30\3\2\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\u00c8\7v\2\2\u00c8\32\3\2\2\2\u00c9\u00ca")
        buf.write("\7t\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd")
        buf.write("\7w\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7p\2\2\u00cf\34")
        buf.write("\3\2\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3")
        buf.write("\7t\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6")
        buf.write("\7i\2\2\u00d6\36\3\2\2\2\u00d7\u00d8\7u\2\2\u00d8\u00d9")
        buf.write("\7v\2\2\u00d9\u00da\7t\2\2\u00da\u00db\7w\2\2\u00db\u00dc")
        buf.write("\7e\2\2\u00dc\u00dd\7v\2\2\u00dd \3\2\2\2\u00de\u00df")
        buf.write("\7u\2\2\u00df\u00e0\7y\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2")
        buf.write("\7v\2\2\u00e2\u00e3\7e\2\2\u00e3\u00e4\7j\2\2\u00e4\"")
        buf.write("\3\2\2\2\u00e5\u00e6\7x\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8")
        buf.write("\7k\2\2\u00e8\u00e9\7f\2\2\u00e9$\3\2\2\2\u00ea\u00eb")
        buf.write("\7y\2\2\u00eb\u00ec\7j\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee")
        buf.write("\7n\2\2\u00ee\u00ef\7g\2\2\u00ef&\3\2\2\2\u00f0\u00f1")
        buf.write("\7-\2\2\u00f1\u00f2\7-\2\2\u00f2(\3\2\2\2\u00f3\u00f4")
        buf.write("\7/\2\2\u00f4\u00f5\7/\2\2\u00f5*\3\2\2\2\u00f6\u00f7")
        buf.write("\7-\2\2\u00f7,\3\2\2\2\u00f8\u00f9\7/\2\2\u00f9.\3\2\2")
        buf.write("\2\u00fa\u00fb\7,\2\2\u00fb\60\3\2\2\2\u00fc\u00fd\7\61")
        buf.write("\2\2\u00fd\62\3\2\2\2\u00fe\u00ff\7\'\2\2\u00ff\64\3\2")
        buf.write("\2\2\u0100\u0101\7?\2\2\u0101\u0102\7?\2\2\u0102\66\3")
        buf.write("\2\2\2\u0103\u0104\7#\2\2\u0104\u0105\7?\2\2\u01058\3")
        buf.write("\2\2\2\u0106\u0107\7>\2\2\u0107:\3\2\2\2\u0108\u0109\7")
        buf.write("@\2\2\u0109<\3\2\2\2\u010a\u010b\7>\2\2\u010b\u010c\7")
        buf.write("?\2\2\u010c>\3\2\2\2\u010d\u010e\7@\2\2\u010e\u010f\7")
        buf.write("?\2\2\u010f@\3\2\2\2\u0110\u0111\7~\2\2\u0111\u0112\7")
        buf.write("~\2\2\u0112B\3\2\2\2\u0113\u0114\7(\2\2\u0114\u0115\7")
        buf.write("(\2\2\u0115D\3\2\2\2\u0116\u0117\7#\2\2\u0117F\3\2\2\2")
        buf.write("\u0118\u0119\7?\2\2\u0119H\3\2\2\2\u011a\u011b\7\60\2")
        buf.write("\2\u011bJ\3\2\2\2\u011c\u011d\7}\2\2\u011dL\3\2\2\2\u011e")
        buf.write("\u011f\7\177\2\2\u011fN\3\2\2\2\u0120\u0121\7*\2\2\u0121")
        buf.write("P\3\2\2\2\u0122\u0123\7+\2\2\u0123R\3\2\2\2\u0124\u0125")
        buf.write("\7=\2\2\u0125T\3\2\2\2\u0126\u0127\7.\2\2\u0127V\3\2\2")
        buf.write("\2\u0128\u0129\7<\2\2\u0129X\3\2\2\2\u012a\u012e\t\3\2")
        buf.write("\2\u012b\u012d\t\4\2\2\u012c\u012b\3\2\2\2\u012d\u0130")
        buf.write("\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f")
        buf.write("Z\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0132\t\5\2\2\u0132")
        buf.write("\\\3\2\2\2\u0133\u0134\t\6\2\2\u0134^\3\2\2\2\u0135\u0137")
        buf.write("\t\7\2\2\u0136\u0138\t\b\2\2\u0137\u0136\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138\u013a\3\2\2\2\u0139\u013b\5]/\2\u013a")
        buf.write("\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013a\3\2\2\2")
        buf.write("\u013c\u013d\3\2\2\2\u013d`\3\2\2\2\u013e\u0140\5]/\2")
        buf.write("\u013f\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u013f\3")
        buf.write("\2\2\2\u0141\u0142\3\2\2\2\u0142b\3\2\2\2\u0143\u0145")
        buf.write("\5]/\2\u0144\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0144")
        buf.write("\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148\3\2\2\2\u0148")
        buf.write("\u014c\7\60\2\2\u0149\u014b\5]/\2\u014a\u0149\3\2\2\2")
        buf.write("\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3")
        buf.write("\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2\u014f\u0151")
        buf.write("\5_\60\2\u0150\u014f\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write("\u0163\3\2\2\2\u0152\u0154\7\60\2\2\u0153\u0155\5]/\2")
        buf.write("\u0154\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0154\3")
        buf.write("\2\2\2\u0156\u0157\3\2\2\2\u0157\u0159\3\2\2\2\u0158\u015a")
        buf.write("\5_\60\2\u0159\u0158\3\2\2\2\u0159\u015a\3\2\2\2\u015a")
        buf.write("\u0163\3\2\2\2\u015b\u015d\5]/\2\u015c\u015b\3\2\2\2\u015d")
        buf.write("\u015e\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015f\u0160\3\2\2\2\u0160\u0161\5_\60\2\u0161\u0163\3")
        buf.write("\2\2\2\u0162\u0144\3\2\2\2\u0162\u0152\3\2\2\2\u0162\u015c")
        buf.write("\3\2\2\2\u0163d\3\2\2\2\u0164\u0168\7$\2\2\u0165\u0167")
        buf.write("\5g\64\2\u0166\u0165\3\2\2\2\u0167\u016a\3\2\2\2\u0168")
        buf.write("\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016b\3\2\2\2")
        buf.write("\u016a\u0168\3\2\2\2\u016b\u016c\7$\2\2\u016c\u016d\b")
        buf.write("\63\3\2\u016df\3\2\2\2\u016e\u0173\n\t\2\2\u016f\u0173")
        buf.write("\5i\65\2\u0170\u0171\7^\2\2\u0171\u0173\7$\2\2\u0172\u016e")
        buf.write("\3\2\2\2\u0172\u016f\3\2\2\2\u0172\u0170\3\2\2\2\u0173")
        buf.write("h\3\2\2\2\u0174\u0175\7^\2\2\u0175\u0183\7d\2\2\u0176")
        buf.write("\u0177\7^\2\2\u0177\u0183\7h\2\2\u0178\u0179\7^\2\2\u0179")
        buf.write("\u0183\7t\2\2\u017a\u017b\7^\2\2\u017b\u0183\7p\2\2\u017c")
        buf.write("\u017d\7^\2\2\u017d\u0183\7v\2\2\u017e\u017f\7^\2\2\u017f")
        buf.write("\u0183\7$\2\2\u0180\u0181\7^\2\2\u0181\u0183\7^\2\2\u0182")
        buf.write("\u0174\3\2\2\2\u0182\u0176\3\2\2\2\u0182\u0178\3\2\2\2")
        buf.write("\u0182\u017a\3\2\2\2\u0182\u017c\3\2\2\2\u0182\u017e\3")
        buf.write("\2\2\2\u0182\u0180\3\2\2\2\u0183j\3\2\2\2\u0184\u0185")
        buf.write("\7^\2\2\u0185\u0193\7d\2\2\u0186\u0187\7^\2\2\u0187\u0193")
        buf.write("\7v\2\2\u0188\u0189\7^\2\2\u0189\u0193\7p\2\2\u018a\u018b")
        buf.write("\7^\2\2\u018b\u0193\7h\2\2\u018c\u018d\7^\2\2\u018d\u0193")
        buf.write("\7t\2\2\u018e\u018f\7^\2\2\u018f\u0193\7)\2\2\u0190\u0191")
        buf.write("\7^\2\2\u0191\u0193\7^\2\2\u0192\u0184\3\2\2\2\u0192\u0186")
        buf.write("\3\2\2\2\u0192\u0188\3\2\2\2\u0192\u018a\3\2\2\2\u0192")
        buf.write("\u018c\3\2\2\2\u0192\u018e\3\2\2\2\u0192\u0190\3\2\2\2")
        buf.write("\u0193l\3\2\2\2\u0194\u0195\n\t\2\2\u0195n\3\2\2\2\u0196")
        buf.write("\u0197\7^\2\2\u0197\u0198\n\n\2\2\u0198p\3\2\2\2\u0199")
        buf.write("\u019b\t\13\2\2\u019a\u0199\3\2\2\2\u019b\u019c\3\2\2")
        buf.write("\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019e")
        buf.write("\3\2\2\2\u019e\u019f\b9\2\2\u019fr\3\2\2\2\u01a0\u01a4")
        buf.write("\7$\2\2\u01a1\u01a3\5g\64\2\u01a2\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2")
        buf.write("\u01a5\u01a8\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u01a9\7")
        buf.write("^\2\2\u01a8\u01a7\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ae")
        buf.write("\3\2\2\2\u01aa\u01af\7\f\2\2\u01ab\u01ac\7\17\2\2\u01ac")
        buf.write("\u01af\7\f\2\2\u01ad\u01af\7\2\2\3\u01ae\u01aa\3\2\2\2")
        buf.write("\u01ae\u01ab\3\2\2\2\u01ae\u01ad\3\2\2\2\u01af\u01b0\3")
        buf.write("\2\2\2\u01b0\u01b1\b:\4\2\u01b1t\3\2\2\2\u01b2\u01b7\7")
        buf.write("$\2\2\u01b3\u01b6\5m\67\2\u01b4\u01b6\5i\65\2\u01b5\u01b3")
        buf.write("\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7")
        buf.write("\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01ba\3\2\2\2")
        buf.write("\u01b9\u01b7\3\2\2\2\u01ba\u01bb\7^\2\2\u01bb\u01bc\n")
        buf.write("\f\2\2\u01bc\u01bd\b;\5\2\u01bdv\3\2\2\2\u01be\u01bf\13")
        buf.write("\2\2\2\u01bf\u01c0\b<\6\2\u01c0x\3\2\2\2\32\2\177\u008a")
        buf.write("\u012e\u0137\u013c\u0141\u0146\u014c\u0150\u0156\u0159")
        buf.write("\u015e\u0162\u0168\u0172\u0182\u0192\u019c\u01a4\u01a8")
        buf.write("\u01ae\u01b5\u01b7\7\b\2\2\3\63\2\3:\3\3;\4\3<\5")
        return buf.getvalue()


class TyCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LINE_COMMENT = 1
    BLOCK_COMMENT = 2
    AUTO = 3
    BREAK = 4
    CASE = 5
    CONTINUE = 6
    DEFAULT = 7
    ELSE = 8
    FLOAT = 9
    FOR = 10
    IF = 11
    INT = 12
    RETURN = 13
    STRING = 14
    STRUCT = 15
    SWITCH = 16
    VOID = 17
    WHILE = 18
    INCREMENT = 19
    DECREMENT = 20
    ADDITION = 21
    SUBTRACTION = 22
    MULTI = 23
    DIVISION = 24
    MODULO = 25
    EQUAL = 26
    NOT_EQUAL = 27
    LESS_THAN = 28
    GREATER_THAN = 29
    LESS_THAN_EQUAL = 30
    GREATER_THAN_EQUAL = 31
    LOGICAL_OR = 32
    LOGICAL_AND = 33
    LOGICAL_NOT = 34
    ASSIGNMENT = 35
    MEMBER_ACCESS = 36
    LEFT_BRACE = 37
    RIGHT_BRACE = 38
    LEFT_PAREN = 39
    RIGHT_PAREN = 40
    SEMICOLON = 41
    COMMA = 42
    COLON = 43
    ID = 44
    INT_LIT = 45
    FLOAT_LIT = 46
    STRING_LIT = 47
    WS = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'case'", "'continue'", "'default'", "'else'", 
            "'float'", "'for'", "'if'", "'int'", "'return'", "'string'", 
            "'struct'", "'switch'", "'void'", "'while'", "'++'", "'--'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", 
            "'<='", "'>='", "'||'", "'&&'", "'!'", "'='", "'.'", "'{'", 
            "'}'", "'('", "')'", "';'", "','", "':'" ]

    symbolicNames = [ "<INVALID>",
            "LINE_COMMENT", "BLOCK_COMMENT", "AUTO", "BREAK", "CASE", "CONTINUE", 
            "DEFAULT", "ELSE", "FLOAT", "FOR", "IF", "INT", "RETURN", "STRING", 
            "STRUCT", "SWITCH", "VOID", "WHILE", "INCREMENT", "DECREMENT", 
            "ADDITION", "SUBTRACTION", "MULTI", "DIVISION", "MODULO", "EQUAL", 
            "NOT_EQUAL", "LESS_THAN", "GREATER_THAN", "LESS_THAN_EQUAL", 
            "GREATER_THAN_EQUAL", "LOGICAL_OR", "LOGICAL_AND", "LOGICAL_NOT", 
            "ASSIGNMENT", "MEMBER_ACCESS", "LEFT_BRACE", "RIGHT_BRACE", 
            "LEFT_PAREN", "RIGHT_PAREN", "SEMICOLON", "COMMA", "COLON", 
            "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "LINE_COMMENT", "BLOCK_COMMENT", "AUTO", "BREAK", "CASE", 
                  "CONTINUE", "DEFAULT", "ELSE", "FLOAT", "FOR", "IF", "INT", 
                  "RETURN", "STRING", "STRUCT", "SWITCH", "VOID", "WHILE", 
                  "INCREMENT", "DECREMENT", "ADDITION", "SUBTRACTION", "MULTI", 
                  "DIVISION", "MODULO", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
                  "GREATER_THAN", "LESS_THAN_EQUAL", "GREATER_THAN_EQUAL", 
                  "LOGICAL_OR", "LOGICAL_AND", "LOGICAL_NOT", "ASSIGNMENT", 
                  "MEMBER_ACCESS", "LEFT_BRACE", "RIGHT_BRACE", "LEFT_PAREN", 
                  "RIGHT_PAREN", "SEMICOLON", "COMMA", "COLON", "ID", "LETTER", 
                  "DIGIT", "EXP_PART", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                  "CHAR_LIT", "ESCAPE_SEQ", "ESC", "NON_ESC", "ILL_ESC", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "TyC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[49] = self.STRING_LIT_action 
            actions[56] = self.UNCLOSE_STRING_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            actions[58] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                if self.text[-1] == '\n' and self.text[-2] == '\r':
                    raise UncloseString(self.text[1:-2])
                elif self.text[-1] == '\n':
                    raise UncloseString(self.text[1:-1])
                else:
                    raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             raise IllegalEscape(self.text[1:]) 
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


