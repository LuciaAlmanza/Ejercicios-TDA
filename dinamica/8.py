def cambio(monedas, monto):
    # Inicializar DP con un valor infinito para representar que no es posible alcanzar ese monto.
    # DP[i] será el mínimo número de monedas necesarias para obtener el valor i.
    DP = [float('inf')] * (monto + 1)
    DP[0] = 0  # No necesitamos monedas para alcanzar 0

    # Llenar la tabla DP
    for moneda in monedas:
        for i in range(moneda, monto + 1):
            DP[i] = min(DP[i], DP[i - moneda] + 1)

    # Si DP[monto] sigue siendo infinito, no hay solución
    if DP[monto] == float('inf'):
        return []

    # Reconstrucción de las monedas utilizadas
    monedas_usadas = []
    i = monto
    while i > 0:
        for moneda in monedas:
            if i - moneda >= 0 and DP[i] == DP[i - moneda] + 1:
                monedas_usadas.append(moneda)
                i -= moneda
                break

    return monedas_usadas