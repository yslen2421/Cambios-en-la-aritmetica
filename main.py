import sys
from antlr4 import InputStream, CommonTokenStream
from G1Lexer import G1Lexer
from G1Parser import G1Parser
from EvalVisitor import EvalVisitor


def evaluar(texto):
    lexer = G1Lexer(InputStream(texto))       # 1. Análisis léxico
    tokens = CommonTokenStream(lexer)
    parser = G1Parser(tokens)                 # 2. Análisis sintáctico
    arbol = parser.prog()

    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"'{texto}' no es una expresión válida")
        return

    try:
        resultado = EvalVisitor().visit(arbol)  # 3. Evaluación
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
        print("Calculadora G1 (escribe 'salir' para terminar)")
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

