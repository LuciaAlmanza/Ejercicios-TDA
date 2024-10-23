def es_seguro(tablero, fila, col, N):
    # Verifica si hay una reina en la misma columna
    for i in range(fila):
        if tablero[i][col] == 1:
            return False
    
    # Verifica la diagonal izquierda arriba
    i, j = fila - 1, col - 1
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Verifica la diagonal derecha arriba
    i, j = fila - 1, col + 1
    while i >= 0 and j < N:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True

def resolver_n_reinas_util(tablero, fila, n, reinas):
    if fila >= n:
        return True
    
    for col in range(n):
        if es_seguro(tablero, fila, col, n):
            tablero[fila][col] = 1
            reinas.append((fila, col))

            if resolver_n_reinas_util(tablero, fila+1, n, reinas):
                return True
            
            # Si colocar la reina en tablero[fila][col] no conduce a una solución, retroceder
            tablero[fila][col] = 0
            reinas.pop()
    
    return False

def nreinas(n):
    tablero = [[0 for _ in range(n)] for _ in range(n)]
    reinas = []
    resolver_n_reinas_util(tablero, 0, n, reinas)
    return reinas