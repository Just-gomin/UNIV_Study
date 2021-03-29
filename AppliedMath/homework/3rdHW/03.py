import numpy as np


def inputLayer(x):
    w1 = np.array([-1, -1, -1])
    w2 = np.array([1, -1, -1])
    w3 = np.array([-2, 2, -1])
    a1 = 1 if np.sum(w1*x) > 0 else 0
    a2 = 1 if np.sum(w2*x) > 0 else 0
    a3 = 1 if np.sum(w3*x) > 0 else 0
    return np.array([1, a1, a2, a3])


def hiddenLayer(a):
    w = np.array([-1, -4, 2, 2])
    res = 1 if np.sum(w*a) > 0 else 0
    return res


def solution(x1, x2):
    x = np.array([1, x1, x2])
    a = inputLayer(x)
    res = hiddenLayer(a)
    return res


exTable = [(1, 1), (-1, 1), (-1, -1), (1, -1), (0, 0), (2, 1)]

print("{0:>4} {1:>4} {2:>4}".format('x1', 'x2', 'y'))
for x1, x2 in exTable:
    print("{0:>4} {1:>4} {2:>4}".format(x1, x2, solution(x1, x2)))
