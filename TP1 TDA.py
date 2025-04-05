# TP1:


# 1) Fj: Fuerza neta ejercida sobre la partícula j. Las cargas de las partículas pueden ser positivas o negativas (es decir, que la partícula vecina tire si tienen cargas distintas
# o empuje si tienen la misma)

'''
Tenemos una serie de n partículas cargadas muy pequeñas, ubicadas a intervalos regulares
a lo largo de una línea recta en las ubicaciones {1, 2, ..., n}. En cada uno de estos puntos,
tenemos una partícula cargada qj, que puede ser positiva o negativa. Queremos estudiar la
fuerza total sobre cada partícula mediante la Ley de Coulomb:

Desarrollar un algoritmo que calcule Fj mediante División y Conquista.
'''


def coulomb():
    pass


########################################################################################################################################################################################################



# 2)

'''Juan Curuchet tiene planeando un rally por el Camino de las Altas Cumbres. Puede llevar
dos litros de agua y rodar 7 kilómetros antes de que se le agote. Tiene un mapa con lugares
donde puede repostar agua, y conoce la distancia entre cada uno. El objetivo de Juan es
detenerse la menor cantidad de veces que sea posible. Desarrollar un algoritmo Greedy que
determine en qué lugares detenerse a cargar agua, y mostrar si siempre encuentra el
óptimo o no'''

# No es como el ejercicio de las patrullas. Es simplemente que cargue en el lugar mas lejano antes de superar el alcance y ya


# asumiendo mapa = [km del camino donde se encuentra cada lugar]
# asumiendo que nunca existirán paradas con más de 7km de distancia entre sí

def camino_cumbres(mapa):
    alcance = 7

    if len(mapa) == 0:
        return []
    if len(mapa) == 1:
        return [mapa[0]] if mapa[0] <= alcance else []    
    
    paradas = []
    ultima_parada = 0
    mapa.sort()

    for i in range(len(mapa) - 1):
        if mapa[i + 1] - ultima_parada > alcance:
            paradas.append(mapa[i])
            ultima_parada = mapa[i]

    # caso última parada
    if mapa[-1] - ultima_parada > alcance:
            paradas.append(mapa[i])
            ultima_parada = mapa[i]

    return paradas


# Complejidad:
    # Sort: O(n log n)
    # Recorrer el mapa: O(n)
    # O(n log n)

# ¿Siempre encuentra el óptimo? Sí, siempre se prioriza avanzar lo máximo antes de repostar, por ende va a ser óptimo para cualquier caso


########################################################################################################################################################################################################



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
        return
    
    if len(secuencia) >= cota_superior:      # poda
        return               
    
    for i in range(len(secuencia) - 1, -1, -1):
        for j in range(i, -1, -1):
            nueva_suma = secuencia[i] + secuencia[j] 
            if nueva_suma > n or nueva_suma in secuencia:            # si no es valido
                continue              # pruebo con un valor de j más pequeño

            secuencia.append(nueva_suma)
            calcular_secuencia(n, secuencia, cota_superior, soluciones)
            secuencia.pop()          # backtracking
     


[1, 2, 4, 8, 16, 32]
     