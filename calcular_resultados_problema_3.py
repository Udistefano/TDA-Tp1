
import os
import time
import csv
# se calculan los resultados y tiempos para el problema 2.

from problema3 import suma_encadenada

CARPETA_CASOS = "casos_problema_3"
CARPETA_RESULTADOS = os.path.join(CARPETA_CASOS, "resultados")
ARCHIVO_TIEMPOS = os.path.join(CARPETA_CASOS, "tiempos_problema_3.csv")



if not os.path.exists(CARPETA_RESULTADOS):
    os.makedirs(CARPETA_RESULTADOS)



def leer_n(path):
    with open(path, 'r') as f:
        return int(f.readline().strip())

def guardar_resultado(nombre, secuencia):
    if not os.path.exists(CARPETA_RESULTADOS):
        os.makedirs(CARPETA_RESULTADOS)
    path = os.path.join(CARPETA_RESULTADOS, f"{nombre}.txt")
    with open(path, 'w') as f:
        f.write(";".join(map(str, secuencia)))

def main():
    tiempos = []

    for archivo in sorted(os.listdir(CARPETA_CASOS)):
        if not archivo.endswith(".txt"):
            continue
        nombre = archivo[:-4]
        path = os.path.join(CARPETA_CASOS, archivo)
        n = leer_n(path)

        print(f"Procesando n={n}")
        inicio = time.time()
        secuencia = suma_encadenada(n)
        fin = time.time()
        duracion = fin - inicio

        guardar_resultado(nombre, secuencia)
        tiempos.append((nombre, n, len(secuencia), duracion))
        print(f"Resultado: {secuencia} | Largo: {len(secuencia)} | Tiempo: {duracion:.4f}s")

    with open(ARCHIVO_TIEMPOS, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Caso", "n", "Longitud Secuencia", "Tiempo (s)"])
        writer.writerows(tiempos)

if __name__ == "__main__":
    main()