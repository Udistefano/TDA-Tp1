def carga_combustible(distancias_estaciones, K=7):
    km_actual = 0
    tanque = 0
    estaciones_convenientes = []
    i = 0
    distancia = distancias_estaciones[i] 
    while i < len(distancias_estaciones):
        distancia = distancias_estaciones[i]
        if tanque < distancia:
            estaciones_convenientes.append(km_actual)
            tanque = K
        else:
            tanque -= distancia
            km_actual += distancia
            i += 1
    return estaciones_convenientes