mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

def es_valido(x, y, tablero, n):
    # Verifica si la posición está dentro del tablero y no ha sido visitada
    return 0 <= x < n and 0 <= y < n and tablero[x][y] == -1

def recorrer_caballo_util(tablero, curr_x, curr_y, mov_i, n):
    # Si el caballo ha visitado todas las casillas, devuelve True
    if mov_i == n * n:
        return True

    # Intenta todos los movimientos posibles desde la posición actual del caballo
    for i in range(8):
        new_x = curr_x + mov_x[i]
        new_y = curr_y + mov_y[i]

        if es_valido(new_x, new_y, tablero, n):
            # Marca el nuevo movimiento con el número de pasos actuales
            tablero[new_x][new_y] = mov_i
            # Recursivamente trata de construir el resto del recorrido
            if recorrer_caballo_util(tablero, new_x, new_y, mov_i + 1, n):
                return True
            # Si el movimiento no es válido, deshacer el paso (backtrack)
            tablero[new_x][new_y] = -1

    return False

def knight_tour(n):
    # Inicializa el tablero con -1 (indica que la casilla no ha sido visitada)
    tablero = [[-1 for _ in range(n)] for _ in range(n)]

    # El caballo empieza en la esquina superior izquierda (0, 0)
    tablero[0][0] = 0  # El primer paso del caballo

    # Llama a la función recursiva para resolver el problema
    if recorrer_caballo_util(tablero, 0, 0, 1, n):
        return tablero
    else:
        return None