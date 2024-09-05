# Detecção de bordas em imagens

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve2d
import math

def show_image(pixel_matrix, pixel_matrix_suavizado, edges1):

    # Definindo o tamanho da janela
    plt.figure(figsize=(8, 6))

    plt.subplot(2, 2, 1)
    plt.imshow(pixel_matrix, cmap='gray')
    plt.title('Imagem original')

    plt.subplot(2, 2, 2)
    plt.imshow(pixel_matrix_suavizado, cmap='gray')
    plt.title('Imagem suavizada')

    plt.subplot(2, 1, 2)
    plt.imshow(edges1, cmap='gray')
    plt.title('Bordas detectadas - Filtro Gradiente')

    plt.tight_layout()
    plt.show()

def filtro_gaussiano(matriz, sigma=1):
    # Calcular o tamanho do kernel com base no sigma
    tamanho = int(2 * np.ceil(3 * sigma) + 1)
    centro = tamanho // 2

    # Criar o kernel gaussiano
    kernel = np.zeros((tamanho, tamanho))
    soma = 0  # Para normalização

    for x in range(tamanho):
        for y in range(tamanho):
            dx = x - centro
            dy = y - centro
            kernel[x, y] = math.exp(-(dx**2 + dy**2) / (2 * sigma**2))
            soma += kernel[x, y]

    # Normalizar o kernel
    kernel /= soma

    # Aplicar o padding à matriz para evitar problemas nas bordas
    padded_matriz = np.pad(matriz, ((centro, centro), (centro, centro)), mode='constant')

    # Criar a matriz de saída
    linhas, colunas = matriz.shape
    matriz_filtrada = np.zeros_like(matriz)

    # Aplicar a convolução
    for i in range(linhas):
        for j in range(colunas):
            submatriz = padded_matriz[i:i+tamanho, j:j+tamanho]
            matriz_filtrada[i, j] = np.sum(submatriz * kernel)

    return matriz_filtrada

def filtro_laplaciano(matriz):
    # Definir o kernel de Laplace (filtro de bordas)
    kernel = np.array([[0, -1, 0],
                       [-1, 4, -1],
                       [0, -1, 0]])

    # Obter as dimensões da matriz de entrada
    linhas, colunas = matriz.shape

    # Criar a matriz de saída
    matriz_filtrada = np.zeros_like(matriz)

    # Aplicar o padding à matriz para evitar problemas nas bordas
    padded_matriz = np.pad(matriz, ((1, 1), (1, 1)), mode='constant')

    # Aplicar a convolução
    for i in range(1, linhas + 1):
        for j in range(1, colunas + 1):
            submatriz = padded_matriz[i-1:i+2, j-1:j+2]
            matriz_filtrada[i-1, j-1] = np.sum(submatriz * kernel)

    return matriz_filtrada

def image_to_pixel_matrix(image_path):
    # Abre a imagem usando PIL
    img = Image.open(image_path)
    
    # Converte a imagem para escala de cinza
    img_gray = img.convert('L')
    
    # Converte a imagem em uma matriz numpy
    pixel_matrix = np.array(img_gray)
    
    return pixel_matrix

def filtro_gradiente(pixel_matrix):
    # Cria um filtro de Sobel
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    # Aplica o filtro de Sobel à matriz de pixels
    edge_x = convolve2d(pixel_matrix, sobel_x, mode='same')
    edge_y = convolve2d(pixel_matrix, sobel_y, mode='same')
    
    # Calcula a magnitude do gradiente
    magnitude = np.sqrt(np.square(edge_x) + np.square(edge_y))

    return magnitude


def algoritmo_1(pixel_matrix):
    # 1) Suavize a imagem, aplicando um filtro Gaussiano
    imagem_suavizada = filtro_gaussiano(pixel_matrix, sigma=1)

    # 2) Na imagem do passo 1, aplique o filtro convolucional de Gradiente
    D = filtro_gradiente(imagem_suavizada)
    # 3) Escolha um valor (float)  para threshold e 
    threshold = 50.0
    # 4) gere uma matriz Final, D, com 
    # >>>>> pixel 0 caso o pixel correspondente da matriz C seja menor do que o threshold
    # >>>>> pixel 1. caso o pixel correspondente da matriz C seja maior do que o threshold.
    for i in range(D.shape[0]):
        for j in range(D.shape[1]):
            if D[i, j] > threshold:
                D[i, j] = 1
            else:
                D[i, j] = 0

    return D, imagem_suavizada

def algoritmo_2(pixel_matrix, tolerance=0.0001):
    # 1) Suavize a imagem, aplicando um filtro Gaussiano
    imagem_suavizada = filtro_gaussiano(pixel_matrix, sigma=1)
    # 2) Na imagem do passo 1, aplique o filtro convolucional de Laplace, gerando uma imagem/matriz A
    A = filtro_laplaciano(imagem_suavizada)
    # 3) Por simplicidade, gere uma imagem/matriz, B, percorrendo a imagem A e escrevendo em B
    # >>>>>  1. caso o pixel correspondente da matriz A seja diferente de 0 dentro de uma tolerância (0.0001, por exemplo)
    # >>>>> 0. cado o pixel correspondente da matriz A seja igual a 0 dentro de uma tolerância (0.0001, por exemplo).
    B = np.zeros_like(A)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if abs(A[i, j]) > tolerance:
                B[i, j] = 1
            else:
                B[i, j] = 0
    return B


def main():
    image_path = "tarefas_unidade_1/imagem.jpg"
    pixel_matrix = image_to_pixel_matrix(image_path)
    edges1, imagem_suavizada = algoritmo_1(pixel_matrix)
    show_image(pixel_matrix, imagem_suavizada, edges1)

if __name__ == "__main__":
    main()