import numpy as np
from potencia_regular import potencia_regular   
from potencia_inversa import potencia_inversa2
from potencia_com_deslocamento import potencia_com_deslocamento

# tarefa 11 - potência regular
A1_t11 = np.array([
    [5, 2, 1], 
    [2, 3, 1],
    [1, 1, 2]
])

A2_t11 = np.array([
    [40, 8, 4, 2, 1],
    [8, 30, 12, 6, 2],
    [4, 12, 20, 1, 2],
    [2, 6, 1, 25, 4],
    [1, 2, 2, 4, 5]
])

# tarefa 12 - potência inversa e potencia com deslocamento
A1_t12 = np.array([
    [5, 2, 1], 
    [2, 3, 1],
    [1, 1, 2]
])

A2_t12 = np.array([
    [-14, 1, -2], 
    [1, -1, 1], 
    [-2, 1, -11]
])

A3_t12 = np.array([
    [40, 8, 4, 2, 1],
    [8, 30, 12, 6, 2],
    [4, 12, 20, 1, 2],
    [2, 6, 1, 25, 4],
    [1, 2, 2, 4, 5]
])

v0 = np.array([1, 1, 1])
v1 = np.array([1, 1, 1, 1, 1])

def menu():
    # escolher entre as tareras 11 e 12
    tarefa = int(input("Escolha a tarefa (11 ou 12): "))
    if tarefa == 11:
        # escolha entre as matrizes A1 e A2
        matriz = int(input(f"A1:\n{A1_t11}\nA2:\n{A2_t11}\nEscolha a matriz que deseja testar (1 - A1 ou 2 - A2): "))
        
        if matriz == 1:
            resultado = potencia_regular(A1_t11, v0, 0.0001)
            print(f"Autovalor dominante: {resultado[0]}\nAutovetor associado: {resultado[1]}")
        elif matriz == 2:
            resultado = potencia_regular(A2_t11, v1, 0.0001)
            print(f"Autovalor dominante: {resultado[0]}\nAutovetor associado: {resultado[1]}")
        else:
            print("Matriz inválida")
        
    elif tarefa == 12:
        # escolha entre o metodo da potencia inversa e o metodo da potencia com deslocamento
        metodo = int(input("Escolha o método (1 - potência inversa ou 2 - potência com deslocamento): "))
        
        if metodo == 1:
            # escolha entre as matrizes A1, A2 e A3
            matriz = int(input(f"A1:\n{A1_t12}\nA2:\n{A2_t12}\nA3:\n{A3_t12}\nEscolha a matriz que deseja testar (1 - A1, 2 - A2 ou 3 - A3): "))
            
            if matriz == 1:
                resultado = potencia_inversa2(A1_t12, v0, 0.0001)
                print(f"Autovalor dominante: {resultado[0]}\nAutovetor associado: {resultado[1]}")
            elif matriz == 2:
                resultado = potencia_inversa2(A2_t12, v0, 0.0001)
                print(f"Autovalor dominante: {resultado[0]}\nAutovetor associado: {resultado[1]}")
            elif matriz == 3:
                resultado = potencia_inversa2(A3_t12, v1, 0.0001)
                print(f"Autovalor dominante: {resultado[0]}\nAutovetor associado: {resultado[1]}")
            else:
                print("Matriz inválida")
                
        elif metodo == 2:
            # escolha entre as matrizes A1, A2 e A3
            matriz = int(input(f"A1:\n{A1_t12}\nA2:\n{A2_t12}\nA3:\n{A3_t12}\nEscolha a matriz que deseja testar (1 - A1, 2 - A2 ou 3 - A3): "))
            
            mu = float(input("Digite o valor de mu: "))
            
            if matriz == 1:
                resultado = potencia_com_deslocamento(A1_t12, v0, 0.0001, mu)
                print(f"Autovalor dominante: {resultado[0]}\nAutovetor associado: {resultado[1]}")
            elif matriz == 2:
                resultado = potencia_com_deslocamento(A2_t12, v0, 0.0001, mu)
                print(f"Autovalor dominante: {resultado[0]}\nAutovetor associado: {resultado[1]}")
            elif matriz == 3:
                resultado = potencia_com_deslocamento(A3_t12, v1, 0.0001, mu)
                print(f"Autovalor dominante: {resultado[0]}\nAutovetor associado: {resultado[1]}")
            else:
                print("Matriz inválida")
                
        else:
            print("Método inválido")
        
# chamada da função menu
while True:
    menu()
    continuar = input("Deseja continuar (s/n)? ")
    if continuar == 'n':
        break
    elif continuar != 's':
        print("Opção inválida")
        break