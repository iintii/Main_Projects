grammar SimpleIR;

unit: function;

function: 'function' functionName=NAME localVariables? parameters? statement* returnStatement end;

statementList : statement* EOF ; // Rule to parse only a sequence of statements

localVariables: 'localVariables' variables=NAME+;

parameters: 'parameters' formals=NAME+;

returnStatement: 'return' operand=(NAME | NUM);

end: 'end' 'function';

statement: assign | dereference | reference | assignDereference | operation | call | label | gotoStatement | ifGoto;

operation: variable=NAME ':=' operand1=(NAME | NUM) operatorKind=('+' | '-' | '*' | '/' | '%') operand2=(NAME | NUM);

assign: variable=NAME ':=' operand=(NAME | NUM);

dereference: variable=NAME ':=' '*' operand=NAME;

reference: variable=NAME ':=' '&' operand=NAME;

assignDereference: '*' variable=NAME ':=' operand=(NAME | NUM);

call: variable=NAME ':=' 'call' functionName=NAME actuals=NAME*;

label: labelName=NAME ':';

gotoStatement: 'goto' labelName=NAME;

ifGoto: 'if' operand1=(NAME | NUM) operatorKind=('=' | '!=' | '<' | '<=' | '>' | '>=') operand2=(NAME | NUM) 'goto' labelName=NAME;

NAME: [a-zA-Z_] ([a-zA-Z_] | [0-9])* ;
NUM: [0-9]+ ;

PLUS: '+' ;
MINUS: '-' ;
STAR: '*' ;
SLASH: '/' ;
PERCENT: '%' ;

EQ: '=' ;
NEQ: '!=' ;
LT: '<' ;
LTE: '<=' ;
GT: '>' ;
GTE: '>=' ;

WS:   [ \t\r\n]+ -> skip ;

COMMENT : '#' ~[\r\n]* -> skip ; // Comments are already skipped by the lexer
