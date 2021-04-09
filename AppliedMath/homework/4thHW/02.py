import numpy as np


def node1(x):
    w = np.array([6, 7, 4])
    tmp = np.sum(w*x)
    return 1 if tmp > 0 else 0


def node2(x):
    w = np.array([-5, 7, 6])
    tmp = np.sum(w*x)
    return 1 if tmp > 0 else 0


def node3(x):
    w = np.array([1/2, -1, 1])
    tmp = np.sum(w*x)
    return 1 if tmp > 0 else 0


def predict(x1, x2):
    x = np.array([1, x1, x2])
    a1 = node1(x)
    a2 = node2(x)

    return node3(np.array([1, a1, a2]))


ex_table = [[-1, 1, 0], [-1, 0, 1], [-1, -1, 1],
            [1, 1, 1], [1, 0, 1], [1, -1, 0], [0, -1, 0]]

print("{0:>5} {1:>5} {2:>5} | {3:>5}".format("x1:", "x2", "y", "myAns"))

for x1, x2, ans in ex_table:
    print("{0:>5} {1:>5} {2:>5} | {3:>5}".format(x1, x2, ans, predict(x1, x2)))
