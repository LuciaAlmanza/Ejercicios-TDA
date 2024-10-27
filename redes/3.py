def construir_red_residual(grafo, flujos):
    # Crear un nuevo grafo residual
    grafo_residual = copiar(grafo)  # Suponemos que `copiar` devuelve una copia del grafo original

    # Iterar sobre todas las aristas en el grafo original
    for (u, v), flujo in flujos.items():
        if flujo > 0:  # Si hay flujo en la arista (u, v)
            # Disminuir la capacidad en la arista original (u, v)
            capacidad_actual = grafo.capacidad(u, v)  # Obtener la capacidad original
            nueva_capacidad = capacidad_actual - flujo
            grafo_residual.actualizar_capacidad(u, v, nueva_capacidad)  # Actualizar la capacidad

            # Aumentar la capacidad de la arista reversa (v, u) en el grafo residual
            capacidad_reversa = grafo_residual.capacidad(v, u)  # Obtener capacidad de la arista reversa
            grafo_residual.actualizar_capacidad(v, u, capacidad_reversa + flujo)  # Actualizar arista reversa

        else:
            # Si no hay flujo, simplemente mantener las capacidades originales
            capacidad_actual = grafo.capacidad(u, v)
            grafo_residual.actualizar_capacidad(u, v, capacidad_actual)  # Mantener la capacidad original

    return grafo_residual

def copiar_grafo(grafo):
    # Crear un nuevo grafo
    grafo_copiado = Grafo(dirigido=grafo.dirigido)  # Asumimos que la propiedad 'dirigido' es accesible
    
    # Agregar todos los vértices del grafo original
    for v in grafo.obtener_vertices():
        grafo_copiado.agregar_vertice(v)
    
    # Agregar todas las aristas del grafo original
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            peso = grafo.peso_arista(v, w)
            grafo_copiado.agregar_arista(v, w, peso)
    
    return grafo_copiado