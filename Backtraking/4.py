def independent_set(grafo):
    vertices=grafo.obtener_vertices()
    if not vertices:
        return []
    conjunto=[]
    max_conjunto=[]
    
    return backtracking(0,grafo,[],max_conjunto,vertices)


def es_valido(grafo,conjunto,v):
    #verifico que el vertice que queremos appendear
    #no este unido a ninguno de nuestro conjunto previo
    for u in conjunto:
        if grafo.estan_unidos(u,v):
            return False
    return True

def backtracking(indice,grafo,conjunto,max_conjunto,vertices):
    #si ya recorri todas las iteraciones posibles al grafo
    if indice==len(vertices):
        #comparo si el conjunto acutal es mas grande al que ya tengo armado
        if len(conjunto)>len(max_conjunto):
            max_conjunto.clear()
            max_conjunto.extend(conjunto)
        return max_conjunto
    
    #vertice actual
    v= vertices[indice]
    #si se puede agregar el vertice al conjunto,
    #lo meto y llamo a la funcion recursiva ahora con el indice actualizado
    #en caso de que la funcion falle,
    #se eliminan vertices hasta encontrar el camino correcto
    if es_valido(grafo,conjunto,v):
        conjunto.append(v)
        backtracking(indice+1,grafo,conjunto,max_conjunto,vertices)
        conjunto.pop()
    #en caso de que popeo el vertice, significa que para ninguna combinacion
    #es util, entonces llamo a la funcion y lo omito complemtamente
    backtracking(indice+1,grafo,conjunto,max_conjunto,vertices)
    return max_conjunto