def dom_set_min(grafo):
    res=[]
    j=[]
    vertices = grafo.obtener_vertices()

    problema=pulp.LpProblem("min_set",pulp.LpMinimize)

    for v in vertices:
        j[v]=pulp.LpVariable(f"j{v}",cat="Binary")

    for v in  vertices:
        problema+=j[v] 

    for v in vertices:
        ws=grafo.adyacentes(v)
        problema+=j[v] + pulp.Sumatoria(j[w] for w in ws)

    problema.solve()

    res.extend[(v for v in  vertices if pulp.Value(j[v])==1)]

    return res