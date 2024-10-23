# 3. Implementar un algoritmo greedy que permita obtener el Independent Set máximo (es decir, que contenga la mayor
# cantidad de vértices) para el caso de un árbol (en el contexto de teoría de grafos, no un árbol binario). Indicar y
# justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. Indicar si el
# algoritmo siempre da solución óptima. Si lo es, explicar detalladamente, sino dar un contraejemplo.

def obtener_hijos(arbol, nodo, padre):
    return [hijo for hijo in arbol.obtener_adyacentes[nodo] if hijo != padre]

def max_independent_set(arbol, nodo, padre, conjunto_indep, visitados):
    # Marcar el nodo como visitado
    visitados.add(nodo)
    incluir = True

    # Revisar los hijos del nodo actual
    for hijo in arbol.obtener_hijos(arbol,nodo, padre):
        if hijo not in visitados:
            # Recursión sobre los hijos
            max_independent_set(arbol, hijo, nodo, conjunto_indep, visitados)

            # Si algún hijo está en el conjunto independiente, no podemos incluir el nodo actual
            if hijo in conjunto_indep:
                incluir = False

    # Incluir el nodo si ninguno de sus hijos está en el conjunto independiente
    if incluir:
        conjunto_indep.add(nodo)

def obtener_max_independent_set(arbol, raiz):
    conjunto_indep = set()
    visitados = set()  # Usamos un conjunto para almacenar los nodos ya visitados
    max_independent_set(arbol, raiz, None, conjunto_indep, visitados)
    return conjunto_indep

# O(n)
