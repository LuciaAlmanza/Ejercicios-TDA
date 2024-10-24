def lunatico_no_circular(ganancias):
    tam_arreglo=len(ganancias)
    if tam_arreglo==0:
        return []
    if tam_arreglo==1:
        return [0]
    optimos=[0]*(tam_arreglo+1)
    optimos[1]=ganancias[0]
    if tam_arreglo>1:
        optimos[2]=max(ganancias[0],ganancias[1])
    for i in range(3,tam_arreglo+1):
        optimos[i]=max(optimos[i-1],optimos[i-2]+ganancias[i-1])
    
    return getRes(optimos,tam_arreglo,ganancias)


def getRes(optimos,tam_arreglo,ganancias):
    res=[]
    while tam_arreglo>0:
        #si los optimos del actual y el anterior son iguales, significa que no entre a robar
        #la casa actual
        if optimos[tam_arreglo]==optimos[tam_arreglo-1]:
            tam_arreglo-=1
        else:
            res.append(tam_arreglo-1)
            #ni voy a tener en cuenta la casa adyacente
            tam_arreglo-=2

    res.reverse()
    return res

def lunatico(ganancias):
    if sum(ganancias)==0:
        return []
    if len(ganancias)==1:
        return [0]
    ganancias_excluyo_primera=ganancias[1:]
    ganancias_excluyo_ultima=ganancias[:-1]

    optimo_excluyo_primera=lunatico_no_circular(ganancias_excluyo_primera)
    optimo_excluyo_ultima=lunatico_no_circular(ganancias_excluyo_ultima)

    #ajusto el indice sumandole 1 porque omito la casa 0
    optimo_excluyo_primera=[i+1 for i in optimo_excluyo_primera]

    #calculo la ganancia total tanto de robar la primera como de robar la ultima
    ganancias_excluyo_primera=sum(ganancias[i] for i in optimo_excluyo_primera)
    ganancias_excluyo_ultima=sum(ganancias[i] for i in optimo_excluyo_ultima)

    if ganancias_excluyo_ultima>ganancias_excluyo_primera:
        return optimo_excluyo_ultima
    return optimo_excluyo_primera