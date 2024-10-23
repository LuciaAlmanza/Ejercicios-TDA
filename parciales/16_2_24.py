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

def backtrack(grafo, ciclo, actual, k):
    if len(ciclo) == k:
        # Verificar si el último vértice se conecta al primero
        if ciclo[0] in grafo.adyacentes(actual):
            return ciclo + [ciclo[0]]  # Retorna el ciclo completo
        return None

    for vecino in grafo.adyacentes(actual):
        if vecino not in ciclo:  # Evitar vértices repetidos
            ciclo.append(vecino)  # Añadir vértice al ciclo
            resultado = backtrack(grafo, ciclo, vecino, k)
            if resultado:  # Si se encontró un ciclo válido
                return resultado
            ciclo.pop()  # Retroceder

    return None  # No se encontró ciclo


def encontrar_ciclo(grafo, k):
    # Probar desde cada vértice del grafo
    for vertice in grafo.obtener_vertices():
        ciclo_inicial = [vertice]
        resultado = backtrack(grafo, ciclo_inicial, vertice, k)
        if resultado:
            return resultado

    return None  