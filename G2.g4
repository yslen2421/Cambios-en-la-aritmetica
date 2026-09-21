// Gramática G2 — Asociatividad derecha, precedencia correcta (*/ > +-)
grammar G2;

prog : e EOF ;

e   : t '+' e   # G2Suma
    | t '-' e   # G2Resta
    | t         # G2TermE
    ;

t   : f '*' t   # G2Mult
    | f '/' t   # G2Div
    | f         # G2TermT
    ;

f   : '(' e ')' # G2Paren
    | NUM       # G2Num
    ;

NUM : [0-9]+ ('.' [0-9]+)? ;
WS  : [ \t\r\n]+ -> skip ;
