# Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah decidió 
# que en una misma parada de colectivo nunca pararán dos colectivos que usen el mismo color. El problema 
# es que ya saben que eso está sucediendo hoy en día, así que van a repintar todas las líneas de colectivos. 
# Por problemas presupuestarios, desean pintar los colectivos con la menor cantidad posible k colores diferentes. 
# Como no quieren parecer un grupo de improvisados que malgasta los fondos públicos, quieren hacer un análisis 
# para saber cuál es ese mínimovalor para cumplir con lo pedido (pintar cada línea con alguno de los k colores,
# de tal forma que no hayan dos de mismo color coincidiendo en la misma parada). Considerando que se tiene 
# la información de todas las paradas de colectivo y qué líneas paran allí, modelar el problema utilizando 
# grafos e implementar un algoritmo que determine el mínimo valor k para resolver el problema. 
# Indicar la complejidad del algoritmo implementado.

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