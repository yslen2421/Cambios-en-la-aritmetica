import sys
from antlr4 import InputStream, CommonTokenStream
from G2Lexer import G2Lexer
from G2Parser import G2Parser
from EvalVisitorG2 import EvalVisitorG2


def evaluar(texto):
    lexer = G2Lexer(InputStream(texto))       # 1. Análisis léxico
    tokens = CommonTokenStream(lexer)
    parser = G2Parser(tokens)                 # 2. Análisis sintáctico
    arbol = parser.prog()

    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"'{texto}' no es una expresión válida")
        return

    try:
        resultado = EvalVisitorG2().visit(arbol)  # 3. Evaluación
        print(f"{texto} = {resultado}")
    except ZeroDivisionError as error:
        print(error)


def main():
    if len(sys.argv) > 1:
        # Modo archivo: evalúa cada línea del archivo
        with open(sys.argv[1], encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    evaluar(linea)
    else:
        # Modo interactivo
        print("Calculadora G2 (escribe 'salir' para terminar)")
        while True:
            try:
                texto = input(">>> ").strip()
            except EOFError:
                break
            if texto.lower() == "salir":
                break
            if texto:
                evaluar(texto)


if __name__ == "__main__":
    main()

