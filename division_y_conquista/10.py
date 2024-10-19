
def mas_de_la_mitad_rec(arr):
    if len(arr) == 1:
        return arr[0]

    l = []
    for i in range(0, len(arr)-1, 2):
        if arr[i] == arr[i+1]:
            l.append(arr[i])
    if l == []:
        return None
    candidato = mas_de_la_mitad_rec(l)
    if candidato is not None and arr.count(candidato) > len(arr) // 2:
        return candidato
    if len(arr) % 2 != 0 and arr.count(arr[-1]) > len(arr) // 2:
            return candidato
    return None

def mas_de_la_mitad(arr):
    candidato = mas_de_la_mitad_rec(arr)
    return None if candidato is None or arr.count(candidato) <= len(arr) // 2 else candidato

# O(n)