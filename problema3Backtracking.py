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

# Con la lista de secuencia actual, yo solo puedo usar sumas de números de la secuencia actual que tengo armada. ¿Me conviene usar siempre la mayor suma de la secuencia actual sin pasarme de n?

def suma_encadenada_NOGREEDY(n):
    secuencia = [1, 2]           # lista vacia con el 1 y el 2
    n_es_impar = (n % 2 != 0)
    if n_es_impar:
        secuencia.append(3)
        
    while secuencia[-1] < n:
        nueva_suma = secuencia[-1] + secuencia[-1]

        if nueva_suma > n:
            encontrado = False

            for i in range(len(secuencia) - 1, -1, -2):        # en reversa, de 2 en 2
                for j in range(i, -1, -2):
                    suma_alternativa = secuencia[i] + secuencia[j]

                    if suma_alternativa <= n and suma_alternativa not in secuencia:                       
                        secuencia.append(suma_alternativa)
                        encontrado = True
                        break                          # salgo del for j

                if encontrado:               # salgo del for i
                    break
            
        else: secuencia.append(nueva_suma)
    
    return len(secuencia)


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

    n_es_impar = (n % 2 != 0)
    if n_es_impar:
        secuencia.append(3)

    calcular_secuencia(n, secuencia, cota_greedy, soluciones)      
    return soluciones[-1]


def calcular_secuencia(n, secuencia, cota_superior, soluciones):
    if secuencia[-1] == n:
        if len(soluciones) == 0 or len(secuencia) < len(soluciones[-1]):
            soluciones.append(secuencia[:])
        return soluciones
    
    if len(secuencia) >= cota_superior:      # poda
        return               
    
    for i in range(len(secuencia) - 1, -1, -1):
        for j in range(i, -1, -1):
            nueva_suma = secuencia[i] + secuencia[j] 
            if nueva_suma > n or nueva_suma in secuencia:            # si no es valido
                continue              # pruebo con un valor de j más pequeño

            secuencia.append(nueva_suma)
            calcular_secuencia(n, secuencia, cota_superior, soluciones)
            # backtracking
     

print(suma_encadenada(4001))
#[1, 2, 4, 8, 16, 32]
