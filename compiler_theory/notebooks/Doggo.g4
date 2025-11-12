grammar Doggo;

// Entry point
start: statement EOF;

// Main statement rules
statement
    : declaration SEMICOLON                     # DeclarationStatement
    | str_method SEMICOLON                      # StringMethods
    | assignment_statement SEMICOLON            # AssignmentStatement
    | expr SEMICOLON                            # ExpressionStatement
    | kennel_definition                         # KennelDefinition
    | import_statement SEMICOLON                # ImportStatement
    | if_statement                              # IfStatement
    | while_statement                           # WhileStatement
    | for_statement                             # ForStatement
    | try_statement                             # TryCatchFinallyStatement
    | raise_statement SEMICOLON                 # GrowlStatement
    | method_call_statement SEMICOLON           # MethodCallStatement
    | list_method_statement SEMICOLON           # ListMethodStatement
    | LEAVE_SCENT '(' expr ',' expr ',' expr ')' SEMICOLON # LeaveScentStatement
    | BURY_BONE '(' expr ')' SEMICOLON          # BuryBoneStatement
    | BEG '(' identifier (',' expr)? ')' SEMICOLON # BegStatement
    | WOOF '(' expr ')' SEMICOLON               # WoofStatement
    ;

// Variable declaration, including list literal assignment
declaration
    : type_ identifier (ASSIGN expr)?           // allow assignment of expr (which can be a list literal)
    ;

// Assignment
assignment_statement : identifier ASSIGN expr;

// Kennel/class definition
kennel_definition : KENNEL ID block;

// Import
import_statement : IMPORT ID;

// Control flow
if_statement
    : IF '(' expr ')' block (SNIFF_ELIF '(' expr ')' block)* (SNIFF_ELSE block)?
    ;

while_statement : WHILE '(' expr ')' block;

for_statement
    : FOR '(' (declaration | assignment_statement | expr)? SEMICOLON expr SEMICOLON (assignment_statement | expr)? ')' block;

// Try-catch-finally
try_statement
    : TRY block sniff_catch_clause* sniff_finally_clause?
    ;

sniff_catch_clause   : SNIFF_CATCH '(' excType=ID excVar=ID ')' block;
sniff_finally_clause : SNIFF_FINALLY block;

// Exceptions
raise_statement : GROWL expr;

// Method calls (object.method(args))
method_call_statement
    : identifier DOT (PEEK | NAP | ID) '(' (expr (',' expr)*)? ')'
    ;

// List methods
list_method_statement
    : identifier DOT LEASHON LPAR element RPAR
    | identifier DOT SNIFFSWAP LPAR INT COMMA element RPAR
    | identifier DOT TUCK LPAR INT COMMA element RPAR
    | identifier DOT UNLEASH LPAR element RPAR
    | identifier DOT SNATCH LPAR RPAR
    | identifier DOT DROPALL LPAR RPAR
    | identifier DOT PAWCOUNT LPAR RPAR
    | identifier DOT HERD LPAR RPAR
    | identifier DOT CLONEPAW LPAR RPAR
    ;

// String methods
str_method
    // <slicing>: <string_var_name>.chew([INTEGER:INTEGER])<end_statement>*
    : identifier DOT CHEW LPAR slicing_args RPAR
        # SlicingMethod
    // <uppercase>: <string_var_name>.howl()<end_statement>*
    | identifier DOT HOWL LPAR RPAR
        # UppercaseMethod
    // <lowercase>: <string_var_name>.whimper()<end_statement>
    | identifier DOT WHIMPER LPAR RPAR
        # LowercaseMethod
    // <remove_whitespace>: <string_var_name>.groom()<end_statement>
    | identifier DOT GROOM LPAR RPAR
        # RemoveWhitespaceMethod
    // <replace>: <string_var_name>.sniffswap(STRING, STRING)<end_statement>*
    | identifier DOT SNIFFSWAP_STR LPAR expr COMMA expr RPAR // expr here will resolve to STRING
        # ReplaceMethod
    // <split>: <string_var_name>.sniffapart(STRING)<end_statement>*
    | identifier DOT SNIFFAPART LPAR expr RPAR // expr here will resolve to STRING
        # SplitMethod
    // <format>: fillbowl [STRING|{}]+ with STRING
    | FILLBOWL string_format_args WITH expr
        # FormatMethod
    ;

