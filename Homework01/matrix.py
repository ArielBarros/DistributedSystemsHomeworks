import threading 
import pprint
import numpy as np

SIZE_M = 6
SIZE_K = 5
SIZE_N = 4

# Matriz de dimensoes (M,K)
matrix1 = np.random.randint(0, 10, size=(SIZE_M, SIZE_K), dtype=np.uint32)
# Matriz de dimensoes (K,N)
matrix2 = np.random.randint(0, 10, size=(SIZE_K, SIZE_N), dtype=np.uint32)
# Matriz Resultante (M,N)
matrix3 = np.zeros((SIZE_M, SIZE_N), dtype=np.uint32)

def processElement(i, j):
	for k in range(SIZE_K):
		matrix3[i][j] += matrix1[i][k] * matrix2[k][j]

th = [ [ 0 for i in range(SIZE_N) ] for j in range(SIZE_M) ]
for i in range(SIZE_M):
	for j in range(SIZE_N):
		th[i][j] = threading.Thread(target=processElement, args=(i,j))
		th[i][j].start()
		
for i in range(SIZE_M):
	for j in range(SIZE_N):
		th[i][j].join()
	
print('Matriz 1:')
pprint.pprint(matrix1)
print('\nMatriz 2:')
pprint.pprint(matrix2)
print('\nMatriz 3:')
pprint.pprint(matrix3)

# verificar corretude do resultado com funcao np.dot() do numpy
print('\nMatriz Numpy:')
pprint.pprint(np.dot(matrix1, matrix2))
