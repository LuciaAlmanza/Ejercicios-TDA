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

# 4.4. Implementar un algoritmo que resuelva el problema de 3-SAT: determinar si, dado un grupo de cláusulas de 3 términos
# (pudiendo ser complementos de variables), existe alguna asignación de valores de las variables tal que la disyunción de
# todas las cláusulas (que son todas conjunciones) evalúan a true.

def es_satisfecho(clausulas, asignacion):
    for clausula in clausulas:
        if not any((literal if literal > 0 else not literal) for literal in clausula):
            return False
    return True

def backtrack(clausulas, variables, index, asignacion):
    if index == len(variables):
        return es_satisfecho(clausulas, asignacion)

    # Asignar True a la variable actual
    asignacion[index] = True
    if backtrack(clausulas, variables, index + 1, asignacion):
        return True

    # Asignar False a la variable actual
    asignacion[index] = False
    if backtrack(clausulas, variables, index + 1, asignacion):
        return True

    return False

# Se tiene una matriz de n × m casilleros, en la cual empezamos en la posición (0, 0) (arriba a la izquierda) y queremos
# llegar a la posición (n − 1, m − 1) (abajo a la derecha), pero solamente nos podemos mover hacia abajo o hacia la
# derecha, y comenzamos con una vida inicial V . Cada casillero puede estar vacío, o tener una trampa. En los casilleros
# que hay trampas se nos reduce la vida en una cantidad Ti conocida (dependiente de cada casillero).
# Diseñar un algoritmo de programación dinámica que dados todos los datos necesarios, permita determinar la cantidad
# de vida máxima con la que podemos llegar a (n − 1, m − 1). Implementar también una forma de poder reconstruir dicho
# camino. Indicar la complejidad del algoritmo propuesto, en tiempo y espacio.

# dp[i][j]=max(dp[i−1][j]−Ti,j ,dp[i][j−1]−Ti,j)

def max_life_path(matrix, V):
    n = len(matrix)
    m = len(matrix[0])
    
    # dp[i][j] will store the maximum life at position (i, j)
    dp = [[-1] * m for _ in range(n)]
    parent = [[None] * m for _ in range(n)]
    
    # Initialize the starting position
    dp[0][0] = V - matrix[0][0]  # Reduce life by T[0][0]

    # Fill the dp table
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            
            # Calculate life from the top
            if i > 0 and dp[i-1][j] >= 0:  # Check if coming from above is possible
                life_from_top = dp[i-1][j] - matrix[i][j]
                if life_from_top > dp[i][j]:  # We want the max life
                    dp[i][j] = life_from_top
                    parent[i][j] = (i-1, j)

            # Calculate life from the left
            if j > 0 and dp[i][j-1] >= 0:  # Check if coming from the left is possible
                life_from_left = dp[i][j-1] - matrix[i][j]
                if life_from_left > dp[i][j]:  # We want the max life
                    dp[i][j] = life_from_left
                    parent[i][j] = (i, j-1)

    # Maximum life at the bottom-right corner
    max_life = dp[n-1][m-1]

    # Reconstruct the path if reachable
    path = []
    if max_life >= 0:
        x, y = n-1, m-1
        while (x, y) is not None:
            path.append((x, y))
            x, y = parent[x][y] if parent[x][y] else (None, None)
        path.reverse()  # Reverse the path to start from the beginning

    return max_life, path