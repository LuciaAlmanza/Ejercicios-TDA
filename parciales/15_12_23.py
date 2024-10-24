# 1. Implementar un algoritmo que, por división y conquista, dado un arreglo de n números enteros devuelva true o false
# según si existe algún elemento que aparezca más de dos tercios de las veces. El algoritmo debe ser O(n). Justificar la
# complejidad del algoritmo implementado.

#ej guia

# 2. Carlitos (primo de Juan, el vago) trabaja para una empresa de publicidad. Tiene un determinado presupuesto P que no
# puede sobrepasar, y tiene que una serie de campañas publicitarias para elegir. La campaña i cuesta $Ci

# . También se
# han realizado diversos estudios que permiten estimar cuánta ganancia nos dará cada campaña, que denominaremos Gi
# .
# Implementar un algoritmo que reciba esta información y devuelva cuáles campañas debe realizar Carlitos. Indicar y
# justificar la complejidad del algoritmo propuesto. ¿Da lo mismo si los valores están expresados en pesos argentinos,
# dólares u otra moneda? (haciendo la equivalencia de divisa, siempre suponiendo valores enteros).

#dp[j]=max(dp[j],dp[j−Ci +Gi)

def seleccionar_campanas(P, costos, ganancias):
    n = len(costos)
    dp = [0] * (P + 1)
    
    for i in range(n):
        for j in range(P, costos[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - costos[i]] + ganancias[i])
    
    # Para reconstruir la solución
    res = []
    j = P
    for i in range(n - 1, -1, -1):
        if j >= costos[i] and dp[j] == dp[j - costos[i]] + ganancias[i]:
            res.append(i)
            j -= costos[i]
    
    res.reverse()
    return res