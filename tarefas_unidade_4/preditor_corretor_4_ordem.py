import numpy as np    

# t0: tempo inicial
# v0: velocidade inicial
# y0: posição inicial
# k: constante de aerodinâmica
# m: massa
# g: gravidade
# delta: passo  

def runge_kutta_4_ordem(t0, v0, y0, k, m, g, delta):
    v_velho = v0
    y_velho = y0
    
    # vetor para armazenar os estados (o método é de passo multiplo)
    s = np.array([v_velho, y_velho])
    
    while y_velho > 0:
        f1 = np.array([-g - (k/m)*v_velho, v_velho])
        v2 = v_velho + (delta/2) * f1[0]
        f2 = np.array([-g - (k/m)*v2, v2])
        v3 = v_velho + (delta/2 * f2[0])
        f3 = np.array([-g - (k/m)*v3, v3])
        v4 = v_velho + (delta * f3[0])
        f4 = np.array([-g - (k/m)*v4, v4])
        
        v_novo = v_velho + (delta/6.0)*(f1[0] + 2*f2[0] + 2*f3[0] + f4[0])
        y_novo = y_velho + (delta/6.0)*(f1[1] + 2*f2[1] + 2*f3[1] + f4[1])
        
        temp = s
        temp = np.append(temp, v_novo)
        temp = np.append(temp, y_novo)
        
        s = temp
        v_velho = v_novo
        y_velho = y_novo
        
    print(f"delta = {delta}")
    print(f"Altura máxima: {max(s[1::2])}")
    print(f"Tempo para atingir a altura máxima: {s[1::2].argmax() * delta}")
    print(f"Tempo total de queda: {len(s[1::2]) * delta}")
    print(f"Velocidade final: {abs(s[-2])}\n")

def preditor_corretor_4_ordem(t0, v0, y0, k, m, g, delta):
    v_velho = v0
    y_velho = y0

    # vetor para armazenar os estados (o método é de passo multiplo)
    s = np.array([v_velho, y_velho, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    
    # inicialização por meio do método de Runge-Kutta de quarta ordem
    for i in range(1, 4):
        f1 = np.array(((-g - (k/m)*v_velho), v_velho))
        v2 = v_velho + (delta/2) * f1[0]
        f2 = np.array(((-g - (k/m)*v2), v2))
        v3 = v_velho + (delta/2 * f2[0])
        f3 = np.array(((-g - (k/m)*v3), v3))
        v4 = v_velho + (delta * f3[0])
        f4 = np.array(((-g - (k/m)*v4), v4))

        # preenche o vetor de estados, o índice pode parecer "estranho" pois
        # os dois primeiros estado já existem (0 e 1), então precisamos atualizados
        # a partir do índice 2.
        s[i*2] = v_velho + (delta/6.0)*(f1[0] + 2*f2[0] + 2*f3[0] + f4[0])
        s[i*2 + 1] = y_velho + (delta/6.0)*(f1[1] + 2*f2[1] + 2*f3[1] + f4[1])

        v_velho = s[i*2]
        y_velho = s[i*2 + 1]

    v_velho = v0
    v_novo = y_velho
    y_velho = y0
    y_novo = y_velho
    
    while y_novo > 0:
        sn1 = np.array(((-g - (k/m) * s[0]), s[0]))
        sn2 = np.array(((-g - (k/m) * s[2]), s[2]))
        sn3 = np.array(((-g - (k/m) * s[4]), s[4]))
        sn4 = np.array(((-g - (k/m) * s[6]), s[6]))
        
        # predição
        r = np.array([0, 0])
        r[0] = s[6] + (delta/24) * (-9 *sn1[0] + 33 * sn2[0] - 59 * sn3[0] + 55 * sn4[0])
        r[1] = s[7] + (delta/24) * (-9 *sn1[1] + 33 * sn2[1] - 59 * sn3[1] + 55 * sn4[1])
        
        f = np.array(((-g - (k/m) * r[0]), r[0]))
        
        # correção
        v_novo = s[6] + (delta/24) * (sn2[0] - 5 * sn3[0] + 19 * sn4[0] + 9 * f[0])
        y_novo = s[7] + (delta/24) * (sn2[1] - 5 * sn3[1] + 19 * sn4[1] + 9 * f[1])
        
        t0 += delta
        
        if v_velho*v_novo < 0:
            if y_novo < y_velho:
                altura_max = y_velho
                tempo_max = t0 - delta
            else:
                altura_max = y_novo
                tempo_max = t0
            
        if y_velho*y_novo < 0:
            v_final = v_velho
            t_final = t0 - delta
        
        temp = s[2:]
        temp = np.append(temp, v_novo)
        temp = np.append(temp, y_novo)

        s = temp
        v_velho = v_novo
        y_velho = y_novo
    
    print(f"delta = {delta}")
    print(f"Altura máxima: {altura_max}")
    print(f"Tempo para atingir a altura máxima: {tempo_max}")
    print(f"Tempo total de queda: {t_final - delta}")
    print(f"Velocidade final: {abs(v_final)}\n")
    
t0 = 0
v0 = 5
y0 = 200
k = 0.25
m = 2
g = 10

deltas = [0.1, 0.01, 0.001, 0.0001]

for delta in deltas:
    preditor_corretor_4_ordem(t0, v0, y0, k, m, g, delta)
