import numpy as np
from auxiliares import normaliza

def potencia_regular(A, v0, epsilon):
    #step2
    lambda_novo = 0
    #step3
    vk_novo = v0.copy()
    while True:
        #step4
        lambda_velho = lambda_novo
        #step5
        vk_velho = vk_novo
        #step6
        vk_velho_normalizado = normaliza(vk_velho)
        #step7
        vk_novo = np.dot(A, vk_velho_normalizado)
        #step8
        lambda_novo = np.transpose(vk_velho_normalizado).dot(vk_novo)
        
        #step9 - verificar convergência de lambda_novo
        if abs((lambda_novo - lambda_velho)/lambda_novo) <= epsilon:
            return lambda_novo, vk_velho_normalizado
        
# matrizes A1 e A2 e vetores chutes correspondentes para a tarefa 11
A1 = np.array([
    [5, 2, 1], 
    [2, 3, 1],
    [1, 1, 2]
])

A2 = np.array([
    [40, 8, 4, 2, 1],
    [8, 30, 12, 6, 2],
    [4, 12, 20, 1, 2],
    [2, 6, 1, 25, 4],
    [1, 2, 2, 4, 5]
])

# usada para a matriz A1
v0 = np.array([1, 1, 1])
# usada para a matriz A2
v1 = np.array([1, 1, 1, 1, 1])     

resultado = potencia_regular(A2, v1, 0.0001) 
print(f"Autovalor dominante: {resultado[0]}\nAutovetor associado: {resultado[1]}")