// Helper rule for slicing (chew)
slicing_args
    // Supports [INTEGER:INTEGER] as per CFG
    : INT COLON INT
    // You may also want to support just INT (index), or INT: (slice to end), or :INT (slice from start)
    | INT COLON
    | COLON INT
    | INT
    ;

string_format_args
    : (STRING | LBRACE RBRACE)+ // Matches [STRING|{}]+
    ;

// Blocks
block : LBRACE statement* RBRACE;

// Types (why leash, profile, etc.)
type_
    : TREATS_TYPE
    | WEIGHT_TYPE
    | NAME_TYPE
    | GOODNESS_TYPE
    | DIARY_TYPE
    | LEASH_TYPE     // list
    | PROFILE_TYPE   // dictionary
    | TOYS_TYPE      // set
    | PAWPRINT_TYPE  // tuple
    | PACK_TYPE      // array
    ;

// Expressions (add list_literal as part of expr)
expr
    : atom                        # AtomicExpression
    | expr EXP expr               # Exp
    | expr MUL expr               # MulDiv
    | expr DIV expr               # MulDiv
    | expr FLOOR_DIV expr         # FloorDiv
    | expr MOD expr               # Modulo
    | expr ADD expr               # AddSub
    | expr SUB expr               # AddSub
    | expr EQ expr                # Equal
    | expr NEQ expr               # NotEqual
    | expr GT expr                # GreaterThan
    | expr LT expr                # LessThan
    | expr GTE expr               # GreaterThanEqual
    | expr LTE expr               # LessThanEqual
    | expr IN expr                # In
    | expr NOT IN expr            # NotIn
    | NOT expr                    # Not
    | expr AND expr               # And
    | expr OR expr                # Or
    
    // START FIX: String Method Expressions (to allow assignment: name var = str.howl();)
    // These alternatives mirror the str_method rule but are included here to be recognized as expressions.
    | identifier DOT CHEW LPAR slicing_args RPAR      # ChewExpression
    | identifier DOT HOWL LPAR RPAR                   # HowlExpression
    | identifier DOT WHIMPER LPAR RPAR                # WhimperExpression
    | identifier DOT GROOM LPAR RPAR                  # GroomExpression
    | identifier DOT SNIFFSWAP_STR LPAR expr COMMA expr RPAR # SniffswapStrExpression
    | identifier DOT SNIFFAPART LPAR expr RPAR        # SniffapartExpression
    | FILLBOWL string_format_args WITH expr           # FillbowlExpression
    // END FIX
    
    | list_literal                # ListLiteral
    ;

// List literal definition, e.g., [a, 1, "hi"]
list_literal
    : LBRACK (element (COMMA element)*)? RBRACK
    ;

element
    : INT
    | FLOAT
    | STRING
    | BOOLEAN
    | identifier
    ;

// Atomic expressions
atom
    : INT                              # Number
    | identifier                       # VariableReference
    | STRING                           # StringLiteral
    | EMPTYBOWL                        # NullLiteral
    | '(' expr ')'                     # Parentheses
    | ID '(' (expr (',' expr)*)? ')'   # CallExpression
    | SQRT '(' expr ')'                # SqrtCall
    | PAWSIZE '(' expr ')'             # PawsizeCall
    | SMALLEST_PUP '(' expr (',' expr)+ ')' # SmallestPupCall
    | BIGGEST_PUP '(' expr (',' expr)+ ')'  # BiggestPupCall
    | ALPHA_POWER '(' expr ',' expr ')'     # AlphaPowerCall
    ;

// Identifiers
identifier : ID;

// ===== Lexer rules start here =====

