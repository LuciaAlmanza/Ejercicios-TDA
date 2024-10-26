def three_sat_min(clausulas, num_variables):
    # Crear un diccionario para almacenar las variables de decisión binarias
    vars_lp = {}
    
    # Crear el problema de optimización, especificando que queremos minimizar
    problema = pulp.LpProblem("3SAT_minimum_true_vars", pulp.LpMinimize)

    # Crear variables binarias para cada variable de 3-SAT
    for i in range(num_variables):
        vars_lp[i] = pulp.LpVariable(f"x{i}", cat="Binary")

    # Función objetivo: minimizar la cantidad de variables que son True
    problema += pulp.lpSum(vars_lp[i] for i in range(num_variables))

    # Agregar restricciones para satisfacer cada cláusula
    for (a, b, c) in clausulas:
        # Si el literal es positivo, usamos la variable tal cual;
        # si es negativo, usamos 1 - la variable (para modelar la negación)
        lit_a = vars_lp[abs(a)] if a > 0 else (1 - vars_lp[abs(a)])
        lit_b = vars_lp[abs(b)] if b > 0 else (1 - vars_lp[abs(b)])
        lit_c = vars_lp[abs(c)] if c > 0 else (1 - vars_lp[abs(c)])
        
        # Restricción para asegurar que al menos un literal de la cláusula sea True
        problema += lit_a + lit_b + lit_c >= 1

    # Resolver el problema
    problema.solve()

    # Devolver los valores de las variables que deben estar en True
    resultado = [i for i in range(num_variables) if pulp.value(vars_lp[i]) == 1]
    
    return resultado