def construir_grafo_bipartito(medicos, pacientes):
    grafo = Grafo(dirigido=False)

    # Crear nodos para cada médico y paciente
    for medico in medicos:
        grafo.agregar_vertice(medico)
    for paciente in pacientes:
        grafo.agregar_vertice(paciente)
    
    # Agregar aristas para compatibilidad de especialidad y disponibilidad
    for medico in medicos:
        for paciente in pacientes:
            if medico.especialidad == paciente.especialidad_requerida:
                # Verificar disponibilidad horaria
                if hay_franja_horaria_en_comun(medico.horarios, paciente.horarios):
                    grafo.agregar_arista(medico, paciente)
    
    return grafo

def maximizar_citas_medicas(medicos, pacientes):
    # Construir el grafo bipartito de citas posibles
    grafo = construir_grafo_bipartito(medicos, pacientes)
    
    # Aplicar el algoritmo de Hopcroft-Karp para encontrar el emparejamiento máximo
    citas_maximas = emparejamiento_maximo_hopcroft_karp(grafo)
    
    return citas_maximas  # Conjunto de emparejamientos que maximiza las citas