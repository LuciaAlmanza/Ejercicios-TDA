def calcular_p(charlas):
    n = len(charlas)
    p = [-1] * n

    for i in range(n):
        for j in range(i - 1, -1, -1):
            if charlas[j][1] <= charlas[i][0]:
                p[i] = j
                break
    return p

#Ecuacion de recurrencia -> OPT[j] = max(OPT[j - 1], OPT[P[j]] + Gj)
def scheduling_dinamico(n, charlas, p):
    optimo_scheduling = [0] * (n + 1)

    for j in range(1, n + 1):
        charla_index = j - 1
        valor_incluir = charlas[charla_index][2] + (optimo_scheduling[p[charla_index] + 1] if p[charla_index] != -1 else 0)
        valor_excluir = optimo_scheduling[j - 1]
        optimo_scheduling[j] = max(valor_incluir, valor_excluir)

    return optimo_scheduling

def recuperar_solucion(optimo_scheduling, charlas, p):
    n = len(charlas)
    j = n
    solucion = []

    while j > 0:
        charla_index = j - 1
        if charlas[charla_index][2] + (optimo_scheduling[p[charla_index] + 1] if p[charla_index] != -1 else 0) >= optimo_scheduling[j - 1]:
            solucion.append(charla_index)
            j = p[charla_index] + 1
        else:
            j -= 1

    solucion.reverse()
    return solucion

def scheduling(charlas):
    charlas.sort(key=lambda x: x[1])
    p = calcular_p(charlas)
    n = len(charlas)
    optimos = scheduling_dinamico(n, charlas, p)
    seleccionadas = recuperar_solucion(optimos, charlas, p)
    return [charlas[i] for i in seleccionadas]