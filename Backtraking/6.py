def resolver_sudoku(tablero):
    if _sudoku(tablero):
        return tablero
    return None

def _sudoku(tablero):
    i, j = find_empty(tablero)
    if i is None:
        return True  # No hay más celdas vacías, el Sudoku está resuelto

    for num in range(1, 10):
        if valid(tablero, num, (i, j)):
            tablero[i][j] = num

            if _sudoku(tablero):
                return True

            # Backtracking
            tablero[i][j] = 0

    return False

def valid(bo, num, pos):
    # Verifica la fila
    for i in range(9):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Verifica la columna
    for i in range(9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Verifica la caja 3x3
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return i, j  # Fila, columna de la primera celda vacía
    return None, None