def mochila(elementos, W):
    n = len(elementos)
    OPT = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        valor, peso = elementos[i - 1]
        for w in range(W + 1):
            OPT[i][w] = OPT[i - 1][w]
            if peso <= w:
                OPT[i][w] = max(OPT[i][w], valor + OPT[i - 1][w - peso])

    elementos_seleccionados = []
    w = W
    for i in range(n, 0, -1):
        if OPT[i][w] != OPT[i - 1][w]:
            elementos_seleccionados.append(elementos[i - 1])
            w -= elementos[i - 1][1]

    # Ordenar la lista de elementos seleccionados
    elementos_seleccionados.sort(key=lambda x: elementos.index(x))

    return elementos_seleccionados