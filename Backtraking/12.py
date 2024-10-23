def max_sumatoria_n(lista, n):
    return backtracking_sumatoria(lista,n,[],[],0,0)

def backtracking_sumatoria(lista,n,mejor_sol,sol_actual,suma,indice):
    #recorri toda la lista
    if indice==len(lista):
        #si justo llego a igualar n luego de la iteracion, mi mejor_sol va a ser la         actual
        if suma==n:
            mejor_sol.clear()
            mejor_sol.extend(sol_actual)
            return mejor_sol
        #si mi mejor sol no supera a n, devuelvo la sol actual
        if suma > sum(mejor_sol) and suma<n:
            mejor_sol.clear()
            mejor_sol.extend(sol_actual)
        #para el caso donde mi sol actual no es la mejor sol
        return mejor_sol

    numero=lista[indice]
    if suma+numero <=n:
        sol_actual.append(numero)
        backtracking_sumatoria(lista,n,mejor_sol,sol_actual,suma+numero,indice+1)
        sol_actual.pop()
    
    mejor_sol =backtracking_sumatoria(lista,n,mejor_sol,sol_actual,suma,indice+1)
    return mejor_sol