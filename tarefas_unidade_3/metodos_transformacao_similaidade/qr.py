import numpy as np
from jacobi import somaDosQuadradosDosTermosAbaixoDaDiagonal
np.set_printoptions(precision=4, suppress=True)

def metodoQR(A, epsilon):
    n = A.shape[0]
    val = 100
    P = np.identity(n)
    A_velha = A.copy()
    passo = 1
    while(val > epsilon):
        Q, R = decomposicao_QR(A_velha)

        print(f"Matriz Q{passo}:")
        print(Q)
        print(f"Matriz R{passo}:")
        print(R)

        A_nova = np.dot(R, Q)
        A_velha = A_nova
        P = np.dot(P, Q)
        val = somaDosQuadradosDosTermosAbaixoDaDiagonal(A_nova)
        passo += 1
    return P, A_nova


def decomposicao_QR(A): 
    n = A.shape[0]
    QT = np.identity(n)
    R_velha = A.copy()
    for j in range(n-1):
        for i in range(j+1, n):
            J_ij = matrizJacobi_R_velha(R_velha, i, j, n)
            R_nova = np.dot(J_ij, R_velha)
            R_velha = R_nova
            QT = np.dot(J_ij, QT)
    Q = np.transpose(QT)
    return Q, R_nova

def matrizJacobi_R_velha(R, i, j, n):
    theta, epsilon = 10e-6, 10e-6
    J_ij = np.identity(n)
    if(abs(R[i][j]) <= epsilon):
        return J_ij
    if(abs(R[j][j]) <= epsilon):
        if(R[i][j] < 0):
            theta = np.pi/2
        else:
            theta = -np.pi/2
    else:
        theta = np.arctan(-R[i][j]/R[j][j])

    J_ij[i][i] = np.cos(theta)
    J_ij[j][j] = np.cos(theta)
    J_ij[i][j] = np.sin(theta)
    J_ij[j][i] = -np.sin(theta)

    return J_ij

def main():
    A = np.array([[40, 8, 4, 2, 1], 
                  [8, 30, 12, 6, 2], 
                  [4, 12, 20, 1, 2], 
                  [2, 6, 1, 25, 4], 
                  [1, 2, 2, 4, 5]])
    epsilon = 10**-6
    P, A_final = metodoQR(A, epsilon)
    print(A_final)
    print(P)

if __name__ == "__main__":
    main()