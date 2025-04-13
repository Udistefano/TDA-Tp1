# Tenemos una serie de n partículas cargadas muy pequeñas, ubicadas a intervalos regulares
# a lo largo de una línea recta en las ubicaciones {1, 2, ..., n}. En cada uno de estos puntos,
# tenemos una partícula cargada qj, que puede ser positiva o negativa. Queremos estudiar la
# fuerza total sobre cada partícula mediante la Ley de Coulomb:
# ponele que la fuerza sobre una particula está definida como: (c es una cte) e i representa a otra particula sobre la recta
# Fj = sumatoria para i < j C * q_i* q_j / (j-i)^2 -  sumatoria para i > j C * q_i* q_j / (j-i)^2
# Desarrollar un algoritmo que calcule Fj mediante División y Conquista.

# siendo particulas: un arreglo con la carga de las particulas
# C: cte
def calcular_fuerzas(q, C):
    fuerzas = [0] * len(q)
    calcular_fuerzas_aux(q, fuerzas, C, 0, len(q) - 1)
    return fuerzas

def calcular_fuerzas_aux(q, fuerzas, C, inicio, fin):
    if inicio == fin or inicio > fin:
        return

    medio = (inicio + fin) // 2

    calcular_fuerzas_aux(q, fuerzas, C, inicio, medio)
    calcular_fuerzas_aux(q, fuerzas, C, medio + 1, fin)

    for j in range(medio + 1, fin + 1):
        for i in range(inicio, medio + 1):
            fuerzas[j] += C * (q[i] * q[j]) / (j - i) **  2

    for j in range(inicio, medio + 1):
        for i in range(medio + 1, fin + 1):
            fuerzas[j] -= C * (q[i] * q[j]) / (i - j) ** 2

