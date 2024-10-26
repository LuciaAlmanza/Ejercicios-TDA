def subset_sum(elementos,v):
    tam=len(elementos)
    optimos=[[0 for _ in range (v+1)]for _ in range(tam+1)]

    for fila in range(1,tam+1):
        for columna in range(v+1):
            if elementos[fila-1]<=columna:
                optimos[fila][columna]=max(optimos[fila-1][columna],optimos[fila-1][columna-elementos[fila-1]]+elementos[fila-1])
            else:
                optimos[fila][columna]=optimos[fila-1][columna]

    return getRes(elementos,v,optimos,tam)

def getRes(elementos,v,optimos,tam):
    res=[]
    for i in range(tam,0,-1):
        if optimos[i][v]!=optimos[i-1][v]:
            res.append(elementos[i-1])
            v-=elementos[i-1]

            if v<0:
                break
    res.reverse()

    return res