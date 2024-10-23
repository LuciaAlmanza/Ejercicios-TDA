from grafo import Grafo

def crear_grafo_tablero(n):
    grafo = Grafo(dirigido=False)

    # Agregar vértices para cada casilla del tablero
    for i in range(n):
        for j in range(n):
            grafo.agregar_vertice((i, j))

    # Definir los movimientos del caballo
    mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
    mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Agregar aristas según los movimientos del caballo
    for i in range(n):
        for j in range(n):
            for k in range(8):
                new_x = i + mov_x[k]
                new_y = j + mov_y[k]
                if 0 <= new_x < n and 0 <= new_y < n:
                    grafo.agregar_arista((i, j), (new_x, new_y))

    return grafo

def es_ciclo_hamiltoniano(grafo, vertice_inicial, visitados, camino):
    camino.append(vertice_inicial)
    visitados.add(vertice_inicial)

    # Si todos los vértices han sido visitados
    if len(visitados) == len(grafo.obtener_vertices()):
        # Verifica si hay un camino de vuelta al inicio
        if vertice_inicial in grafo.adyacentes(camino[0]):
            return True, camino

    for vertice in grafo.adyacentes(vertice_inicial):
        if vertice not in visitados:
            exito, solucion = es_ciclo_hamiltoniano(grafo, vertice, visitados, camino)
            if exito:
                return True, solucion

    # Backtrack
    camino.pop()
    visitados.remove(vertice_inicial)
    return False, []

def knight_tour(n):
    grafo = crear_grafo_tablero(n)
    vertice_inicial = (0, 0)  # Comienza en la esquina superior izquierda

    visitados = set()
    camino = []

    existe_solucion, camino_solucion = es_ciclo_hamiltoniano(grafo, vertice_inicial, visitados, camino)

    if existe_solucion:
        return camino_solucion
    else:
        return None