from PIL import Image
import math

#---------------------------LEITURA DA IMAGEM E TRANSFORMAÇÃO EM UMA MATRIZ---------------------------#

# função para carregar a imagem
def load_image(file_path):
    image = Image.open(file_path)
    # Converter para escala de cinza
    image = image.convert('L')
    # Converter a imagem em uma matriz de pixels
    pixel_matrix = list(image.getdata())
    width, height = image.size
    pixel_matrix = [pixel_matrix[i * width:(i + 1) * width] for i in range(height)]
    return pixel_matrix

def save_image(pixel_matrix, output_file):
    # Converter a matriz de pixels de volta para uma imagem
    image = Image.new('L', (len(pixel_matrix[0]), len(pixel_matrix)))
    image.putdata([pixel for row in pixel_matrix for pixel in row])
    # Salvar a imagem
    image.save(output_file)

#---------------------------INICIO DAS IMPLEMENTAÇÕES DO FILTRO GAUSSIANO---------------------------#

# essa função cria um kernel gaussiano, que é um padrão de pesos que será aplicado a cada pixel da imagem.
# o kernel é um filtro que suaviza a imagem, removendo ruídos e detalhes.
# o tamanho do kernel determina o quão forte será o efeito de suavização.    
def create_gaussian_kernel(size, sigma=1):
        gaussian_kernel = [] 
        center = size // 2 
        total = 0 
        # Criar um kernel de tamanho size x size, onde cada elemento é um peso que será aplicado a um pixel da imagem.
        for i in range(size):
            row = []
            for j in range(size): 
                x, y = i - center, j - center
                # em weights, calculamos o peso de cada pixel com base na distância do pixel central, usando a fórmula do kernel gaussiano.
                weight = (1 / (2 * math.pi * sigma**2)) * math.exp(-(x**2 + y**2) / (2 * sigma**2))
                row.append(weight)
                total += weight
            gaussian_kernel.append(row)
        # Normalizar o kernel: garantir que a soma de todos os pesos seja 1.
        # isso é importante para manter a intensidade da imagem (brilho) após a aplicação do filtro (convolução).
        for i in range(size): 
            for j in range(size):
                gaussian_kernel[i][j] /= total
        return gaussian_kernel
    
#---------------------------INICIO DA IMPLEMENTAÇÃO DO FILTRO DE GRADIENTE--------------------------#

# criação do kernel sobel
# 2.1) um filtro de Sobel para a derivada na direção x, gerando uma imagem/matriz, A, com os valores da derivada em cada pixel/elemento da matriz;
# 2.2) um filtro de Sobel para a derivada na direção y, gerando uma imagens/matriz, B, com os valores da derivada em cada pixel/elemento da matriz;
# 2.3) em cada uma das matrizes, A e B, eleve ao quadrado os valores dos elementos;
# 2.4) some as duas matrizes A e B modificadas no passo 2.3 e tire a raiz quadrada  de cada elemento dessa matriz, C

sobel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
sobel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

def sum_stqr_matrix(matrix_A, matrix_B):
    result = [[0]*len(matrix_A[0]) for _ in range(len(matrix_A))] # cria uma matriz de zeros com o mesmo tamanho da matriz A
    for y in range(len(matrix_A)): # percorre as linhas da matriz A
        for x in range(len(matrix_A[0])): # percorre as colunas da matriz A
            result[y][x] = math.sqrt(matrix_A[y][x]**2 + matrix_B[y][x]**2) # calcula a raiz quadrada da soma dos quadrados dos elementos correspondentes das matrizes A e B
    return result


#---------------------------INICIO DA IMPLEMENTAÇÃO DO FILTRO DE CONVOLUÇÃO--------------------------#

# essa função aplica o kernel na imagem, este processo é chamado de convolução.
# a convolution é uma operação matemática que combina duas funções para produzir uma terceira função.
def apply_kernel(image, kernel):
    # nas linhas a seguir definimos o tamanho da imagem e do kernel. 
    # também definimos o tamanho do preenchimento (padding) que será necessário para garantir que o kernel possa ser aplicado a todos os pixels da imagem.
    height, width = len(image), len(image[0]) 
    kernel_size = len(kernel)
    padding = kernel_size // 2 
    
    # em alguns casos, é necessário adicionar pixels extras ao redor da imagem para garantir que o kernel possa ser aplicado a todos os pixels.
    # isso é chamado de preenchimento (padding), que é o que fazemos nas linhas a seguir, da seguinte forma:
    # criamos uma nova matriz de pixels, que é uma versão maior da imagem original, com pixels extras ao redor.
    padded_image = [[0] * (width + 2 * padding) for _ in range(height + 2 * padding)]
    for y in range(height):
        for x in range(width):
            padded_image[y + padding][x + padding] = image[y][x]
     
    result = [[0]*width for _ in range(height)]
    # nos loops aninhados, percorremos cada pixel da imagem e aplicamos o kernel a ele (convolução).
    # passo a passo, o que fazemos é: para cada pixel, multiplicamos os valores dos pixels vizinhos pelo peso correspondente no kernel.
    # somamos todos esses valores e usamos o resultado como o novo valor do pixel, que é armazenado na matriz result.
    for y in range(height):
        for x in range(width): 
            total = 0
            for i in range(kernel_size):
                for j in range(kernel_size):
                    # dissecando o que acontece aqui: 
                    # a variável total, que foi inicialmente preenchida com zeros, recebe a soma de todos os pixels vizinhos multiplicados pelo peso correspondente no kernel.
                    total += padded_image[y + i][x + j] * kernel[i][j]
            result[y][x] = total
    return result

#---------------------------ANALISE DO THRESHOLD--------------------------#

def threshold (matrix, threshold):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] < threshold:
                matrix[y][x] = 0
            else:
                matrix[y][x] = 255
    return matrix


#---------------------------APLICAÇÃO DOS FILTROS NA IMAGEM--------------------------#

# imagem teste
image_matrix = load_image('tr01_mn2/imagem_inicial.jpg')
# criação do kernel gaussiano
gaussian_kernel = create_gaussian_kernel(3)
# aplicação do kernel gaussiano na imagem
gaussian_filter_image = apply_kernel(image_matrix, gaussian_kernel)
# matriz resultante da convolução do filtro de sobel na direção x
matrix_A = apply_kernel(gaussian_filter_image, sobel_x)
# matriz resultante da convolução do filtro de sobel na direção y
matrix_B = apply_kernel(gaussian_filter_image, sobel_y)
# matriz resultante da soma das matrizes A e B modificadas
matrix_C = sum_stqr_matrix(matrix_A, matrix_B)
# aplicação do threshold na matriz C
matrix_D = threshold(matrix_C, 100)

save_image(matrix_D, 'tr01_mn2/imagem_final_alg1.jpg')