#Ecuacion de recurrencia: OPT[n] = OPT[n - 1] + OPT[n - 2] + OPT[n - 3]

def escalones(n):

    #Casos base:
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    optimo = [0] * (n + 1)

    optimo[0] = 1
    optimo[1] = 1
    optimo[2] = 2

    for i in range(3, n + 1):
        optimo[i] = optimo[i - 1] + optimo[i - 2] + optimo[i - 3]

    return optimo[n]