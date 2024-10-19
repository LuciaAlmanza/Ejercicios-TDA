def raiz(funcion, a, b, tol=1e-6):
    # Asegurarse de que la función cumple las condiciones del teorema de Bolzano
    if funcion(a) * funcion(b) > 0:
        raise ValueError("La función debe tener signos opuestos en los extremos del intervalo.")
    if (b - a) < tol:
        return (a + b) // 2
    m = (a + b) // 2
  
    fm = funcion(m)
        
    if fm == 0:
        return m  # Se encontró la raíz exacta
    elif funcion(a) * fm < 0:
        return raiz(funcion, a,m)
    else:
        return raiz(funcion, m,b)
    
# O(logn)