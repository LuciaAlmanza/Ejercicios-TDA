def backtrack(n, s, current_roll, all_rolls):
    # Verificamos si hemos alcanzado el objetivo
    if n == 0:
        if s == 0:
            all_rolls.append(current_roll.copy())
        return
    
    # Límite inferior y superior
    min_sum_remaining = n  # Todos los dados muestran 1
    max_sum_remaining = 6 * n  # Todos los dados muestran 6

    # Si la suma deseada es inalcanzable, retornamos
    if s < min_sum_remaining or s > max_sum_remaining:
        return

    for i in range(1, 7):
        if s - i >= 0:
            current_roll.append(i)
            backtrack(n - 1, s - i, current_roll, all_rolls)
            current_roll.pop()

def sumatoria_dados(n, s):
    all_rolls = []
    backtrack(n, s, [], all_rolls)
    return all_rolls