import os
import time
import csv

from problema1 import calcular_fuerzas  # Asegurate de tener esta función implementada

CARPETA_CASOS = "casos_problema_1"
CARPETA_RESULTADOS = os.path.join(CARPETA_CASOS, "resultados")
ARCHIVO_TIEMPOS = os.path.join(CARPETA_CASOS, "tiempos_problema_1.csv")
C = 1  # elegimos uno para simplificar los resultados


if not os.path.exists(CARPETA_RESULTADOS):
    os.makedirs(CARPETA_RESULTADOS)

def leer_caso(path):
    with open(path, 'r') as f:
        linea = f.readline()
        return list(map(int, linea.strip().split(";")))

def guardar_resultado(nombre, fuerzas):
    path = os.path.join(CARPETA_RESULTADOS, f"{nombre}.txt")
    with open(path, 'w') as f:
        f.write(";".join(map(str, fuerzas)))

def main():
    tiempos = []
    for archivo in sorted(os.listdir(CARPETA_CASOS)):
        if not archivo.endswith(".txt"):
            continue
        nombre = archivo[:-4]
        path = os.path.join(CARPETA_CASOS, archivo)
        print(f"Procesando: {nombre}")

        q = leer_caso(path)
        inicio = time.time()
        fuerzas = calcular_fuerzas(q, C)
        fin = time.time()

        duracion = fin - inicio
        tiempos.append((nombre, len(q), duracion))
        guardar_resultado(nombre, fuerzas)
        print(f"Tiempo: {duracion:.4f} segundos")

    # Guardar los tiempos
    with open(ARCHIVO_TIEMPOS, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Caso", "Tamaño", "Tiempo"])
        writer.writerows(tiempos)

if __name__ == "__main__":
    main()
