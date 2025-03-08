grammar While;

s:   ID ':=' a # Assignment
   | 'skip' # Skip
   // | s ';' s # Sequence
   | 'begin' s (';' s)* 'end' # Compound
   | 'if' b 'then' s 'else' s # If
   | 'while' b 'do' s # While
   ;

b:   'true' # True
   | 'false' # False
   | 'not' b # Not
   | b 'and' b # And
   | b 'or' b # Or
   | a op=('<' | '<=' | '=' | '>' | '>=') a # ROp
   | '(' b ')' # BParen
   ;

a:   ID # Var
   | NUM # Num
   | a op=('+' | '-' | '*' | '/') a # AOp
   | '(' a ')' # AParen
   ;

TRUE: 'true' ;
FALSE: 'false' ;
AND: 'and' ;
OR: 'or' ;
NOT: 'not' ;

ID: [a-zA-Z] ([a-zA-Z] | [0-9])* ;
NUM: [0-9]+ ;

EQ: '=' ;
LT: '<' ;
LE: '<=' ;
GT: '>' ;
GE: '>=' ;

PLUS: '+' ;
MINUS: '-' ;
MULT: '*' ;
DIV: '/' ;

WS:   [ \t\n\r]+ -> skip ;
SL_COMMENT:   '//' .*? '\n' -> skip ;
