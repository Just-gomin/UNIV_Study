import numpy as np


def perceptron(x1, x2):
    x = np.array([1, x1, x2])
    w = np.array([-2, 8, -1])
    res = np.sum(x*w)
    return 1 if res > 1 else -1


exTable = [(0.3, 0.6), (0.5, 0.1), (0.7, 2), (1.2, 0.5)]
print("{0:>4} {1:>4} {2:>4}".format('x1', 'x2', 'y'))
for x1, x2 in exTable:
    print("{0:>4} {1:>4} {2:>4}".format(x1, x2, perceptron(x1, x2)))
