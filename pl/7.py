def max_IndSet(grafo):
    #es bastante mas cómodo asignar las variables binarias con un diccionario que con una lista
    j={}
    res=[]
    vertices=grafo.obtener_vertices()

    problema = pulp.LpProblem("ind_set",pulp.LpMaximize)

    for v in vertices:
        j[v]=(pulp.LpVariable(f"j{v}",cat="Binary"))

    problema+=pulp.lpSum(j[v] for v in vertices)

    #restricción
    for v in vertices:
        for w in grafo.adyacentes(v):
            problema+=j[v]+j[w]<=1

    problema.solve()

    for v in vertices:
        if pulp.value(j[v])==1:
            res.append(v)
    
    return res