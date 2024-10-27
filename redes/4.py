from collections import deque

def encontrar_camino_aumento(grafo_residual, s, t):
    # Cola para el BFS
    cola = deque()
    cola.append(s)
    
    # Diccionario para almacenar los predecesores
    predecesor = {s: None}
    
    # Conjunto para rastrear los nodos visitados
    visitados = set()
    visitados.add(s)

    while cola:
        nodo_actual = cola.popleft()
        
        # Si hemos llegado al nodo sumidero, reconstruimos el camino
        if nodo_actual == t:
            camino = []
            while nodo_actual is not None:
                camino.append(nodo_actual)
                nodo_actual = predecesor[nodo_actual]
            camino.reverse()  # Invertir el camino para que vaya de s a t
            return camino
        
        # Explorar los nodos adyacentes
        for vecino in grafo_residual.adyacentes(nodo_actual):
            if vecino not in visitados and grafo_residual.peso_arista(nodo_actual, vecino) > 0:
                visitados.add(vecino)
                predecesor[vecino] = nodo_actual
                cola.append(vecino)

    # Si no se encontró un camino
    return None