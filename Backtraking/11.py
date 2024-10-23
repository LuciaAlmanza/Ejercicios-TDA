def sumatorias_n(lista, n):
    result = []
    subset_sum(lista, 0, n, [])
    return result


def subset_sum(L, index, n, solucion_parcial):
	# Si encuentro una solucion la devuelvo
	if sum(solucion_parcial) == n:
		return solucion_parcial
	
	# Si por esta rama me paso, dejo de probar
	if sum(solucion_parcial) > n or index >= len(L):
		return []

	solucion_parcial.append(L[index])
	solucion = subset_sum(L, index+1, n, solucion_parcial)
	if solucion != []: # en este caso hay solución válida
		return solucion
	solucion_parcial.pop()

	return subset_sum(L, index+1, n, solucion_parcial)
