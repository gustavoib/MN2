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
        lambda_1_novo = np.transpose(vk_velho_normalizado).dot(vk_novo)
        #step 10
        if abs((lambda_1_novo - lambda_1_velho)/lambda_1_novo) <= epsilon:
            break
    
    #step 11
    lambda_n = 1/lambda_1_novo
    #step 12
    x_n = vk_velho_normalizado

    #step 5
    return lambda_n, x_n

#matrizes A1 e A2 e A3 e vetores de chute correspondentes para a tarefa 12
A1 = np.array([
    [5, 2, 1], 
    [2, 3, 1],
    [1, 1, 2]
])

A2 = np.array([
    [-14, 1, -2], 
    [1, -1, 1], 
    [-2, 1, -11]
])

A3 = np.array([
    [40, 8, 4, 2, 1],
    [8, 30, 12, 6, 2],
    [4, 12, 20, 1, 2],
    [2, 6, 1, 25, 4],
    [1, 2, 2, 4, 5]
])