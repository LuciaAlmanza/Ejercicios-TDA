# 1.Un algoritmo sencillo para multiplicar matrices de n × n demora O(n ^3). 
# El algoritmo de Strassen (que utiliza División y Conquista) lo hace en O(n log2 7). 
# La profesora Manterola quiere implementar un algoritmo de División y Conquista que sea aún más veloz, 
# donde divida al problema en A subproblemas de tamaño de n /8, y que juntar las soluciones parciales sea O(n ^2). 
# ¿Cuál es el máximo A para que el orden del algoritmo sea menor que el del algoritmo de Strassen? Justificar.

#esta la resolucion en la foto, da feo :(

# 4. Implementar un algoritmo Greedy que busque aproximar la solución óptima al problema del mínimo Vertex Cover:
# dado un grafo, obtener el mínimo Vertex Cover del mismo. Indicar la complejidad del algoritmo implementado, dar un
# contraejemplo para el algoritmo implementado y justificar por qué el algoritmo implementado es un algoritmo greedy.

def vertex_cover(self):
    cover = set()
    aristas = self.obtener_aristas()

    while aristas:
            # Elegir una arista arbitraria
       
        v, w = aristas[0]
        cover.add(v)
        cover.add(w)
            # Eliminar aristas incidentes a u y v
        aristas = [(u, z) for u, z in aristas if u != v and u != w and z != v and z != w]

    return cover

#O(m) numero de aristas del grafo

# Contraejemplo
#Este algoritmo no garantiza encontrar siempre el mínimo Vertex Cover. A continuación, un contraejemplo:

#Consideremos el siguiente grafo en forma de ciclo de 4 vértices
# 1 - 2
# |   |
# 4 - 3

#En este caso, el mínimo Vertex Cover tiene 2 vértices: {1, 3} o {2, 4}. Sin embargo, 
# el algoritmo podría seleccionar 3 vértices si elige las aristas en un orden desfavorable, por ejemplo:

# Elige la arista (1, 2), agregando {1, 2} al Vertex Cover.
# Luego, selecciona la arista (3, 4), agregando {3, 4} al Vertex Cover.
# En este caso, se habrán seleccionado 4 vértices (1, 2, 3, 4) en lugar del óptimo que solo requiere 2 vértices.

# 2. El papá de Pepe le dió n monedas para repartir entre él y su hermanito. El padre puso las monedas formando una
# única fila. Cada moneda tiene con diferente valor vi

# . El padre de Pepe le dice que primero debe elegir una para él,
# y que sólo puede elegir la primera o la última de la fila. Luego, debe elegir una para su hermano menor siguiendo la
# misma regla, luego otra para él, y así.
# Implementar un algoritmo que, utilizando programación dinámica, obtenga el valor máximo que pueda quedarse Pepe
# dadas estas condiciones (asumamos que usará parte de sus ganancias para comprarle un chocolate a su hermano).
# Importante: antes de escribir código, plantear y explicar la ecuación de recurrencia correspondiente.

#este basicamente es el ej del tp :(

#F(i, j) = Max(Vi + min(F(i+2, j), F(i+1, j-1) ), Vj + min(F(i+1, j-1), F(i, j-2) ))

def optimalStrategyOfGame(arr, n):
 
    # Create a table to store
    # solutions of subproblems
    table = [[0 for i in range(n)]
             for i in range(n)]
 
    # Fill table using above recursive
    # formula. Note that the table is
    # filled in diagonal fashion
    # from diagonal elements to
    # table[0][n-1] which is the result.
    for gap in range(n):
        for j in range(gap, n):
            i = j - gap
 
            # Here x is value of F(i + 2, j),
            # y is F(i + 1, j-1) and z is
            # F(i, j-2) in above recursive
            # formula
            x = 0
            if((i + 2) <= j):
                x = table[i + 2][j]
            y = 0
            if((i + 1) <= (j - 1)):
                y = table[i + 1][j - 1]
            z = 0
            if(i <= (j - 2)):
                z = table[i][j - 2]
            table[i][j] = max(arr[i] + min(x, y),
                              arr[j] + min(y, z))
    return table[0][n - 1]