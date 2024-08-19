import numpy as np

def jacobi(A, erro=10**-6):
    n = A.shape[0]
    lambdas = np.zeros(n)
    val = 100
    P = np.identity(n)
    A_velha = A.copy()
    while val > erro:
        A_nova, J = varreduraDeJacobi(A_velha, n)
        A_velha = A_nova
        P = P.dot(J)
        val = somaDosQuadradosDosTermosAbaixoDaDiagonal(A_velha)
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

if __name__ == "__main__":
    A = np.array([[40, 8,  4,  2,  1],
                  [8,  30, 12, 6,  2],
                  [4,  12, 20, 1,  2],
                  [2,  6,  1,  25, 4],
                  [1,  2,  2,  4,  5]], dtype=float)
    P, lambdas = jacobi(A)
    print(P)
    print(lambdas)
