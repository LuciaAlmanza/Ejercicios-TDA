def mas_mitad(arr, ini, fin):
    if fin - ini < 1:
        return arr[ini]
    medio = (ini+fin)//2
    e1 = mas_mitad(arr, ini, medio)
    e2 = mas_mitad(arr, medio+1, fin)
    count1 = count2 = 0
    for i in range(ini,fin+1):
        if e1 == arr[i]:
            count1 += 1
        if e2 == arr[i]:
            count2 += 1
    if count1 > (fin-ini)//2:
        return e1
    if count2 > (fin-ini)//2:
        return e2
    return None

def masmitad(arr):
    return mas_mitad(arr, 0, len(arr)-1)

# O(nlogn)