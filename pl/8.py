def min_color(grafo):
    vertices=grafo.obtener_vertices()
    #en el peor de los casos, cada vertice tiene que tener su propio color
    colores_max=len(vertices)
    j={}
    res={}
    problema= pulp.LpProblem("coloreo",pulp.LpMinimize)

    for v in vertices:
        #variables enteras cuyo valor abarca del 1 al colores_max
        j[v]=pulp.LpVariable(f"j{v}",lowBound=1,upBound=colores_max,cat="Integer")

    for v in vertices:
        for w in grafo.adyacentes(v):
            #restriccion del color
            problema+= abs(j[v]-j[w])>=1

    problema.solve()

    for v in vertices:
        res[v]=pulp.value(j[v])

    return res