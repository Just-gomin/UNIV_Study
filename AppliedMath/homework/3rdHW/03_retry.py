import numpy as np


def node1(x):
    w = np.array([-2, -1, -1])
    tmp = abs(np.sum(w*x))
    return 1 if tmp <= 1/2 else 0


def node2(x):
    w = np.array([2, -1, -1])
    tmp = abs(np.sum(w*x))
    return 1 if tmp <= 1/2 else 0


def node3(x):
    w = np.array([1/2, -1, -1])
    res = np.sum(w*x)

    return 1 if res > 0 else 0


def solution(x1, x2):
    x = np.array([1, x1, x2])
    a1 = node1(x)
    a2 = node2(x)

    return node3(np.array([1, a1, a2]))


exTable = [(1, 1), (-1, 1), (-1, -1), (1, -1), (0, 0), (2, 1)]

print("{0:>4} {1:>4} {2:>4}".format('x1', 'x2', 'y'))
for x1, x2 in exTable:
    print("{0:>4} {1:>4} {2:>4}".format(x1, x2, solution(x1, x2)))
