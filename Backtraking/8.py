def hay_isomorfismo(g1, g2):
    v1=g1.obtener_vertices()
    v2=g2.obtener_vertices()
    #si son grafos dispares ya la corto
    if len(v1)!=len(v2):
        return False
    
    return backtracking_iso(g1,g2,v1,v2,{},set())

def iso_valido(g1,g2,imagen):
    #veo al vertice1 y sus adyacentes, comparo que la imagen de v1
    #en el g2 debe tener la misma relacion con sus respectivos adyacentes
    for v1 in g1.obtener_vertices():
        for w1 in g1.adyacentes(v1):
            #si v1 adyacente de w1, sus imagenes tmb lo son
            v2=imagen[v1]
            w2=imagen[w1]
            if not g2.estan_unidos(v2,w2):
                return False
    return True

def backtracking_iso(g1,g2,vertices1,vertices2,imagen,visitados):

    #si complete todas las imagenes del grafo, veo que se cumpla
    if len(imagen)==len(vertices1):
        return iso_valido(g1,g2,imagen)

    #itero sobre un grafo
    for v1 in vertices1:
        if v1 not in imagen:
            for v2 in vertices2:
                #si v2 no fue visitado y cumple mismas adyacencias
                #es candidato a ser imagen de v1
                if v2 not in visitados and len(g1.adyacentes(v1))==len(g2.adyacentes(v2)):
                    #lo agrego como imagen
                    visitados.add(v2)
                    imagen[v1]=v2
                    #si v1 y v2 son imagenes correctas , sigo de largo
                    if backtracking_iso(g1,g2,vertices1,vertices2,imagen,visitados):
                        return True
                    #si no son imagenes
                    #los libero
                    del imagen[v1]
                    visitados.remove(v2)
            break

    return False