def encontrar_submarinos(matriz):
    submarinos_pos = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]:
                submarinos_pos.append((i, j))
    return submarinos_pos

def calcular_celdas_iluminadas(faro, filas, columnas):
    direcciones = [(dx, dy) for dx in range(-2, 3) for dy in range(-2, 3)]
    iluminadas = set()
    x, y = faro
    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if 0 <= nx < filas and 0 <= ny < columnas:
            iluminadas.add((nx, ny))
    return iluminadas

def estan_todos_iluminados(submarinos_pos, iluminadas):
    return all(submarino in iluminadas for submarino in submarinos_pos)

def mejores_posiciones(submarinos_pos, filas, columnas):
    posiciones = []
    cobertura = {}
    for i in range(filas):
        for j in range(columnas):
            celdas_iluminadas = calcular_celdas_iluminadas((i, j), filas, columnas)
            cobertura[(i, j)] = sum(1 for sub in submarinos_pos if sub in celdas_iluminadas)
    
    posiciones = sorted(cobertura.keys(), key=lambda pos: cobertura[pos], reverse=True)
    return posiciones

def backtrack(submarinos_pos, faros, indice, filas, columnas, mejor_solucion, iluminadas, posiciones_candidatas):
    if estan_todos_iluminados(submarinos_pos, iluminadas):
        if len(faros) < len(mejor_solucion[0]):
            mejor_solucion[0] = list(faros)
        return

    if indice >= len(posiciones_candidatas):
        return

    x, y = posiciones_candidatas[indice]
    nuevas_iluminadas = iluminadas | calcular_celdas_iluminadas((x, y), filas, columnas)
    
    faros.append((x, y))
    if len(faros) < len(mejor_solucion[0]):
        backtrack(submarinos_pos, faros, indice + 1, filas, columnas, mejor_solucion, nuevas_iluminadas, posiciones_candidatas)
    faros.pop()
    
    backtrack(submarinos_pos, faros, indice + 1, filas, columnas, mejor_solucion, iluminadas, posiciones_candidatas)

def submarinos(matriz):
    if not matriz or not matriz[0]:
        return [] 
    
    filas = len(matriz)
    columnas = len(matriz[0])
    submarinos_pos = encontrar_submarinos(matriz)
    
    if not submarinos_pos:
        return [] 
    
    posiciones_candidatas = mejores_posiciones(submarinos_pos, filas, columnas)
    
    mejor_solucion = [submarinos_pos] 
    backtrack(submarinos_pos, [], 0, filas, columnas, mejor_solucion, set(), posiciones_candidatas)
    
    return mejor_solucion[0]