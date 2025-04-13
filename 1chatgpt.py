def calcular_fuerzas(q, c=0.3):
    def divide_conquista(q, left, right):
        if left == right:
            return [0]  # fuerza de una sola partícula es 0

        mid = (left + right) // 2

        # Fuerzas internas en cada mitad
        F_izq = divide_conquista(q, left, mid)
        F_der = divide_conquista(q, mid + 1, right)

        # Fuerzas cruzadas: izquierda → derecha y derecha → izquierda
        F_cruzadas_izq = [0] * (mid - left + 1)
        F_cruzadas_der = [0] * (right - mid)

        for i in range(left, mid + 1):
            for j in range(mid + 1, right + 1):
                d = j - i
                fuerza = c * (q[i] * q[j]) / (d * d)
                # Fuerza sobre i por j (izquierda ← derecha)
                F_cruzadas_izq[i - left] += -fuerza  # dirección opuesta
                # Fuerza sobre j por i (derecha ← izquierda)
                F_cruzadas_der[j - (mid + 1)] += fuerza

        # Combinar resultados
        F_total = (
            [F_izq[i] + F_cruzadas_izq[i] for i in range(len(F_izq))] +
            [F_der[i] + F_cruzadas_der[i] for i in range(len(F_der))]
        )

        return F_total

    return divide_conquista(q, 0, len(q) - 1)

# Ejemplo: 4 partículas con cargas [+1, -1, +2, -2]
q = [1, -1]
fuerzas = calcular_fuerzas(q)
print(fuerzas)