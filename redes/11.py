def asignar_libros_a_alumnos(alumnos, libros):
    grafo = Grafo(direccionado=True)

    # Crear vértices de la red
    grafo.agregar_vertice("S")  # Fuente
    for alumno in alumnos:
        grafo.agregar_vertice(alumno)
    for libro in libros:
        grafo.agregar_vertice(libro)
    grafo.agregar_vertice("T")  # Sumidero

    # Agregar aristas de la fuente a los alumnos
    for alumno in alumnos:
        grafo.agregar_arista("S", alumno, 10)  # Capacidad 10

    # Agregar aristas de los alumnos a los libros
    for alumno in alumnos:
        for libro in alumno.libros_pedidos:  # Asumiendo que hay una lista de libros que cada alumno quiere
            grafo.agregar_arista(alumno, libro, 1)  # Capacidad 1

    # Agregar aristas de los libros al sumidero
    for libro in libros:
        grafo.agregar_arista(libro, "T", 3)  # Capacidad 3

    # Calcular el flujo máximo
    flujo_max = flujo_maximo(grafo, "S", "T")
    
    return flujo_max