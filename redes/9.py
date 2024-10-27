def encontrar_matching_maximo(grafo):
    matching = {}
    visited = set()

    def dfs(v):
        for u in grafo[v]:
            if u not in visited:
                visited.add(u)
                if u not in matching or dfs(matching[u]):
                    matching[u] = v
                    matching[v] = u
                    return True
        return False

    for v in grafo:
        if v not in matching:
            visited.clear()
            dfs(v)

    return matching