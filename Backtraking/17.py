def iluminar_con_faro(matriz, x, y):
    n = len(matriz)
    m = len(matriz[0])
    cobertura = []
    # Marcar las celdas en un radio de 2 alrededor de (x, y)
    for i in range(max(0, x-2), min(n, x+3)):
        for j in range(max(0, y-2), min(m, y+3)):
            if matriz[i][j]:
                matriz[i][j] = False  # Marcar la celda como iluminada
                cobertura.append((i, j))  # Guardar la celda cubierta para restaurarla después
    return cobertura

def restaurar_iluminacion(matriz, cobertura):
    for (i, j) in cobertura:
        matriz[i][j] = True

def backtrack(matriz, faros, min_faroles):
    # Si todos los submarinos han sido iluminados, devuelve la cantidad actual de faros
    if not any(any(row) for row in matriz):
        return min(len(faros), min_faroles)

    n = len(matriz)
    m = len(matriz[0])

    # Probar colocar un faro en cada posición y continuar con backtracking
    for i in range(n):
        for j in range(m):
            if matriz[i][j]:  # Colocar un faro solo donde haya un submarino
                # Iluminar la matriz desde la posición (i, j)
                cobertura = iluminar_con_faro(matriz, i, j)
                faros.append((i, j))

                # Llamada recursiva para buscar la solución mínima
                min_faroles = backtrack(matriz, faros, min_faroles)

                # Restaurar el estado de la matriz y remover el faro (backtracking)
                restaurar_iluminacion(matriz, cobertura)
                faros.pop()

    return min_faroles

def minimo_de_faroles(matriz):
    return backtrack(matriz, [], float('inf'))