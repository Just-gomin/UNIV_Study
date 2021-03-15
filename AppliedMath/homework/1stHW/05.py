import numpy as np

A = np.array([[-1, 2, -5.4], [0, 1, -100.5]])

print('Before A\n{0}'.format(A))

A[np.where(A < 0)] = 0

print('After A\n{0}'.format(A))
