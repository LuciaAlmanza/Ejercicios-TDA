def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    anterior = 1
    actual = 1
    for i in range(2, n+1):
        nuevo = actual + anterior
        anterior = actual
        actual = nuevo
    return actual