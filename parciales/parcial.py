# ejercicio 3
def max_profit(p):
    n = len(p)
    if n < 2:
        return 0  # No se puede comprar y vender en un solo día
    
    # Variables para seguimiento
    min_price = p[0]
    max_profit = 0
    
    # Recorrer el arreglo
    for i in range(1, n):
        # Actualizar el precio mínimo hasta el día i
        min_price = min(min_price, p[i])
        # Calcular la ganancia máxima posible si se vende el día i
        max_profit = max(max_profit, p[i] - min_price)
    
    return max_profit

# ejercicio 2
# aca la idea es hacer el contragrafo, osea invertirlo

#ejercicio 1

def mochila_con_k(elementos, W, K):
    """
    Resuelve el problema de la mochila con restricciones de peso y cantidad mínima K mediante backtracking.

    Args:
    - elementos: Lista de tuplas (valor, peso) para cada elemento.
    - W: Peso máximo permitido.
    - K: Cantidad mínima de elementos que deben incluirse.

    Returns:
    - max_valor: El valor máximo obtenido.
    - mejor_seleccion: Lista de índices de los elementos seleccionados.
    """

    n = len(elementos)
    mejor_valor = [0]  # Usamos una lista para permitir modificaciones por referencia
    mejor_seleccion = [[]]

    def backtrack(indice, peso_actual, valor_actual, seleccionados):
        # Caso base: Si hemos revisado todos los elementos
        if indice == n:
            # Verificar si cumple la restricción de K elementos
            if len(seleccionados) >= K and valor_actual > mejor_valor[0]:
                mejor_valor[0] = valor_actual
                return seleccionados.copy()

        # Caso 1: No incluir el elemento actual
        backtrack(indice + 1, peso_actual, valor_actual, seleccionados)

        # Caso 2: Incluir el elemento actual (si el peso lo permite)
        valor, peso = elementos[indice]
        if peso_actual + peso <= W:
            seleccionados.append(indice)
            backtrack(indice + 1, peso_actual + peso, valor_actual + valor, seleccionados)
            seleccionados.pop()  # Deshacer la inclusión del elemento actual

    # Iniciar el proceso de backtracking
    backtrack(0, 0, 0, [])
    return mejor_valor[0], [elementos[i] for i in mejor_seleccion[0]]

#ejercicio 4
#explicacion y modelo en la foto, pero paso el codigo por si les sirve:
def max_clique(grafo):
    # Grafo: objeto que permite obtener los vértices y aristas
    vertices = grafo.obtener_vertices()  # Lista de vértices
    aristas = grafo.obtener_aristas()    # Lista de aristas (tuplas (u, v))
    problema = pulp.LpProblem("max_clique", pulp.LpMaximize)

    # Variables de decisión: x_v es 1 si el vértice está en el clique
    x = {v: pulp.LpVariable(f"x_{v}", cat="Binary") for v in vertices}

    # Función objetivo: maximizar el número de vértices en el clique
    problema += pulp.lpSum(x[v] for v in vertices)

    # Restricciones: para cada par (u, v) que no es una arista, x_u + x_v <= 1
    for u in vertices:
        for v in vertices:
            if u != v and (u, v) not in aristas and (v, u) not in aristas:
                problema += x[u] + x[v] <= 1

    # Resolver el problema
    problema.solve()

    # Construir el conjunto de vértices en el clique máximo
    clique = [v for v in vertices if pulp.value(x[v]) == 1]
    return clique


#ejercicio 5

def max_ganancia_divide_conquista(precios):
    """
    Encuentra la máxima ganancia posible al comprar y vender una casa.
    :param precios: Lista de precios para cada día.
    :return: La máxima ganancia posible.
    """
    if len(precios) < 2:
        return 0  # No es posible comprar y vender con menos de dos días
    
    return _max_ganancia_recursivo(precios, 0, len(precios) - 1)

def _max_ganancia_recursivo(precios, inicio, fin):
    # Caso base: si el segmento tiene un solo elemento, no hay ganancia posible
    if inicio >= fin:
        return 0
    
    # Dividimos el arreglo en dos mitades
    medio = (inicio + fin) // 2
    
    # Ganancia máxima en la mitad izquierda
    ganancia_izquierda = _max_ganancia_recursivo(precios, inicio, medio)
    
    # Ganancia máxima en la mitad derecha
    ganancia_derecha = _max_ganancia_recursivo(precios, medio + 1, fin)
    
    # Mejor ganancia que atraviese las mitades
    min_izquierda = min(precios[inicio:medio + 1])
    max_derecha = max(precios[medio + 1:fin + 1])
    ganancia_cruzada = max_derecha - min_izquierda
    
    # Devuelve el máximo de las tres ganancias
    return max(ganancia_izquierda, ganancia_derecha, ganancia_cruzada)