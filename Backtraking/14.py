def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    solucion_parcial = set([])
    sol_optima = set(vertices)
    return list(dominating_set_rec(grafo, vertices, 0, solucion_parcial, sol_optima))

def dominating_set_rec(grafo, vertices, indice, solucion_parcial, sol_optima):
    if len(solucion_parcial) >= len(sol_optima):
        return sol_optima
    if es_dominating_set(grafo, solucion_parcial):
        return set(solucion_parcial)
    if indice == len(vertices):
        return sol_optima

    v = vertices[indice]
    solucion_parcial.add(v)
    sol_optima = dominating_set_rec(grafo, vertices, indice+1, solucion_parcial, sol_optima)
    
    solucion_parcial.remove(v)
    return dominating_set_rec(grafo, vertices, indice+1, solucion_parcial, sol_optima)

def es_dominating_set(grafo, solucion_parcial):
    for v in grafo.obtener_vertices():
        if v in solucion_parcial:
            continue
        tiene_adyacente = False
        for w in grafo.adyacentes(v):
            if w in solucion_parcial:
                tiene_adyacente = True
                break
        if tiene_adyacente == False:
            return False
    return True