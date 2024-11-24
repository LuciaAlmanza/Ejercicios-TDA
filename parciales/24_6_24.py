# 4.Implementar un algoritmo potencia(b, n) que nos devuelva el resultado de b ^(n) en tiempo O(log n).
# Justificar  adecuadamente la complejidad del algoritmo implementado. Ayuda: recordar propiedades matemáticas de la potencia. 

# Por ejemplo, que a ^(h)· a^(k) = a ^(h+k ).

def potencia(b, n):
    if n == 0:
        return 1
    elif n == 1:
        return b

    medio = potencia(b, n // 2)
    if n % 2 == 0:
        return medio * medio # b^n = b^(n/2) * b^(n/2)
    else:
        return b * medio* medio # b^n = b * b^((n-1)/2) * b^((n-1)/2)

    
# O(logn)
# 2.Implementar un algoritmo greedy que permita obtener el mínimo del problema del viajante: dado un Grafo pesado G y
# un vértice de inicio v, obtener el camino de menor costo que lleve a un viajante desde v hacia cada uno de los vértices
# del grafo, pasando por cada uno de ellos una única vez, y volviendo nuevamente al origen. Se puede asumir que el grafo
# es completo. Indicar y justificar la complejidad del algoritmo implementado.
# ¿El algoritmo obtiene siempre la solución óptima? Si es así, justificar detalladamente, sino dar un contraejemplo. Indicar
# y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy.

def tsp_vecino_mas_cercano(grafo, inicio):
    visitados = set()
    camino = [inicio]
    actual = inicio
    total_cost = 0
    visitados.add(inicio)
    
    # Visitar cada nodo no visitado seleccionando el vecino más cercano
    while len(visitados) < len(grafo.obtener_vertices()):
        siguiente = None
        min_peso = float('inf')
        
        # Buscar el vecino más cercano no visitado
        for vecino in grafo.adyacentes(actual):
            if vecino not in visitados and grafo.peso_arista(actual, vecino) < min_peso:
                siguiente = vecino
                min_peso = grafo.peso_arista(actual, vecino)
        
        if siguiente is None:
            break  # No quedan más vértices para visitar (debería no suceder en grafo completo)
        
        # Añadir al camino y actualizar costo total
        camino.append(siguiente)
        total_cost += min_peso
        visitados.add(siguiente)
        actual = siguiente

    # Volver al inicio para cerrar el ciclo
    if grafo.estan_unidos(actual, inicio):
        camino.append(inicio)
        total_cost += grafo.peso_arista(actual, inicio)
    
    return camino, total_cost

# No se me ocurre ningun contraejemplo la verdad

# O(V^2)

# Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados,
# utilizando programación dinámica. Indicar y justificar la complejidad del algoritmo implementado (cuidado con esto, es
# fácil tentarse a dar una cota más alta de lo correcto). Implementar un algoritmo que permita reconstruir la solución.
# Aclaración: siempre es posible escribir a n como suma de n términos de la forma 1
# 2
# , por lo que siempre existe solución.

# Sin embargo, la expresión 10 = 32 + 12

# es una manera más económica de escribirlo para n = 10, pues sólo tiene dos

# términos.

#dp[i]=min(dp[i−j^2]+1)para todos los j tales que j^2 ≤ i

def min_squares(n):
    # Paso 1: Crear la tabla para almacenar los resultados
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # 0 términos para el número 0
    
    # Paso 2: Calcular el número mínimo de cuadrados para cada número
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
            
    # Paso 3: Reconstrucción de la solución
    result = []
    temp = n
    while temp > 0:
        for j in range(1, int(temp**0.5) + 1):
            if dp[temp] == dp[temp - j * j] + 1:
                result.append(j * j)
                temp -= j * j
                break
                
    return dp[n], result 

# 1. Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar
# tres días seguidos. Se tiene la información de la ganancia del día i (Gi), para cada día. Implementar un modelo de
# programación lineal que maximice el monto a ganar por Juan, sabiendo que no aceptará trabajar tres días seguidos.

def maximizar_ganancias(ganancias):
    n = len(ganancias)  # Número de días

    # Variables binarias que indican si Juan trabaja en el día i
    x = pulp.LpVariable.dicts("x", range(n), cat="Binary")

    # Crear el problema de optimización
    problema = pulp.LpProblem("Maximizar_Ganancias", pulp.LpMaximize)

    # Función objetivo: maximizar la ganancia total
    problema += pulp.lpSum(g ganancias[i] * x[i] for i in range(n)), "Ganancia_Total"

    # Restricciones para evitar trabajar tres días seguidos
    for i in range(n - 2):
        problema += x[i] + x[i + 1] + x[i + 2] <= 2, f"Restriccion_Tres_Dias_{i}"

    # Resolver el problema
    problema.solve()

    # Obtener el resultado: días en los que Juan trabaja
    dias_trabajo = [i for i in range(n) if pulp.value(x[i]) == 1]
    ganancia_total = pulp.value(problema.objective)

    return dias_trabajo, ganancia_total