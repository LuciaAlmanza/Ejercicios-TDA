from grafo import Grafo

def contar_ordenamientos(grafo):
    orden_actual = []
    visitados = set()  # Usar un conjunto en lugar de un diccionario
    total_ordenamientos = [0]  # Usar una lista para contar por referencia

    # Inicia el proceso de backtracking
    backtrack(orden_actual, visitados, grafo, total_ordenamientos)

    return total_ordenamientos[0]

def backtrack(orden_actual, visitados, grafo, total_ordenamientos):
    if len(orden_actual) == len(grafo.obtener_vertices()):
        total_ordenamientos[0] += 1
        return

    for v in grafo.obtener_vertices():
        if v not in visitados and es_valido_para_agregar(v, orden_actual, grafo):
            visitados.add(v)  # Marcar como visitado usando un conjunto
            orden_actual.append(v)
            backtrack(orden_actual, visitados, grafo, total_ordenamientos)  # Recurre
            orden_actual.pop()  # Deshacer la acción
            visitados.remove(v)  # Marcar como no visitado al hacer backtracking

def es_valido_para_agregar(v, orden_actual, grafo):
    # Verifica si se puede agregar el vértice v al orden actual
    for w in grafo.adyacentes(v):
        if w in orden_actual:  # Si w ya está en el orden actual, no se puede agregar v
            return False
    return True