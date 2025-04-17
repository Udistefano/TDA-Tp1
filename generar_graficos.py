import matplotlib.pyplot as plt
import csv
import os
from collections import defaultdict

def graficar_ej1(path_csv):
    datos = defaultdict(list)

    with open(path_csv, 'r') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            caso = fila['Caso']
            tamanio = int(fila['Tamaño'])
            tiempo = float(fila['Tiempo'])

            tipo = caso.split('_')[-1]  # aleatorio, constantes, etc.
            datos[tipo].append((tamanio, tiempo))

    fig, ax = plt.subplots(figsize=(10, 5))
    for tipo, valores in datos.items():
        valores.sort()  # ordenar por tamaño
        tamanios = [v[0] for v in valores]
        tiempos = [v[1] for v in valores]
        ax.plot(tamanios, tiempos, marker='o', label=tipo.capitalize())

    ax.set_xlabel('Tamaño')
    ax.set_ylabel('Tiempo (s)')
    ax.set_title('Ejercicio 1 - Tiempo de ejecución por tipo de entrada')
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.legend()
    plt.tight_layout()
    plt.show()


def graficar_ej2(path_csv):
    tamanios = []
    tiempos = []
    datos = []
    with open(path_csv, 'r') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            datos.append((int(fila['Tamaño']),float(fila['Tiempo'])))

    fig, ax = plt.subplots(figsize=(10, 5))
    datos =  sorted(datos, key=lambda x: x[0])
    for tamanio, tiempo in datos:
       tamanios.append(tamanio)
       tiempos.append(tiempo)

    ax.plot(tamanios, tiempos, marker='o', label='Random', color='mediumblue')
    ax.set_xlabel('Tamaño (N)')
    ax.set_ylabel('Tiempo (s)')
    ax.set_title('Ejercicio 2 - Tiempo de ejecución vs Tamaño')
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.legend()
    plt.tight_layout()
    plt.show()


def graficar_ej3(path_csv):
    tamanios = []
    tiempos = []
    datos = []
    with open(path_csv, 'r') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            datos.append((int(fila['n']), fila['Tiempo (s)']))
    
    fig, ax = plt.subplots(figsize=(10, 5))


    datos =  sorted(datos, key=lambda x: x[0])
    for tamanio, tiempo in datos:
       tamanios.append(tamanio)
       tiempos.append(tiempo)
       
    ax.plot(tamanios, tiempos, marker='o', label='Backtracking', color='darkgreen')
    ax.set_xlabel('n')
    ax.set_ylabel('Tiempo (s)')
    ax.set_title('Ejercicio 3 - Tiempo de ejecución (Backtracking)')
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    path_ej1 = os.path.join("casos_problema_1", "tiempos_problema_1.csv")
    path_ej2 = os.path.join("casos_problema_2", "tiempos_problema_2.csv")
    path_ej3 = os.path.join("casos_problema_3", "tiempos_problema_3.csv")

    graficar_ej1(path_ej1)
    graficar_ej2(path_ej2)
    graficar_ej3(path_ej3)
