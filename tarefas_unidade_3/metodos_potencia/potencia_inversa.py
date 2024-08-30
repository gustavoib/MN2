import numpy as np
from potencia_regular import potencia_regular
from auxiliares import calculaLU, solverLU, normaliza

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

def potencia_inversa2(A, v0, epsilon):
    #step 2
    L, U = calculaLU(A)
    #step 3
    lambda_1_novo = 0
    #step 4
    vk_novo = v0.copy()
    
    while True:
        #step 5
        lambda_1_velho = lambda_1_novo
        #step 6
        vk_velho = vk_novo
        #step 7
        vk_velho_normalizado = normaliza(vk_velho)
        #step 8
        vk_novo = solverLU(L, U, vk_velho_normalizado)
        #step 9
        lambda_1_novo = vk_velho_normalizado.dot(vk_novo)
        #step 10
        if abs((lambda_1_novo - lambda_1_velho)/lambda_1_novo) <= epsilon:
            break
    
    #step 11
    lambda_n = 1/lambda_1_novo
    #step 12
    x_n = vk_velho_normalizado

    #step 5
    return lambda_n, x_n