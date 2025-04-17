import os
import random

# Se generan sets de datos para el problema 1, d & c calculo de fuerza de coulumb

CARPETA_CASOS = "casos_problema_2"
SEMILLA = 50
MAX_DISTANCIA = 7  # máxima distancia entre estaciones permitida
MIN_DISTANCIA = 1
random.seed(SEMILLA)


def guardar_caso(nombre, distancias):
    if not os.path.exists(CARPETA_CASOS):
        os.makedirs(CARPETA_CASOS)
    path = os.path.join(CARPETA_CASOS, f"{nombre}.txt")
    with open(path, 'w') as f:
        f.write(";".join(map(str, distancias)))
    print(f"Caso guardado: {path}")

def generar_caso_random(n):
    return [random.randint(MIN_DISTANCIA, MAX_DISTANCIA) for _ in range(n)]

def generar_casos():
    for n in [10000, 20000, 40000, 60000, 80000, 100000]:
        guardar_caso(f"{n}_random", generar_caso_random(n))

if __name__ == "__main__":
    generar_casos()