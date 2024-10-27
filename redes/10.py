def max_caminos_disjuntos(grafo, s, t):
    # Inicializa el grafo de flujo con la misma estructura
    flujo_grafo = Grafo(direccionado=True)

    # Agregar vértices y aristas al grafo de flujo
    for v in grafo.obtener_vertices():
        flujo_grafo.agregar_vertice(v)
    
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            # Cada arista se agrega con capacidad 1
            flujo_grafo.agregar_arista(v, w, 1)

    # Aplicar el algoritmo de flujo máximo (Ford-Fulkerson o Edmonds-Karp)
    flujo_maximo = flujo_maximo(flujo_grafo, s, t)  # Debe implementar la función de flujo máximo

    return flujo_maximo

# Metodología para Resolver el Problema
# Paso 1: Modelar el Grafo
# Crear un grafo dirigido donde cada arista tiene una capacidad de 1.
# Paso 2: Encontrar el Flujo Máximo
# Utilizar un algoritmo de flujo máximo (como Ford-Fulkerson o Edmonds-Karp) para calcular el flujo máximo entre s y 𝑡
# Paso 3: Interpretar el Resultado
# El resultado del flujo máximo será igual al número máximo de caminos disjuntos desde s a t.