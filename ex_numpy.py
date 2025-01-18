# atividade numpy
#Exercício 1
import numpy as np

"""
# Cria um array numpy com 6x6 elementos preenchidos com zeros
array_zeros = np.zeros((6, 6))
print(array_zeros)

"""

# prencha o centro deste array com 4x4 elementos preenchidos com 1
array_1 = np.ones((4, 4))
array_1 = array_1[1:-1, 1:-1]
print(array_1)