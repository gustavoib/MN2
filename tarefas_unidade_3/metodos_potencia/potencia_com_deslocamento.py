import numpy as np
from potencia_inversa import potencia_inversa2

def potencia_com_deslocamento(A, v0, epsilon, mu):
    #step 1
    A_deslocada = A - mu*np.identity(len(A))
    #step 2
    lambda_chapeu, x_chapeu = potencia_inversa2(A_deslocada, v0, epsilon)
    #step 3
    lambdai = lambda_chapeu + mu
    #step 4
    xi = x_chapeu
    
    return lambdai, xi