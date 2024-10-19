# 2. Todos los años la asociación de Tiro con Arco profesional realiza una preclasificación de los n jugadores que terminaron
# en las mejores posiciones del ranking para un evento exclusivo. En la tarjeta de invitación quieren adjuntar el número de
# posición en la que está actualmente y a cuántos rivales invitados logró superar en el ranking, en comparación al ranking
# del año pasado. Contamos con un listado que tiene el nombre del jugador y la posición del ranking del año pasado
# ordenado por el ranking actual. Implementar un algoritmo que dada la lista mencionada, devuelva (por ejemplo, en un
# diccionario) a cuántos rivales ha superado cada uno de los invitados. Para realizar esto de forma eficiente, recomendamos
# utilizar División y Conquista.
# Ejemplo: LISTA: [(A, 3), (B, 4), (C, 2), (D, 8), (E, 6), (F, 5)]. Se puede ver que el jugador A pasó del
# 3er lugar al 1er lugar, superando al jugador C. El jugador B llegó al segundo lugar y superó al jugador C. El jugador C
# no logró superar a ninguno de los invitados (si bien se encuentra en la tercera posición, ya tenía el año anterior mejor
# clasificación que el resto de invitados, por tanto no logró superar a ninguno), etc. . .

#es parecido al de inversiones :)

def contar_superados(jugadores):
    # Función principal que inicia el proceso
    resultado = [0] * len(jugadores)
    _contar_superados(jugadores, resultado, 0, len(jugadores) - 1)
    return {jugadores[i][0]: resultado[i] for i in range(len(jugadores))}

def _contar_superados(jugadores, resultado, inicio, fin):
    if inicio >= fin:
        return

    mitad = (inicio + fin) // 2

    # Contar en las mitades izquierda y derecha
    _contar_superados(jugadores, resultado, inicio, mitad)
    _contar_superados(jugadores, resultado, mitad + 1, fin)

    # Contar rivales superados durante la fusión
    fusionar(jugadores, resultado, inicio, mitad, fin)

def fusionar(jugadores, resultado, inicio, mitad, fin):
    # Crear una copia de la parte de la lista que se está fusionando
    izquierda = jugadores[inicio:mitad + 1]
    derecha = jugadores[mitad + 1:fin + 1]

    i = 0  # Índice para la mitad izquierda
    j = 0  # Índice para la mitad derecha
    k = inicio  # Índice para la lista original

    # Contador de cuántos han sido superados en la parte derecha
    contador_superados = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i][1] < derecha[j][1]:  # Si el jugador de la izquierda tiene mejor posición
            resultado[inicio + i] += contador_superados
            jugadores[k] = izquierda[i]
            i += 1
        else:
            contador_superados += 1
            jugadores[k] = derecha[j]
            j += 1
        k += 1

    # Copiar cualquier resto de la izquierda
    while i < len(izquierda):
        resultado[inicio + i] += contador_superados
        jugadores[k] = izquierda[i]
        i += 1
        k += 1

    # Copiar cualquier resto de la derecha
    while j < len(derecha):
        jugadores[k] = derecha[j]
        j += 1
        k += 1

# O(nlogn)

