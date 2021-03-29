import numpy as np


def inputLayer(x):
    w1 = np.array([])
    w2 = np.array([])
    a1 = 1 if np.sum(w1*x) else 0
    a2 = 1 if np.sum(w2*x) else 0
    return np.array([1, a1, a2])


def hiddenLayer(a):
    w = np.array([])
    res = np.sum(w*a)
    return 1 if res else 0


def solution(x1, x2):
    x = np.array([1, x1, x2])
    a = inputLayer(x)
    res = hiddenLayer(a)
    return res


exTable = []

print("{0:>4} {1:>4} {2:>4}".format('x1', 'x2', 'y'))
for x1, x2 in exTable:
    print("{0:>4} {1:>4} {2:>4}".format(x1, x2, solution(x1, x2)))
