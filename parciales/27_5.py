# 4. Implementar un algoritmo que (por backtracking) dado un grafo no dirigido en el que sus vértices tienen valores positivos,
# permita obtener el Dominating Set de suma mínima. Es decir, aquel dominating set en el cual la suma de todos los
# valores de los vértices sea mínima (no es importante que la cantidad de vértices del set sea mínima). Por simplicidad,
# considerar que el grafo es conexo.

def es_dominante(grafo, conjunto_dominante):
    vertices = set(conjunto_dominante)
    for v in grafo.obtener_vertices():
        if v not in vertices:  # Solo verificar los vértices no en el conjunto
            if not any(ad in vertices for ad in grafo.adyacentes(v)):
                return False
    return True

def backtrack(grafo, vertices, index, conjunto_actual, mejor_conjunto, suma_actual):
    if index == len(vertices):
        if es_dominante(grafo, conjunto_actual):
            if (suma_actual < mejor_conjunto[0]):
                mejor_conjunto[0] = suma_actual
                mejor_conjunto[1] = conjunto_actual.copy()
        return

    # Omitir el vértice actual
    backtrack(grafo, vertices, index + 1, conjunto_actual, mejor_conjunto, suma_actual)

    # Incluir el vértice actual
    v_actual = vertices[index]
    conjunto_actual.append(v_actual)
    backtrack(grafo, vertices, index + 1, conjunto_actual, mejor_conjunto, suma_actual + grafo.valores[v_actual])
    conjunto_actual.pop()  # Deshacer la elección

def encontrar_dominating_set_minimo(grafo):
    vertices = grafo.obtener_vertices()
    mejor_conjunto = [float('inf'), []]  # [suma mínima, conjunto]
    backtrack(grafo, vertices, 0, [], mejor_conjunto, 0)
    return mejor_conjunto

# Sea G un grafo dirigido “camino” (las aristas son de la forma (vi

# , vi−1)). Cada vertice tiene un valor (positivo).
# Implementar un algoritmo que, utilizando programación dinámica, obtenga el Dominating Set de suma mínima
# dentro de un grafo de dichas características. Dar la ecuación de recurrencia correspondiente al problema. Indicar
# y justificar la complejidad del algoritmo implementado. Indicar y justificar la complejidad espacial del algoritmo
# implementado, y si hay una optimización que permita consumir menos espacio.

# dp[i]=min(dp[i−1],dp[i−2]+wi)

def dominating_set_min_sum(weights):
    n = len(weights)
    if n == 0:
        return 0
    if n == 1:
        return weights[0]
    if n == 2:
        return min(weights[0], weights[1])
    
    # Inicializar las variables
    prev2 = weights[0]  # dp[i-2]
    prev1 = min(weights[0], weights[1])  # dp[i-1]
    
    for i in range(2, n):
        current = min(prev1, prev2 + weights[i])
        prev2 = prev1
        prev1 = current

    return prev1

# 3. Realizar un modelo de programación lineal que obtenga el mínimo Dominating Set de un Grafo no dirigido. En dicho
# grafo, cada vértice tiene un valor (positivo), y se quiere que dicho Dominating Set sea el de mínima suma de dichos
# valores.

def minimum_dominating_set(grafo, valores):
    vertices = grafo.obtener_vertices()
    n = len(vertices)  # Número de vértices

    # Variable binaria que indica si el vértice v está en el Dominating Set
    x = pulp.LpVariable.dicts("x", vertices, cat="Binary")

    # Crear el problema de optimización
    problema = pulp.LpProblem("Minimum_Dominating_Set", pulp.LpMinimize)

    # Función objetivo: minimizar la suma de los valores de los vértices seleccionados
    problema += pulp.lpSum(valores[v] * x[v] for v in vertices), "Suma_Valores"

    # Restricción de dominación
    for u in vertices:
        # Cada vértice u debe estar dominado por sí mismo o por uno de sus vecinos
        problema += x[u] + pulp.lpSum(x[v] for v in grafo.adyacentes(u)) >= 1, f"Dominacion_{u}"

    # Resolver el problema
    problema.solve()

    # Obtener el resultado: vértices en el Dominating Set
    resultado = [v for v in vertices if pulp.value(x[v]) == 1]

    return resultado, pulp.value(problema.objective)