# 3)

'''
Una suma encadenada es una secuencia de números a0, a1, ..., an tal que a0=1 y para cada
k>0: ak=ai+aj para algún i, j, k. Por ejemplo, 1, 2, 3, 6 es una suma encadenada para 6 de
longitud 3 ya que:
● 2=1+1
● 3=2+1
● 6=3+3
Desarrollar un algoritmo de Backtracking para calcular una suma encadenada de longitud
mínima para un entero positivo n
'''



'''SOLUCION LENTA'''

# exponencial btw
def suma_encadenada_greedy(n):
    secuencia = [1]  # La secuencia siempre comienza con 1

    while secuencia[-1] < n:
        # Busca la mayor suma posible dentro de la secuencia actual sin pasarse n
        mayor_suma = 0
        for i in range(len(secuencia)):
            for j in range(i, len(secuencia)):           # desde i porque debo sumar algo mayor
                suma = secuencia[i] + secuencia[j]
                if suma <= n and suma > mayor_suma:
                    mayor_suma = suma

        # Agrega la mayor suma encontrada a la secuencia
        secuencia.append(mayor_suma)

    return len(secuencia)
     

# soluciones[-1] será la mejor suma encadenada hasta ahora
def suma_encadenada(n):
    cota_greedy = suma_encadenada_greedy(n)
    soluciones = []
    secuencia = [1, 2]

    calcular_secuencia(n, secuencia, cota_greedy, soluciones)      
    return soluciones[-1]

def calcular_secuencia(n, secuencia, cota_superior, soluciones):
    if len(secuencia) > cota_superior:
        return
    if soluciones and len(secuencia) >= len(soluciones[-1]):
        return
    if secuencia[-1] == n:
        soluciones.append(secuencia[:])
        return True

    for i in range(len(secuencia) - 1, -1, -1):
        for j in range(i, -1, -1):
            nueva_suma = secuencia[i] + secuencia[j]
            if nueva_suma > n or nueva_suma in secuencia:
                continue

            secuencia.append(nueva_suma)
            if calcular_secuencia(n, secuencia, cota_superior, soluciones):
                return True
            secuencia.pop()


print(suma_encadenada(7000))


#####################################################################################################################################################################################################################



'''SOLUCION TODAS LAS SOLUCIONES'''



def calcular_secuencia(n, secuencia, cota_superior, soluciones):
    if len(secuencia) > cota_superior:  # poda por longitud
        return
    
    if secuencia[-1] == n:
        soluciones.append(secuencia[:])  # Guardamos la solución
        return

    if soluciones and len(secuencia) >= len(soluciones[-1]):
        return
    
    max_valor = secuencia[-1]
    restantes = cota_superior - len(secuencia)
    max_alcanzable = max_valor * (2 ** restantes)  # en el mejor de los casos duplicás en cada paso
    if max_alcanzable < n:
        return

    for i in range(len(secuencia) - 1, len(secuencia) - 2, -1):
        for j in range(i, -1, -1):
            nueva_suma = secuencia[i] + secuencia[j]
            if nueva_suma > n or nueva_suma in secuencia or nueva_suma < secuencia[-1]:
                continue  

            secuencia.append(nueva_suma)
            calcular_secuencia(n, secuencia, cota_superior, soluciones)
            secuencia.pop()  # backtracking


########################################################################################################################################################################################################


'''SOLUCION COMPLETA'''


def suma_encadenada_greedy(n):
    secuencia = [1]  

    while secuencia[-1] < n:
    
        mayor_suma = 0
        for i in range(len(secuencia)):
            for j in range(i, len(secuencia)):           # desde i porque debo sumar algo mayor
                suma = secuencia[i] + secuencia[j]
                if suma <= n and suma > mayor_suma:
                    mayor_suma = suma

        secuencia.append(mayor_suma)

    return len(secuencia)
     

# soluciones[-1] será la mejor suma encadenada hasta ahora
def suma_encadenada(n):
    cota_greedy = suma_encadenada_greedy(n)
    soluciones = []

    # modo rápido 
    secuencia = [1, 2]
    calcular_secuencia(n, secuencia, cota_greedy, soluciones, modo_amplio=False)

    # si no encontró nada modo amplio
    if not soluciones:
        secuencia = [1]
        calcular_secuencia(n, secuencia, cota_greedy, soluciones, modo_amplio=True)

    return soluciones[-1] if soluciones else []



def calcular_secuencia(n, secuencia, cota_superior, soluciones, modo_amplio):
    if len(secuencia) > cota_superior:
        return

    if secuencia[-1] == n:
        if not soluciones or len(secuencia) < len(soluciones[0]):
            soluciones.clear()
            soluciones.append(secuencia[:])
        return

    if soluciones and len(secuencia) >= len(soluciones[0]):
        return

    # Poda: máximo alcanzable desde esta rama
    max_valor = secuencia[-1]
    restantes = cota_superior - len(secuencia)
    max_alcanzable = max_valor * (2 ** restantes)
    if max_alcanzable < n:
        return

    if modo_amplio:
        # considerar todas las sumas posibles ai + aj
        posibles_sumas = set()
        for i in range(len(secuencia)):
            for j in range(i, len(secuencia)):
                suma = secuencia[i] + secuencia[j]
                if suma > secuencia[-1] and suma <= n:
                    posibles_sumas.add(suma)
    else:
        # solo sumar los últimos dos (más rápido pero menos completo)
        if len(secuencia) >= 2:
            a = secuencia[-1]
            b = secuencia[-2]
            posibles_sumas = [a + a, a + b, b + b]
        else:
            a = secuencia[-1]
            posibles_sumas = [a + a]

    for nueva_suma in sorted(posibles_sumas):
        if nueva_suma in secuencia:
            continue
        secuencia.append(nueva_suma)
        calcular_secuencia(n, secuencia, cota_superior, soluciones, modo_amplio)
        secuencia.pop()


print(suma_encadenada(733))

