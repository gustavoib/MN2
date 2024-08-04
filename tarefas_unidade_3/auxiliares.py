import math
import numpy as np

def normaliza(v):
    v_transposto = np.transpose(v)
    v_normalizado = v/math.sqrt(np.dot(v_transposto, v))
    return v_normalizado

def criar_identidade(n):
    identidade = np.zeros((n, n))
    for i in range(n):
        identidade[i][i] = 1
    return identidade
    
def inverter_matriz(A):
    n = len(A)
    inversa = [[0 for i in range(n)] for j in range(n)]
    
    inversa = criar_identidade(n)
    
    for i in range(n):
        for j in range(n):
            if i != j:
                ratio = A[j][i]/A[i][i]
                for k in range(n):
                    A[j][k] = A[j][k] - ratio * A[i][k]
                    inversa[j][k] = inversa[j][k] - ratio * inversa[i][k]
    for i in range(n):
        a = A[i][i]
        for j in range(n):
            A[i][j] = A[i][j]/a
            inversa[i][j] = inversa[i][j]/a
    return inversa

print(inverter_matriz(np.array([[2, 1], [1, 2]])))