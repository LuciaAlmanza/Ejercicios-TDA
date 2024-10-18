def posicion_pico(arr, inicio, final):
    if inicio == final:
        return inicio

    medio = (inicio + final) // 2

    if arr[medio-1] < arr[medio] and arr[medio] > arr[medio+1]:
        return medio
    if arr[medio - 1] < arr[medio] and arr[medio] < arr[medio + 1]:
        return posicion_pico(arr, medio+1, final)
    if arr[medio - 1] > arr[medio] and arr[medio] > arr[medio + 1]:
        return posicion_pico(arr, inicio, medio)