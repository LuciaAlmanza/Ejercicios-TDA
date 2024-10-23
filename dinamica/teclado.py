vecinos = {
    0: [0, 8],
    1: [1, 2, 4],
    2: [2, 1, 3, 5],
    3: [3, 2, 6],
    4: [4, 1, 5, 7],
    5: [5, 2, 4, 6, 8],
    6: [6, 3, 5, 9],
    7: [7, 4, 8],
    8: [8, 0, 5, 7, 9],
    9: [9, 6, 8]
}

def numeros_posibles(k, N):
    # Si N es 1, simplemente hay una única opción, que es presionar el mismo número
    if N == 1:
        return 1

    # Tabla de DP donde dp[d][i] indica cuántos números de longitud i se pueden formar comenzando en d
    dp = [[0] * (N + 1) for _ in range(10)]

    # Inicializar para N = 1 (primer paso)
    for d in range(10):
        dp[d][1] = 1  # Solo un número posible si la longitud es 1, el propio número

    # Llenar la tabla de DP para longitudes de 2 hasta N
    for i in range(2, N + 1):
        for d in range(10):
            # Para cada dígito d, sumar todas las formas de llegar a él desde sus vecinos
            dp[d][i] = sum(dp[vecino][i - 1] for vecino in vecinos[d])

    # El resultado es el número de combinaciones que podemos formar de longitud N comenzando en k
    return dp[k][N]