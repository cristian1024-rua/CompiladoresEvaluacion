grammar WhileLang;

program: statement+ EOF;

statement
    : assignment
    | whileStatement
    | ifStatement
    | breakStatement
    | continueStatement
    ;

assignment: ID ASSIGN expr SEMI;

whileStatement: WHILE LPAREN condition RPAREN LBRACE statement* RBRACE;

ifStatement: IF LPAREN condition RPAREN LBRACE statement* RBRACE (ELSE LBRACE statement* RBRACE)?;

breakStatement: BREAK SEMI;

continueStatement: CONTINUE SEMI;

condition: expr (GT | LT | EQ | NE) expr;

expr
    : ID
    | NUMBER
    | expr (PLUS | MINUS | MULT | DIV) expr
    | LPAREN expr RPAREN
    ;

WHILE: 'while';
IF: 'if';
ELSE: 'else';
BREAK: 'break';
CONTINUE: 'continue';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
ASSIGN: '=';

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';

GT: '>';
LT: '<';
EQ: '==';
NE: '!=';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;

WS: [ \t\r\n]+ -> skip;
