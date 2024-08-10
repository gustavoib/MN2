from potencia_regular import potencia_regular
from potencia_inversa import potencia_inversa2
from potencia_com_deslocamento import potencia_com_deslocamento
import numpy as np

def menu():
    print("Escolha o método de cálculo para os autovalores e autovetores:")
    print("1 - Potência Regular")
    print("2 - Potência Inversa")
    print("3 - Potência com Deslocamento")

    opcao = int(input("Opção: "))
    return opcao

A = np.array([[5, 2, 1], [2, 3, 1], [1, 1, 2]])
v0 = np.array([1, 1, 1])
epsilon = 0.0001

opcao = menu()

while opcao != 0:
    if opcao == 1:
        lambda1, x1 = potencia_regular(A, v0, epsilon)
        print("MÉTODO DA POTÊNCIA REGULAR")
        print("Autovalor: ", lambda1)
        print("Autovetor: ", x1)
        print("\n")
    elif opcao == 2:
        lambda2, x2 = potencia_inversa2(A, v0, epsilon)
        print("MÉTODO DA POTÊNCIA INVERSA\n")
        print("Autovalor: ", lambda2)
        print("Autovetor: ", x2)
        print("\n")
    elif opcao == 3:
        mu = 1
        lambdai, xi = potencia_com_deslocamento(A, v0, epsilon, mu)
        print("MÉTODO DA POTÊNCIA COM DESLOCAMENTO")
        print("Autovalor: ", lambdai)
        print("Autovetor: ", xi)
        print("\n")
    else:
        print("Opção inválida")
    
    opcao = menu()
    