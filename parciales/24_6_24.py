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