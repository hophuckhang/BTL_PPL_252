grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options{
	language=Python3;
}

// TODO: Define grammar rules here
program: decl_list EOF;
decl_list: decl_list decl | ;
decl: func_decl | struct_decl;

// ===================== PARSER - DECLARATIONS =====================

func_decl: (typ | VOID | ) ID LEFT_PAREN param_list RIGHT_PAREN LEFT_BRACE stmt_list RIGHT_BRACE;

param_list: param_list_exist | ;

param_list_exist: param_decl COMMA param_list_exist | param_decl;

param_decl: typ ID;

struct_decl: STRUCT ID LEFT_BRACE struct_member_list RIGHT_BRACE SEMICOLON;

struct_member_list: struct_member_list struct_member | ;

struct_member: typ ID SEMICOLON;

struct_var_decl_list: struct_var_decl_list_exist | ;

struct_var_decl_list_exist: struct_var_decl_list_exist COMMA struct_var_decl | struct_var_decl;

struct_var_decl: ID ID SEMICOLON | ID ID ASSIGNMENT LEFT_BRACE (struct_var_member_list | )RIGHT_BRACE SEMICOLON;

struct_var_member_list: struct_var_member_list COMMA struct_var_member | ;

struct_var_member: operand | func_call_expr;

var_decl_list: var_decl_list var_decl | var_decl;

var_decl: auto_var_decl | explicit_var_decl;

auto_var_decl: AUTO ID SEMICOLON | AUTO ID ASSIGNMENT assign_expr SEMICOLON;

explicit_var_decl: typ ID SEMICOLON | typ ID ASSIGNMENT assign_expr SEMICOLON;

// ===================== PARSER - TYPES =====================

typ: primitive_typ | ID;

primitive_typ: INT | FLOAT | STRING;

// ===================== PARSER - EXPRESSIONS =====================

expr_list: expr_list_exist | ;

expr_list_exist: expr_list_exist COMMA expr | expr;

expr: assign_expr;

assign_expr: assign_lhs ASSIGNMENT assign_expr | or_expr; //right

assign_lhs: ID | member_access_expr MEMBER_ACCESS ID;

or_expr: or_expr LOGICAL_OR and_expr | and_expr; //left

and_expr: and_expr LOGICAL_AND eq_expr | eq_expr; //left

eq_expr: eq_expr (EQUAL | NOT_EQUAL) relational_expr | relational_expr; //left

relational_expr: relational_expr (LESS_THAN | LESS_THAN_EQUAL | GREATER_THAN | GREATER_THAN_EQUAL) add_sub_expr | add_sub_expr; //left

add_sub_expr: add_sub_expr (ADDITION | SUBTRACTION) multi_div_mod_expr | multi_div_mod_expr; //left

multi_div_mod_expr: multi_div_mod_expr (MULTI | DIVISION | MODULO) unary_expr | unary_expr; //left

unary_expr: (LOGICAL_NOT | SUBTRACTION | ADDITION) unary_expr | prefix_expr; //

prefix_expr: (INCREMENT | DECREMENT) prefix_expr | postfix_expr; //right

postfix_expr: postfix_expr (INCREMENT | DECREMENT) | member_access_expr; //left

member_access_expr: member_access_expr MEMBER_ACCESS ID | operand; //left

operand: INT_LIT | FLOAT_LIT | STRING_LIT | struct_lit | func_call_expr | paren_expr | ID;

struct_lit: LEFT_BRACE expr_list RIGHT_BRACE;

func_call_expr: ID LEFT_PAREN expr_list RIGHT_PAREN;

paren_expr: LEFT_PAREN expr RIGHT_PAREN;

// ===================== PARSER - STATEMENTS =====================

stmt_list: stmt_list stmt | ;

stmt: var_decl_stmt | block_stmt | if_stmt | while_stmt | for_stmt | switch_stmt | break_stmt | continue_stmt | return_stmt | expr_stmt;

var_decl_stmt: var_decl;

block_stmt: LEFT_BRACE (var_decl_list | stmt_list) RIGHT_BRACE;

