# 5. El famoso ladrón Francesco Rizzoli (hermano del “árbitro” de la final del 2014), ha decidido hacer un atraco a un
# laboratorio farmacéutico. Allí puede robarse diferentes fármacos que se están estudiando (en formato líquido). Tiene un
# catálogo del valor de cada fármaco, que puede vender en el mercado negro. De cada fármaco hay una diferente cantidad
# disponible (medible en ml). Rizzoli sólo tiene posibilidad en su equipo de llevarse como máximo L ml en fármacos. Lo
# bueno es que sabe que puede fraccionar y poner proporciones de los fármacos; y en ese caso lo vendería en su valor
# proporcional. Implementar un algoritmo greedy que obtenga los fármacos (y cantidades) que Rizzoli debe robarse para
# obtener la máxima ganancia posible (el algoritmo debe ser óptimo, en esta familia no se aceptan los robos a medias).
# Justificar por qué el algoritmo propuesto es Greedy. Indicar y justificar la complejidad del algoritmo implementado.

def max_ganancia(farmacos, L):
    # Calcular valor por mililitro y crear una lista de fármacos
    f_list = [(valor, cantidad, valor / cantidad) for valor, cantidad in farmacos]
    
    # Ordenar los fármacos por valor por mililitro (en orden descendente)
    f_list.sort(key=lambda x: x[2], reverse=True)

    total_ganancia = 0
    cantidad_tomada = []

    for valor, cantidad, valor_por_ml in f_list:
        if L == 0:
            break  # Ya no podemos llevar más

        if cantidad <= L:
            # Tomar todo el fármaco
            total_ganancia += valor
            cantidad_tomada.append((valor, cantidad))
            L -= cantidad
        else:
            # Tomar fracción del fármaco
            total_ganancia += valor_por_ml * L
            cantidad_tomada.append((valor_por_ml * L, L))
            L = 0  # Capacidad alcanzada

    return total_ganancia, cantidad_tomada

# 3.Implementar un algoritmo que reciba un grafo no dirigido y un número k, y devuelva un ciclo de tamaño exactamente k
# del grafo, si es que existe.

def ciclo_k(grafo, k):
    for v in grafo:
        resultado = []
        if bt(grafo, k, resultado, set(), v, v):
            return resultado
    return None

def bt(grafo, k, posible_solucion, visitados, v_inicio, v):
    posible_solucion.append(v)
    visitados.add(v)

    if len(posible_solucion) == k:
        if v_inicio in grafo.adyacentes(v):
            posible_solucion.append(v_inicio)
            return True
        else:
            posible_solucion.pop()
            visitados.remove(v)
            return False

    for w in grafo.adyacentes(v):
        if w not in visitados:
            if bt(grafo, k, posible_solucion, visitados, v_inicio, w):
                return True

    posible_solucion.pop()
    visitados.remove(v)
    return False

# En clase vimos una solución óptima del problema del cambio utilizando programación dinámica. Ahora planteamos un
# problema similar: Implementar un algoritmo que dado un set de monedas posibles y una cantidad de cambio a dar,
# devuelva la cantidad de formas diferentes que hay para dar dicho cambio. El algoritmo a implementar debe ser
# también por programación dinámica. Indicar y justificar la complejidad del algoritmo implementado. Importante: antes
# de escribir código, escribir (y describir) la ecuación de recurrencia.

# dp[i]=dp[i]+dp[i−mj]

def contar_formas_monedas(monedas, C):
    # Inicializamos el arreglo DP
    dp = [0] * (C + 1)
    dp[0] = 1  # Hay exactamente una forma de dar 0 de cambio (no usar monedas)
    
    # Para cada moneda, actualizamos el arreglo dp
    for moneda in monedas:
        for i in range(moneda, C + 1):
            dp[i] += dp[i - moneda]
    
    return dp[C]