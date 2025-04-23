grammar TypeWhile;

s:   ID ':=' e # Assignment
   | 'skip' # Skip
   | 'begin' s (';' s)* 'end' # Compound
   | 'if' e 'then' s 'else' s # If
   | 'while' e 'do' s # While
	 | typeName=('int' | 'bool') ID # Declaration
   ;

e:   'true' # True
   | 'false' # False
   | ID # Var
   | NUM # Num
   | e op=('+' | '-' | '*' | '/' | '<' | '<=' | '=' | '>' | '>=' | 'and' | 'or') e # BinOp
   | 'not' e # Not
   | '(' e ')' # Paren
   ;

INT: 'int' ;
BOOL: 'bool' ;

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
