# 2.Tenés una colección de n libros con diferentes espesores, que pueden estar entre 1 y n (valores no necesariamente
# enteros). Tu objetivo es guardar esos libros en la menor cantidad de cajas. Todas las cajas que disponés son de la
# misma capacidad L (se asegura que L ≥ n). Obviamente, no podés partir un libro para que vaya en múltiples cajas,
# pero sí podés poner múltiples libros en una misma caja, siempre y cuando no superen esa capacidad L. Implementar un
# algoritmo Greedy que obtenga la mínima cantidad de cajas a utilizar. Indicar y justificar la complejidad del algoritmo
# implementado. Justificar por qué se trata de un algoritmo greedy (no dar una respuesta genérica, sino aplicada a tu
# algoritmo). ¿El algoritmo propuesto encuentra siempre la solución óptima? Justificar.

#ej de la guia

# 4. Implementar un algoritmo que reciba un Grafo y un número k y devuelva un dominating set de dicho grafo de a lo
# sumo k vértices (si existe).

def dominating_set(grafo, k):
    vertices = grafo.obtener_vertices()
    n = len(vertices)  # Número de vértices

    # Variable binaria que indica si el vértice v está en el Dominating Set
    x = pulp.LpVariable.dicts("x", vertices, cat="Binary")

    # Crear el problema de optimización
    problema = pulp.LpProblem("Dominating_Set", pulp.LpMinimize)

    # Restricción para asegurarse de que cada vértice está dominado
    for v in vertices:
        # Sumar x[v] y x[w] donde w es adyacente a v
        problema += x[v] + pulp.lpSum(x[w] for w in grafo.adyacentes(v)) >= 1

    # Restricción para el tamaño del Dominating Set
    problema += pulp.lpSum(x[v] for v in vertices) <= k

    # Resolver el problema
    problema.solve()

    # Obtener el resultado: vértices en el Dominating Set
    resultado = [v for v in vertices if pulp.value(x[v]) == 1]

    if len(resultado) <= k:
        return resultado
    else:
        return [] 