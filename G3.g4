// Gramática G3 — Asociatividad izquierda, precedencia invertida (+- > */)
grammar G3;

prog : e EOF ;

e   : e '*' t   # G3Mult
    | e '/' t   # G3Div
    | t         # G3TermE
    ;

t   : t '+' f   # G3Suma
    | t '-' f   # G3Resta
    | f         # G3TermT
    ;

f   : '(' e ')' # G3Paren
    | NUM       # G3Num
    ;

NUM : [0-9]+ ('.' [0-9]+)? ;
WS  : [ \t\r\n]+ -> skip ;
