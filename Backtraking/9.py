def obtener_combinaciones(materias):
    resul=[]
    combinaciones=[]

    return backtracking_materias(materias,resul,combinaciones,0)



def backtracking_materias(materias,resul,combinaciones,indice):
    if len(materias)==indice:
        combinaciones.append(list(resul))
        return
    materia=materias[indice]
    

    for curso in materia:
        valido=True
        for posible in resul:
            if not son_compatibles(curso,posible):
                valido=False
                break
        
        if valido:
            resul.append(curso)
            backtracking_materias(materias,resul,combinaciones,indice+1)
            resul.pop()

    return combinaciones