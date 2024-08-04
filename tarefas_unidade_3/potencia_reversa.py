import numpy as np
from auxiliares import normaliza, inverter_matriz

def potencia_inversa1(A, v0, epsilon):
    #receber a matriz inversa de A
    A_inv = inverter_matriz(A)
    
    
    