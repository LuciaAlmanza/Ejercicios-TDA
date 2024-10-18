from grafo import Grafo

def contar_ordenamientos(grafo):
    vertices = grafo.obtener_vertices()
    orden_actual = []
    visitados = {v: False for v in vertices}
    total_ordenamientos = [0]  # Usar una lista para contar por referencia

    # Inicia el proceso de backtracking
    backtrack(orden_actual, visitados, grafo, total_ordenamientos)

    return total_ordenamientos[0]

def backtrack(orden_actual, visitados, grafo, total_ordenamientos):
    if len(orden_actual) == len(visitados):
        total_ordenamientos[0] += 1
        return

    for v in visitados.keys():
        if not visitados[v] and es_valido_para_agregar(v, orden_actual, grafo):
            visitados[v] = True
            orden_actual.append(v)
            backtrack(orden_actual, visitados, grafo, total_ordenamientos)  # Recurre
            orden_actual.pop()  # Deshacer la acción
            visitados[v] = False  # Marcar como no visitado

def es_valido_para_agregar(v, orden_actual, grafo):
    # Verifica si se puede agregar el vértice v al orden actual
    for w in grafo.adyacentes(v):
        if w in orden_actual:  # Si w ya está en el orden actual, no se puede agregar v
            return False
    return True