def mst_min(grafo):
    j=[]
    aristas=grafo.obtener_aristas()
    vertices=grafo.obtener_vertices()

    problema = pulp.LpProblem("mst_minimize",pulp.LpMinimize)

    #cada arista del grafo es una variable binaria
    for (v,w) in aristas:
        j[(v,w)]=pulp.LpVariable(f"j{(v,w)}",cat="Binary")

    #no me acuerdo si existia el metodo obtener peso :P pero de ultima 
    #la implementation seria la misma solo que hacemos v=>adyacenteW
    #obtener_peso(v,w)
    for (v,w) in aristas:
        problema +=pulp.Sumatoria(grafo.obtener_peso()*j[a])

    #ahora tenemos que asegurar que eun vertice se conecte con una arista
    for v in vertices:
        adyacentes=grafo.adyacentes(v)
        
        problema+=pulp.LpSum()

    #incompleto
    problema.solve()