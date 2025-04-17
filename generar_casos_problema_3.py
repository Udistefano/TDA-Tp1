import os


# Se generan sets de datos para el problema 3

CARPETA_CASOS = "casos_problema_3"
CASO_MIN = 50
CASO_MAX = 10000
PASO = 1000
def guardar_caso(nombre, n):
    if not os.path.exists(CARPETA_CASOS):
        os.makedirs(CARPETA_CASOS)
    path = os.path.join(CARPETA_CASOS, f"{nombre}.txt")
    with open(path, 'w') as f:
        f.write(str(n))

def generar_casos():
    
    for n in range(CASO_MIN, CASO_MAX+PASO, PASO):
        guardar_caso(f"{n}", n)

if __name__ == "__main__":
    generar_casos()
