import numpy as np
from auxiliares import normaliza

def potencia_regular(A, v0, epsilon):
    #STEP 2 - inicia o autovalor lambda1
    lambda_novo = 0
    #STEP 3 - copia o vetor v0 para vk_novo
    vk_novo = v0.copy()
    while True:
        #STEP 4 - copiar lambda1 para lambda0
        lambda_velho = lambda_novo
        #STEP 5 - copiar vk_novo para vk_velho
        vk_velho = vk_novo
        #STEP 6 - normalizar vk_velho
        vk_velho_normalizado = normaliza(vk_velho)
        #STEP 7 - calcular vk_novo
        vk_novo = np.dot(A, vk_velho_normalizado)
        #STEP 8 - calcular lambda_novo
        lambda_novo = np.transpose(vk_velho_normalizado).dot(vk_novo)
        
        #STEP 9 - verificar convergência de lambda_novo
        if abs((lambda_novo - lambda_velho)/lambda_novo) <= epsilon:
            return lambda_novo, vk_velho_normalizado
        
resultado = potencia_regular(np.array([[2, 1], [1, 2]]), np.array([1, 1]), 0.0001)
print(resultado)