def max_subarray(arr):
    _, start, end = _max_subarray(arr, 0, len(arr) - 1)
    return arr[start:end + 1]

def _max_subarray(arr, start, end):
    if start == end:
        return arr[start], start, end
    
    mid = (start+end) // 2

    # Tipico mergesort
    izq_sum, izq_start, izq_end = _max_subarray(arr, start, mid)
    der_sum, der_start, der_end = _max_subarray(arr, mid + 1, end)

    # Obtengo la mejor combinacion de la cruza de particiones
    cross_sum, cross_start, cross_end =  hallar_max_subarray(arr, start, mid, end)
    
    # Comparo los resultados obtenidos y devuelvo el mejor
    if izq_sum >= der_sum and izq_sum >= cross_sum:
        return izq_sum, izq_start, izq_end
    elif der_sum >= izq_sum and der_sum >= cross_sum:
        return der_sum, der_start, der_end
    else:
        return cross_sum, cross_start, cross_end


def hallar_max_subarray(arr, start, mid, end):
    izq_sum = float('-inf')
    izq_max = mid

    der_sum = float('-inf')
    der_max = mid + 1

    izq_total = 0
    der_total = 0

    for i in range(mid, start - 1, -1):
        izq_total += arr[i]
        if izq_total > izq_sum:
            izq_sum = izq_total
            izq_max = i

    for i in range(mid + 1, end + 1):
        der_total += arr[i]
        if der_total > der_sum:
            der_sum = der_total
            der_max = i

    return izq_sum + der_sum, izq_max, der_max