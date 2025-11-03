grammar Doggo;

// Parser Rules (Start with lowercase: ANTLR needs these to generate the Parser)
start: expr EOF;

expr
    : expr MUL expr # MulDiv
    | expr DIV expr # MulDiv
    | expr ADD expr # AddSub
    | expr SUB expr # AddSub
    | atom # AtomicExpression // Renamed label to avoid conflict
    ;

atom
    : INT # Number
    | '(' expr ')' # Parentheses
    ;

// Lexer Rules (Start with uppercase)
ADD : '+' ;
SUB : '-' ;
MUL : '*' ;
DIV : '/' ;

INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
