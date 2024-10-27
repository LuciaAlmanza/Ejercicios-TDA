def buscar_camino_disjunto(grafo, inicio, fin, caminos_ocupados):
    # Realizar una búsqueda (BFS) desde inicio a fin evitando nodos y aristas en caminos_ocupados
    cola = Queue()
    cola.enqueue([inicio])
    visitado = set([inicio])
    
    while not cola.is_empty():
        camino = cola.dequeue()
        ultimo_nodo = camino[-1]
        
        if ultimo_nodo == fin:
            return camino  # Camino encontrado

        for vecino in grafo.adyacentes(ultimo_nodo):
            if (ultimo_nodo, vecino) not in caminos_ocupados and vecino not in visitado:
                nuevo_camino = camino + [vecino]
                cola.enqueue(nuevo_camino)
                visitado.add(vecino)
                
    return None  # No hay camino disponible

def enviar_hijos_a_escuela(grafo, casa, escuela):
    caminos_ocupados = set()
    caminos_para_hijos = []

    for i in range(5):  # Intentamos encontrar un camino para cada uno de los 5 hijos
        camino = buscar_camino_disjunto(grafo, casa, escuela, caminos_ocupados)
        
        if camino is None:
            return False  # No se puede encontrar un camino disjunto para este hijo
        
        # Marcar aristas y nodos del camino como ocupados (excepto el nodo escuela y casa)
        for j in range(len(camino) - 1):
            caminos_ocupados.add((camino[j], camino[j+1]))
            caminos_ocupados.add((camino[j+1], camino[j]))

        caminos_para_hijos.append(camino)
    
    return True 