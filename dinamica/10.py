def plan_operativo(arreglo_L, arreglo_C, costo_M):
    n = len(arreglo_L)
    
    # Inicialización de costos
    dp_L = [0] * n
    dp_C = [0] * n
    
    # Costos del primer mes
    dp_L[0] = arreglo_L[0]
    dp_C[0] = arreglo_C[0]

    # Calcular costos para cada mes
    for i in range(1, n):
        dp_L[i] = arreglo_L[i] + min(dp_L[i-1], dp_C[i-1] + costo_M)
        dp_C[i] = arreglo_C[i] + min(dp_C[i-1], dp_L[i-1] + costo_M)

    # Costo mínimo total al final
    if dp_L[n-1] < dp_C[n-1]:
        current_city = 'L'  # Último mes en Londres
    else:
        current_city = 'C'  # Último mes en California

    # Reconstrucción de la secuencia de operaciones
    secuencia = []
    for i in range(n-1, -1, -1):
        if current_city == 'L':
            secuencia.append('londres')
            if i > 0:
                if dp_L[i] == arreglo_L[i] + dp_L[i-1]:
                    current_city = 'L'
                else:
                    current_city = 'C'
        else:
            secuencia.append('california')
            if i > 0:
                if dp_C[i] == arreglo_C[i] + dp_C[i-1]:
                    current_city = 'C'
                else:
                    current_city = 'L'

    secuencia.reverse()  # Invertir para obtener el orden correcto
    return secuencia