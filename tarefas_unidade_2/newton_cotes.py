import math

# funcao geral de controle levando em conta o epson passado
def controle(f, a, b, epson, tipo):
    delta = 0
    Xi = 0
    erro = 0
    resultado_anterior = 0
    resultado = 0
    interacoes = 0
    N = 2

    while True:
        interacoes += 1
        delta = (b-a)/N
        integral = 0
        for i in range(N):
            Xi = a + i*delta
            Xf = Xi + delta
            if(tipo=="F1"):
                integral += regra_trapezio_fechada(f, Xi, Xf)
            elif(tipo=="F2"):
                integral += regra_simpson_1_3_fechada(f, Xi, Xf)
            elif(tipo=="F3"):
                integral += regra_simpson_3_8_fechada(f, Xi, Xf)
            elif(tipo=="F4"):
                integral += regra_quadratura_fechada(f, Xi, Xf)
            elif(tipo=="A1"):
                integral += regra_trapezio_aberta(f, Xi, Xf)
            elif(tipo=="A2"):
                integral += regra_simpson_1_3_aberta(f, Xi, Xf)
            elif(tipo=="A3"):
                integral += regra_simpson_3_8_aberta(f, Xi, Xf)
            elif(tipo=="A4"):
                integral += regra_quadratura_aberta(f, Xi, Xf)
        
        N = N*2
        resultado_anterior = resultado
        resultado = integral
        erro = abs(resultado_anterior - resultado)
        
        if (erro < epson): 
            break
    
    return interacoes, resultado
    
        
def funcao(x):
    return (math.sin(2*x) + 4*x**2 + 3*x)**2

# polinomio de grau 1 - regra do trapézio - fechada
def regra_trapezio_fechada(f, a, b):
    delta_meio = (b - a)/2
    
    return delta_meio * (f(a) + f(b))

# polinomio de grau 2 - regra de Simpson 1/3 - fechada
def regra_simpson_1_3_fechada(f, a, b):
    h = (b - a)/2
    delta_terco = h/3
    
    return delta_terco * (f(a) + 4*f(a + h) + f(b))

#polinomio de grau 3 - regra de Simpson 3/8 - fechada
def regra_simpson_3_8_fechada(f, a, b):
    h = (b - a)/3
    delta_tres_oitavos = 3*h/8
    
    return delta_tres_oitavos * (f(a) + 3*f(a + h) + 3*f(a + 2*h) + f(b))

# polinomio de grau 4 - desenvolvido por nos e chamaremos de regra da quadratura - fechada
def regra_quadratura_fechada(f, a, b):
    h = (b - a)/4
    delta_quarta = 2*h/45
    
    return delta_quarta * (7*f(a) + 32*f(a + h) + 12*f(a + 2*h) + 32*f(a + 3*h) + 7*f(b))

# polinomio de grau 1 - regra do trapézio - aberta
def regra_trapezio_aberta(f, a, b):
    h = (b - a)/3
    delta_meio = 3*h/2
    
    return delta_meio * (f(a + h) + f(a + 2*h))

# polinomio de grau 2 - regra de Simpson 1/3 - aberta
def regra_simpson_1_3_aberta(f, a, b):
    h = (b - a)/4
    delta_terco = 4*h/3
    
    return delta_terco * (2*f(a + h) - f(a + 2*h) + 2*f(a + 3*h))

# polinomio de grau 3 - regra de Simpson 3/8 - aberta
def regra_simpson_3_8_aberta(f, a, b):
    h = (b - a)/5
    delta_tres_oitavos = 5*h/24
    
    return delta_tres_oitavos * (11*f(a + h) + f(a + 2*h) + f(a + 3*h) + 11*f(a + 4*h))

# polinomio de grau 4 - regra da quadratura - aberta
def regra_quadratura_aberta(f, a, b):
    h = (b - a)/6
    delta_quarta = 3*h/10
    
    return delta_quarta * (11*f(a + h) - 14*f(a + 2*h) + 26*f(a + 3*h) - 14*f(a + 4*h) + 11*f(a + 5*h))

a = 0
b = 1
epson = 10**(-6)

print("============== FILOSÓFIA FECHADA ================")
print(f"REGRA DO TRAPÉZIO:\n{controle(funcao, a, b, epson, "F1")}\n")
print(f"REGRA DE SIMPSON 1/3:\n{controle(funcao, a, b, epson, "F2")}\n")
print(f"REGRA DE SIMPSON 3/8:\n{controle(funcao, a, b, epson, "F3")}\n")
print(f"REGRA DA QUADRATURA:\n{controle(funcao, a, b, epson, "F4")}\n")

print("\n============= FILOSÓFIA ABERTA ================")
print(f"REGRA DO TRAPÉZIO:\n{controle(funcao, a, b, epson, "A1")}\n")
print(f"REGRA DE SIMPSON 1/3:\n{controle(funcao, a, b, epson, "A2")}\n")
print(f"REGRA DE SIMPSON 3/8:\n{controle(funcao, a, b, epson, "A3")}\n")
print(f"REGRA DA QUADRATURA:\n{controle(funcao, a, b, epson, "A4")}\n")