import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'metodos_potencia')))
from metodos_potencia.potencia_regular import potencia_regular
from metodos_transformacao_similaidade.houseHolder import houseHolder
import tabelas as tb

np.set_printoptions(suppress=True)
casas_decimais = 7

def jacobi(A, erro=10**-6):
    n = A.shape[0]
    lambdas = np.zeros(n)
    val = 100
    P = np.identity(n)
    A_velha = A.copy()
    passo = 1
    while val > erro and passo < 100:
        A_nova, J = varreduraDeJacobi(A_velha, n)

        # iii. Imprima a matriz que sai de cada varredura de Jacobi
        tb.print_matrix(A_nova, f"Matriz da varredura {passo}:", casas_decimais)

        A_velha = A_nova
        P = P.dot(J)
        val = somaDosQuadradosDosTermosAbaixoDaDiagonal(A_velha)
        passo += 1
    for i in range(n):
        lambdas[i] = A_nova[i][i]
    return P, lambdas

def somaDosQuadradosDosTermosAbaixoDaDiagonal(A):
    n = A.shape[0]
    soma = 0
    for i in range(n):
        for j in range(i+1, n):
            soma += A[i][j]**2
    return soma

def varreduraDeJacobi(A, n):
    J = np.identity(n)
    A_velha = A.copy()
    for j in range(n-1):
        for i in range(j+1, n):
            J_ij = matrizJacobi(A_velha, i, j, n)
            A_nova = np.transpose(J_ij).dot(A_velha).dot(J_ij)
            A_velha = A_nova
            J = J.dot(J_ij)
    return A_nova, J

def matrizJacobi(A, i, j, n):
    theta, epsilon = 10e-6, 10e-6
    J_ij = np.identity(n)
    if(abs(A[i][j]) <= epsilon):
        return J_ij
    if(abs(A[i][i] - A[j][j]) <= epsilon):
        theta = np.pi/4
    else:
        theta = 0.5*np.arctan(-2*A[i][j]/(A[i][i] - A[j][j]))

    J_ij[i][i] = np.cos(theta)
    J_ij[j][j] = np.cos(theta)
    J_ij[i][j] = np.sin(theta)
    J_ij[j][i] = -np.sin(theta)

    return J_ij

def main():
    A1 = np.array([[40, 8,  4,  2,  1],
                   [8,  30, 12, 6,  2],
                   [4,  12, 20, 1,  2],
                   [2,  6,  1,  25, 4],
                   [1,  2,  2,  4,  5]])
    
    A2 = np.array([[5, 2, 1], 
                   [2, 3, 1],
                   [1, 1, 2]])
    
    A = A1

    print("\n\033[31m+---------------------- PARTE 1 ----------------------+\n\033[0m")

    tb.print_matrix(A, "Matriz A", 0)

    # 1) Implemente o método de Jacobi e aplique-o sobre A para encontrar
    #   i. a matriz diagonal A_barra
    #   ii. a matriz acumulada P = P1.P2.P3. ...
    P, lambdas = jacobi(A)

    # iv. Imprima os pares (autovalor, autovetor) da matriz A
    for i in range(len(P[0])):
        auto_vetor = P[:, i]
        # auto_vetor = auto_vetor / auto_vetor[len(auto_vetor) -1]
        auto_valor = lambdas[i]
        tb.print_matrix([auto_vetor], f"Autovalor: {auto_valor:.{casas_decimais}f} | Autovetor:", casas_decimais)

    # v. Compare os resultados com os obtidos pelo método de Householder
    A_barra, H = houseHolder(A)
    autovalor_de_A_barra, autovetor_de_A_barra = potencia_regular(A_barra, np.ones(len(A)), 1e-6)
    autovetor_de_A = H.dot(autovetor_de_A_barra)
    autovalor_de_A = autovalor_de_A_barra
    tb.print_matrix([autovetor_de_A], "Resultado da tarefa 13 (Householder)", -1)
    tb.print_matrix([autovetor_de_A], f"Autovalor de A: {autovalor_de_A:.{casas_decimais}f} | Autovetor:", casas_decimais)
    
    print("\n\033[31m+---------------------- PARTE 2 ----------------------+\n\033[0m")
    # 2) Adapte o método de varredura de Jacobi para receber a matriz tridiagonal 
    # que sai do método de Householder. Neste caso, observe que:

    # i. as varreduras de colunas e linhas continuam as mesmas
    def varreduraDeJacobiAdaptada(A, erro):
        n = len(A)
        J = np.identity(n)
        A_velha = A.copy()
        val = 100
        passo = 1
        while val > erro and passo < 100:
            for j in range(n-1):
                for i in range(j+1, n):
                    J_ij = matrizJacobi(A_velha, i, j, n)
                    A_nova = np.transpose(J_ij).dot(A_velha).dot(J_ij)

                    tb.print_matrix(A_nova, f"Matriz da varredura adaptada:", casas_decimais)

                    A_velha = A_nova
                    J = J.dot(J_ij)
                    passo += 1
            val = somaDosQuadradosDosTermosAbaixoDaDiagonal(A_nova)
        return A_nova, J
    
    A_barra, H = houseHolder(A)
    A_nova, J = varreduraDeJacobiAdaptada(A_barra, 1e-6)
    tb.print_matrix(J, "Matriz P", casas_decimais)

    P_nova = np.dot(H, J)
    tb.print_matrix(P_nova, "Matriz P nova", casas_decimais)
    tb.print_matrix(P, "Matriz para comparação", casas_decimais)
if __name__ == "__main__":
    main()
