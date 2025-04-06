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

