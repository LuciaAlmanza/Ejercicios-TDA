
CERO = 0
NO_HAY_CERO = -1

def indice_primer_cero(arr):
    inicio = 0
    final = len(arr) - 1
    return dividr_y_obtener_indice_primer_cero(arr, inicio, final)

def obtener_indice_primer_cero_del_par(arr, izq, der):
    if arr[izq] == CERO:
        return izq
    if arr[der] == CERO:
        return der
    return NO_HAY_CERO
    

def dividr_y_obtener_indice_primer_cero(arr, inicio, final):

    if inicio == final:
        if arr[inicio] == CERO:
            return inicio
        return NO_HAY_CERO

    if final == inicio + 1:
        return obtener_indice_primer_cero_del_par(arr, inicio, final)

    medio = (inicio + final) // 2

    if arr[medio] == CERO:
        return dividr_y_obtener_indice_primer_cero(arr, inicio, medio)
    else:
        return dividr_y_obtener_indice_primer_cero(arr, medio+1, final)