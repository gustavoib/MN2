from potencia_regular import potencia_regular
from potencia_inversa_alg1 import potencia_inversa1
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

mu = 1
if opcao == 1:
    resultado = potencia_regular(A, v0, epsilon)
    print("Autovalor: ", resultado[0], "Autovetor: ", resultado[1])
    menu()
elif opcao == 2:
    resultado = potencia_inversa1(A, v0, epsilon)
    print("Autovalor: ", resultado[0], "Autovetor: ", resultado[1])
    menu()
elif opcao == 3:
    resultado = potencia_com_deslocamento(A, v0, epsilon, mu)
    print("Autovalor: ", resultado[0], "Autovetor: ", resultado[1])
    menu()
    