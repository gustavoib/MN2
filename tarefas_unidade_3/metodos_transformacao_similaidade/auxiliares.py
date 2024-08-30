import math
import numpy as np

def normaliza(v):
    v_transposto = np.transpose(v)
    v_normalizado = v/math.sqrt(np.dot(v_transposto, v))
    return v_normalizado

def calculaLU(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            soma = 0
            for k in range(i):
                soma += L[i][k]*U[k][j]
            U[i][j] = A[i][j] - soma
        for j in range(i, n):
            if i == j:
                L[i][i] = 1
            else:
                soma = 0
                for k in range(i):
                    soma += L[j][k]*U[k][i]
                L[j][i] = (A[j][i] - soma)/U[i][i]
    return L, U

def solverLU(L, U, b):
    n = len(L)
    y = np.zeros(n)
    x = np.zeros(n)
    for i in range(n):
        soma = 0
        for j in range(i):
            soma += L[i][j]*y[j]
        y[i] = b[i] - soma
    for i in range(n-1, -1, -1):
        soma = 0
        for j in range(i+1, n):
            soma += U[i][j]*x[j]
        x[i] = (y[i] - soma)/U[i][i]
    return x
    
v = np.array([8.96738, 7.44911, 4.4302, 2.91429, 1])