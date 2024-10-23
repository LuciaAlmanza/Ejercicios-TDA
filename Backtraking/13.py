def vertex_cover_min(grafo):
    #inicialmente la mejor solucion son todos los vertices
    return backtracking_vertex(grafo,grafo.obtener_vertices(),[],0)

#osea, todas las aristas del grafo tienen por lo menos una conexion al vertex
def backtracking_vertex(grafo,mejor_res,res_actual,indice):
    vertices=grafo.obtener_vertices()

    #si consigo una sol actual menor a la mejor, la reemplazo
    if vertex_valido(grafo,res_actual,vertices):
        if len(res_actual)<len(mejor_res):
            mejor_res.clear()
            mejor_res.extend(res_actual)
        return mejor_res

    #termine de iterar el grafo
    if indice>=len(vertices):
        return mejor_res
    
    
    actual = vertices[indice]
    res_actual.append(actual)
    backtracking_vertex(grafo,mejor_res,res_actual,indice+1)
    res_actual.pop()
    d=set()
    d.re
    
    mejor_res=backtracking_vertex(grafo,mejor_res,res_actual,indice+1)
    return mejor_res


def vertex_valido(grafo,res_actual,vertices):
    #debe haber una conexion entre todos los vertices del grafo con el vertex
    for v in vertices:
        for w in grafo.adyacentes(v):
            if v not in res_actual and w not in res_actual:
                return False
    return True