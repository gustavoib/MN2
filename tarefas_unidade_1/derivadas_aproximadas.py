# Dada uma função, um ponto, uma filosofia, 
# a ordem da derivada de 1 a 4 e um delta, 
# calcular a derivada da função.
import numpy as np

def derivada(funcao, ponto, filosofia, ordem, delta):
    if ordem < 1 or ordem > 4:
        raise ValueError("A ordem da derivada deve ser de 1 a 4.")
    
    if filosofia == 1:
        if ordem == 1:
            return (funcao(ponto + delta) - funcao(ponto)) / delta
        elif ordem == 2:
            return (funcao(ponto + 2 * delta) - 2 * funcao(ponto + delta) + funcao(ponto)) / delta**2
        elif ordem == 3:
            return (funcao(ponto + 3 * delta) - 3 * funcao(ponto + 2 * delta) + 3 * funcao(ponto + delta) - funcao(ponto)) / delta**3
        elif ordem == 4:
            return (funcao(ponto + 4 * delta) - 4 * funcao(ponto + 3 * delta) + 6 * funcao(ponto + 2 * delta) - 4 * funcao(ponto + delta) + funcao(ponto)) / delta**4
    
    elif filosofia == 2:
        if ordem == 1:
            return (funcao(ponto) - funcao(ponto - delta)) / delta
        elif ordem == 2:
            return (funcao(ponto) - 2 * funcao(ponto - delta) + funcao(ponto - 2 * delta)) / delta**2
        elif ordem == 3:
            return (funcao(ponto) - 3 * funcao(ponto - delta) + 3 * funcao(ponto - 2 * delta) - funcao(ponto - 3 * delta)) / delta**3
        elif ordem == 4:
            return (funcao(ponto) - 4 * funcao(ponto - delta) + 6 * funcao(ponto - 2 * delta) - 4 * funcao(ponto - 3 * delta) + funcao(ponto - 4 * delta)) / delta**4
    
    elif filosofia == 3:
        if ordem == 1:
            return (funcao(ponto + delta) - funcao(ponto - delta)) / (2 * delta)
        elif ordem == 2:
            return (funcao(ponto + delta) - 2 * funcao(ponto) + funcao(ponto - delta)) / delta**2
        elif ordem == 3:
            return (funcao(ponto + 2 * delta) - 2 * funcao(ponto + delta) + 2 * funcao(ponto - delta) - funcao(ponto - 2 * delta)) / (2 * delta**3)
        elif ordem == 4:
            return (funcao(ponto + 2 * delta) - 4 * funcao(ponto + delta) + 6 * funcao(ponto) - 4 * funcao(ponto - delta) + funcao(ponto - 2 * delta)) / delta**4
    
    else:
        raise ValueError("Filosofia inválida. Escolha entre '1 - Forward', '2 - Backward' ou '3 - Central'.")


if __name__ == "__main__":
    # Função para derivar:
    def f(x):
        return np.sin(x)

    ponto = np.pi
    ordem = 1
    # 1 - Forward, 2 - Backward , 3 - Central
    filosofia = 3
    delta = 0.001
    
    derivada = derivada(f, ponto, filosofia, ordem, delta)
    print(f"\nA {ordem}ª derivada da função no ponto {ponto:.4f} é aproximadamente {derivada:.4f}\n")
