def es_compatible(grafo, v, colores):
    for w in grafo.adyacentes(v):
        if w in colores and colores[v] == colores[w]:
            return False
    return True

def colorear_rec(grafo, v, colores, color, n):
    colores[v] = color

    if len(colores) == len(grafo):
        if es_compatible(grafo, v, colores):
            return True
        else:
            del colores[v]
            return False

    if not es_compatible(grafo, v, colores):
        del colores[v]
        return False

    for w in grafo.adyacentes(v):
        if w in colores:
            continue
        for color in range(n):
            if colorear_rec(grafo, w, colores, color, n):
                return True

    del colores[v]
    return False

def colorear(grafo, n):
    if len(grafo) == 0:
        return True

    colores = {}
    return colorear_rec(grafo, grafo.vertice_aleatorio(), colores, 0, n)