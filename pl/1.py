def mochila(v: list[int],w: list[int],W: int):
    #es res
    y=[]
    #y se appendea variables con el indice de los elementos
    #son de categoria binaria, osea que indican dos estados(True,False)
    #para ver si lo agregamos a la mochi o no
    for i in range(len(v)):
        y.append(pulp.LpVariable("y"+str(i),cat="Binary"))

    #voy a buscar maximizar
    problem=pulp.LpProblem("products",pulp.LpMaximize)
    #la sumatoria de la variable por la constante peso siendo menores al W
    problem+=Sumatoria([y[i],w[i]]for i in range(len(v))) <=W
    #sumatoria de los valores
    problem+=Sumatoria([y[i],v[i]]for i in range(len(v)))

    problem.solve()

    return list(map(lambda yi : pulp.value(yi),y))