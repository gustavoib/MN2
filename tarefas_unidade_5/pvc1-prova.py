# PVC aplicado a questão da prova

import numpy as np

def esquerdo(delta, r):
    return 1 - delta / (2*r)

def centro(delta, r):
    return -2

def direito(delta, r):
    return 1 + delta / (2*r)
def pvc(n):

    delta = 0.3 / n
  
    A = np.zeros((n, n))

    pontos = np.linspace(0.2, 0.5, n+1)
    i = 0
    for r_i in pontos:
        if i > 0:
            A[i, i-1] = esquerdo(delta, r_i)

        A[i, i] = centro(delta,r_i)

        if i < n-1:
            A[i, i+1] = direito(delta,r_i)
        i += 1

    print(A)

    b = [4] * n

    solucao = np.linalg.solve(A, b)
    return solucao

n = 3
pontos = np.linspace(0.2, 0.5, n+1)
solucao = pvc(n)
print(f"Pontos: {pontos[1:n]}")
print(f"Solucao: ", solucao)