// Operators, delimiters, keywords, etc.
ADD        : '+' ;
SUB        : '-' ;
MUL        : '*' ;
DIV        : '/' ;
FLOOR_DIV  : '//' ;
MOD        : '%' ;
EXP        : '**' ;

EQ         : '==' ;
NEQ        : '!=' ;
GT         : '>' ;
LT         : '<' ;
GTE        : '>=' ;
LTE        : '<=' ;

AND        : 'and' ;
OR         : 'or' ;
NOT        : 'not' ;
IN         : 'in' ;
ASSIGN     : '=' ;
SEMICOLON  : ';' ;
DOT        : '.' ;
COLON      : ':' ; // Used in slicing_args and possibly elsewhere
WITH       : 'with' ; // Used in the fillbowl method

LBRACE     : '{' ;
RBRACE     : '}' ;
LBRACK     : '[' ;
RBRACK     : ']' ;
LPAR       : '(' ;
RPAR       : ')' ;
COMMA      : ',' ;

// Control flow
IF         : 'if' ;
SNIFF_ELIF : 'sniff_elif' ;
SNIFF_ELSE : 'sniff_else' ;
WHILE      : 'while' ;
FOR        : 'for' ;

// Try/catch/finally, exceptions
TRY           : 'try' ;
SNIFF_CATCH   : 'sniff_catch' ;
SNIFF_FINALLY : 'sniff_finally' ;
GROWL         : 'growl' ;

// Classes/kennels
KENNEL   : 'kennel' ;
IMPORT   : 'import' ;

// Types
TREATS_TYPE    : 'treats' ;
WEIGHT_TYPE    : 'weight' ;
NAME_TYPE      : 'name' ;
GOODNESS_TYPE  : 'goodness' ;
DIARY_TYPE     : 'diary' ;
LEASH_TYPE     : 'leash' ;
PROFILE_TYPE   : 'profile' ;
TOYS_TYPE      : 'toys' ;
PAWPRINT_TYPE  : 'pawprint' ;
PACK_TYPE      : 'pack' ;

EMPTYBOWL : 'emptybowl' ;

// File methods
PEEK        : 'peek' ;
NAP         : 'nap' ;
LEAVE_SCENT : 'leave_scent' ;
BURY_BONE   : 'bury_bone' ;

// I/O, math, and min/max utilities
BEG          : 'beg' ;
WOOF         : 'woof' ;
SQRT         : 'sqrt' ;
PAWSIZE      : 'pawsize' ;
SMALLEST_PUP : 'smallest_pup' ;
BIGGEST_PUP  : 'biggest_pup' ;
ALPHA_POWER  : 'alpha_power' ;

// List methods
LEASHON   : 'leashon' ;
SNIFFSWAP : 'sniffswap' ;
TUCK      : 'tuck' ;
UNLEASH   : 'unleash' ;
SNATCH    : 'snatch' ;
DROPALL   : 'dropall' ;
PAWCOUNT  : 'pawcount' ;
HERD      : 'herd' ;
CLONEPAW  : 'clonepaw' ;

// String Methods (New Tokens)
CHEW : 'chew' ;
HOWL : 'howl' ;
WHIMPER : 'whimper' ;
GROOM : 'groom' ;
SNIFFSWAP_STR : 'sniffswap_str' ; // Differentiate from list sniffswap if needed, though context usually handles it.
SNIFFAPART : 'sniffapart' ;
FILLBOWL : 'fillbowl' ;

// Literals and basic types
STRING  : '"' ( ~('\\' | '"') | '\\' . )* '"' ;
INT     : [0-9]+ ;
FLOAT   : [0-9]+ '.' [0-9]+ ;
BOOLEAN : 'true' | 'false' ;
ID      : [a-zA-Z_][a-zA-Z0-9_]* ;

// Whitespace and comments
WS                 : [ \t\r\n]+ -> skip ;
COMMENT_SINGLE_LINE: '#' ~[\r\n]* -> skip ;
COMMENT_MULTI_LINE : '/*' .*? '*/' -> skip ;
