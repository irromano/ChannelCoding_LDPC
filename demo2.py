import numpy as np

K_INPUT = 10000
N_OUTPUT = 20000

A = np.zeros((K_INPUT, N_OUTPUT), dtype=np.int16)

A[1][2] = 1
A[1][4] = 1
print(A)
print(A.dtype)
