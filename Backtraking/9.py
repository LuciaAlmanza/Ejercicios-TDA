from compatibles import *

def solucion_compatible(horarios):
    for i in range(len(horarios)):
        for j in range(i + 1, len(horarios)):
            if not son_compatibles(horarios[i], horarios[j]):
                return False
    return True

def obtener_combinaciones_backtrack(materias, solucion_parcial):
    if len(materias) == 0:
        return [solucion_parcial] if solucion_compatible(solucion_parcial) else []

    materia_actual = materias[0]
    restantes = materias[1:]
    soluciones = []

    for curso in materia_actual:
        nueva_solucion = solucion_parcial + [curso]
        if solucion_compatible(nueva_solucion):
            soluciones.extend(obtener_combinaciones_backtrack(restantes, nueva_solucion))

    return soluciones

def obtener_combinaciones(materias):
    if len(materias) == 0:
        return []
    return obtener_combinaciones_backtrack(materias, [])