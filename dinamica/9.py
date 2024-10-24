def subset_sum(elementos, v):
    n = len(elementos)

    # Creamos una tabla DP para almacenar si una suma j es posible con los primeros i elementos
    dp = [[False] * (v + 1) for _ in range(n + 1)]

    # Inicializamos la primera columna (suma 0 es siempre posible)
    for i in range(n + 1):
        dp[i][0] = True

    # Llenamos la tabla DP
    for i in range(1, n + 1):
        for j in range(1, v + 1):
            if elementos[i - 1] <= j:
                # El número puede ser incluido o excluido
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - elementos[i - 1]]
            else:
                # Solo podemos excluir el número
                dp[i][j] = dp[i - 1][j]

    # Buscamos la mayor suma posible que no exceda V
    for j in range(v, -1, -1):
        if dp[n][j]:
            max_sum = j
            break

    # Encontramos qué elementos componen la suma máxima
    resultado = []
    j = max_sum

    for i in range(n, 0, -1):
        if not dp[i - 1][j]:  # El elemento i-1 está incluido
            resultado.append(elementos[i - 1])
            j -= elementos[i - 1]

    resultado.reverse()  # Para devolver en el orden original
    return resultado