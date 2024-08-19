import numpy as np
import math
from auxiliares import normaliza
from potencia_regular import potencia_regular

np.set_printoptions(suppress=True)

def houseHolder(A):
    n = A.shape[0]
    H = np.identity(n, dtype=float)
    A_velho = A.copy()
    for i in range(n-2):
        H_i = matriz_householder(A_velho, i)
        A_i = np.transpose(H_i).dot(A_velho).dot(H_i)
        A_velho = A_i
        H = H.dot(H_i)
    
    return A_i, H

def matriz_householder(A, i):
    n = A.shape[0]
    w = np.zeros(n)
    w_linha = np.zeros(n)
    for j in range(i+1, n):
        w[j] = A[j][i]
    l_w = math.sqrt(np.dot(w, w))
    w_linha[i+1] = l_w
    N = np.subtract(w, w_linha)
    N_normalizado = normaliza(N)
    H = np.identity(n) - 2*np.outer(N_normalizado, N_normalizado)
    return H


def main():
    A = np.array([[40, 8, 4, 2, 1], 
                  [8, 30, 12, 6, 2], 
                  [4, 12, 20, 1, 2], 
                  [2, 6, 1, 25, 4], 
                  [1, 2, 2, 4, 5]])
    
    # 1) Implemente o método de Householder e aplique-o sobre A para encontrar
        # i. a matriz tridiagonal A_barra
        # ii. a matriz acumulada H = H1.H2.H3.H4...
    A_barra, H = houseHolder(A)

    # 2) Use os métodos da potência para encontrar os autovalores e autovetores da matriz A_barra.
    autovalor_de_A_barra, autovetor_de_A_barra = potencia_regular(A_barra, np.ones(5), 1e-6)

    # 4) Usando a matriz H e os autovetores da matriz A_barra encontre os autovetores da matriz A.
    autovetor_de_A = H.dot(autovetor_de_A_barra)

    # 5) Imprima os autovalores e autovetores de A.
    print("Autovalor de A:")
    print(f"{autovalor_de_A_barra}")
    print(f"Autovetor normalizado de A relacionado a {autovalor_de_A_barra}:")
    print(autovetor_de_A)

if __name__ == "__main__":
    main()


