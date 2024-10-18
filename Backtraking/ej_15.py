# Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los 
# grupos que quieren sentarse a comer, y la cantidad de integrantes que conforma a cada uno. 
# Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas 
# que integran el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, 
# las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse. 
# Implementar un algoritmo que, por backtracking, obtenga el conjunto de grupos que ocupan la mayor 
# cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos).

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
