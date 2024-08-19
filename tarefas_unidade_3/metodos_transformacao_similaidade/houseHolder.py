import numpy as np
import math
from auxiliares import normaliza
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

if __name__ == "__main__":
    A = np.array([[40, 8,  4,  2,  1],
                  [8,  30, 12, 6,  2],
                  [4,  12, 20, 1,  2],
                  [2,  6,  1,  25, 4],
                  [1,  2,  2,  4,  5]], dtype=float)
    A_barra, H = houseHolder(A)
    print(A_barra)
    print(H)


