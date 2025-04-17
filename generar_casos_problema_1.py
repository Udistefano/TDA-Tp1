import os
import random

# Se generan sets de datos para el problema 1, d & c calculo de fuerza de coulumb

CARPETA_CASOS = "casos_problema_1"
SEMILLA = 50
CARGA_MAXIMA = 10
CARGA_MINIMA = 1
random.seed(SEMILLA)

def guardar_caso(nombre, q_values):
    if not os.path.exists(CARPETA_CASOS):
        os.makedirs(CARPETA_CASOS)
    path = os.path.join(CARPETA_CASOS, f"{nombre}.txt")
    with open(path, 'w') as f:
        f.write(";".join(map(str, q_values)))
    print(f"Caso guardado: {path}")

def caso_cargas_aleatorias(n):
    return [random.randint(-CARGA_MAXIMA, CARGA_MAXIMA) for _ in range(n)]

def caso_todas_positivas(n):
    return [random.randint(CARGA_MINIMA, CARGA_MAXIMA) for _ in range(n)]

def caso_todas_negativas(n):
    return [-random.randint(CARGA_MINIMA, CARGA_MAXIMA) for _ in range(n)]

def caso_signos_alternados(n):
    return [(-1)**i * random.randint(CARGA_MINIMA, CARGA_MAXIMA) for i in range(n)]

def caso_cargas_constantes(n):
    valor = random.randint(CARGA_MINIMA, CARGA_MAXIMA)
    return [valor] * n

def generar_casos_para_tamano(n):
    casos = {
        f"{n}_aleatorio": caso_cargas_aleatorias,
        f"{n}_positivas": caso_todas_positivas,
        f"{n}_negativas": caso_todas_negativas,
        f"{n}_alternado": caso_signos_alternados,
        f"{n}_constantes": caso_cargas_constantes
    }
    for nombre, generador in casos.items():
        guardar_caso(nombre, generador(n))

def generar_todos_los_casos():
    for n in [1000, 2000, 4000, 6000, 8000, 10000]:
        generar_casos_para_tamano(n)

if __name__ == "__main__":
    generar_todos_los_casos()
