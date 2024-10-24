def problema_soga(n):
    # Asegurarse de que n es al menos 2
    if n < 2:
        return 0  # No es posible cortar si n < 2

    # Inicializamos el array dp donde dp[i] representa el producto máximo para una soga de longitud i
    dp = [0] * (n + 1)

    # Llenamos los casos base
    dp[1] = 1  # No se puede cortar, pero si fuera necesario, el producto es trivial
    if n >= 2:
        dp[2] = 1  # Para n = 2, 1 * 1
    if n >= 3:
        dp[3] = 2  # Para n = 3, 2 * 1

    # Llenamos el dp para longitudes desde 4 hasta n
    for i in range(4, n + 1):
        for j in range(1, i // 2 + 1):
            # max(i - j, dp[i - j]) asegura que estamos considerando la mejor opción
            dp[i] = max(dp[i], j * max(i - j, dp[i - j]))

    return dp[n]