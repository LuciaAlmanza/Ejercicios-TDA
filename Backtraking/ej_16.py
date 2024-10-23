
def pintar_colectivos(colectivos, paradas):
    grafo = Grafo(False, vertices_init=colectivos)
    for parada in paradas:
        for i, c1 in enumerate(parada):
            for c2 in parada[i+1:]:
                if not grafo.estan_unidos(c1, c2):
                    grafo.agregar_arista(c1, c2)
    return colorear(grafo)

def colorear(grafo):
    n_colores = 0
    colores = {}
    vertices = grafo.obtener_vertices()
    return colorear_rec(grafo, n_colores, colores, vertices, 0, len(vertices))

def colorear_rec(grafo, n, colores, vertices, i, sol_min):
    if sol_min <= n:
        return sol_min
    if i == len(vertices):
        return n

    v = vertices[i]
    for color in range(n+1):
        colores[v] = color
        if not compatible(grafo, v, colores):
            continue
        if color != n:
            sol = colorear_rec(grafo, n, colores, vertices, i+1, sol_min)
        else:
            sol = colorear_rec(grafo, n+1, colores, vertices, i+1, sol_min)
        
        if sol < sol_min:
            sol_min = sol

    del colores[v]
    return sol_min

def compatible(grafo, v, colores):
    for w in grafo.adyacentes(v):
        if w in colores and colores[v] == colores[w]:
            return False
    return True