if_stmt: IF LEFT_PAREN expr RIGHT_PAREN
(LEFT_BRACE stmt RIGHT_BRACE
| LEFT_BRACE stmt RIGHT_BRACE ELSE LEFT_BRACE stmt RIGHT_BRACE
| stmt
| stmt ELSE stmt
| LEFT_BRACE stmt RIGHT_BRACE ELSE stmt
| stmt ELSE LEFT_BRACE stmt RIGHT_BRACE);

while_stmt: WHILE LEFT_PAREN expr RIGHT_PAREN stmt;

for_stmt: FOR LEFT_PAREN init condition SEMICOLON update RIGHT_PAREN stmt;
init: var_decl | assign_lhs ASSIGNMENT expr SEMICOLON | SEMICOLON;
condition: expr | ;
update: assign_lhs ASSIGNMENT expr | (INCREMENT | DECREMENT) prefix_expr | postfix_expr (INCREMENT | DECREMENT) | ;

switch_stmt: SWITCH LEFT_PAREN expr RIGHT_PAREN LEFT_BRACE switch_body RIGHT_BRACE;
switch_body: case_list | case_list_branch DEFAULT COLON stmt_list case_list_branch | ;
case_list_branch: case_list | ;
case_list: case_list case_stmt | case_stmt;
case_stmt: CASE expr COLON stmt_list;

break_stmt: BREAK SEMICOLON;

continue_stmt: CONTINUE SEMICOLON;

return_stmt: RETURN (expr | ) SEMICOLON;

expr_stmt: expr SEMICOLON;

// ===================== LEXER - COMMENTS =====================

LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

// ===================== LEXER - KEYWORDS =====================

AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
IF: 'if';
INT: 'int';
RETURN: 'return';
STRING: 'string';
STRUCT: 'struct';
SWITCH: 'switch';
VOID: 'void';
WHILE: 'while';

// ===================== LEXER - OPERATORS =====================

INCREMENT: '++';
DECREMENT: '--';
ADDITION: '+';
SUBTRACTION: '-';
MULTI: '*';
DIVISION: '/';
MODULO: '%';
EQUAL: '==';
NOT_EQUAL: '!=';
LESS_THAN: '<';
GREATER_THAN: '>';
LESS_THAN_EQUAL: '<=';
GREATER_THAN_EQUAL: '>=';
LOGICAL_OR: '||';
LOGICAL_AND: '&&';
LOGICAL_NOT: '!';
ASSIGNMENT: '=';
MEMBER_ACCESS: '.';

// ===================== LEXER - SEPARATORS =====================

LEFT_BRACE: '{';
RIGHT_BRACE: '}';
LEFT_PAREN: '(';
RIGHT_PAREN: ')';
SEMICOLON: ';';
COMMA: ',';
COLON: ':';

// ===================== LEXER - IDENTIFIERS =====================

ID: [A-Za-z_] [A-Za-z_0-9]*;

// ===================== LEXER - LITERALS =====================

fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
fragment EXP_PART: [eE] [+-]? DIGIT+;
INT_LIT: DIGIT+;
FLOAT_LIT: DIGIT+ '.' DIGIT* EXP_PART? | '.' DIGIT+ EXP_PART? | DIGIT+ EXP_PART;
STRING_LIT: '"' CHAR_LIT* '"' {self.text = self.text[1:-1]};
fragment CHAR_LIT: ~["\\\r\n] | ESCAPE_SEQ | '\\"';
fragment ESCAPE_SEQ: '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\"' | '\\\\';

fragment ESC: '\\b'
			| '\\t'
			| '\\n'
			| '\\f'
			| '\\r'
			| '\\\''
			| '\\\\';
fragment NON_ESC : ~[\n\r"\\];			
fragment ILL_ESC : '\\' ~[bfrnt'\\];

WS : [ \t\r\n\f]+ -> skip ; 


UNCLOSE_STRING: '"' CHAR_LIT*  '\\'? ('\n' | '\r\n' | EOF) {
    if self.text[-1] == '\n' and self.text[-2] == '\r':
        raise UncloseString(self.text[1:-2])
    elif self.text[-1] == '\n':
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' (NON_ESC | ESCAPE_SEQ)* '\\' ~[bfrnt"\\\r\n] { raise IllegalEscape(self.text[1:]) };
ERROR_CHAR: . {raise ErrorToken(self.text)};