import numpy as np


def perceptron(x1, x2):
    x = np.array([1, x1, x2])
    w = np.array([-0.5, -0.7, 0.7])
    result = np.sum(x*w)
    return 1 if result > 0 else 0


exTable = [(0, 0), (-1, 0), (-1, 1), (0, 1)]

print("{0:>4} {1:>4} {2:>4}".format('x1', 'x2', 'y'))
for x1, x2 in exTable:
    print("{0:>4} {1:>4} {2:>4}".format(x1, x2, perceptron(x1, x2)))
