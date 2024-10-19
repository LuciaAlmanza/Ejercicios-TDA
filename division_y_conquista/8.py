def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Índice para la sublista izquierda
    j = mid + 1 # Índice para la sublista derecha
    k = left    # Índice para el array temporal
    inv_count = 0

    # Proceso de merge y conteo de inversiones
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)  # Contamos las inversiones
            j += 1
        k += 1

    # Copiamos los elementos restantes de la sublista izquierda
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copiamos los elementos restantes de la sublista derecha
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copiamos los elementos ordenados al arreglo original
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right)//2

        # Recursivamente contamos las inversiones en las dos mitades
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)

        # Contamos las inversiones durante el proceso de merge
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

def contar_inversiones(A, B):
    # Creamos un diccionario que mapea los elementos de A a sus posiciones
    mapa_A = {valor: i for i, valor in enumerate(A)}

    # Convertimos B en un arreglo de índices relativos a A
    indices_B = [mapa_A[valor] for valor in B]

    # Usamos Merge Sort para contar las inversiones
    n = len(B)
    temp_arr = [0]*n
    return merge_sort_and_count(indices_B, temp_arr, 0, n-1)

# O(nlogn)