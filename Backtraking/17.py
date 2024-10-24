from grafo import Grafo
def submarinos(matriz):
    g = Grafo()
    submarinos = []
    # construimos el grafo de las posiciones de los submarinos, en este caso los vertices son las coordenadas de cada cuadradito del tablero
    for i in range(len(matriz)):
        for j in range(len(matriz[i])): #si hay un subamrino lo appendeo
            if matriz[i][j]: submarinos.append((i, j))
            g.agregar_vertice((i,j)) # agrego coordenadas lo agrego como vertice
            if i-2 >= 0: #agrego conexiones con celdas vecinas que pueden llegar a ser iluminadas osea de radio de 2 y luego de radio de 1
                g.agregar_arista((i-2, j), (i, j))
                if j-1 >= 0:g.agregar_arista((i-2, j-1), (i, j))
                if j-2 >= 0: g.agregar_arista((i-2, j-2), (i, j))
                if j+2 < len(matriz[i-1]):g.agregar_arista((i-2, j+2), (i, j))
                if j+1 < len(matriz[i-1]):g.agregar_arista((i-2, j+1), (i, j))
            if i-1 >= 0:
                g.agregar_arista((i-1, j), (i, j))
                if j-1 >= 0:g.agregar_arista((i-1, j-1), (i, j))
                if j-2 >= 0: g.agregar_arista((i-1, j-2), (i, j))
                if j+1 < len(matriz[i-1]):g.agregar_arista((i-1, j+1), (i, j))
                if j+2 < len(matriz[i-1]):g.agregar_arista((i-1, j+2), (i, j))
            if j-2 >= 0: g.agregar_arista((i, j-2), (i, j))
            if j-1 >= 0: g.agregar_arista((i, j-1), (i, j))
    return iluminar_submarinos(g, g.obtener_vertices(), 0, [], submarinos, submarinos)

def iluminar_submarinos(g, vertices, ind_vertice, sol_actual, mejor_sol, submarinos):
    if len(sol_actual) >= len(mejor_sol):
        return mejor_sol
    if esSolucion(g, sol_actual, submarinos):
        return sol_actual[:]
    if ind_vertice >= len(vertices):
        return mejor_sol
    sol_actual.append(vertices[ind_vertice])
    agregando_vertice = iluminar_submarinos(g, vertices, ind_vertice+1, sol_actual, mejor_sol, submarinos)
    if len(agregando_vertice) < len(mejor_sol):
        mejor_sol = agregando_vertice
    sol_actual.remove(vertices[ind_vertice])
    quitando_vertice = iluminar_submarinos(g, vertices, ind_vertice+1, sol_actual, mejor_sol, submarinos)
    if len(quitando_vertice) < len(mejor_sol):
        mejor_sol = quitando_vertice
    return mejor_sol

def esSolucion(g, solucion_candidata, submarinos):
    for sub in submarinos:
        esta_iluminado = False
        for v in solucion_candidata:
            if g.estan_unidos(v, sub) or v == sub:
                esta_iluminado = True
                break
        if not esta_iluminado:
            return False
    return True