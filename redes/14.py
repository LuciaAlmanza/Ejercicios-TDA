def construir_grafo(habitantes, clubes, partidos, n):
    grafo = Grafo(dirigido=True)

    # Nodo fuente y sumidero
    fuente = 'S'
    sumidero = 'T'
    grafo.agregar_vertice(fuente)
    grafo.agregar_vertice(sumidero)
    
    # Agregar habitantes y conexiones al grafo
    for habitante in habitantes:
        partido = habitante.partido
        grafo.agregar_vertice(habitante)
        
        # Conectar fuente al habitante según su partido
        capacidad_partido = n // 2
        if partido not in grafo.adyacentes(fuente):
            grafo.agregar_arista(fuente, habitante, capacidad=capacidad_partido)
        
        # Conectar habitante a sus clubes
        for club in habitante.clubes:
            if club not in grafo.obtener_vertices():
                grafo.agregar_vertice(club)
            grafo.agregar_arista(habitante, club, capacidad=1)
    
    # Conectar cada club al sumidero
    for club in clubes:
        grafo.agregar_arista(club, sumidero, capacidad=1)

    return grafo

def asignar_representantes(habitantes, clubes, partidos, n):
    grafo = construir_grafo(habitantes, clubes, partidos, n)
    
    # Calcular el flujo máximo de fuente a sumidero
    flujo_maximo = calcular_flujo_maximo(grafo, fuente='S', sumidero='T')
    
    # Verificar si el flujo máximo es igual al número de clubes
    if flujo_maximo == len(clubes):
        return "Es posible asignar los representantes"
    else:
        return "No es posible asignar los representantes"