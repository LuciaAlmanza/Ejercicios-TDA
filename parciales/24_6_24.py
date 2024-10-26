# 4.Implementar un algoritmo potencia(b, n) que nos devuelva el resultado de b ^(n) en tiempo O(log n).
# Justificar  adecuadamente la complejidad del algoritmo implementado. Ayuda: recordar propiedades matemáticas de la potencia. 

# Por ejemplo, que a ^(h)· a^(k) = a ^(h+k ).

def potencia(b, n):
    # Caso base: cualquier número elevado a la potencia de 0 es 1
    if n == 0:
        return 1
    # Caso recursivo
    if n % 2 == 0:  # n es par
        half_pow = potencia(b, n // 2)  # Divide el problema
        return half_pow * half_pow  # Combina las soluciones
    else:  # n es impar
        return b * potencia(b, n - 1)  # Un caso más simple

    
# O(logn)
# 2.Implementar un algoritmo greedy que permita obtener el mínimo del problema del viajante: dado un Grafo pesado G y
# un vértice de inicio v, obtener el camino de menor costo que lleve a un viajante desde v hacia cada uno de los vértices
# del grafo, pasando por cada uno de ellos una única vez, y volviendo nuevamente al origen. Se puede asumir que el grafo
# es completo. Indicar y justificar la complejidad del algoritmo implementado.
# ¿El algoritmo obtiene siempre la solución óptima? Si es así, justificar detalladamente, sino dar un contraejemplo. Indicar
# y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy.

def tsp_nearest_neighbor(grafo, inicio):
    n = len(grafo)  # Cantidad de vértices
    visitados = [False] * n  # Seguimiento de los vértices visitados
    camino = [inicio]  # Iniciar el camino en el vértice de inicio
    costo_total = 0  # Costo acumulado del recorrido
    actual = inicio  # Vértice actual
    visitados[inicio] = True  # Marcar el vértice inicial como visitado

    for _ in range(n - 1):  # Repetir n-1 veces para visitar todos los vértices
        siguiente = -1
        menor_distancia = float('inf')

        # Buscar el vecino no visitado más cercano
        for vecino in range(n):
            if not visitados[vecino] and grafo[actual][vecino] < menor_distancia:
                menor_distancia = grafo[actual][vecino]
                siguiente = vecino

        # Moverse al vecino más cercano
        camino.append(siguiente)
        costo_total += menor_distancia
        visitados[siguiente] = True
        actual = siguiente

    # Volver al vértice de inicio
    costo_total += grafo[actual][inicio]
    camino.append(inicio)

    return camino, costo_total

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