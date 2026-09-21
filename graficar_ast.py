import sys
import os
import importlib
import subprocess
from antlr4 import InputStream, CommonTokenStream, Token
from antlr4.tree.Tree import TerminalNode


class Nodo:
    """Nodo del AST: un operador con dos hijos, o un número sin hijos."""
    def __init__(self, valor, hijos=None):
        self.valor = valor
        self.hijos = hijos or []


def construir_ast(arbol):
    """Convierte el árbol sintáctico de ANTLR en un AST."""
    if isinstance(arbol, TerminalNode):
        return Nodo(arbol.getText())

    hijos = [arbol.getChild(i) for i in range(arbol.getChildCount())]
    # Quitar el token EOF
    hijos = [h for h in hijos
             if not (isinstance(h, TerminalNode) and h.getSymbol().type == Token.EOF)]

    # Nodo que solo pasa a otro nivel (e -> t, t -> f): se salta
    if len(hijos) == 1:
        return construir_ast(hijos[0])

    # Paréntesis: se queda solo con lo de adentro
    if len(hijos) == 3 and isinstance(hijos[0], TerminalNode) and hijos[0].getText() == "(":
        return construir_ast(hijos[1])

    # Operación binaria: izquierda OPERADOR derecha
    if len(hijos) == 3:
        operador = hijos[1].getText()
        return Nodo(operador, [construir_ast(hijos[0]), construir_ast(hijos[2])])

    raise ValueError("Estructura no reconocida")


def evaluar(nodo):
    """Evalúa el AST recursivamente."""
    if not nodo.hijos:
        return float(nodo.valor)
    izq = evaluar(nodo.hijos[0])
    der = evaluar(nodo.hijos[1])
    if nodo.valor == "+":
        return izq + der
    if nodo.valor == "-":
        return izq - der
    if nodo.valor == "*":
        return izq * der
    if der == 0:
        raise ZeroDivisionError("división por cero")
    return izq / der


def a_texto(nodo):
    """Muestra el AST en texto con paréntesis explícitos."""
    if not nodo.hijos:
        return nodo.valor
    return f"({a_texto(nodo.hijos[0])} {nodo.valor} {a_texto(nodo.hijos[1])})"


def a_dot(raiz, titulo):
    """Genera el código Graphviz (formato DOT) del AST."""
    lineas = [
        "digraph AST {",
        f'  label="{titulo}"; labelloc=t; fontsize=18; fontname="Helvetica";',
        '  node [shape=circle, style=filled, fontname="Helvetica", fontsize=16];',
    ]
    contador = [0]

    def recorrer(nodo):
        id_nodo = f"n{contador[0]}"
        contador[0] += 1
        color = "lightblue" if nodo.hijos else "lightyellow"
        lineas.append(f'  {id_nodo} [label="{nodo.valor}", fillcolor={color}];')
        for hijo in nodo.hijos:
            id_hijo = recorrer(hijo)
            lineas.append(f"  {id_nodo} -> {id_hijo};")
        return id_nodo

    recorrer(raiz)
    lineas.append("}")
    return "\n".join(lineas)


def main():
    if len(sys.argv) != 3:
        print("Uso: python3 graficar_ast.py <G1|G2|G3|G4> <archivo_pruebas>")
        return

    gramatica, archivo = sys.argv[1], sys.argv[2]
    Lexer = getattr(importlib.import_module(f"{gramatica}Lexer"), f"{gramatica}Lexer")
    Parser = getattr(importlib.import_module(f"{gramatica}Parser"), f"{gramatica}Parser")

    carpeta = f"ast_{gramatica}"
    os.makedirs(carpeta, exist_ok=True)

    with open(archivo, encoding="utf-8") as f:
        expresiones = [linea.strip() for linea in f if linea.strip()]

    print(f"===== {gramatica} =====")
    for i, expresion in enumerate(expresiones, 1):
        parser = Parser(CommonTokenStream(Lexer(InputStream(expresion))))
        arbol = parser.prog()

        if parser.getNumberOfSyntaxErrors() > 0:
            print(f"[{i}] {expresion}  ->  expresión inválida, no se grafica")
            continue

        ast = construir_ast(arbol)
        try:
            resultado = evaluar(ast)
        except ZeroDivisionError as error:
            resultado = f"Error: {error}"

        print(f"[{i}] {expresion}  ->  AST: {a_texto(ast)}  =  {resultado}")

        nombre = os.path.join(carpeta, f"prueba_{i:02d}")
        with open(nombre + ".dot", "w", encoding="utf-8") as salida:
            salida.write(a_dot(ast, f"{gramatica}:  {expresion}  =  {resultado}"))
        subprocess.run(["dot", "-Tpng", nombre + ".dot", "-o", nombre + ".png"], check=True)

    print(f"Imágenes guardadas en la carpeta {carpeta}/")


if __name__ == "__main__":
    main()
