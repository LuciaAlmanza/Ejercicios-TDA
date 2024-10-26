def carlitos(c_publicitaria, P):
    #separo el arreglo en dos para mas placer
    costos=[c_publicitaria[i][1] for i in range(0,len(c_publicitaria))]
    ganancias=[c_publicitaria[i][0] for i in range(0,len(c_publicitaria))]
    tam_arreglo=len(c_publicitaria)
    #repito lo de la mochi, una matriz donde el tamaño de sus col lo determina el P
    #y las filas por la cantidad de elementos
    optimos=[[0 for _ in range(P+1)] for _ in range(tam_arreglo+1)]

    for fila in range(1,tam_arreglo+1):
        for columna in range(1,P+1):
            #esto vendría a significar, si el costo del item iterado es menor al presupuesto actual
            #entonces puedo ver de calcular un optimo para las dimensiones dadas
            #Aplico, entonces, la ec de recurrencia de la mochi
            if costos[fila-1]<=columna:
                optimos[fila][columna]=max(optimos[fila-1][columna],optimos[fila-1][columna-costos[fila-1]]+ganancias[fila-1])
            else:
                #si entro aca, significa que el costo de la campaña actual es muy grande para el P dado
                #entonces el optimo sería no realizar la campaña y que su optimo sea la sol anterior
                optimos[fila][columna]=optimos[fila-1][columna]

    return getRes(optimos,tam_arreglo,P,c_publicitaria,costos)


def getRes(optimos,tam_arreglo,P,c_publicitaria,costos):
    res=[]
    for i in range(tam_arreglo,0,-1):
        #si los optimos de la actual y el anterior difieren, significa que el optimo de la campaña actual la considera 
        if optimos[i][P]!=optimos[i-1][P]:
            res.append(c_publicitaria[i-1])
            #voy actualizando el presupuesto en base a la campaña que itero
            P-=costos[i-1]

    res.reverse()
    return res