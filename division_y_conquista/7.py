import math

# es horrendo, pero asi lo hace victor, hechenle la culpa a el 

def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def fuerza_bruta(P):
    min_dist = float("inf")
    p1, p2 = None, None
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            dist = distancia(P[i], P[j])
            if dist < min_dist:
                min_dist = dist
                p1, p2 = P[i], P[j]
    return p1, p2, min_dist


def puntos_cerc_rec(Px, Py):
    n = len(Px)
    
 
    if n <= 3:
        return fuerza_bruta(Px)
    
    
    mitad = n // 2
    Qx = Px[:mitad]
    Rx = Px[mitad:]
    
  
    x_medio = Qx[-1][0]
    
    
    Qy = list(filter(lambda p: p[0] <= x_medio, Py))
    Ry = list(filter(lambda p: p[0] > x_medio, Py))
    
 
    (q0, q1, d_q) = puntos_cerc_rec(Qx, Qy)
    (r0, r1, d_r) = puntos_cerc_rec(Rx, Ry)
    
    
    d = min(d_q, d_r)
    min_pair = (q0, q1) if d_q < d_r else (r0, r1)
    
   
    S = [p for p in Py if abs(p[0] - x_medio) < d]
    
   
    for i in range(len(S)):
        for j in range(i + 1, min(i + 7, len(S))):
            dist_s = distancia(S[i], S[j])
            if dist_s < d:
                d = dist_s
                min_pair = (S[i], S[j])
    
    return min_pair[0], min_pair[1], d


def puntos_mas_cercanos(P):
    Px = sorted(P, key=lambda p: p[0])
    Py = sorted(P, key=lambda p: p[1])
    return puntos_cerc_rec(Px, Py)
