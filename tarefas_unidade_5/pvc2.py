import numpy as np

def pvc2(n, value):
    delta_x = 1.0/n
    delta_y = 1.0/n

    borda_y = 1/(delta_y**2)
    borda_x = 1/(delta_x**2)
    centro = - (2/(delta_x**2) + 2/(delta_y**2))

    dim = (n-1) * (n-1)
    A = np.zeros((dim, dim))

    k = 0
    y = 0
    for i in range(dim):
        if i > 0:
            k = k + 1
            if k%(n-1) != 0: 
                A[i][i-1] = borda_y
            else:
                A[i][i-1] = 0

        if i > (n-2):
            A[i][i-(n-1)] = borda_x

        A[i][i] = centro

        if i < dim-(n-1):
            A[i][i+(n-1)] = borda_x

        if i < dim-1:
            y = y + 1
            if y%(n-1) !=0: 
                A[i][i+1] = borda_y
            else:
                A[i][i+1] = 0
    
    print(A)

    b = np.array([value for i in range(dim)])

    solucao = np.linalg.solve(A, b)

    return solucao

n = 4
value = 4
solucao = pvc2(n, value)
print(f"Solucao: {solucao}")





