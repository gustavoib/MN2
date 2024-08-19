import math

def funcao(x):
    return (math.sin(2*x) + 4*x**2 + 3*x)**2

# calcula o valor de x(sk)
def x(sk, xi, xf):
    x_final = (xi + xf) / 2 + ((xf - xi) / 2) * sk
    return x_final

# calcula gauss legendre com 2 pontos
def gauss_Legendre_2_pontos(a, b, erro):
    s = math.sqrt(1/3)
    raizes_s = [s, -s]
    w = 1
    pesos_w = [w, w]

    return integra(2, pesos_w, raizes_s, erro, a, b)

# calcula gauss legendre com 3 pontos
def gauss_Legendre_3_pontos(a, b, erro):
    s = math.sqrt(3/5)
    raizes_s = [s, 0, -s]
    w1 = 5/9
    w2 = 8/9
    pesos = [w1, w2, w1]

    return integra(3, pesos, raizes_s, erro, a, b)

# calcula gauss legendre com 4 pontos
def gauss_Legendre_4_pontos(a, b, erro):
    raizes_s = [0.861136, -0.861136, 0.339981, -0.339981]
    w1 = 0.34785
    w3 = 0.65214 
    pesos_w = [w1, w1, w3, w3]

    return integra(4, pesos_w, raizes_s, erro, a, b)


def integra(qtd_pontos, pesos_w, raizes_s, epson, a, b):
    #definindo as variaveis
    delta = 0
    xi = 0
    xf = 0
    erro = 0
    resultado_anterior = 0
    resultado = 0
    resultado_aux = 0 
    N = 1

    while True:
        resultado_anterior = resultado
        resultado_aux = resultado
        resultado = 0
        interacoes = 0
        
        delta = (b - a) / N
        for i in range(N):
            xi = a + i*delta
            xf = xi + delta
            somatorio = 0
            for k in range(qtd_pontos):
                somatorio += (pesos_w[k] * funcao(x(raizes_s[k], xi, xf)))
           
            resultado  += ((xf - xi) / 2) * somatorio
           
            interacoes += 1
          
        N = N*2
        resultado_anterior = resultado_aux
      
        erro = abs((resultado_anterior - resultado)/2)
     
        if (erro < epson): 
            break
    
    return interacoes, resultado

erro = 10**(-6)
a = 0 
b = 1

print("====== GAUSS LEGENDRE 2 PONTOS ======")
print(f"{gauss_Legendre_2_pontos(a, b, erro)}\n")

print("====== GAUSS LEGENDRE 3 PONTOS ======")
print(f"{gauss_Legendre_3_pontos(a, b, erro)}\n")

print("====== GAUSS LEGENDRE 4 PONTOS ======")
print(f"{gauss_Legendre_4_pontos(a, b, erro)}\n")
