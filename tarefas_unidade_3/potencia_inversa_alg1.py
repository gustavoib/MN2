import numpy as np
from auxiliares import inverter_matriz
from potencia_regular import potencia_regular as pr

def potencia_inversa1(A, v0, epsilon):
    #step 1
    A_inv = np.linalg.inv(A)
    #step 2
    lambda_dominante, x_dominante = pr(A_inv, v0, epsilon)
    #step 3
    lambda_n = 1/lambda_dominante
    #step 4
    x_n = x_dominante

    #step 5
    return lambda_n, x_n

resultado = potencia_inversa1(np.array([[2, 1], [1, 2]]), np.array([1, 1]), 0.0001)
print(resultado)
    
    