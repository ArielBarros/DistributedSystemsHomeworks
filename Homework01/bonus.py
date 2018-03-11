import threading 
import pprint
import numpy as np

def poolThreads(ths, pool=4):
    """
    Funcao que implementa um pool de Threads.

    Args:
        ths (list): Lista de Threads
        pool (int): Tamanho do Pool de Threads, default = 4.
    """
    ativas = []
    # Executa ate que todas as threads sejam computadas    
    while len(ths) > 0:
        # coleta sempre o proximo elemento da lista de threads nao iniciadas
        thread = ths[0]
        # Executa quando o limite nao eh atingido
        if(len(ativas) <= pool):
            # Adiciona a thread na lista de ativas
            ativas.append(thread)
            # deleta da lista de threads que nao foram iniciadas
            del ths[0]
            # inicia a thread em questao
            thread.start()
        # executa quando o limite foi atingido
        else:
            # certifica o fim da thread mais velha
            ativas[0].join()
            # Tira a thread terminada da lista de ativas
            del ativas[0] 

def processElement(i, j):
    """
    Funcao que calcula o elemento cij da matriz resultante.

    Args:
        i (int): Elemento correspondente a linha da matriz resultante.
        pool (int): Elemento correspondente a coluna da matriz resultante.
    """
    for k in range(SIZE_K):
        matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
        
def createThreads():
    """
    Funcao que cria uma lista de Threads com target processElement(i,j)
    
    Returns:
        th (list): Lista de threads criadas
    """
    th = []
    for i in range(SIZE_M):
        for j in range(SIZE_N):
            th.append( threading.Thread(target=processElement, args=(i,j)) )
    return th

if __name__ == '__main__':
    # Dimensoes
    SIZE_M = 6
    SIZE_K = 5
    SIZE_N = 4
    
    # Matriz de dimensoes (M,K)
    matrix1 = np.random.randint(0, 10, size=(SIZE_M, SIZE_K), dtype=np.uint32)
    # Matriz de dimensoes (K,N)
    matrix2 = np.random.randint(0, 10, size=(SIZE_K, SIZE_N), dtype=np.uint32)
    # Matriz Resultante (M,N)
    matrix3 = np.zeros((SIZE_M, SIZE_N), dtype=np.uint32)
    
    threads = createThreads() # cria Threads.
    poolThreads(threads, 5) # Executa o processamento paralelo com o pool = 5
    
    print('Matriz 1:')
    pprint.pprint(matrix1)
    print('\nMatriz 2:')
    pprint.pprint(matrix2)
    print('\nMatriz 3:')
    pprint.pprint(matrix3)
    
    # verificar corretude do resultado com funcao np.dot() do numpy
    print('\nMatriz Numpy:')
    pprint.pprint(np.dot(matrix1, matrix2)) 