def operaciones(k):
    # Inicializamos un arreglo dp con valores infinitos excepto dp[0]
    dp = [float('inf')] * (k + 1)
    dp[0] = 0  # Llegar a 0 requiere 0 operaciones

    # Llenamos el arreglo dp con la cantidad mínima de operaciones para cada número
    for i in range(1, k + 1):
        # Operación de suma +1
        dp[i] = dp[i - 1] + 1
        # Operación de duplicar si i es par
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

    # Ahora reconstruimos el camino de operaciones
    operaciones = []
    while k > 0:
        if k % 2 == 0 and dp[k // 2] + 1 == dp[k]:  # Si el número es par y viene de k // 2
            operaciones.append('por2')
            k //= 2
        else:  # Sino, la operación fue un +1
            operaciones.append('mas1')
            k -= 1

    operaciones.reverse()  # Invertimos el orden para obtener desde 0 a K
    return operaciones