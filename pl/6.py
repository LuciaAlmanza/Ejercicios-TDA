def mst_min(grafo):
    x=[]
    aristas=grafo.obtener_aristas()
    vertices=grafo.obtener_vertices()

    prob = pulp.LpProblem("MinimumSpanningTree", pulp.LpMinimize)

# Variables: una para cada arista (i, j)
    x = pulp.LpVariable.dicts("x", edges, cat="Binary")

    # Función objetivo: minimizar la suma de los pesos de las aristas seleccionadas
    prob += pulp.lpSum(weights[(i, j)] * x[(i, j)] for (i, j) in edges)

    # Restricción de número de aristas: |V| - 1
    prob += pulp.lpSum(x[(i, j)] for (i, j) in edges) == len(vertices) - 1

    # Resolver el problema
    prob.solve()

    #incompleto
    problema.solve()