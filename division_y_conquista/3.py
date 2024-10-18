
def parte_entera_raiz(n):
    return _integer_square_root(n, 0, n)

def _integer_square_root(n, start, end):
    if start > end:
        return -1
        
    mid = (start + end) // 2
    
    if (mid ** 2 == n):
        return mid 
        
    if (mid ** 2 > n):
        if (mid - 1 > 0 and (mid - 1)**2 < n):
            return mid - 1
        return _integer_square_root(n, start, mid)
        
    return _integer_square_root(n, mid+1, end)