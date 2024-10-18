from balanza import *

def encontrar_joya(joyas):
    """
    Encuentra la joya verdadera utilizando un enfoque de división y conquista.
    joyas: una lista con las joyas, donde una pesa más que las demás.
    Retorna el índice de la joya verdadera.
    """
    return encontrar_joya_recursivo(joyas, 0, len(joyas) - 1)

def encontrar_joya_recursivo(joyas, inicio, fin):
    # Caso base: si solo queda una joya, es la verdadera
    if inicio == fin:
        return inicio
    
    # Dividimos el conjunto de joyas en dos mitades
    mitad = (fin - inicio + 1) // 2
    conjunto_izq = joyas[inicio:inicio + mitad]
    conjunto_der = joyas[inicio + mitad:inicio + 2 * mitad]
    
    # Usamos la balanza para comparar las dos mitades
    resultado = balanza(conjunto_izq, conjunto_der)
    
    if resultado == 1:
        # El lado izquierdo es más pesado
        return encontrar_joya_recursivo(joyas, inicio, inicio + mitad - 1)
    elif resultado == -1:
        # El lado derecho es más pesado
        return encontrar_joya_recursivo(joyas, inicio + mitad, inicio + 2 * mitad - 1)
    else:
        # Si las dos mitades pesan lo mismo, la joya verdadera está en la parte restante
        return inicio + 2 * mitad
    

#Explicacion: la recurcion la hice asi por si el arreglo tiene longuitud impar. Sino tendriamos dos casos, si es par o impar
# y seria mucho mas largo. Es dificil de entender pero simplifica el codigo.