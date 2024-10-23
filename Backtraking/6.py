#aviso que no lo pude porbar qx rpl no me agarra el grafo :( pero deberiiiaa funcionar

def construir_grafo_sudoku(tablero):
    grafo = Grafo(dirigido=False)
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:  # Solo para celdas vacías
                for k in range(9):
                    if k != j:  # Fila
                        grafo.agregar_arista((i, j), (i, k))
                    if k != i:  # Columna
                        grafo.agregar_arista((i, j), (k, j))
                # Caja 3x3
                box_row_start = (i // 3) * 3
                box_col_start = (j // 3) * 3
                for box_i in range(box_row_start, box_row_start + 3):
                    for box_j in range(box_col_start, box_col_start + 3):
                        if (box_i, box_j) != (i, j):
                            grafo.agregar_arista((i, j), (box_i, box_j))
    return grafo

def es_valido(grafo, colores, vertice, color):
    for vecino in grafo.adyacentes(vertice):
        if colores.get(vecino) == color:
            return False
    return True

def backtracking(grafo, colores, indice=0):
    if indice == len(grafo.obtener_vertices()):
        return True  # Se han coloreado todos los vértices

    vertice = grafo.obtener_vertices()[indice]
    for color in range(1, 10):  # Colores del 1 al 9
        if es_valido(grafo, colores, vertice, color):
            colores[vertice] = color
            if backtracking(grafo, colores, indice + 1):
                return True
            del colores[vertice]  # Retroceder

    return False

def resolver_sudoku_con_grafo(tablero):
    grafo = construir_grafo_sudoku(tablero)
    colores = {}
    if backtracking(grafo, colores):
        for (i, j), color in colores.items():
            tablero[i][j] = color
        return tablero
    return None