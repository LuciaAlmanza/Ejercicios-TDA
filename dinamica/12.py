# cada campaña publicitaria i de la forma (Gi, Ci)
def carlitos(c_publicitaria, P):
    n = len(c_publicitaria)
    
    # Matriz dp donde dp[i][p] almacena la máxima ganancia posible con i campañas y presupuesto p
    dp = [[0] * (P + 1) for _ in range(n + 1)]
    
    # Llenado de la tabla dp
    for i in range(1, n + 1):
        G_i, C_i = c_publicitaria[i - 1]
        for p in range(P + 1):
            if C_i > p:
                dp[i][p] = dp[i - 1][p]  # No podemos incluir la campaña i
            else:
                dp[i][p] = max(dp[i - 1][p], G_i + dp[i - 1][p - C_i])
    
    # Reconstrucción de las campañas seleccionadas
    resultado = []
    p = P
    for i in range(n, 0, -1):
        if dp[i][p] != dp[i - 1][p]:  # Si la campaña i fue seleccionada
            resultado.append(c_publicitaria[i - 1])
            p -= c_publicitaria[i - 1][1]  # Restamos el costo de la campaña seleccionada
    
    return resultado[::-1]