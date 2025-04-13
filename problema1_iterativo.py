
def calcular_fuerzas(q, C=0.3):
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
