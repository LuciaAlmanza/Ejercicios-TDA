# Lo adapte para que devuelva la reconstruccion de la ganancia, pero no creo q tomen algo asi
# es super largo y complicado

def laberinto(matriz):
    if not matriz or not matriz[0]:  # Verifica si la matriz está vacía o tiene filas vacías.
        return 0
    
    N = len(matriz)        # Número de filas
    M = len(matriz[0])     # Número de columnas

    # Tabla de DP para almacenar ganancias máximas
    dp = [[0] * M for _ in range(N)]
    # Tabla para rastrear las decisiones
    decision = [[None] * M for _ in range(N)]

    # Casos base:
    if matriz[0][0] == -1: # Si la posición inicial es un obstáculo
        return 0
    dp[0][0] = matriz[0][0]

    # Llenar la primera fila (solo se puede mover desde la izquierda)
    for j in range(1, M):
        if matriz[0][j] == -1:
            dp[0][j] = float('-inf')  # Obstacle, no se puede pasar
        else:
            dp[0][j] = dp[0][j-1] + matriz[0][j] if dp[0][j-1] != float('-inf') else float('-inf')
            decision[0][j] = (0, j-1)  # Desde la izquierda

    # Llenar la primera columna (solo se puede mover desde arriba)
    for i in range(1, N):
        if matriz[i][0] == -1:
            dp[i][0] = float('-inf')  # Obstacle, no se puede pasar
        else:
            dp[i][0] = dp[i-1][0] + matriz[i][0] if dp[i-1][0] != float('-inf') else float('-inf')
            decision[i][0] = (i-1, 0)  # Desde arriba

    # Llenar el resto de la tabla dp
    for i in range(1, N):
        for j in range(1, M):
            if matriz[i][j] == -1:
                dp[i][j] = float('-inf')  # Obstacle, no se puede pasar
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    dp[i][j] = matriz[i][j] + dp[i-1][j]
                    decision[i][j] = (i-1, j)  # Decisión desde arriba
                else:
                    dp[i][j] = matriz[i][j] + dp[i][j-1]
                    decision[i][j] = (i, j-1)  # Decisión desde la izquierda

    return dp[N-1][M-1] if dp[N-1][M-1] != float('-inf') else 0, decision

def reconstruir_camino(matriz, decision):
    camino = []
    i, j = len(matriz) - 1, len(matriz[0]) - 1
    
    while i is not None and j is not None:
        camino.append((i, j))
        i, j = decision[i][j]  # Sigue la decisión hacia atrás

    camino.reverse()  # Invertir para mostrar desde el inicio
    return camino

def resolver_laberinto(matriz):
    ganancia_maxima, decision = laberinto(matriz)
    if ganancia_maxima == 0:
        return 0, []  # No hay camino válido

    camino = reconstruir_camino(matriz, decision)
    return ganancia_maxima, camino