# 4.Implementar un algoritmo potencia(b, n) que nos devuelva el resultado de b ^(n) en tiempo O(log n).
# Justificar  adecuadamente la complejidad del algoritmo implementado. Ayuda: recordar propiedades matemáticas de la potencia. 

# Por ejemplo, que a ^(h)· a^(k) = a ^(h+k ).

def potencia(b, n):
    # Caso base: cualquier número elevado a la potencia de 0 es 1
    if n == 0:
        return 1
    # Caso recursivo
    if n % 2 == 0:  # n es par
        half_pow = potencia(b, n // 2)  # Divide el problema
        return half_pow * half_pow  # Combina las soluciones
    else:  # n es impar
        return b * potencia(b, n - 1)  # Un caso más simple

    
# O(logn)