
def max_grupos_bodegon(P, W):
    
    return bodegon(P, W, 0, [], [])

    
def bodegon(P, W, i_actual, solucion_parcial, solucion_optima):
    
    if sum(solucion_parcial) > W: 
        return solucion_optima

    if i_actual >= len(P):
        if sum(solucion_parcial) > sum(solucion_optima):
            return solucion_parcial.copy()

        return solucion_optima
    
    solucion_parcial.append(P[i_actual])
    solucion_optima = bodegon(P, W, i_actual + 1, solucion_parcial, solucion_optima)
    solucion_parcial.remove(P[i_actual])
    return bodegon(P, W, i_actual +1, solucion_parcial, solucion_optima)
