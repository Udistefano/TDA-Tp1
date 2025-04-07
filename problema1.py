# problema 1:
"""
Tenemos una serie de n partículas cargadas muy pequeñas, ubicadas a intervalos regulares
a lo largo de una línea recta en las ubicaciones {1, 2, ..., n}. En cada uno de estos puntos,
tenemos una partícula cargada qj, que puede ser positiva o negativa. Queremos estudiar la
fuerza total sobre cada partícula mediante la Ley de Coulomb:
Desarrollar un algoritmo que calcule Fj mediante División y Conquista.
"""

def division_y_conquista(lista, izquierda, derecha):

    medio = (izquierda + derecha) // 2
    fuerzas_izquierda = division_y_conquista(lista, izquierda, medio)
    fuerzas_derecha = division_y_conquista(lista, medio, derecha)
    #seguir

    
# esta es sin division y conquista
def calcular_fuerzas(q, C=1):
    n = len(q)
    F = [0.0] * n
    for j in range(n):
        for i in range(n):
            if i == j:
                continue
            fuerza = C * q[i] * q[j] / ((j - i)**2)
            if i < j:
                F[j] += fuerza
            else:
                F[j] -= fuerza
    return F


lista_particulas = [1, -1, 2, -2]
#division_y_conquista(lista_particulas, 0, len(lista_particulas))
print(calcular_fuerzas(lista_particulas))