import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 0], [0, 1], [1, 0]])

print("a. 2A \n {0}\n".format(2*A))
print("b. A의 각 성분의 제곱 \n {0}\n".format(A**2))
print("c. A*B \n {0}\n".format(np.matmul(A, B)))

# np.matmul 보다 dot() method 이용
print("c. A*B \n {0}\n".format(A.dot(B)))
