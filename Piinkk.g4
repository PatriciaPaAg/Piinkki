grammar Piinkk;

@header {
    package antlr;
}

prog: programita0 ';' vars0? fun0* body0 EOF;
programita0: PROGRAM PROGRAMID ;

type0: INT | FLOAT;

array0: ID '[' NUMBER ']';

if0: IF '(' expresion0 ')' if1;
if1: bloque0 else0?;
else0: ELSE bloque0;

while0: WHILE '(' expresion0 ')' while1;
while1: DO bloque0;

for0: FOR ID '=' exp0 TO exp0 DO bloque0;

var0: ID | array0 | NUMBER | FLOAT_NUMBER;
var1: ID | array0;

vars0: VARS (vars1 ';')+;
vars1: type0 ':' var1 (',' var1)*;

expresion0: exp0 expresion1?;
expresion1: ('==' | '>' | '<' | '!=' | '>=' | '<=') expresion0;

exp0: termino0 exp1?;
exp1: ('+' | '-') exp0;

termino0: factor0 termino1?;
termino1: ('*' | '/') termino0;

factor0: var0;
factor1: ('(' expresion0 ')') | var0;

bloque0: '{' estatuto0* '}';
bloque1: '{' estatuto0* return0? '}';


estatuto0: asignacion0
            | if0
            | while0
            | for0
            | escritura0
            | lecturaInt0
            | escritura0
            | funCall;
            
asignacion0: ID '=' asignacion1 ';';
asignacion1: expresion0
            | funCall0;

escritura0: WRITE '(' escritura1+ ')' ';';
escritura1: (escri1 | escri2) (','(escri1 | escri2))*;
escri1: exp0;
escri2: STRING;

lecturaInt0: READ '(' ID ')' ';';

return0: RETURN '(' exp0 ')' ';' ;

typeFun0: (type0 | VOID) | BOOL;
fun0: FUNCTION fun1 vars0? funContent0;
fun1: typeFun0 ':' ID '(' (fun2)? ')';
fun2: fun3 (',' fun3)* ;
fun3: type0 ':' var1;
funContent0: bloque1;

funCall: funCall0 ';';
funCall0: ID '(' funCall1 ')';
funCall1: funCallExp funCall2*;
funCallExp: exp0;
funCall2: (',' funCall1);

body0: MAIN '('')' bloque0;
start : 'hola mundo' ;


WS: [ \t\n\r]+ -> skip;
PROGRAM: 'Program';
MAIN: 'main';
VARS: 'VARS';
FUNCTION:'function';
INT: 'int';
FLOAT: 'float';
BOOL: 'bool';
CHAR: 'char';
VOID: 'void';
RETURN: 'return';
READ: 'read';
WRITE: 'write';
IF: 'if';
THEN: 'then';
ELSE: 'else';
WHILE: 'while';	
DO: 'do';
FOR: 'FOR';
TO: 'to';
MEDIA: 'Media';
MODA: 'Moda';
VARIANZA: 'Varianza';
REGRESION_SIMPLE: 'RegresionSimple';
PLOTXY: 'PlotXY';
MEDIANA: 'Mediana';
DESVIACION_ESTANDAR: 'DesviacionEstandar';
RANGO: 'Rango';
COEFICIENTE_VARIACION: 'CoeficienteVariacion';
NUMBER: [0-9]+;
FLOAT_NUMBER: NUMBER '.' [0-9]+;
PROGRAMID: [A-Z][a-zA-Z0-9_]*;
ID: [a-z][a-zA-Z0-9_]*;
STRING: '\'' .*? '\'' | '"' .*? '"';
COMMENT:  '<3' .*? '\n' -> skip;