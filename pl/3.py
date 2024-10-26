def vertex_cover_min(grafo):
    res=[]
    j={}
    vertices=grafo.obtener_vertices()

    problema=pulp.LpProblem("min_cover",pulp.LpMinimize)
    for v in vertices:
        j[v]=pulp.LpVariable("j",cat="Binary")
    
    problema+=pulp.lpSum(j[v] for v in vertices)

    for v in vertices:
        for w in grafo.adyacentes(v):
            problema+=j[v]+j[w]<=1

    problema.solve()

    for v in vertices:
        if pulp.value(j[v])==1:
            res.append(v)


    return res