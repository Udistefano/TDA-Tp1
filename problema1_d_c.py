# Tenemos una serie de n partículas cargadas muy pequeñas, ubicadas a intervalos regulares
# a lo largo de una línea recta en las ubicaciones {1, 2, ..., n}. En cada uno de estos puntos,
# tenemos una partícula cargada qj, que puede ser positiva o negativa. Queremos estudiar la
# fuerza total sobre cada partícula mediante la Ley de Coulomb:
# ponele que la fuerza sobre una particula está definida como: (c es una cte) e i representa a otra particula sobre la recta
# Fj = sumatoria para i < j C * q_i* q_j / (j-i)^2 -  sumatoria para i > j C * q_i* q_j / (j-i)^2
# Desarrollar un algoritmo que calcule Fj mediante División y Conquista.

# siendo particulas: un arreglo con la carga de las particulas
# C: cte
def calcular_fuerzas_coulomb(particulas, c=0.3):
    n = len(particulas)
    fuerzas = [0.0] * n
    inicio = 0
    fin = n -1
    _calcular_fuerzas_coulomb(inicio, fin, particulas, fuerzas, c)
    return fuerzas

def _calcular_fuerzas_coulomb(inicio, fin, particulas, fuerzas, c):
    if inicio >=  fin:
        return 
    
    medio = (inicio + fin) // 2

    _calcular_fuerzas_coulomb(inicio, medio, particulas, fuerzas, c)
    _calcular_fuerzas_coulomb(medio + 1, fin, particulas, fuerzas, c)

    for j in range(inicio, medio +1): # siempre va a pasar que j sea menor a i!!! e i siempre mayor conlo que
        for i in range(medio+1, fin+1):
            distancia = i - j
            fuerza = c * particulas[j] * particulas[i] / (distancia ** 2)
            
            fuerzas[j] -= fuerza

            fuerzas[i] += fuerza # fuerza sobre i desde j (j < i)


print(calcular_fuerzas_coulomb([1, -1]))