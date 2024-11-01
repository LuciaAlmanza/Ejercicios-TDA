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

def resolver_3SAT(clausulas):
    variables = obtener_variables(clausulas)
    asignacion = {}
    return backtrack(clausulas, variables, asignacion, 0)

def obtener_variables(clausulas):
    variables = set()
    for clausula in clausulas:
        for literal in clausula:
            variables.add(abs(literal))  # Añadimos solo el valor absoluto de la variable
    return list(variables)

def backtrack(clausulas, variables, asignacion, indice):
    # Si ya asignamos todas las variables, verificamos si la fórmula es satisfactible
    if indice == len(variables):
        return verificar_clausulas(clausulas, asignacion)
    
    # Seleccionamos la siguiente variable a asignar
    var = variables[indice]
    
    # Intentamos asignar True a la variable y probamos si la fórmula se cumple
    asignacion[var] = True
    if backtrack(clausulas, variables, asignacion, indice + 1):
        return True
    
    # Intentamos asignar False a la variable y probamos si la fórmula se cumple
    asignacion[var] = False
    if backtrack(clausulas, variables, asignacion, indice + 1):
        return True
    
    # Deshacer la asignación para este nivel de backtracking
    del asignacion[var]
    return False

def verificar_clausulas(clausulas, asignacion):
    for clausula in clausulas:
        satisfactible = False
        for literal in clausula:
            var = abs(literal)
            valor_literal = asignacion.get(var, False)
            # Si el literal es negativo, invertimos su valor
            if literal < 0:
                valor_literal = not valor_literal
            # Si algún literal en la cláusula es verdadero, la cláusula es satisfactible
            if valor_literal:
                satisfactible = True
                break
        # Si encontramos una cláusula que no es satisfactible, la fórmula no es válida
        if not satisfactible:
            return False
    # Todas las cláusulas son satisfactibles
    return True

# Se tiene una matriz de n × m casilleros, en la cual empezamos en la posición (0, 0) (arriba a la izquierda) y queremos
# llegar a la posición (n − 1, m − 1) (abajo a la derecha), pero solamente nos podemos mover hacia abajo o hacia la
# derecha, y comenzamos con una vida inicial V . Cada casillero puede estar vacío, o tener una trampa. En los casilleros
# que hay trampas se nos reduce la vida en una cantidad Ti conocida (dependiente de cada casillero).
# Diseñar un algoritmo de programación dinámica que dados todos los datos necesarios, permita determinar la cantidad
# de vida máxima con la que podemos llegar a (n − 1, m − 1). Implementar también una forma de poder reconstruir dicho
# camino. Indicar la complejidad del algoritmo propuesto, en tiempo y espacio.

# dp[i][j]=max(dp[i−1][j]−Ti,j ,dp[i][j−1]−Ti,j)

def max_life_path(matrix, V):
    n, m = len(matrix), len(matrix[0])
    
    # Crear la matriz DP inicializada con un valor negativo para indicar inalcanzabilidad
    dp = [[-float('inf')] * m for _ in range(n)]
    dp[0][0] = V - matrix[0][0]  # Vida inicial menos el costo de la primera casilla
    
    # Llenar la matriz DP
    for i in range(n):
        for j in range(m):
            if i > 0 and dp[i - 1][j] > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] - matrix[i][j])
            if j > 0 and dp[i][j - 1] > 0:
                dp[i][j] = max(dp[i][j], dp[i][j - 1] - matrix[i][j])
    
    # La vida máxima para llegar a (n-1, m-1)
    max_life = dp[n - 1][m - 1]
    
    # Reconstrucción del camino desde (n-1, m-1) hasta (0, 0)
    path = []
    if max_life > 0:  # Solo reconstruimos si es alcanzable
        i, j = n - 1, m - 1
        while i > 0 or j > 0:
            path.append((i, j))
            if i > 0 and dp[i][j] == dp[i - 1][j] - matrix[i][j]:
                i -= 1
            else:
                j -= 1
        path.append((0, 0))  # Agregar la posición inicial
        path.reverse()  # Invertir para obtener el camino en orden
    
    return max_life, path