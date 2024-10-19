def multiplicar(a, b):
    return karatsuba(a, b)

def partir_num(num, mitad):
    x1 = int(num / (10**mitad))
    x0 = int(num - (x1 * (10**mitad)))
    return [x1, x0]

def karatsuba(a, b):
    tam = len(str(a))
    if tam == 1:
        return a * b

    m = tam // 2

    a1, a0 = partir_num(a,m)
    b1, b0 = partir_num(b,m)

    p = karatsuba(a1 + a0, b1 + b0)
    x0y0 = karatsuba(a0, b0)
    x1y1 = karatsuba(a1, b1)

    t1 = x1y1 * (10**(2*m))
    t2 = (p - x1y1 - x0y0) * (10**m)
    return t1 + t2 + x0y0

# O(n^og_2_3 )