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
