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

# Implementar un algoritmo que dado un grafo, obtenga el clique de mayor tamaño del mismo.
def es_clique(grafo, conjunto):
    for i in range(len(conjunto)):
        for j in range(i + 1, len(conjunto)):
            if not grafo.son_vecinos(conjunto[i], conjunto[j]):
                return False
    return True

def backtrack(grafo, vertices, index, conjunto_actual, mejor_clique):
    if es_clique(grafo, conjunto_actual):
        if len(conjunto_actual) > len(mejor_clique[0]):
            mejor_clique[0] = conjunto_actual.copy()

    for i in range(index, len(vertices)):
        conjunto_actual.append(vertices[i])
        backtrack(grafo, vertices, i + 1, conjunto_actual, mejor_clique)
        conjunto_actual.pop()  # Deshacer la elección

def encontrar_clique_maxima(grafo):
    vertices = grafo.obtener_vertices()
    mejor_clique = [[]]  # Almacena el clique de mayor tamaño
    backtrack(grafo, vertices, 0, [], mejor_clique)
    return mejor_clique[0]
