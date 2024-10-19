
def elemento_desordenado(arr):
    inicio = 0
    final = len(arr) - 1
    return dividir_y_encontrar_desubicado(arr, inicio, final)


def obtener_desubicado_2_elementos(izq, der):
    if izq > der:
        return izq
    return None

def dividir_y_encontrar_desubicado(arr, inicio, final):

    if inicio == final:
        return None

    
    if final == inicio + 1:
        return obtener_desubicado_2_elementos(arr[inicio], arr[final])

    medio = (inicio + final) // 2

    if arr[medio] < arr[medio - 1]:
        return arr[medio-1]

    if arr[medio] > arr[medio + 1]:
        return arr[medio]
  
    desubicado_izq = dividir_y_encontrar_desubicado(arr, inicio, medio)
    desubicado_der = dividir_y_encontrar_desubicado(arr, medio + 1, final)

    if desubicado_izq != None:
        return desubicado_izq
    if desubicado_der != None:
        return desubicado_der
    return None


#Complejidad: O(n)
