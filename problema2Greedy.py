'''Juan Curuchet tiene planeando un rally por el Camino de las Altas Cumbres. Puede llevar
dos litros de agua y rodar 7 kilómetros antes de que se le agote. Tiene un mapa con lugares
donde puede repostar agua, y conoce la distancia entre cada uno. El objetivo de Juan es
detenerse la menor cantidad de veces que sea posible. Desarrollar un algoritmo Greedy que
determine en qué lugares detenerse a cargar agua, y mostrar si siempre encuentra el
óptimo o no'''
# suponemos que entre estación y estación no hay mas de 7km
# si supera, rompe, consultar al profe

def carga_agua(distancias_estaciones, autonomia):
    km_actual = 0
    tanque = 0
    estaciones_convenientes = []
    i = 0
    distancia = distancias_estaciones[i] 
    while i < len(distancias_estaciones):
        distancia = distancias_estaciones[i]
        if distancia > autonomia:
            raise ValueError(f"La distancia entre estaciones ({distancia} km) excede la autonomía ({autonomia} km).")
        if tanque < distancia:
            estaciones_convenientes.append(km_actual)
            tanque = autonomia
        tanque -= distancia
        km_actual += distancia
        i += 1
    return estaciones_convenientes

# Sets de datos para probar codigo
distancias1 = [5, 3, 3, 4, 7, 2, 3, 4]
distancias2 = [5, 3, 2]
distancias3 = [5, 3, 3, 4, 7, 2, 3, 4, 6, 3, 6, 4, 4, 2, 7, 7, 3, 5]
#set de datos para corroborar la excepción
# distancias4 = [5, 3, 3, 4, 8, 2, 3, 4]

print(carga_agua(distancias1, 7))
print(carga_agua(distancias2, 7))
print(carga_agua(distancias3, 7))
#print(carga_agua(distancias4, 7))
# complejidad O(n)
# La complejidad óptima para este tipo de problema es O(n).
# este algoritmo greedy sí encuentra el óptimo para este problema porque cumple con la propiedad del subproblema óptimo