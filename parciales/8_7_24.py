# Definimos a un grafo ordenado como un grafo dirigido con vértices v1, · · · , vn en el que todos los vértices, salvo vn
# tienen al menos una arista que sale del vértice, y cada arista va de un vértice de menor índice a uno de mayor índice (es
# decir, las aristas tienen la forma (vi

# , vj ) con i < j). Implementar un algoritmo de programación dinámica que dado
# un grafo ordenado (y, si les resulta útil, una lista con los vértices en orden) determine cuál es la longitud del camino más
# largo. Dar la ecuación de recurrencia correspondiente. Dar también el algoritmo de recontrucción de la solución. Indicar
# y justificar la complejidad del algoritmo implementado. Se pone a continuación un ejemplo de un grafo ordenado.

#dp[i]=max(dp[j]+1)para todos los j tales que (vj,v i) es una arista y j<i

def longest_path_ordered_graph(vertices, edges):
    n = len(vertices)
    
    # Paso 1: Inicializar el array dp
    dp = [1] * n  # Longitud mínima es 1 (el vértice mismo)
    prev = [-1] * n  # Para reconstruir el camino

    # Paso 2: Calcular la longitud del camino más largo
    for i in range(1, n):
        for j in range(i):
            if (vertices[j], vertices[i]) in edges:  # Si hay una arista de v_j a v_i
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j  # Guardar el índice de v_j

    # Paso 3: Encontrar la longitud máxima del camino
    max_length = max(dp)
    end_vertex = dp.index(max_length)

    # Paso 4: Reconstrucción del camino
    path = []
    while end_vertex != -1:
        path.append(vertices[end_vertex])
        end_vertex = prev[end_vertex]

    path.reverse()  # Invertir el camino para tenerlo en el orden correcto
    return max_length, path


# 3. Implementar un algoritmo greedy que permita obtener el Independent Set máximo (es decir, que contenga la mayor
# cantidad de vértices) para el caso de un árbol (en el contexto de teoría de grafos, no un árbol binario). Indicar y
# justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. Indicar si el
# algoritmo siempre da solución óptima. Si lo es, explicar detalladamente, sino dar un contraejemplo.

def max_independent_set(raiz):
    incluido, excluido = dfs(raiz)
    return max(incluido, excluido)

def dfs(nodo):
    if not nodo:
        return (0, 0)

    nodo_incluido = 1
    nodo_excluido = 0

    for hijo in nodo.hijos:
        incluido, excluido = dfs(hijo)
        nodo_incluido += excluido #si incluimos este nodo, no incluimos hijos
        nodo_excluido += max(incluido, excluido)  #tomamos el mejor de incluir o no incluir el hijo
    return (nodo_incluido, nodo_excluido)

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
