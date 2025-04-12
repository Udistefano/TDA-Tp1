# Una suma encadenada es una secuencia de números a0
# , a1
# , ..., al tal que a0=1 y para cada
# k>0: ak=ai+aj para algún i, j, k < l. Por ejemplo, 1, 2, 3, 6 es una suma encadenada para n=6
# de longitud l=3 ya que:
# ● 2=1+1
# ● 3=2+1
# ● 6=3+3
# Desarrollar un algoritmo de Backtracking para calcular una suma encadenada de longitud
# mínima para un entero positivo n

def suma_encadenada(n):
    solucion_parcial = []
    solucion_optima = []
    i = 1
    if _suma_encadenada(n, solucion_parcial, solucion_optima, i):
        return solucion_optima
    return None

def _suma_encadenada(n, solucion_parcial, solucion_optima, i):
    pass