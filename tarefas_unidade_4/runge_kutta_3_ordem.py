import numpy as np

# t0: tempo inicial
# v0: velocidade inicial
# y0: posição inicial
# k: constante de aerodinâmica
# m: massa
# g: gravidade
# delta: passo

def runge_kutta_3_ordem(t0, v0, y0, k, m, g, delta):
    s0 = np.array([v0, y0])
    altura_max = y0
    tempo_max = t0
    v_final = 0
    
    while s0[1] >= 0:
        v_meio = v0 + (delta/2)*(-g - (k/m)*v0)
        y_meio = y0 + (delta/2)*v0  
        
        v1 = v0 + delta*(-g - (k/m)*v0)
        y1 = y0 + delta*v0
        
        # atualizacao melhorada dos estados
        ed1 = np.array([-g - (k/m)*v0, v0])
        ed2 = np.array([-g - (k/m)*v_meio, v_meio])
        ed3 = np.array([-g - (k/m)*v1, v1])
        
        s1 = s0 + delta*((1/6)*ed1 + (4/6)*ed2 + (1/6)*ed3) 
        
        # atualizacao dos estados
        t0 += delta
        v_final = v0
        v0 = s1[0]
        y0 = s1[1]
        s0 = s1
               
        if y0 > altura_max:
            altura_max = y0
            tempo_max = t0
    
    print(f"delta = {delta}")
    print(f"Altura máxima: {altura_max}")
    print(f"Tempo para atingir a altura máxima: {tempo_max}")
    print(f"Tempo total de queda: {t0 - delta}")
    print(f"Velocidade final: {abs(v_final)}\n")
    
t0 = 0
v0 = 5
y0 = 200
k = 0.25
m = 2
g = 10

deltas = [0.1, 0.01, 0.001, 0.0001]

for delta in deltas:
    runge_kutta_3_ordem(t0, v0, y0, k, m, g, delta)