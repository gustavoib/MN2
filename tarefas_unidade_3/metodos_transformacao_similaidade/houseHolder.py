import numpy as np
import math
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'metodos_potencia')))
from metodos_potencia.auxiliares import normaliza
from metodos_potencia.potencia_regular import potencia_regular
import tabelas as tb

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
    A1 = np.array([[40, 8,  4,  2,  1],
                   [8,  30, 12, 6,  2],
                   [4,  12, 20, 1,  2],
                   [2,  6,  1,  25, 4],
                   [1,  2,  2,  4,  5]])
    
    A2 = np.array([[5, 2, 1], 
                   [2, 3, 1],
                   [1, 1, 2]])
    
    A = A1
    
    tb.print_matrix(A, "Matriz A", 0)
    
    # 1) Implemente o método de Householder e aplique-o sobre A para encontrar
        # i. a matriz tridiagonal A_barra
        # ii. a matriz acumulada H = H1.H2.H3.H4...
    A_barra, H = houseHolder(A)
    tb.print_matrix(A_barra, "A_barra", 5)
    tb.print_matrix(H, "H")

    # 2) Use os métodos da potência para encontrar os autovalores e autovetores da matriz A_barra.
    autovalor_de_A_barra, autovetor_de_A_barra = potencia_regular(A_barra, np.ones(len(A)), 1e-6)
    tb.print_matrix([autovetor_de_A_barra], f"Autovalor de A_barra: {autovalor_de_A_barra:.5f} | Autovetor:", 5)

    # 3) Usando a matriz H e os autovetores da matriz A_barra encontre os autovetores da matriz A.
    autovetor_de_A = H.dot(autovetor_de_A_barra)

    # 4) Encontre os autovalores da matriz A.
    autovalor_de_A = autovalor_de_A_barra

    tb.print_matrix([autovetor_de_A], f"Autovalor de A: {autovalor_de_A:.5f} | Autovetor:", 5)

if __name__ == "__main__":
    main()


