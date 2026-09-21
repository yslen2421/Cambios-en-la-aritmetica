// Gramática G1 — Asociatividad izquierda, precedencia correcta (*/ > +-)
grammar G1;

prog : e EOF ;

e   : e '+' t   # G1Suma
    | e '-' t   # G1Resta
    | t         # G1TermE
    ;

t   : t '*' f   # G1Mult
    | t '/' f   # G1Div
    | f         # G1TermT
    ;

f   : '(' e ')' # G1Paren
    | NUM       # G1Num
    ;

NUM : [0-9]+ ('.' [0-9]+)? ;
WS  : [ \t\r\n]+ -> skip ;
