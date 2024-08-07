import numpy as np
from potencia_regular import potencia_regular

def potencia_inversa1(A, v0, epsilon):
    #step 1
    A_inv = np.linalg.inv(A)
    #step 2
    lambda_dominante, x_dominante = potencia_regular(A_inv, v0, epsilon)
    #step 3
    lambda_n = 1/lambda_dominante
    #step 4
    x_n = x_dominante

    #step 5
    return lambda_n, x_n