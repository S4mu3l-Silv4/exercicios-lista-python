# Questão 9:

import numpy as np

matriz = np.zeros((3,2), dtype=np.float64)
print(matriz)

for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        matriz[i][j] = int(input('\nDigite um número qualquer para as posições {} x {}: '.format(i, j)))

print('\nA soma dos elementos dessa matriz é {}'.format(np.sum(matriz)))
