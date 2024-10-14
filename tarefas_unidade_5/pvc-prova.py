# PVC aplicado a questão da prova
import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tabelas as tb

def esquerdo(delta, r):
    return 1 - delta / (2*r)

def centro(delta, r):
    return -2

def direito(delta, r):
    return 1 + delta / (2*r)
def pvc(n):

    delta = 0.3 / n
  
    A = np.zeros((n-1, n-1))

    pontos = np.linspace(0.2, 0.5, n+1)[1:n]
    tb.print_matrix([pontos], "Partição do domínio", 7)
    i = 0
    for r_i in pontos:
        if i > 0:
            A[i, i-1] = esquerdo(delta, r_i)

        A[i, i] = centro(delta,r_i)

        if i < n-2:
            A[i, i+1] = direito(delta,r_i)
        i += 1

    tb.print_matrix(A, "Matriz do Sistema", 7)

    b = [-4/13 * delta**2] * (n-1)
    tb.print_matrix([b], "Vetor b", 7)

    solucao = np.linalg.solve(A, b)
    return solucao

if __name__ == "__main__":
    n = 6
    solucao = pvc(n)
    tb.print_matrix([solucao], "Solução", 7)