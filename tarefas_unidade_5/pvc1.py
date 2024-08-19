import numpy as np

def pvc1(n):
    
    delta = 1.0/n
    borda = 1/delta**2
    centro = - (2/(delta**2) + 1)
    A = np.zeros((n-1, n-1))

    for i in range(n-1):
        if i > 0:
            A[i, i-1] = borda

        A[i, i] = centro

        if i < n-2:
            A[i, i+1] = borda
    
    print(A)

    b = np.zeros(n-1)
    b[n-2] = - borda
    
    solucao = np.linalg.solve(A, b)
    return solucao

n = 8
pontos = np.linspace(0, 1, n+1)
solucao = pvc1(n)
print(f"Pontos: {pontos[1:n]}")
print(f"Solucao: ", solucao)





    
    