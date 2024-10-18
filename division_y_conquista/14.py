def encontrar_contagiado(personas):

    if len(personas) == 1:
        return personas[0] if pcr(personas) else None
    
    
    mitad = len(personas) // 2
    grupo_izq = personas[:mitad]
    grupo_der = personas[mitad:]
    
   
    if pcr[mitad]:
        return personas[mitad]
    if pcr(grupo_izq):
        
        return encontrar_contagiado(grupo_izq)
    else:
       
        return encontrar_contagiado(grupo_der)