def lazy_john(dias):
    #aca guardo mis variables binarias
    j=[]
    #indicamos que queremos maximizar
    problema=pulp.LpProblem("max_ganancia",pulp.LpMaximize)
    for i in range(len(dias)):
        #seteo variables binarias
        j.append(pulp.LpVariable("x"+i,cat="Binary"))

    #planteo la inecuacion
    problema+=Sumatoria(dias[i]*j[i]for i in range(len(dias)))

    #planteo restriccion
    for c in range(len(dias)-1):
        problema+=j[c]+j[c+1]<=1

    problema.solve()

    return list(map(lambda ji : pulp.value(ji),j))