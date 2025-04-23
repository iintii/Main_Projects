grammar While;

s:   ID ASSIGN a               # Assignment
   | SKIP_ln                   # Skip
   | BEGIN s (SEMICOLON s)* END # Compound
   | IF b THEN s ELSE s        # If
   | WHILE b DO s              # While
   ;

b:   TRUE                      # True
   | FALSE                     # False
   | NOT b                     # Not
   | b AND b                   # And
   | b OR b                    # Or
   | a ROP a                   # ROp
   | '(' b ')'                 # BParen
   ;

a:   ID                        # Var
   | NUM                       # Num
   | a AOP a                   # AOp
   | '(' a ')'                 # AParen
   ;

// Explicit lexer rules for keywords and operators.
SEMICOLON: ';';
ASSIGN: ':=';
SKIP_ln: 'skip';
BEGIN: 'begin';
END: 'end';
IF: 'if';
THEN: 'then';
ELSE: 'else';
WHILE: 'while';
DO: 'do';

TRUE: 'true';
FALSE: 'false';
NOT: 'not';
AND: 'and';
OR: 'or';

ROP: '<' | '<=' | '=' | '>' | '>=';

AOP: '+' | '-' | '*' | '/' ;

ID: [a-zA-Z] ([a-zA-Z0-9])* ;
NUM: [0-9]+ ;

WS: [ \t\n\r]+ -> skip ;
SL_COMMENT: '//' .*? '\n' -> skip ;
