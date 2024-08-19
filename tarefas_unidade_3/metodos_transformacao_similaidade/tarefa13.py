import tarefas_unidade_3.metodos_transformacao_similaidade.houseHolder as hh
import metodos_potencia.potencia_regular as pr
import numpy as np

def main():
    A = np.array([[40, 8, 4, 2, 1], 
                  [8, 30, 12, 6, 2], 
                  [4, 12, 20, 1, 2], 
                  [2, 6, 1, 25, 4], 
                  [1, 2, 2, 4, 5]])
    
    # 1) Implemente o método de Householder e aplique-o sobre A para encontrar
        # i. a matriz tridiagonal A_barra
        # ii. a matriz acumulada H = H1.H2.H3.H4...
    A_barra, H = hh.houseHolder(A)

    # 2) Use os métodos da potência para encontrar os autovalores e autovetores da matriz A_barra.
    autovalor_de_A_barra, autovetor_de_A_barra = pr.potencia_regular(A_barra, np.ones(5), 1e-6)

    # 4) Usando a matriz H e os autovetores da matriz A_barra encontre os autovetores da matriz A.
    autovetor_de_A = H.dot(autovetor_de_A_barra)

    # 5) Imprima os autovalores e autovetores de A.
    print(f"Autovalor de A: {autovalor_de_A_barra}")
    print(f"Autovetor normalizado de A relacionado a {autovalor_de_A_barra}:")
    print(autovetor_de_A)

main()

