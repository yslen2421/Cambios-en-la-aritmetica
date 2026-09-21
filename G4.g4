// Gramática G4 — Precedencia: / > * > - > +, asociatividad izquierda
grammar G4;

prog   : suma EOF ;

suma   : suma '+' resta     # G4Suma
       | resta              # G4PasaResta
       ;

resta  : resta '-' mult     # G4Resta
       | mult               # G4PasaMult
       ;

mult   : mult '*' div       # G4Mult
       | div                # G4PasaDiv
       ;

div    : div '/' factor     # G4Div
       | factor             # G4PasaFactor
       ;

factor : '(' suma ')'       # G4Paren
       | NUM                # G4Num
       ;

NUM : [0-9]+ ('.' [0-9]+)? ;
WS  : [ \t\r\n]+ -> skip ;
