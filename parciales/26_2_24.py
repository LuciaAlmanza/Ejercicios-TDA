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
    arr_temp = [0] * len(jugadores)
    _contar_superados(jugadores, resultado, 0, len(jugadores) - 1,arr_temp)
    return {jugadores[i][0]: resultado[i] for i in range(len(jugadores))}

def _contar_superados(jugadores, resultado, inicio, fin,arr_temp):
    if inicio >= fin:
        return

    mitad = (inicio + fin) // 2

    # Contar en las mitades izquierda y derecha
    _contar_superados(jugadores, resultado, inicio, mitad,arr_temp)
    _contar_superados(jugadores, resultado, mitad + 1, fin,arr_temp)

    # Contar rivales superados durante la fusión
    fusionar(jugadores, resultado, inicio, mitad, fin;arr_temp)


def fusionar(jugadores, resultado, inicio, mitad, fin,arr_temp):

    i = inicio  # Índice para la mitad izquierda
    j = mitad+1  # Índice para la mitad derecha
    k = inicio  # Índice para la lista original

    # Contador de cuántos han sido superados en la parte derecha
    contador_superados = 0

    while i <= mitad and j <= fin:
        if jugadores[i][1] < jugadores[j][1]:  # Si el jugador de la izquierda tiene mejor posición
            resultado[i] += contador_superados
            arr_temp[k] = jugadores[i]
            i += 1
        else:
            contador_superados += 1
            arr_temp[k] = jugadores[j]
            j += 1
        k += 1

    # Copiar cualquier resto de la izquierda
    while i <= mitad:
        resultado[i] += contador_superados
        arr_temp[k] = jugadores[i]
        i += 1
        k += 1

    # Copiar cualquier resto de la derecha
    while j <= fin:
        arr_temp[k] = jugadores[j]
        j += 1
        k += 1
    for i in range(inicio, fin + 1):
        jugadores[i] = arr_temp[i]

# O(nlogn)

# 3. El K-core de un grafo es el subgrafo del mismo en el cuál todos los vértices tienen grados mayor o igual a K. Implementar
# un algoritmo greedy que dado un grafo y un valor K devuelva el K-core del grafo (es decir, el subgrafo en el cuál todos
# los vértices involucrados tienen grado mayor o igual a K, en dicho subgrafo). Indicar y justificar la complejidad del
# algoritmo implementado. Justificar por qué se trata de un algoritmo greedy.

def k_core(grafo, K):
    cambios = True
    while cambios:
        cambios = False
        vertices = grafo.obtener_vertices()
        for v in vertices:
            if grafo.obtener_grado(v) < K:
                for vecino in grafo.adyacentes(v):
                    grafo.borrar_arista(v, vecino)
                grafo.borrar_vertice(v)
                cambios = True
    return grafo

#O(n+m).