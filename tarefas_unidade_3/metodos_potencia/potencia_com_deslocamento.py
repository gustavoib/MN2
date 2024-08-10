import numpy as np
from potencia_inversa import potencia_inversa1

def potencia_com_deslocamento(A, v0, epsilon, mu):
    #step 1
    A_deslocada = A - mu*np.identity(len(A))
    #step 2
    lambda_chapeu, x_chapeu = potencia_inversa1(A_deslocada, v0, epsilon)
    #step 3
    lambdai = lambda_chapeu + mu
    #step 4
    xi = x_chapeu
    
    return lambdai, xi

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

# usado para ambas as matrizes A1 e A2
v0 = np.array([1, 1, 1])
# usado para a matriz A3
v1 = np.array([1, 1, 1, 1, 1])

# mu
mu = 1

resultado = potencia_com_deslocamento(A3, v1, 0.0001, mu)

print(f"Autovalor dominante: {resultado[0]}\nAutovetor associado: {resultado[1]}")